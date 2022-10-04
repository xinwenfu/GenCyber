Under construction

# Networking

We are going to first look at different
views of networks. Then we are going to
look at the network data encapsulation, that is, how your messages are put into network packets.
At last we are going to look at the denial of service and the distributed
denial of service attacks.

## What is the Internet?

### IP address and port number
The internet is a network of networks.
When we use the Internet, how can you communicate with a remote computer?
For example, if you want to access a web server running on a remote computer,
how do you know where the web server is?
You have to know the IP address of the web server.
When you want to send the data to the remote server or remote computer,
your computer and software actually adds extra data called headers to your message.
For example, the IP header contains the destination IP address, which indicates where this
message is addressed to.

However on one IP address, there may be multiple servers.
Recall servers are software programs.
A web server uses a web server program.
An email server uses an email server program.
If we run multiple servers on one IP, when you want to talk with a particular server,
how can you differentiate different servers on one IP?
We use port numbers.
The tuple (IP, port) uniquely identified a server on a computer.

### Network Protocols

We can send a message to a server.
How can the server understand our message?
This is a where the network protocols play their roles.
To talk with a server, our computer and the server must have a common language.
The common language is is the protocol, which defines the rules of the communication, the procedures and the
format of the data.

For example, here is an example HTTP request message sent by a web browser to a web server (www.aol.com).
```
GET / HTTP/1.1
host: www.aol.com
```
The first part of the message is the request line, containing:
* A method (HTTP command) such as *GET*, which requests data such a web page
* A document address such as /, which indicates the root folder
* An HTTP version number such as HTTP/1.1
The second part of the message is the optional information. For example, *host* indicates the server to which the request is being sent. The can be observed the HTTP request message has a well defined format. Therefore, the server will be able to understand the the request.
Networks have many protocols so that computers can talk with each other.

The TCP/IP protocol suite is the protocol architecture of the Internet.
It has four layers: Application, Transport, Network, and Data Link Layer.
Protocols on each layer do particular things.
Details of implementation of lower layers are hidden from upper layers.

<img src="https://user-images.githubusercontent.com/69218457/193728165-261300f6-0291-4647-a144-f39430dc3563.png" width=128>


## Different views of networks

### Application View of Networking

Based on the protocols we actually have
different views of a network. 
We discussed web browsing. When we try to access a web server we need to know the IP address (corresponding to url) and the port
number. That's basically the view of the application.

You may question: I never used an IP address, only web url/link like http://www.cs.uml.edu/~xinwenfu/index.html. Actually the web url/link corresponds to the IP address.
Before your web browser sends out the web request, it contacts another Internet server, DNS server, asking the IP address of the web url (called domain name too).

You may alo question: I never used a port number during web browing like http://www.cs.uml.edu/~xinwenfu/index.html. The reason you never specified the port number for web browsing is
if you don't specify the port number, the web browser assumes you use the default port number.
For example, for unsecure version of web browsing using http like http://www.cs.uml.edu/~xinwenfu/index.html, the default port number is 80. For the secure version of web browsing like https://www.cs.uml.edu/~xinwenfu/index.html, the default port number is 443.
When you don't specify the port number, your software will assume you are using the default port number.

<img src="https://user-images.githubusercontent.com/69218457/193731583-cad31124-0546-48a7-887d-5c321466ee9d.png" width=480>


### Transport View of Networking
On the Internet, data may get lost during transmission. A web browser at a sender computer can send a reqeust to a web server. The request may transmit across a lot of cables and network work equipment like routers. There are a lot of routers, which are responsible for relayings user data to the destination. The data may corrupt somehow during the transmission. For example, a router gets very busy and may drop the data. So we got a problem. How can the sender computer know the data got dropped? What shall the sender computer do if the data got dropped?

