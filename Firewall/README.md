# Introduction to Firewalls
We are going to introduce the firewalls.
We first look at the concept of defense in depth and why do we need the firewalls.
Once we understand the the firewalls, we will introduce the firewall rules, which are used to block and allow certain network traffic, which refers to network packets or messages.
As a concrete exampleof firewall, we are going to introduce the Windows firewall.
We will talk about how to define rules to block up an IP address and block and allow ping, which is a network applciation. 
At last we are going to introduce the hands-on labs for this lecture.

## Overview of Defense in Depth
Let's first look at this big picture about how cyber defense works.
You can see in this picture on the left we have the
Internet. The internet is the wild west. There are attackers and hackers.
There are all kinds of weird things going on on the internet.
You can see we have also the external firewall, something called the dmz, internal firewall and LAN.
Those things often belong to one entity, for example a school or a company.
So normally a school or company has this kind of setup to protect their network.

<img src="../Imgs/DefenseInDepth.png" width=512>

To understand the defense in depth, we have to first look at a few terms.
The first term is the internet. We know internet contains networks of computers.
The Internet is a network of networks.
A school like UMass Lowell has a big networkof computers.
For such a large network, we are going to divide it into smaller network segments, called subnets.
Why do we need subnets?
The reason is that UMass Lowell has many departments.
We can put different departments into different subnets so that it is easier to manage them, sometimes for the sake of security.
Another benefit is with diffrent departments in different subnets, messages generated with one department will stay in that department, not going through the networking devices of other departments. This will reduce network traffic congestion.

The DMZ means the demilitarized zone. It is one subnet. What is in this subnet>
Often within the DMZ subnet, we have the web, email and other servers.
What is the common property of those servers?
Those servers can be reached from the Internet directly.
For example, an attacker can send a web request to a web server and get a web page.
You can imagine because they can be reached from the Internet directly, the attackers may attack those computers directly.
That's why we put them together in one subnet and use the external firewall to protect them.
That's the purpose of external firewall.

The purpose of the internal firewall is protect other parts of the campus nerwork and computers.
We want to protect our assetts and don't want the attackers to reach most of our computers directly.
Most of the computers behind the internal firewall cannot be reached by the bad guys directly although these computers can still use the Internet.
The firewalls make it happen.

There is another defense component called IDS, which refers to intrusion detection system.
The purpose of the IDS is collect network packets and messages, denoted network
traffic. The IDS analyzes the network traffic for the abnormalities.
That's called intrusion detection.

What is the benefit of the strategy of defense in depth?
Let's assume the external firewall is not strong enough.
The web server and the email server have vulnerabilities and they are compromised.
However, we still have the internal firewall blocking
the attackers from using the compromised servers to attack our other computers in the LAN.
So you can see it's very important to have this kind of defense architecyure, DMZ between two firewalls and LAN behind the internal firewall.

## Types of Firewalls
What are firewalls?
Firewalls are hardware devices or software
applications which are used to protect our system.
Tts purpose is to inspect and the filter netwrok traffic.

### Categorizing Firewalls based on Firewall Mechanisms 

Let's look at at different firewalls so we have a better
understanding of what firewalls are doing.
We can classify them into three categories based on
how firewall works internally.

#### Packet filters

The first type of firewall is called packet filters.
On the internet when you send the messages,
your messages are put into packets, which are formatted data based on the Internet standard and protocol.
Packets will be sent from a sender to a receiver.
As we learned in computer networking, when you want to send a message to
the receiver, you need to specify the destination IP address in a packet. You may also need to specify the port at which a server works on.
For example if it's for the web, the port number will be 80 or 443.
A packet also contains your IP address as the source IP address.
A packet filter checks the packet header which contains the IPs, ports, and other information like flags.

Let's see we want to block traffic from known bad actors on the Internet.
There are known bad actors and we know their IP addresses and want to block them.
A packet filter can do it based on the packet header information.

#### Session-Layer Proxies 

The second type of firewall is related with a concept called session layer.
What is a session? When you browse a webpage, it is a session.
In a web browsing session, the network protocol such as the TCP protcol makes sure the web content is sent to the browser in order and reliably.
Session-layer proxies check a session follows the specific protocol.
Sometimes a bad guy may try to manipualte the session and do something bad. One such attack is the <a href="https://owasp.org/www-community/attacks/Session_hijacking_attack">session hijacking attack</a>. 

#### Application Proxies
The application proxies are another kind of firewalls.
Here are example network applications, FTP (File Transfer Protocol), SMTP (Simple Mail Transfer Protocol) and SSH (Secure Shell Protocol).
They check if your application data is normal or not.
If the attacker actually changes something,
an application proxy checks if the application protocol is followed and may find such abnormalities. 

