# Intrusion Detection

We are going to introduce the intrusion detection system. 
We first look at the big picture of cyber defense. Firewalls are often not enough. That is why we need intrusion detection..
Oonce we understand the idea of intuition detection, we'll talk about where we are going to deploy intrusion
detection systems.
Then we will talk about intrusion prevention.
Intrusion prevention is actually partitially implemented by firewalls.
But we can add the intrusion prevention functionality to an intrusion detection system (IDS), shutting down detected attacks.
As an example of intrusion detection, we are going to introduce a protocol analyzer called Wiresahrk.
Wireshark is designed for not intrusion detection, but capturing network traffic and showing packet details.
But you can use Wireshark to demonstrate the principle of intrusion detection.
At last we are going to introduce the hands-on labs.

## What is intrusion detection

Let's have a look at the defense in depth picture. 
The internet is on the left and the rest of all the components belong to a company or campus like UML.
We discussed the external firewall is used to protect servers like email and webh servers in the DMZ.
The internal firewall blocks direct access to computers in the LAN, e.g., other computers of UML.
In this way, even if servers in DMZ are compromised, it will still be not easy to hack into other computers of UML.

An example IDS is <a href="https://www.snort.org/documents">Snort</a>, a popular open source IDS. It has a few components.
The packet acquisition compoment captures packets.
The packet decoder compoment determines packet protocols and the content location.
A pre-processor is a plugin to extend functionalities of Snort.
The detection engine matches extracted packet information against rulesets for detection of potential attacks.
The alerts/logging component reports potential attacks to the admin and saves related data into a database.

<img src="../Imgs/DefenseInDepth.png" width=512>

However, firewalls cannot defeat all attacks.
There are unknown attacks.
Firewalls are normally used to block known attacks.
That's why we need the intrusion detection system (IDS).
One way of intrusion detection system uses is to
check if the network traffic is normal or not.
The intrusion detection system collects network traffic from computers of interest.
It check if the network traffic is normal.
For example, because of a DDoS attack, suddenly there is a huge spike of traffic coming into the campus.
The IDS can detect such abnormality and send alerts.

What is intrusion detection?
Intrusion detection is a process of identifying and responding to malicious
activities against computers and networks.
An intrusion detection system can be software or hardware, which performs intrusion detection.

<img src="../Imgs/Snort.png" width=512>