A sender such as the web browser relies on the transport layer, particularly the TCP protocol of the transport layer, to deliver the data reliably to the receiver such as the web server. 
The TCP protocol adds a TCP header to the application data and form the TCP segment that contains the TCP header and application data.
The TCP header contains a sequene number for the data.
When the receiver's transport layer receives the TCP segment, it shall acknowledge the arrival of the TCP segment by sending the sender an acknowledgement.
If the sender's transport layer does not receive the acknowledgment after some time, the sender's transport layer decides the TCP segment is lost. The original TCP segment is buffered at the transport layer of the sender. If the TCP segment is lost, the sender's transport layer retransmits the TCP segment until the sender's transport layer receives the acknowlegement.

From the perspective of the transport layer, TCP segments are exchanged between two computers. The transport layer does not differentiate the applications data. It assumes the TCP segment may get lost, and thus buffers the data and retranmits the data if needed.

### Network View of Internet

We now know the TCP protocol at the transport layer can ensure the TCP segment will be delivered to the destination reliably. 
However, the sender and receiver may be far away from each other. There are a lot of routers, thus a lot of routes, between the sender and the receiver.
When the network layer of the sender receives the TCP segment from the transport layer, it adds a network header to the TCP segment and form the packet, which contains the network header and TCP segment.
The network header contains the source IP address (sender's IP) and destination IP address (receiver's IP). The sender computer is with default gateway (i.e., router). Therefore, the packet will be delivered across the local network to the sender's default router, which works with other routers to find the shortest path to the receiver.
So the routers connect different networks of computers together.

The network view of the Internet is routers form paths between pairs of computers.
Routers run routing protocols and find the best route between pairs of computers.
Routers forwards a packet based on the destination IP address of the packet to other routers.

<img src="https://user-images.githubusercontent.com/69218457/193841722-2e72bd4b-9dd4-48d2-bdf2-dd0526c071d9.png" width=480>

### Data Link Layer View of Internet

We now know the network protocols find the best through a bunches of routers to deliver network packets.
However, we still have the task of delivering the data from a computer to its default router.
Computers and their router can form a local network and exchange data bewteen them.
We look at a popular technology, Ethernet, that can connect local computers including the router together.
A home network is an example of local area network.

Ethernet can use shared medium like Ethernet cables connecting all computers together.
We've got a problem.
Since it is a shared medium, at any time one computer can send data to the shared media to the receiver.
Otherwise, if multiple computers send data at the same time, those data override each other and all will get corrupt. This is called collision.
So which computer should send first and which should send second?
One critical functionality of the data linker is to addres the collision problem.
Ethernet uses the carrier-sense multiple access with collision detection (CSMA/CD) scheme to solve the collision problem.

For Ethernet, when the data linker layer of the sender receives the network packet,
it adds the Ethernet header to the packet and form an Ethernet frame.
The Ethernet header contains the Ethernet address of next hop (e.g., router) as the destination Ethernet address.
In this way, when the router receives the Ethernet frame, it knows it is the receiver.
It then finds the destination IP address from the network header and perform the routing.

<img src="https://user-images.githubusercontent.com/69218457/193858685-4e973637-861c-4d44-8c5d-0be39bf54cfa.png" width=480>