So we have introdcued three type of firewalls based on how the firewalls actually inspect
network traffic and data.
After the inspection, the firewalls decide what to do, for example dropping (discarding) the messages or letting them pass.

### Categorizing Firewalls based on Users 

There are other ways of categorizing firewalls.
We now categories firewalls based on who are the users of the firewalls.
Again we have three types of firewalls, enterprise class firewalls, consumer class firewalls and roll-your firewalls.

The enterprise class firewall are normally very expensive and advanced.
They are often integrated with company routers, switches or many other kinds
of network devices.
Such firewalls may perform inspection, filtering and even intrusion detection.

The consumer class firewalls can be integrated in  your home WiFi routers.
Did you actually ever tryto log into your WiFi router to configure it?
If you ever did that, then you know actually you can actually change
your router and may be able to set up firewall rules to block network traffic.
For example if you don't want messages from an IP address, you can configure the WiFi router block it.
Consumer class firewalls are often cheap and do basic things.
For example, they are not designed to process high speed and large volume network traffic.

Roll-your-own firewalls are commercial or open-source software firewall applications.
They are often used by researchers and people seeking low-cost optons for firewalls.
Linux has a firewall application called *iptables*. 
It can be used to configure firewall rules as complex as complex as you
want. 

## Firewall rules

okay so now we understand the firewalls and you know to make firewalls work
you handle different rules and then to make the decision when you see attribute
traffic when the firewalls see that why uh i mean the network traffic right
and uh so we already mentioned so firewalls will help to protect computers
from unsolicited network traffic for example you know i mean
attackers always stay on the internet they try to compromise our computers we don't want their traffic
right and uh so what are the final rules five rules of course
uh kind of uh rules or kind of configurations
and now you use such kind of configurations to specify what to allow and what to deny
okay and uh so that's the basic idea of the fiber rules
okay the first step in fiber root creation is uh so of course we are dealing with the
networks and we try to protect us from better guys on the internet
i know so how can the bad guys reach us they reach us because
we use network applications those network applications send the
messages out and receive a message from the internet so when the bad guys try to reach you
they will actually try to manipulate your
network applications because they may pretend to send messages to your
applications right and um so for example if your applications have problems then
maybe they may utilize that and we actually learned this when we discussed the
software security right so that's why you can see the first step in firewall rule creation is we need to find out
which applications are actually doing networking stuff okay
and uh so how do we actually do that so here are a few things that we can do first you know
we can identify the network of facing applications what are applications messengers
and emails and those are basically uh applications we call them applications
and the second thing is about something called services networking fees services and
i know most of you guys may not know what our services but think about that right
and uh so your computers uh have a lot of applications and how can your computer actually uh doing
authentication doing other things those because there are many actually
applications which are called the services running in the background
okay for example in windows you can share files with
other computers why can't you do that because you know there's a
background application oh we should call that as service actually
doing that for you that's why you can actually share files
across different computers even across networks okay so those are called the
services and we also have actually
network confusing drivers for example when you install a computer i mean sorry
when you install a printer right network printer you haven't installed a driver and the driver will help you actually
send your documents your beautiful pictures to the
printer which actually is a maybe connected to your computer through wi-fi right and that you can see here
the printer will clean it to actually your your uh device right your computer and
uh so why the computer can contact uh the driver that is because you know i
mean sorry why your computer can contact the printer that's because you have
drivers over there in your computer drivers are also software and
so they will actually help you contact the printer which
uses wi-fi connecting to your computer okay so we have to actually identify all
those uh application services drivers otherwise you know if you dig some of them i mean
if they have a vulnerabilities and if you don't protect them then you are in trouble i mean the attackers may
actually attack the application services or drivers right
so next step is uh you know you find out all the applications services drivers you have
to find out the dependencies you know crease creating
firewall rules is a very complex procedure one is complex
you know today an application they use many other kind
of services software and if you actually don't identify the dependencies
carefully when you block one application then it may affect a lot of application the
other application may not work because you actually block the other application now your
students maybe like us right your consumers your customers will complain why it didn't work i actually everything
should work right so you have to be very careful with the five rules deciding okay what
applications you want to block what service you want to block what actually drivers you want to block
or want to protect or define the rules and what other dependencies okay
and so basically you have all the assets right like a computer services software
whatever services and you made in your mind okay you want to actually protect them
and uh so now you will start to actually write your rules of course the firewall has
the mechanism already you actually define the rules specify which ip you want to block which
whatever whatever other things you want to do okay and uh so
you can see here we see you want to define a group of rules you may have a few kind of
rules for different scenario so you can see we've mentioned here your core scenario
what is the scenario for example you have your laptop you bring your laptop
right actually to school right do you do that i mean you bring your laptop to starbucks or to dunkins do you do that
you also use your laptop at home you can see it right and when you're at the home you are protected by your wi-fi
router when you're under school you may be protected by your school's uh i mean networking
defense mechanisms but at the donkeys then you are not protected by anybody
right and because of their you know networking is very simple
most of the time they don't invest anything in defense
okay so you can see here so at different locations you know
you are protected differently so you want to actually set up
your rules for different scenarios for your
computer for example at home you may just feel relaxed like you don't actually
free them and so you you don't use any fibo i'll show you files sometimes it's very
not convenient okay and so so that's something right so you you
want to actually define your rules for your core deployment scenarios maybe a
few scenarios maybe one scenario depend on how you use your computer okay and so
now let's let's look at uh what you want to actually focus so here
we see you want to focus on inbound rules so what is the inbox inbound means the
traffic the network of messages coming into your computer
you know because when you actually try to contact other
servers right it's called outbound messages you will send the message is contacting
servers right it's called outbound i mean so we want to focus inbound rules
because you know most of times the attacker wants to attack you right so they want to contact you directly that's
why so we want to pay attention to the inbound rules so that we can block
the attacker attacking you directly okay and upon
rules here you know are also very important but the first you need to actually pay attention in
boundaries okay so once you define your rules you know
think about that if your computer has a lot of networking
components then your rules may be comple very complex you have a lot of rules
they may actually have conflicts that's why you have to test and make sure everything actually is smooth right you
you do not accidentally block up any other
applications you want right so that's something you want to pay attention okay
good so and understand we have been talking about the serial lot so let's look at
a particular example uh the windows firewalls so the windows firewalls basically
follows everything we just talked about and the windows firewall offers three
firewall profiles that means scenarios called the private public domain privacy
means when you are at home okay so when you're in the home you may use different rules
right so basically i mean when you choose the rules uh for private right then
you can enable it when you enter home so maybe at one time you just enable one uh
profile okay the public means you are at dunkin donut means you are at a at the
school okay for different scenarios you have different rules because you feel you are developed you are protected at a
different level and also you want your own freedom right and the biggest firewall sometimes blocks things very
kind of uh weirdly and you don't want another kind of trouble so here you can see we already mentioned
that what is the private profile right and uh so normally it's used for the private or
home networks public profile is a normally used for coffee shops
airports and other locations and so default profile is a public profile
because normally you define the strongest
viable rules for public profile because your computer is in a public network
anybody can attack you that's why normally your public profile
has the strongest viral rules okay and what we also have domain profile when
you are in school you know and you must know when you actually use a domain profile right and uh
basically you will be actually logged into your computer through
the university authentication procedures so you know it's a very different kind of program
so the the best apprentice of a profiles and uh so here is a you only enable the
firewall rule group uh on the profiles that uh
actually match your scenarios right and uh so because you know those
viable rules can be very different right and so you want to just enable the one that
actually really protect you in particular kind of scenario okay
so we haven't talked about the firewall right let's look at a few uh let's look at the windows firewall so the windows firewall
is called windows defender firewall so you can actually search right you know windows has the
windows icon right if you have the keyboard when you push that then you can actually tap and search anything any
application on your windows computer so here you can actually search your windows define the
firewall if you type it you'll find it okay so you can see here right and uh on
the left right you have the manual here called the turn windows defender firewall on or off so if you turn it off basically
your computer is not product at all okay now we also have other ones and settings i'm going to show you later now here
for our windows of virtual machine that we actually disabled
the firewall because you know we want to kind of uh to show you uh the danger right and so we disabled that you can
see we have private network disabled and we also have the public network profile disabled i know i don't have domain
because i don't use this computer uh in in the university okay
and uh okay so when you disable your windows firewall
your computer is reachable by anybody any computer
from the internet now of course if your computer is behind the you know
your wi-fi router that's a different story because the wi-fi router has a firewall over there protecting you
so i'm going to show you a few examples so i'm not sure if you guys know ping of
course you guys know ping i'm talking to the high school students now and uh
so when you uh setting up your computers sometimes you have a bunch of computers
right you want to actually do some fun things for example you want to play with your friends or game and so in those
cases now you may find oh my goodness i cannot actually seems um
connected to my friend's computer and his community doesn't respond and so
normally in those scenarios the first thing people will do is that people will use
a software program called the pin so pn is a command which actually is available on linux
windows and most of the platforms and the pin is used to test if an app
address is active so basically if the computer with not active address is
online or not okay so here is a simple description of the pin process so the
ping program it actually uses a one kind of internet protocol called
icmp so it sends out a request matches it's called echo means you i want you to
send them my uh request back okay so ping sends the echo request message to
an ip so if the ip is active right and then the computer restart the ip will
send back something called the echo reply and so basically hello are you over there and
then the ip right the receiver and we will respond yes i'm here that's basically
that's what happens um uh with me okay and if the ip is not active then every message
will be displayed by your team program telling you i cannot reachable cannot
reach the uh the ip something like that so here we have a question here shall we
block the pin messages okay and uh you know ping is a very useful
kind of application why should we actually sometimes block the pin messages of course i'm gonna stop here
ask the high school students but the answer is we should sometimes because we
want to hide ourselves from the attackers we don't want them to fund ourselves right fund our computer using
ping okay that's why sometimes we block the pin messages okay
and uh so that's about pin and so here is a pin example i'm using the pin from caddy
uh actually here i'm a ping let me have a look yes i'm pim
the windows vm from the candy vm then you can see here i just uh
uh i should actually put the show the pin message here i need to change this one okay and uh so
basically you just do team uh the ip then it will show you this uh message
here okay and uh so that's a about uh ping how you use a ping here okay
and uh so yeah so that's the key example and you can see here you have to specify the ip
mp of the pin for the pin
so why did this pin actually i
disabled the firewall so when you enable the firewall by default windows disables the
ping icon reply so when you pin windows you cannot ping actually and uh
so here of course sometimes we want to use pin right because pin is useful in
some scenarios and so this is how you actually uh enable pin even with your firewall
enabled so in this case we enable the firewall we just want to allow ping we want to keep other default options uh
default rules okay and so here you can see all the steps here first we assume
the windows define the firewall is enabled right now we go for the windows uh search button over there the search
box over there and a search for windows defender firewall then you click and open it right and then down here i just
showed you the the menu item called the one settings on the left right and you just click there over there and you it
pop up actually window and uh so and then you go ahead and you you
actually you can see here and uh you need to do something to enable
this rule here so let me show you here okay and uh so this is a basically uh the one
settings so when you actually click the advanced settings and uh you actually it's disabled that
this enabled and you change this and uh so here when you actually click
advanced settings you will pop up the window windows different the firewall which advanced
security so you click inbound rules then you search for this one uh file and a
printer sharing i call request okay so basically you
just you can see here by default when we enable windows firewall
you know it's no right so basically windows will not respond to the pin
message okay and uh so of course you just right click and you just enable it so when you
enabled you can see here right and uh then you can paint okay
and uh so here right you also can see i enable this for the private profile but you can
also enable it for the domain profile and and uh there's a lot of private profile
actually i'm gonna try with that but anyway you can just uh enable the pin
for your scenario okay so that's about how you enable pin rule here you can see there are many
other rules actually i don't know them and i didn't try to understand all of them
okay and uh so now let's see no let's see you don't
like your kind of uh another troublemaker in your dom and you
want to actually block his ip okay how do you do that you don't want to actually him to blood to contact you or
maybe you think he's a bad guy or whatever and so you want to block another guy's ip or you want a black or
the hikers ip you know you know there are better actors on the internet right
you can block them let me tell you our you must know at the how
many eyepiece blacklist blockade okay and we know some
of the bad actors on the internet so we block them and so so this is how you do it you can
see again you you start another window right the windows defender firewall with other one
security and you click on the emojis then you click on the new rules right then you do you just blow it and uh so
so basically here i think i need to add a few words that's here maybe and uh so basically you know you have to
uh you will add a few eyepiece and uh here so you can see here
and uh for which remote ip address does this will apply and uh let me here have a look yeah
click next after adding the eyepiece right so basically at the step seven you
will add ip addresses you want to block and just follow the instructions here
that you will actually finish uh the blocking okay you will block the
ip so finally let's you guys will do the i mean do the
hands-on right so the first hands-on is uh uh you enable firewall
on windows and because by default our windows vm firewall is disabled
on our windows of virtual machine so when you actually enable windows firewall please try if you can ping
windows vm from cali vm okay the second thing you will do is uh
okay then you actually allow people see if you can actually enable the ping rule so the third
hands-on is uh you want to actually uh add an mp address for example the candid
vm ip address see if you can block another ip so these are all the hands-ons
okay oh my goodness let me see let me stop the
recording okay usually you wanted to start it yes
