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
