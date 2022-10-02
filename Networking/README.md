Under construction

## Networking

in this lecture we are going to talk
about networking and the distributed
denial of service
here is a the outline of this lecture we
are going to first look at different
views of networks then we are going to
look at the network data encapsulation
how your messages are put into Network
package
then at the last we are going to look at
the net of service and the distributed
dinner of service attacks
so what is the internet the internet is
a network of Networks
when we use internet
there's one question here how can you
communicate with a remote computer for
example if you want access a web server
running on a remote computer how can you
access that how do you know where the
web server is
basically you have to know the IP
address of the web server okay and then
so here is an example of the IP address
so basically
when you want to send the data to the
remote server or remote computer
your
computer and the software
actually adds
headers to it's a data to the message
the headers are actual information added
to your original message for example the
IP header contains the destination IP
address which indicates where this
message is addressed to
however on one IP address we may run
multiple servers remember servers are
software programs web server
uses the web server program
and the email server
uses email server program
if we run multiple servers on one IP
when you want to talk with a
particular server
how can you differentiate different
servers on one IP
here we use important numbers so
basically
the top of Ip and the port uniquely I
didn't find a server
so the question here is a
now
you can send a message to a server you
can send any data to a server how can
data server understand your data
this is a where
the network protocols play their roles
to talk with a server you must have a
common language
but common language is the protocol
which defines the rules of the
communication the procedures and the
format of a
your data so for example you may want to
put a particular information
at a some
offset of your message
and uh so for example and the message
may contain command and may contain the
parameter for that commands and in that
way right if you put a commands and
parameters at a fixed locations then
the
receiver will know where to find the
command and the where to find
the parameters
so that's how we design the particle
for networks we have many particles
and uh
those particles will have computers to
talk with each other
based on the particles we actually have
different views of a networking
we mentioned about the web browsing when
you try to access a web server you need
to know the IP address and the port
number
right and uh that's basically the view
of the application so
when you actually
do the web browsing right you just need
to know the IP address support number
and you you may ask hey I never actually
used a port number
the reason you never specified the port
number for web browsing is
if you don't specify the port numbers
you use the default port numbers for
example for unsecure version of a the
web server the port number is 80. for
the secure version of a web browsing the
port number is 443 so when you don't
specify
the port numbers and your software will
assume you are using the default port
numbers
okay
so that's the view of the application
right and the internet actually uses a
protocol Suite called the TCP
and the TP PMP
Suite has folders the application layer
and that's actually what you see every
day when you use browsing messaging and
then that's the application then
and the application layer we have the
transport layer then we have the network
layer and the link layer so
protocols on each layer do particular
things
and the details of implementation of a
lower layers are hidden from up layers
that means if you change
your low alert
actually The Operators will not occur if
actually your provider
the fixed interface for the operator to
use the lower layers
so let's look at a
different wheels and then let's first
look at the application view of a
networking
so this is a the web browsing example we
discussed before right and for the
client this may be your web browser and
then we have the web server on the right
we start IP and the port number
when a client doesn't specify the port
number then
we use a default port number so you can
see here so basically the HTTP client
actually uses the lower layer TCP
to talk with the remote web server and
the remote web server entry is the HTTP
server which relies on the TCP server
and so basically what happens is that
the TC I mean the HTTP client sends its
a message to the TCP layer and a TCP
layer will use a lower layers and the
forwarded the message to the TCP
layer enter the web server then the TC
builder at the web server will forward
that data up to the HTTP server
so what is the purpose of the TCP layer
and uh so the purpose of the TCP there
that's the transporter layer
the idea is a you know
on the internet
when we transform the data if there's
lighting and other events your data may
be lost
while your data is lost how can you
recover the lost data right how can you
guarantee the message will be delivered
reliably to the remote
that's what TCP layer does okay that's
where what that transporter does and uh
for example
in the case of a TTP
if
you know your standard data and uh
actually you will expand there will be
some acknowledgment
from the receiver
if you do not receive the acknowledgment
then the transport layer actually
buffers
the message and it will retransmit
the message if it doesn't receive
the acknowledgment in a particular
period of time
so that's the view of a application
layer and the transporter layer now
let's look at the let the work layer
so what is the purpose of a network
layer and so we can see from this
picture here
so in a network layer we have some
important
network devices called routers
so the routers
basically collect different networks
together and so different networks how
a bunch of computers right so basically
routers will collect all the computers
and other networks together
but we have so many routers and they are
all collected to each other
so we have a question when a client
sends
the data to a remote IP address
which route should we actually go
through
should your data first go to Europe and
come back to us of course you know if
you use does not
a very
efficient path
so basically the routers
use protocols
to find out
the best
route
which is a sequence of routers
for your message to reach the
destination IP address
so that's basically the network view of
the internet so
basically
the routers
we will look at all the computers in
terms of ips and the vendor the best
route
from one and to the other end
okay so now we understand the
application layer transporter layer and
the network layer
let's look at
the
data declare what is data declare I
guess you heard of Internet so on
one region
for example within one department or
within your home
you may actually collect
different
computers all together right so in this
case you can see I have the client I
have another computer
the letter to the ethernet so that's
actually some kind of physical words
collecting the client collecting the
another computer and routers together
so we've got a question here the
question is
while we use the computers to send
messages
who should stand first who should send a
second
the challenge here is if other computers
talk at the same time
those message will be sent to the wire
then basically they will override each
other
we have a collision
nobody's data will be delivered
and all the data will be
corrupt
so basically
enter the date link layer one important
thing
that will be done is to determine
who
should send now who should ascendant
next
okay and uh
so that's about the data link layer so
in this way you know our data can be
reliably delivered
to
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
so now let's look at the US and DDOS so
once we understand the network it's a
not hard to understand dos and DDOS
so what is a DOS
we run different servers we run
different services on internet
so if a service is attacked and ticked
down is called Data of service
really there are many ways of performing
dos attack and that here are a few
examples
the first example is called the pin of
death
so this is a
old attack happening to a Windows
computer so in early windows
versions
windows
didn't
process
the P impact properly
and if a bad guy
crops a large pin packet
then the windows version couldn't
process that large pin packet and then
the computer will crash because you know
the program was not programmed to
process such a larger pin
another
example is a the above workflow attack
so in computers when you send
a message to a server or to a program
and the program often uses
some
buffer to
hold the data temporarily a buffer is
just a temporary place in the memory to
hold the data
normally you can think about that you
have to allocator
are large enough Buffalo
to hold the data
however the attacker will send you a
large amount of data you didn't expect
such large data
you did it allocate or large enough
buffer now if you copy data to your
buffer
you do not actually check the boundary
of your buffer then the larger data will
cause your
limit buffer to overflow
however the buffer exists in your
computer memory
when the buffer overflows the larger
amount of data May override
the computer memory
which may save other data now you can
imagine it disturbs the normal execution
of a
the computer because it actually
disrupts and it crops the computer
memory and the computer May crash
okay so that's a
nothing else service attack caused by
the buffer overflow vulnerability of a
computer server
a closer concept is called the denial of
service attack
a closed concept is called the
distributed Dynamic service attack so
what is a distributed in our service
attack
and uh so in distributed Dynamic service
attack many computers Attack One victim
and for example
right let's see you have a server you're
running the server on your computer and
your server will process the user
request
however what if
a lot of computers send you a lot of
requests then your computer will be busy
with processing those like a garbage
requests and there has no time to
respond to
request right and so that's basically
the distributed denial service attack so
you can see here a typical DDOS attack
proceeds as follows
the better guys compromise as many
networked computers as possible
then they install special software
in the compromised computers then at a
particular time
issue an attack command to every
compromise computer we call data
computers as zombie computers sometimes
to launch a device attack on the same
Target and at the same time so that's
why we call this as a distributed dos
attack because the device attack is
launched from many computers at the same
time


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
