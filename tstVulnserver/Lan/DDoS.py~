import socket
import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
   
    HOST = '10.0.2.7'  # The server's hostname or IP address
    PORT = 9999        # The port used by the server
 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            data = s.recv(1024)

    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":

    for i in range(0, 102):

        format = "%(asctime)s: %(message)s"
        logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
        logging.info("Main    : before creating thread")
        x = threading.Thread(target=thread_function, args=(i,))
        logging.info("Main    : before running thread")
        x.start()
        logging.info("Main    : wait for the thread to finish")
        # x.join()
        logging.info("Main    : all done")
