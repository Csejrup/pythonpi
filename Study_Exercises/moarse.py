import datetime
import threading
import time
import RPi.GPIO as GPIO
import InternationalMorseCode as ICM

BASE_TIME_SECONDS = 1.0
TOLERANCE = BASE_TIME_SECONDS / 2.0

def initialize_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup([11, 32, 36], GPIO.OUT)
    GPIO.setup(31, GPIO.IN)
    GPIO.output([32, 36], GPIO.LOW)
    GPIO.add_event_detect(31, GPIO.BOTH, callback=intercept_morse_code)

last_edge = GPIO.LOW
press = datetime.datetime.now()
release = datetime.datetime.now()


# Intercept a rise or fall on pin 31 (button press/release)
def intercept_morse_code(channel):
    global last_edge, press, release
 
    # Button pressed - determine if start of new letter/word
    if GPIO.input(channel) == GPIO.HIGH and last_edge == GPIO.LOW:
        last_edge = GPIO.HIGH
        press = datetime.datetime.now()
        detect_termination()
 
    # Button released - determine what the input is
    elif GPIO.input(channel) == GPIO.LOW and last_edge == GPIO.HIGH:
        last_edge = GPIO.LOW
        release = datetime.datetime.now()
        interpret_input()
 
sequence = ""
letters = []
words = []

# Detect whether most recent button press is start of new letter or word
def detect_termination():
    global sequence
 
    if sequence == "":
        return
 
    delta = calc_delta_in_sec(release, press)
 
    # Check for start of new letter (gap equal to 3 dots)
    if (delta >= ((BASE_TIME_SECONDS * 3) - TOLERANCE)) and (delta <= ((BASE_TIME_SECONDS * 4) + TOLERANCE)):
        process_letter()
 
    # Check for start of new word (gap equal to 7 dots - but assume anything > 7 dots is valid too)
    elif delta >= ((BASE_TIME_SECONDS * 7) - TOLERANCE):
        process_word()
 
    # If it's not a new letter or word, and it's a gap greater than a single dot, tell the user
    elif delta > (BASE_TIME_SECONDS + TOLERANCE):
        print("")
 
# Process letter
def process_letter():
    global sequence
    character = ICM.symbols.get(sequence, '')
 
    if character != '':
        print("Interpreted sequence " + sequence + " as the letter: " + character)
        letters.append(character)
        sequence = ""
        initialize_signal(32)
        return True
    else:
        print('Invalid sequence: ' + sequence + " (deleting current sequence)")
        sequence = ""
        initialize_signal(36)
        return False
 
# Process word
def process_word():
    if process_letter():
        word = ''.join(letters)
        letters[:] = []
        if word == "AR":
            print("End of transmission. Here's your message: " + ' '.join(words))
            print('\nClearing previous transmission. Start a new one now...\n')
            words[:] = []
        else:
            words.append(word)
 
# Interpret button click (press/release) as dot, dash or unrecognized
def interpret_input():
    global sequence
 
    delta = calc_delta_in_sec(press, release)
 
    if (delta >= (BASE_TIME_SECONDS - TOLERANCE)) and (delta <= (BASE_TIME_SECONDS + TOLERANCE)):
        sequence += '.'
        print(str(delta) + " : Added dot to sequence:  " + sequence)
        initialize_signal(32)
    elif (delta >= ((BASE_TIME_SECONDS * 3) - TOLERANCE)) and (delta <= ((BASE_TIME_SECONDS * 3) + TOLERANCE)):
        sequence += '-'
        print(str(delta) + " : Added dash to sequence: " + sequence)
        initialize_signal(32)
    else:
        print(str(delta) + " : Unrecognized input!")
        initialize_signal(36)
 
def calc_delta_in_sec(time1, time2):
    delta = time2 - time1
    return delta.seconds + (delta.microseconds / 1000000.0)

def main()
    try:
	initialize_gpio()
	message = raw_input("\nPress any key to exit. \n")
    except KeyboardInterrupt:
	print("ctr + c pressed, program is terminated")
    finally:
	GPIO.cleanup()

if __name__=="__main__":
   main()