the router to another computer
so here
is a big picture of layers in example
when you actually
design your
particles you only care about the
protocols stay on the same layer so for
example
when you actually trying to use HTTP you
really need to care about the TCP IP
internet you only need to know
how you can use TCP but normally we call
that as a programming interface the
programming interface is determined
although the implementation of TCP is
hidden from
http
okay so you can just reliably use a the
program interface and
design your own application protocol and
then
you will communicate it with your
friends and the destination happily and
then for example we mentioned the
purpose of the transporter layer one
purpose is to deliver data reliably you
may have different ideas to implement
that idea right and but really you know
uh you can Implement you can try them
and see which one works but that will
not affect the up layer protocol
and also you can see here
when you did that your way of
re-transformation to ensure the data
will be delivered you don't need to care
about how the data will be routed to the
destination that's basically
the function of the network layer here
the IP layer right and so you just there
to know the program interface
of
the IP layer and
the typical error just in the standard
data to the IP layer then an IP layer
will use any kind of a relative protocol
to deliver your data efficiently to the
destination
so again here you can see here in the
appear don't need to care about the
implementation of the ethernet and as we
mentioned the purpose of the ethernet
the one purpose is a to
ensure locally
and every computer
has the chance to standard their data
and that data will not have creation and
everything will be standard
effectively right and we do I mean the
IP there really doesn't need to care
about the
the implementation of the Eastern
Ethernet or the data link layer okay
so there are many many protocols and
here are some examples and you can see
here right on the application layers
then we have many protocols pin HTTP
telnet FTP DNS SNMP
and other transport layers we have TCP
UDP and other network layer that we have
icmp idmp DHCP
and the rip pm ospf on the data link
layer that we have arp we have ethernet
and finally you can see at the bottom of
all the layers
is the network interface that is
basically the mystery fifth layer
physical layer
okay so you can see we have different
layers
on the TCP Network Suite
and actually you know for
each layer when your data passes through
each layer
the header will be added to your
actually
data so for example let's see
the example for http
and your adtp may be about a
downloading
like a message right so when you use
HTTP you do web browsing and you will be
actually download
the HTML file from the remote web server
then your web server will actually show
the HTML file to you then you see
basically the web page and so the HTML
file corresponds to the web page you'll
see so the HTM file is the user data
so
however you cannot just extend the user
data
to the remote and you have to
add the hdb header to the user data to
indicate and what is that the data you
understand is audio image file lens and
so the hdb header actually
will contain such information
so then now
your data enter the application of HTTP
is ready and it will be sent to the TCP
layer okay and as we mentioned the TCP
layer here
will ensure actually
your data will be reliably delivered so
the TCP header for example will contain
a sequence number which is used to
identify your data and in this way right
and uh
when the receiver receives the data they
can acknowledge okay I receive the data
with a secret number like that
and so basically you know the tsp header
will contain such information like a
sequence number to implement its own
functionality okay and then we call
actually the TCP layer data as a TCP
segment
so now the TCP segment is ready
all right
we send this TV segment to the IP layer
the appear
of class will add the destination IP in
the source IP to the TCP segment and
because you know for routers to find the
best route the routers need to know the
destination IP so that's why we're going
to put the decision IP into the IP
header okay
good and then so we call the IPL data as
a IP datagram or IP packet and this IP
packet will be extended to the ethernet
and the ethernet will add
the ethernet header to the IP datagram
and then the incident header contains
information needed for
ensure the data can be delivered to the
local device reliably
so here is a
actually the
ethernet frame okay so you can see here
and we have the incident header it
contains the destination address and the
source address which refers to the MAC
address is okay and so the Mac addresses
are the addresses for devices
within the local network and uh so the
incident there requires those addresses
to ensure the data will be delivered to
the right device
now we have the IP layer which contains
the source IP address destination API
address
so we have the TCP header which actually
contains the X6 number as we mentioned
and we also have it's another trailer
here and default reliable delivery of
your data
foreign program
for protocol analysis you can use word
shock to capture networker packets
to your
network card on your computer so here is
one example I captured some packets you
can see here at the top panel here we
have all the metadata of the package if
you click
one entry here then it will show you the
details of the
internal frame which contains the IP
packet then you can see here there's
some kind of Arrow here you click Arrow
it will expand to show you more details
okay and then at the bottom
panel here we have
the banner data
for all the information about okay so
they are the same thing so basically
here you want to pay attention the
barrel numbers are the same thing as we
show in other panels but really you know
the other information so because of the
protocols
now we can explain the banner data
appropriately

## Hands-on

### Hands-on 1: Common Linux command line terminal commands
Many Linux applications may not have graphical user interfaces. You may have to run them within a terminal.
Refer to <a href="https://linuxconfig.org/linux-commands-cheat-sheet">Linux commands cheat sheet</a>. Try the following Linux command line terminal commands and understand what they do. *Terminal Emulator* is Kali Linux's terminal program. 
- Click the dragon icon at the top left corner of of Kali Linux desktop to show applications

<img src="../Imgs/Kali-Terminal.png" width=640>

