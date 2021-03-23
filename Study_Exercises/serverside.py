import socket
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.OUT,initial=GPIO.LOW) #green
GPIO.setup(21,GPIO.OUT,initial=GPIO.LOW) #red
GPIO.setwarnings(False)

host = '192.168.87.191'
port = 5560

def setupServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created.")
    try:
        s.bind((host, port))
    except socket.error as msg:
        print(msg)
    print("Socket bind comlete.")
    return s

def setupConnection():
    s.listen(1) # Allows one connection at a time.
    conn, address = s.accept()
    print("Connected to: " + address[0] + ":" + str(address[1]))
    return conn

def RED(t):
    #Red LED
    GPIO.output(21,1)
    time.sleep(1)
    GPIO.output(21,0)

def GREEN(t):
    #GREEN LED
    GPIO.outdefput(20,1)
    time.sleep(t)
    GPIO.output(20,0)

def dataTransfer(conn):
    # A big loop that receives data until told not to.

    while True:
        # Receive the data
        data = conn.recv(1024) # receive the data
        data = data.decode('utf-8')

        # Split the data such that you separate the command
        # from the rest of the data.
        dataMessage = data.split(' ', 1)
        # Command
        command = dataMessage[0]
        # parameter
        para=dataMessage[1]
        y=int(para)
        if len(command)>0:
            print(command)
        if command == 'RED':
            RED(y)
        elif command == 'GREEN':
            GREEN(y)
        elif command == 'KILL':
            print("Our server is shutting down.")
            s.close()
            break
        else:
            print('Unknown Command')
    #conn.close()
s = setupServer()
#while True:
#    try:
#        conn = setupConnection()
#        dataTransfer(conn)
#    except:
#        break
def main():
    try:
        while True:
            try:
                conn = setupConnection()
                dataTransfer(conn)
            except:
                break
    except KeyboardInterrupt:
        print("program terminated")
    finally:
        GPIO.cleanup()
        conn.close()
#Runs Main Function
if __name__=="__main__":
    main()

