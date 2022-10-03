# Availability

Availability means when we need particular resources, they should be available if we are authorized to use them.
We will first introduce the denial of service (DoS) attack and then distributed DoS (DDoS) attack, which may deny the availability of resources.

## DoS

What is a DoS? 
There are various servers such as web servers and email servers on the Internet?
So if a service is attacked and taken down, it is called Denial of Service.
There are many ways of performing
DoS attacks. Here are a few examples.

### Ping of death
This is an old attack happening to various operating systems (OSs) including Linux, Windows and Mac.
If an attacker crafts a large ping packet, the OS couldn't process the large ping packet right and would crash.

### DoS by buffer overflow
When a message is sent to a computer program (locally or over the Internet), the program often uses a buffer to hold the data temporarily.
A buffer is a piece of computer memory.
If an attacker sends a large amount of data and the allocated buffer cannot hold it,
sometimes the large amount of data may overflow the buffer and overwrite other parts of the computer memory.
Such overflow may disrupt normal execution of the computer, which may crash.
This is a DoS attack caused by the buffer overflow vulnerability of a computer program.

#### DoS against our vulnerable chat server

In our lecture on <a href="https://github.com/xinwenfu/GenCyber/tree/main/SoftwareSecurity">Penetration Testing and Software Security</a>, we have exploited the vulnerable chat server (vchat) and deployed the buffer overflow attack against vchat. We were able to hack into the Windows VM through vchat.

The same vulnerability can be exploited for a denial of service (DoS) attack. 
A large message with junk content is sent to the chat server. The server program copies the message to its buffer within a function. The allocated buffer size is fixed and the code does not check if the message could overflow the buffer. The code just copies the entire junk message into the buffer and buffer overflow occurs then. The junk message overflows the buffer and overwrites things above the buffer. For example, a function return address may be overwritten with junk. Therefore, when the function returns, it returns to a wronng memory place, where there may not be even code, and the chat server crashes.

<img src="../Imgs/BufferOverflow-junk.png" width=480>

Below is the C language function of the chat server in trouble.  *Function3*(.) copies the message into *Buffer2S* using the problematic function strcpy(.), which does not check the boundary of the buffer during copying.
```
void Function3(char* Input) {
	char Buffer2S[2000];
	strcpy(Buffer2S, Input);
}
```


### SYN flooding attack
There is a well known attack called SYN flooding attack against any server that runs the TCP protocol, which is one type of Internet protocol. For example, when you browse a web server, you use TCP, which ensures all data will be correctly delivered. An attacker can send a large number of TCP SYN packets to a server. A SYN packet asks the server to open a connection. The server has to allocate resources to maintain such a connection. If there are too many connection requests, the resources will be used up and the server cannot accept any more connection requests, which may be legitimate requests not from the attackers.

## DDoS

What is a distributed denial of service (DDoS) attack?
In a DDoS, multiple attackers, maybe many of them, coordinate to deploy the attack against a single target. 
For example, assume we have a server, which processes user requests. What if a lot of attacking computers send our server a lot of requests?
Then our server will be busy with processing those junk requests and have no time to respond to legitimate requests.

In a DDoS attack, the bad guys may compromise as many computers as possible.
They install special software on the compromised computers.
At a particular time, they issue an attack command to every compromised computer.
We call compromised computers as zombie computers sometimes, which are used to launch the attack on the same
target and at the same time.
That's why we call this as a distributed DoS attack because the attack is launched from many computers at the same time.

For example, a lot of zombie computers may deploy the SYN flooding attack against one server and halt the serivce provided by the server. An attacker may also rent botnets for DDoS. A botnet is a network of compromised computers.

In our hands-on, the vulnerable chat server can handle 100 clients. If a lot of attackers create connections to the server, the server cannot serve any new clients. This is the principle of the DDoS attack; a lot of attackers coordiante to exhaust the resources at the target.

Actually, if one attacker creates more than 100 connections to the chat server, the chat server cannot serve more clients either. The later attack becomes a DoS attack, not a DDoS attack.

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