1. <a href="https://man7.org/linux/man-pages/man1/touch.1.html">touch</a>: change file timestamps or create a new file
```
touch test1 # create an empty file called test1
```
2. <a href="https://man7.org/linux/man-pages/man1/ls.1.html">ls</a>: list files in a folder; current folder by default
```
ls # show files in current workng folder
```
where # indicates a comment and does not need to be entered

3. <a href="https://man7.org/linux/man-pages/man1/pwd.1.html">pwd</a>: print full path name of current working folder
```
pwd # show the name of current working folder 
```
4. <a href="https://man7.org/linux/man-pages/man1/cd.1p.html">cd</a>: change the working folder to another folder
```
cd .. # go to parent folder of current working folder
cd GenCyber # go to the GenCyber folder, which is a sub-folder of current working folder
cd /home/kali # go to folder /home/kali, which is a full path name
```
5. <a href="https://man7.org/linux/man-pages/man1/mkdir.1.html">mkdir</a>: create folders
```
mkdir mine # create a folder called mine in the current working folder
```
6. <a href="https://man7.org/linux/man-pages/man1/rm.1.html">rm</a>: remove files
```
rm test # remove a file called test
rm -r mine # remove a folder called mine and all its subfolders in the current working folder
```
7. <a href="https://linux.die.net/man/1/mv">mv</a>: move files or folders
```
mv test1 tset2 # move test1 to test2; no test1 any more
```
8. <a href="https://man7.org/linux/man-pages/man1/cp.1.html">cp</a>: copy files or folders
```
cp test2 test3 # copy test2 to test3; test2 still exists
```
9. <a href="https://man7.org/linux/man-pages/man8/ifconfig.8.html">ifconfig</a>: configure or show info of a network interface
```
ifconfig # show information of network interfaces; what is ip address of your Kali VM?
```
10. <a href="https://man7.org/linux/man-pages/man1/less.1.html">less</a>: Show content of a file
```
less encrypt.txt # show content of encrypt.txt; press q to quit
```
11. <a href="https://linux.die.net/man/8/ping">ping</a>:	ping IP addresses and see if they are active
```
ping 192.168.1.19 # ping ip address of 192.168.1.19
```

### Hands-on 2: Common Windows console commands
Most operations of Windows console commands can be completed with *File Explorer* of Windows. However, knowing Windows console (cmd) commands is still useful in some cases. For examples, commands applications are written for Windows console. Running console applications within a console may be more convenient even if you can still run them with File Explorer.

Press the Windows *Start* icon and search cmd.
Click *Command Prompt* to start Windows console. 
Refer to <a href="https://www.thomas-krenn.com/en/wiki/Cmd_commands_under_Windows">Cmd commands under Windows</a>.
No comment is allowed to follow commands immediately within Windows console.

<img src="../Imgs/Windows-Terminal.png" width=640>

1. dir: list folder content
```
dir 
```
Show content of current working folder.

2. cd:	change directory
```
cd c:\Tools 
```
Change working folder to c:\Tools.

3. ipconfig: show network interface settings 
```
ipconfig 
```
Show all network interface settings.

4. ping: ping IP addresses and see if they are active
```
ping 192.168.1.22 
```
ping ip address of 192.168.1.22

5. type:	show content of text files
```
type victim.c
```
Show the content of victim.c

### Hands-on 3: Run chat server and client from terminal
1. Please run the chat server (located in the folder of C:\Tools\vchat\Server) on Windows VM from Windows console 
2. Please run the chat client (located in the folder of /home/kali/GenCyber/vchat/Client) on Kali VM from terminal
3. Chat with another student

### Hands-on 4: Use Wireshark to check packet contents
1. Read the short <a href="https://github.com/xinwenfu/GenCyber/tree/main/IntrusionDetection#wireshark">introduction to Wireshark</a>. Search for "Wireshark" in the page if you cannot find it.
2. Use Wireshark to check packet content. Can you find source IP address and destination IP address shown in the IP header figure below in Wireshark?

The picture below shows the structure of the Internet packet IP header.

<img src="../Imgs/IP.gif" width=512>

The picture below show the IP header and other packet contents in Wireshark. Pay attention to the highlighted part.

<img src="../Imgs/Wireshark-IP.png" width=720>
