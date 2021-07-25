from boofuzz import *
from sys import exit

def get_banner(target, logger, session, *args, **kwargs):
    ## define how the Vulnserver banner looks
    banner_template = b"Welcome to Vulnerable Server! Enter HELP for help."
    try:
        ## Attempt to grab the banner from vulnserver and save it as "banner"
        banner = target.recv(10000)    
    except:
        ## If that fails, the target is down so we exit and stop the fuzzer
        print("Unable to connect. Target is down. Exiting.") 
        exit(1)

    ## If we connected and received data we log the check
    logger.log_check('Receiving banner..')  
    if banner_template in banner:   ## check if what we grabbed matches the banner
        ## if its a match we just log the success and hand back to the fuzzer to continue
        logger.log_pass('banner received')  
    else:
        ## if it's not a match we assume something has happened with the app and exit.
        logger.log_fail('No banner received') 
        print("No banner received, exiting..")
        exit(1)

def main():
    ip = "10.0.2.7"  # IP address of the victim machine
    port = 9999            # Vulnserver's port

    # By default, Boofuzz will output its session logs to a SQLite formatted,
    # timestamped database (.db) file.
    # You can grab whatever your software of choice is to open
    # and interact with the database file.
    # OR you can create a new logger that will output its results
    # to a nicely formatted CSV file.
    # Log file to capture boofuzz session results.
    csv_output_log = open("fuzzing_results.csv", "w") # create a csv file
    logger = [FuzzLoggerCsv(file_handle=csv_output_log)]

    # Network socket
    _socket = SocketConnection(ip, port, proto="tcp")
    _target = Target(connection = _socket)

    # Session(.): Extends pgraph.graph and provides a container
    # for architecting protocol dialogs
    session = Session(target = _target, fuzz_loggers = logger)

    # ...............Define one request ..........................
    # Boofuzz makes use of the concept of requests and blocks when
    # creating a fuzzing template.
    # Requests begin with s_initialize(‘requestname’).
    # Blocks (or primitives) that follow a request declaration form
    # part of that request.
    s_initialize("Request") # "Request" is the name of the request message 
    # s_string(.): Push a string onto the current block stack
    # fuzzable (bool) – (Optional, def=True)
    # Enable/disable fuzzing of this primitive
    # s_string("TRUN ", fuzzable=False) 
    s_string("LTER", fuzzable=False)
    # The next block of our request contains the space that is
    # needed between command and value
    s_delim(" ", fuzzable=False)
    s_string("data") # what we will fuzz
#    s_string("\r\n")
    # -------------------------------------------------------------

    # s-get(.): The selected request is also set as the default current. 
    # Create a connection between the two requests (nodes) and register an optional
    # callback to process in between transmissions of the source and destination
    # request. Leverage this functionality to handle situations such as challenge
    # response systems. The session class maintains a top level node that all
    # initial requests must be connected to.
    session.connect(s_get("Request"), callback=get_banner)
    session.fuzz()

main()