okay and uh so this is a normally
uh how an intrusion detection system is uh
uh programmed always works okay this shows the components of intrusion
detection system so here down over there is a targeted computer this may be a lot of computers
and we are going to collect network packets from
this red uh you know protected computers we want to see if this computer is performing
normally or not so once you actually uh capture all the traffic then you can see here we have
something called thing called the sensor here this is just kind of like a software here and uh
analyzing the collect the network of packets and see if there's anything wrong right for
example if there are no attacks and if that's too much traffic something like that and you can see here basically this
uh decision making mechanism refers to databases right configuration and here
you can see ids knowledge something for example no attacks and uh
so basically this sensor here checks uh the traffic
and uh referring to known knowledge to find
if there are attacks or not so if there are attacks
some intrusion detection system may actually
try to respond for example one response is we just actually turn
off our network right so that's one kind of uh action here we just block
everything and then we need to actually check what's wrong with those protected computers right so this
is normally how you know an nds works and there are components
okay so now let's look at where we put the intrusion detection systems
so first let's look at actually something called host-based intrusion detections but
before we do that so let's look at the internet right we already did this before we already introduced what is the
internet that you can see here right in the middle here the block does over are
like a routers and you know then we have so those routers
are responsible you know relating your messages from end to end right from your to your friend
from your mom to your dad something like that and you can see also you know there are many other routers
which are managed by the like a comcast and uh resident and those
companies so those routers they work together and they actually
forward our messages to the destination in very uh efficient way
right then in the middle it's a the you know kind of a transportation
network now at the end now we have our local networks here that you can see
here we have different customer networks one example is a the um slow uh network
so within you must know you know we have so many computers so basically maybe
we actually use the department as a unit so each development has their own
network so we call that as a local error network but it's really kind of a relative concept here and so that's how
actually internet is uh structured so let's first look at what is the
host based intrusion detection system so a whole space intrusion vegetation
system basically will stay on a single computer
and sometimes it could be a software but most of the time we use the software programs as intuition detection systems
for example i'm not sure if you heard of snort snort is a software package
which can be used for intrusion detection okay so you can install snort on your computer and the snort will
collect your network traffic and the snort will analyze your package by entering your
computer and leaving your computer and and the snort can also actually check
the log files on your computer and uh snort can also actually for example
check the processes and assistance running on your computer okay and uh
so this is what hosts the intrusion detection system will do most of the time but you can see
here and sometimes you know as uh the science advances right we actually
refine host the basic intrusion detection system and uh so that they can do more we can protect
better our computers so here one example is called the protocol involvement what does this mean it means
when you run your browsing right we are you are using the http
protocol to browse a website and so the protocol enforcement means we
want to make sure the particle is properly followed not actually
changed by the attack okay so where is uh the host based uh
intuition detection system is on your local computer here so you can see here on each local computer right
and uh so we have the host-based intrusion detection okay system
then the next type of intrusion detection system is the network-based intrusion detection
that you can see here right so we call this network interesting detection basically it means you know
this system will collect traffic from all
the computers on the network so basically whatever goes through the cable right
and these network-based intrusion detection system will dump it and it will analyze
the network package okay so thought i i said something wrong it doesn't i mean
an ids doesn't actually collect you know things from your host but it
will just intercept all network packets passing along the
network cable okay and uh so you can see here and uh
send it to unlocked by host so you can see here the host may send actually the ids their logo files of course if hosts
do that that's okay and uh and also here you can see processes and the system running on the network host
people you want to actually do that okay and uh so this is about uh the whole the
network with the intrusion detection system and uh
so you can see here uh so the reason the advances in intrusion
detection for the network-based intrusion return system is you know
at the beginning intrusion detention system is designed for
owning detection but as time goes we find sometimes we
have to respond to the attack that's why you can see here
and uh for recent advances of a network-based intrusion detection system
we may have active rules means that we're going to do something not just passively
analyzing the network package we're going to actively shut down
the trouble making connections okay
so where is the network based intrusion detection system on the
internet okay so basically you can see
the solder is a the intrusion detection system okay the network basic intrusion
detection system it will just collect the traffic from
the cable okay and so you can see here you know
the network intrusion detection system i mean the network-based intrusion detection systems is kind of a
more than the host of this intriguing detail system as we saw here right and
uh so basically the meta-worker-based intriguing design
system will collect traffic maybe logs from anywhere
within this uh local area networks okay and uh so it's more than
host based intrusion detection system okay
now let's look at the third type of intrusion detection system called a perimeter based intrusion detection
system and so the perimeter-based intrusion detection
system you can see normally it's located on a rod so you know
our campus has something called the edge rotor which stays on the edge of our network
which means all your network packets will go through the router because the router is responsible
for forwarding your packets to the destination right you must have done how so many edge routers maybe i think maybe
two or three and routers which are responsible for that purpose
okay and you can see that's very important and uh we need to protect those edge routers
right and then because you know those edge rotors can see all incoming
traffic from internet maybe those traffic are from the bad guys
so if we put an intrusion detection system at the end
router that will form our first line of defense
right so basically that's why we need this kind of a perimeter-based intrusion detection
system and this kind of system will analyze you can you can see network packets
passing through the gateway the router right and anything you know on the router and uh the logs processes systems on the
on the router or gateway okay and uh
recent advances in intrusion prevention uh in terms of uh perimeter-based intrusion
detection scene so here the key idea here is you know because of the router sees
the attack the doctor is the first to see the attacks right and uh so the router
should be able to block the attacks once it happens of course we have to think about how to do
that but we call that as a zero ladies and gentlemen if there's any attack the
router will block it uh you know right and uh at the earliest time and but the zero leading the blocking is
not easy okay and uh and uh so because you know think about that right and there are so much traffic
going through the router and can you actually inspect all the network packages one by one and
that is impossible so it's very challenging to do this okay so here is a uh the perimeter-based
intrusion design system on the internet it's just at the edge of our campus network that's normally where
we put the pids okay okay so we have talked about uh you know
intuition detection another important concept is intrusion prevention
and uh so what is the intrusion permission you know intuitive prevention means that we want to actually prevent the attack right and
so that's why we call this intrusion prevention and so one challenge
for intrusion detection is how can we perform the real-time intrusion
detection and for today's
internet it creates huge amount of network
traffic at a tremendous speed and uh really it's a very challenge
to actually detect attacks among so much traffic in real time
you know either you use software right you know software is very slow sometimes you know
and the software most of the time cannot do real-time intrusion detection that's why you know many people
now turn to hardware for intrusion detection so we
use a hardware to implement the intrusion detection aggregates so that
we can actually perform real-time intrusion detection but it's still a very good big challenge
think about the speed and the amount of traffic right and uh
so that's a big problem okay
so you know
so basically uh we know we want to do intrusion
detection and we also want to do intrusion preparation
but uh how can you do intrusion detection and intrusion prevention
effectively so i just showed you guys uh the
minus plot and the multiplier payload
if you already analyzed such mirror then you know it's features
that you can actually try to detect such kind of features in a network package see if it is a metasploit
payload or not right for known attacks it's a
easier to block it right but in reality
there is so much traffic over there even for example you create the features for
an attack how can you guarantee such features
are not existing in other kind of a normal traffic
right and maybe a lot of application will create a similar traffic your features
will not actually be effective okay so that could be a problem
and a lot of challenges to intrusion probation is let's see you know you know
there are so many possibilities you may block the wrong traffic
right that's called the false positives it's not a real attack but you think it is but you think fine i just don't want
anybody to protect me i'm going to block everything that is suspicious even it's not a real attack
okay however that's good for your home if you want to do that but
can an sp do that no if an sp
blocks so much traffic you'll be fierce because you know let me tell you
most of the intrusion detection systems how huge number of possibilities you'll
be theories and if they deploy that because you know
you will be blocked a lot okay so that's the problem another one is
latency right for intrusion detection prevention you know there's so much traffic how much time
does it take to analyze the traffic and fund the attack so that's a lot of problem here right and but anyways
people have been thinking about this you know how do we do intrusion prevention and
detection together efficiently it's an ongoing challenge but uh we are advancing although we still have a lot
of challenges so again i want why we did to understand
detection interim prevention here so basically you can see here right you use firewalls now you can do permission
because you know some more tags you can prevent it for sure and also you can do detection here you
can see oh my my goodness today the traffic from another computer from non-ip is huge i don't like that i
think it's bad i think most time it is like a maybe detailed service attack traffic so
i'm going to block it so in this way because if you find the huge amount of
traffic from another computer it's not normal you can detect okay that's maybe an attack you can block it right however
you know if it's a zeod attack means it's new attack then
the attacker will compromise your computer so this will happen and uh you know that's
why we need to still study intrusion prevention and detection and
see if you can find the attacks and but this is the reality
in the world okay so we have discussed intrusion detection
and interim permission let's look at some real-world examples so let's look at
a worm called sql sum worm so what is a worm a worm is one kind of software this
software can discover vulnerable computers on the internet then
this warm and diesel malware can send itself to those compromised computers
and the model will work again on those compromised computers and again
the malware on those computers will try to find other vulnerable computers on the internet and
in fact the other computers but you can see here using this approach the worms
can propagate itself to many many computers right from other one coming to another computer from another event to
more computers so that's why we call this as a worm because this mirror can
propagate itself autonomously okay and the sql stem world was the fastest
internet war ever right in history so this is what happened
on july 24 2002 microsoft announced okay we found a problem
now you can see here at that point everybody was not so kind of a sensitive to attacks
and in 2002 the vulnerability was announced
then in 2003 this sequel snap worm was
unleashed and then at this point
okay somebody found oh there's a sql stand worm there's some mirror running on the
internet but at that point you know it already affected
ninety percent of available hosts within 10 minutes okay and you can see how fast this can be
right because you know as we mentioned that the worm can propagate itself and so what is the worm the worm is a
mirror so basically the worm will send out the mirror payload the code
and in a single udp packet so the whole mirror can be put into
a packet and the whole payload right the whole mirror is only
376 bytes so
this payload right this packet is sent to a server that server actually runs
at a port 1434 okay so basically
if you didn't upgrade your server the sql server
then if your server runs at the port
1434 this maywear will compromise your computer as we did
in our labs then you can imagine once you know
this uh mayweather right this worm compromise your computer what will happen right the
whole thing is compromised okay and uh so that's what happened now how can this shows actually how fast it
affects everything here you can see right and uh before like that and after the
warming you can see so many computers were compromised okay and uh
so how can you stop uh this worm how can you stop this attack of course you need to first patch your
server so that you know there is no such programming uh error in your super animal because
there's no such error i mean when the mirror tries to attack
that port it will not work now you can also use fireball firewall
to block the traffic targeting port 1434 right
and uh so that's what you do you can also use vpn anybody has to use vpn to access
the server right and in this way you know basically you have a firewall blocking everything you have to use vpn
to access this port number and the network will not work okay and uh so because you know this protein
silicone is a vinyl introducing uh i mean why not protocol you know so basically you we can actually do the
intuitive detention permission but at that point nobody cared about the cyber security that's why you know
there was a huge impact when the major was released on the internet okay
and uh here we see zero releasing active ids and dps is the only way of
blocking this form theoretically means okay once you fund the attack and you know it's attack okay and once you see
the packet you know it's an attack you know that requires some knowledge
the active means you block the worm basically it means you drop the
package uh send by this malware right and uh so basically that's
how you do it but it's ready to challenge if it's a new attack oh it's a new way where you don't know right you
don't know all the knowledge right and how can you do that that's a big challenge
so i want to talk about wireshark so word shock is a software program and uh
the word shock can actually capture network packets into your computer and going out of your
computer and uh to show all the packets uh of the network
traffic okay and uh so so let's look at the interface here and
uh so this is the interface when you click the workshop right you can find it on windows vm and this is the interface
you will see and then you will see different network cards and uh so
this workshop can stop all network traffic
uh going out of this ethernet
card or coming into this ethernet card okay and
so when you click it basically workshop will begin to capture all the
network packages that you can see here this is a all the commands right command menus and
here is a display filter because there's so much traffic here and you don't want to see all the
packets sometimes then you can actually set up a filter for example in this case we see mp.source
this means okay and uh within the packet right the source ip is a 10
delta 0.2.16 and here the destination ip is the
10.0.2 the 13 here so you only want to see
okay a packet which has such a kind of a source mp and that system ipa or
the other way okay so that this is what this display filter means you just want
to show the traffic right with such kind of a packet of headers you don't want to
see other traffic and then in this panel here we show the details of a
selected packet header so when you click a package in this panel here and it will
show you actually here the headers of those
packets that's a single package and you can see here there's a lot of headers here so you
have to actually come to college to learn everything here okay but if you actually
click the packet it'll also show you the banner content so what is the
real data within the packet of course right the headers
here are part of the banner content but as you know
you know most of the data here have minions some of the data here refer to the
headers each header has their own meanings each
maybe data here is a field within the headers so
what word shark does best is it will show you what each data means
in this panel here so this will actually help you understand the protocols so when you
actually learn internet of particles and this software will help you a lot telling you
what each field means and what is the the name okay this
help this is a very useful software okay
so so so this is basically what is going on here and and then we have hands-on lab right so for the hands-on lab
uh what i want to what we want to do here is you know we are going to deploy uh
we are going to deploy the knock attack against the windows vm and
i want you guys to use workshop to capture the attack traffic and uh so the question
for you is that can you actually find the attacker package send from kelly ram to windows vm so that's basically what
we're going to do with the intrusion detection here i think that's all let me actually stop
recording
