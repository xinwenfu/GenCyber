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
### Identifying Networking Components and Dependencies

To make firewalls work, we need firewall rules which make the decision of blocking and allowing network traffic.
What are firewall rules?
They are configurations to specify what to allow and what to deny.
The first step in firewall rule creation is to identify which components on your computer are network-facing.
A network-facing component sends/receives network traffic (using <a href="https://beej.us/guide/bgnet/">network sockets</a>).

We need to identify network facing applications such as messengers
and emails. Those applications often have interfaces so that users can interact with them doing things like sending messages and emails.

The second kind of network facing components are called services.
For example, you can install the <a href="https://httpd.apache.org/">Apache web server</a> on your computer,
which then becomes a web server.
However, you will not be able to see a graphical interface of the Apache web server, which is running in the background.

The third type of network facing components are network confusing drivers.
For example when you install a network printer, you need to install the network printer driver,
which sends your documents to the printer, e.g., through WiFi.

Next step of creating firewall rules is find out the dependencies between networking facing applications, services and drivers.
Creating firewall rules is a very complex procedure.
One network facing component may use other network facing applications, services and driver to work.
If you actually don't identify the dependencies carefully when you block one component,
it may affect other components. 

### Rule Authoring
Once you are clear about network facing applications, services, derivers and their dependencies,
you will start to write your rules.
Of course the firewall program has the mechanism, allowing you to define the rules, e.g., specifying IPs to block.
You may want to define rules for different scenarios.
At least you shall define rules for your core scenario.
What is a scenario? A scanario is where you use your computer.
For example you have your laptop,
and may use it at home, school or Dunkin'.
At home, you are protected by your WiFi router. You may not need to define many firewall rules on the laptop.
At school you may be protected by your school's defense mechanisms. So maybe again you do not need to define many firewall rules on the laptop.
But at Dunkin', your laptop is open to attacks since there may be no much security mechnism implemented over there,
Your laptop could be under attack by other customers of Dunkin'.

In different locations you are protected differently. So you want to actually set up
different rules for different scenarios for your computer.
Sometimes, too much security brings inconvenience. That is why we need different firewall rules for different scenarios.
For example at home you may just feel relaxed given the protection by the WiFi router.
You are also not afraid your family members may attack your computer.
Therefore, maybe you can related firewall rules too, allowing all the computers at home to share and communicate with each other freely.

We may also want to focus on inbound rules.
So what does inbound mean?
Inbound traffic is messages and packets coming into your computer.
Outbound traffic is messages and packets going out of your computer.
Apparently inbound traffic may contain messages and packets sent by attackers. That is why we shall focus on inbound traffic.

Firewall rules can very complex.
A firewall on a computer needs to protect a lot of networking components like applications, services and drivers.
A firewall on a campus is set to protect the entire network and computers on campus.
Given the complexity, if you have a lot of rules, those rules can be wrong or have conflicts, preventing them from working properly.
That's why you have to test and make sure everything works and
you do not accidentally block up any services or applications.

## Windows Firewalls
Now Let's look at
a particular Firewall example, the Windows firewall.
The Windows firewall is part of the Windows operating system.
It follows everything we just talked above.

### Windows Firewall Profiles
The Windows firewall offers three firewall profiles, private, public, and domain for different scenarios.
The private profile means when you are at home. The set of firewall rules for the private profile protects your Windows when you are at home.
You can enable the private profile when you are at home.
The public profile means you are at a public place like Dunkin'.
The domain profile means you are at a school or companies which employs the concept of domain to authenticate people using the school/company resources.
For different scenarios you have different rules because you are overall protected at a different level.
The default profile is a public profile because normally you define the strongest
firewall rules for the public profile.
If your computer is in a public network, anybody can attack you.
That's why normally your public profile has the strongest firewall rules.

The best practice of profiles is a you only enable the firewall rule group on the profiles that suit your scenarios.
You know those firewall rules can be very different.
So you want to just enable the one that actually really protects you in the particular kind of scenario.

### Windows Defender Firewall

The Windows firewall is called *Windows Defender Firewall* as the picture below shows.
How can you open the firewall application and configure it?
You can actually search for it.
You can click the Windows Start button and then type *Windows Defender Firewall* to find it.
Actually you can use this approach to search for any program installed on Windows.

<img src="../Imgs/WindowsDefenderFirewall.png" width=640>

On the left of the Windows Defender Firewall interface, you can manually turn the firewall on or off.
If you turn it off, your computer has no protection at all.
There are many other settings.
For our Windows virtual machine, we actually disabled the firewall.
Both private profile and public profile are disabled. I don't have the domain profile for the VM because i don't use this VM in the university network.

#### Allow and Block ping
When you set up your computers and play games with friends, you have a bunch of computers.
But you got some networking problem and one computer does not work.
You want to test if the network is set up right or now.
In such a scenarion, people often use a program called ping to test if that computer in trouble is in the network or not.
*ping* is available on Linux, Windows and other operating systems.
ping is used to test if an IP address is active. If the computer does not have an active IP address, we say it is offline.
Otherwise, it is online. Here is a ping example: we ping the Windows VM from Kali VM.
```
ping 192.168.1.19
```
<img src="../Imgs/ping.png" width=640>

Here is a simple description of the ping process .
ping uses an Internet protocol called ICMP.
It sends out *echo request* message (just a message with particular format) to an IP.
This is analogous to the shout "Are you there?"
If the IP is active, the computer with the ip sends the *echo reply* message. 
This is analogous to the shout back "Yes, I'm here."
If the IP is not active, error messages are displayed by ping.

We have a question here. Shall we block the pin messages fromsent by other computers to our computer?
You know ping is a very useful.
Why should we sometimes block the ping messages?
It is because we want to hide ourselves from the attackers.
Sometime we don't want them to find our computers using ping so easily.
That's why sometimes we block the ping messages.
But please note: they are other ways such as port scanning of identifying active IPs as we discussed in the cyber attack cycle.

If Windows Defender Firewall is disabled, all rules are disabled and ping works.
Assume Windows Defender Firewall is enabled. ping reply is disabled by detault settings as shown below.

<img src="../Imgs/ping_disabled.png" width=640>

Here is how we enable ping reply
1. Search for Windows Defender Firewall, and click to open it
2. Click Advanced Settings on the left
3. From left pane of the resulting window, click Inbound Rules
4. In the right pane, find the rules titled File and Printer Sharing (Echo Request - ICMPv4-In)
5. Right-click each such rule and choose *Enable Rule*

Now ping reply is enabled.
<img src="../Imgs/ping_enabled.png" width=640>

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
