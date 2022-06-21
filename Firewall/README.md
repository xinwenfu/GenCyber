# Introduction to Firewalls
We are going to introduce the firewalls.
We first look at the concept of defense in depth and why do we need the firewalls.
Once we understand the the firewalls, we will introduce the firewall rules, which are used to block and allow certain network traffic, which refers to network packets or messages.
As a concrete exampleof firewall, we are going to introduce the Windows firewall.
We will talk about how to define rules to block up an IP address and block and allow ping, which is a network applciation. 
At last we are going to introduce the hands-on labs for this lecture.

## Overview
Let's first look at this big picture about how cyber defense works.
You can see in this picture on the left we have the
Internet. The internet is the wild west. There are attackers and hackers.
There are all kinds of weird things going on on the internet.
You can see we have also the external firewall, something called the dmz, internal firewall and LAN.
Those things often belong to one entity, for example a school or a company.
So normally a school or company has this kind of setup to protect their network.

<img src="../Imgs/DefenseInDepth.png" width=640>

To understand the architecture the defense in depth we
have to first look at a few terms so the first term is about the internet right we know internet uh contains networks of
computers so basically internet is a networks of a network
right and uh so you can see here so you know for example um slow right it's a
big kind of uh enterprise as you can see it's a big school and we have a lot of computers
so most of the time for such a large network we are going to divide
the network into smaller network segments smaller kind of
networks and we call such a small network as a subnet so why do we need a
subnet the reason is that you know we want to to control
different department and different uh you know institutions within the school easily
and uh sometimes you know we need a subnet to actually deploy battery
security okay so let me give you one example here the dmz so dmz means
de-miniaturize the zoom here so here basically dmzing refers to one subnet
and uh what is in this subnet so often within the dm zone subnet we have
the web we have the email and we have many other kind of servers so you can see what is the
common property of those servers so those servers can be reached from the internet strategy now you can imagine
because they can be reached from the internet directly you know the attackers may attack those
computers directly right that's why we put them together right and then you can
see we have the external firewall to which is used to protect this
dmz okay and uh so that's uh the purpose of external firewall now what is the
purpose of the internal firewall here you know we
want protect our properties and uh we actually don't want the
attackers to reach most of our computers directly so that's why we have with
internal firewalls so most of the computers behind the internal firewalls right there's maybe
one firewall there may be a few firewalls but anyway we call them internal firewall and so
the computers behind internet firewall cannot be reached by the bad guys directly you can
see so that's another lyric defense okay so this is basically
normally how an entity how a company our school
defines their systems right they use layers of defense
here you see another system called ids so ids refers to intrusion detection
system we'll talk about that in another lecture the purpose of the ideas is a
interclass network package messages we call that as network
traffic and uh so that the system has some kind of software analyzing the network
traffic for the nominees okay so that's called intrusion detection
so what is the benefit of this kind of uh defines in depth this
kind of a layered defines the benefit is you can see here right so even let's see
the external firewall is not strong enough and even now i see here the dmz i
mean all the web servers are the email servers they are bridged they are compromised so
we have another firewall called the internet fiber which will actually block
the attackers from using the compromise computers to attack our other computers
so you can see right it's very important to have this kind of structure to have
two firewalls and the dmd is between the two firewalls okay so we are talking
about the fireworks a lot so what are firewalls so firewalls are hardware devices or software
applications which used to protect our system okay so its purpose is to inspect
and the filter and want the traffic so here again that's a bad guy here like i
forgot to play it and uh so let's look at at different fibers so we have a better
understanding what firewalls are doing so we actually
classify uh them into three categories based on
you know how firewall works internally and uh so the first type of firewall is
called the packet filters you know on the internet when you send the messages
your messages are put into something called a package basically a packet is packed off of messages and
there's some data over there right and your messages are put into one packet or a few package and they will be sent from
a one sender to another receiver right and uh so we also discussed uh you know
the internet professor new actually introduced the internet right how everything works
and we know that we have routers and we know you know when you want to send a message to
the receiver you need to specify the ip address and also you need to specify the portal
number for example if it's for the web the port number will be 80 or 443 right if it is https now also in the package
and the packet will contain your ip address okay so basically the packet filters filters
will do this so it will check actually the packet
header which contains the ports mp addresses and other kind of
flag information and for example let's see we want to block up
traffic from the internet from like russia from china from africa from
everywhere europe right so you know those regions they have particular ip
addresses and you can actually block the traffic coming into the campers based on their
ip addresses that's why it's called the package filters so it's based on the package header information
okay so then the second type of proxy is more kind of advanced so we call this as
a session layer and we didn't actually introduce this around you know when you
create a collection from your computer to a lot of computer sending messages so
you need a something called a collection so this will actually uh
order your messages otherwise you know when you send the messages right and how can we know the order right i mean the
receiver must receive the message in order right so you know so to
actually make sure the messages are in order then the package
i'm sorry the package actually has sequence numbers so we call such kind of information right
and as a part of the collection okay so that's called the collection otherwise
we need a collection to make sure everything is in order and you can see here so the collection is a kind of a
more advanced concepts than package so some of the firewalls they use collections
to check if i mean the traffic or the message are normal or not
right because sometimes the bad guys may cut in
between of your collection and they they may do something okay so that's called a session layer proxy
so the application uh proxies is another advanced kind of a
feature here so basically for this kind of firewalls
you know they will check if your application data is normal or
not so if the attacker actually changes something
in your message so sometimes you know based on such kind of change you may
find that actually since are not normal so you can see here so we have these three type of
fibers based on how the fibers will actually inspect
your data your messages right they will just you actually will decide how you
want to actually filter them for example you drop the messages because you think they are bad
so of course there are other ways of categorizing firewalls so let's look at
you know the categories of firewalls be some who are the users of the firewalls so
again we have three kind of uh you know type of firewalls we have enterprise
class firewalls we have consumer classifiers we have low url and so what is the
the enterprise class firewall those firewalls are normally very
expensive and they are integrated with the company routers switches many other kind
of other ones the network devices and so they
basically work as a whole and uh performing
filtering inspection you can see here even intrusion detection so
those firewalls are normally advanced and expensive they do a lot of
things then we have the consumer clouds classifiable then i know you know
your home i mean most of people have wi-fi in their home
and you use the wi-fi routers right and the wi-fi router actually
is integrated with the fiber most of them and i'm not sure if you guys actually ever
tried to log into your wi-fi router to config your wi-fi router
if you ever did that then you knew you know actually you can actually change
your router in a set of bible rules for example you don't want messages from professor food and if you know his ip
address you can block a provider for from reaching you okay you can actually configure that at your wi-fi router so
but you know those are not very advanced uh firewalls and often they are very simple
doing basic things for example they cannot do introduction they do basically routing right those are used for the
home not for enterprises so finally we have the lawyer owned like
a we right and we are researchers we are students we don't have money sometimes we just want to test our our ideas you
know so that's why we have this kind of open source software applications as uh
firewalls and uh edx has the firewall called the ip tables and i know you guys are another
family with ip tables and uh so but anyway you can use a data
software to configure five rules as complex as complex as you
want and they are kind of designed for doing those kind of things okay so those
are the uh firewalls based on who use the firewalls
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
