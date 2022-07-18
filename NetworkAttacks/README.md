# Availability

We will first introduce denial of service (DoS) attack and then distributed DoS (DDoS) attack.

## DoS
In a DoS attack, servers or network resouces are made unavailable to legitimate users. There are many types of DoS attacks. All the goals are to crash the servers or congest the networks so that the servers or networks are not available any more.

We will look at a few example. In our hands-on lab, we exploit the buffer overflow vulnerability of our vulnerable chat server. A large message with junk content is sent to the chat server. The server program copies the message to its buffer. The allocated buffer is too small and the code does not check if the message could overflow the buffer. The code just copies the entire junk message into the buffer and buffer overflow occurs then. The junk message overflows the buffer and overwrites things above the buffer. For example, 

## Hands-on

### Hands-on 1: DoS attack 
#### Doing this alone
Because of the vulnerability exploited by knock, an attacker can also crush the chat server
- Click and start the chat server C:\Tools\vchat\Server\vchat.exe
- Use armitage to scan Windows VM and find attacks
- Click the found Windows VM (IP)
- Deploy auxillary/dos/vchat/DoS
- Does the chat server stop running?

#### Doing this with another student
You can play with another student and crash each other's chat server.

### Hands-on 2: DDoS attack 
#### Doing this alone
Our chat server allows 100 users at the same time. In this hands-on, students use auxillary/dos/vchat/DDoS to create many connections to the chat server. Once the limit is reached, no more users can use the chat server

- Click and start chat server C:\Tools\vchat\Server\vchat.exe
- Use armitage to scan Windows VM and find attacks
- Click the found Windows VM (IP)
- Deploy auxillary/dos/vchat/DDoS
  - There is an option called *ThreadNum* when you pop up the DDoS module configuration window. Change it and see the effect.
- Can your chat client still connect to the chat server?

#### Doing this with another student
You can also do this with another student: One student starts the chat server and deploys the attack. Can the other student start a chat client connecting to the chat server?
