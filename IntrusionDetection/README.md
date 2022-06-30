# Intrusion Detection and Prevention

We are going to introduce the intrusion detection system (IDS) and intrusion prevention system (IPS). 
We first look at the big picture of cyber defense.
Firewalls block and filter network traffic based on IPs, port numbers and protocol information in packet headers, and are often not enough for cyber defense.
That is why we need intrusion detection, which seaches packet contents for signs of intrusion, and intrusion prevention, which acts on detected attacks by intrusion detection.
We will first define the IDS, and discuss where we are going to deploy it.
Then we will talk about intrusion prevention.
As an example of intrusion detection, we are going to introduce a protocol analyzer called Wiresahrk.
Wireshark is not particularly designed for intrusion detection, but capturing network traffic and showing packet details.
But we can use Wireshark to demonstrate the principle of searching packet contents for intrusion detection.
At last we are going to introduce the hands-on labs.

## What is intrusion detection

Let's have a look at the defense in depth picture. 
The internet is on the left and the rest of all the components belong to a company or campus like UML.
We discussed the external firewall is used to protect servers like email and webh servers in the DMZ.
The internal firewall blocks direct access to computers in the LAN, e.g., other computers of UML.
In this way, even if servers in DMZ are compromised, it will still be not easy to hack into other computers of UML.

<img src="../Imgs/DefenseInDepth.png" width=512>

However, firewalls cannot defeat all attacks.
There are unknown attacks.
Firewalls performs blocking and filtering based on IPs, port numbers and protocols.
They are not normally used to detect attacks, particularly unknown attacks.
An IDS does intrusion detection.
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

An example IDS is <a href="https://www.snort.org/documents">Snort</a>, a popular open source IDS. It has a few components.
The packet acquisition compoment captures packets from protected computers.
The packet decoder compoment determines packet protocols and the content location.
A pre-processor is a plugin to extend functionalities of Snort.
The detection engine matches extracted packet information against rulesets for detection of potential attacks.
The alerts/logging component reports potential attacks to the admin and saves related data into a database.

<img src="../Imgs/Snort.png" width=512>

## Host, Network & Perimeter Detection

Let's look at where we put the intrusion detection systems.
Before we do that, let's look at the Internet.
Routers are responsible for relaying your messages from end to end, e.g., from you to your friend.
There are many routers. Core routers form the Internet backdone and managed by Internet Service Providers (ISPs) like Verizon and Comcast.
The networks of enterprises and schools like UML are customer networks.
They use routers, called edge routers, to connect the campus network to the Internet.
All routers work together, find the best route and forward our messages to the destination.
A big enterprise or campus network may be divided into smaller networks, called local area networks (LANs)
LANs are managed by individual units of the enterprise or campus, such as a department.
Each development may have their own network.

<img src="../Imgs/HIDS.png" width=512>

### Host based intrusion detection system (HIDS)
A host based intrusion detection system stays on a single computer.
A HIDS is often a software poragm and protects a single computer. For example, Snort can be used as a HIDS protecting one computer.
Snort collects network traffic coming into a computer and going out of the computer and analyzes it for intrusion detection.
A HIDS may also collect and analyze audit and log files, processes and application running on the host.

We may also deploy a host based intrusion prevention system (HIPS) on a host.
A HIPS may perform protocol enforcement (allowing only allowed services running on the host), stack enforcement (dis-allowing code running in a particular memory region for data storage, called stack), and file checksum monitoring to prevent files from being changed.

### Network-based intrusion detection (HIDS)
The next type of intrusion detection system is the network-based intrusion detection system.
A HIDS can be a standalone server, collecting network traffic from computers in the network and analyzing it for intrusion.
Snort can also be a HIDS if we feed network traffic from computers in a network and on the network cable into Snort for analysis.

<img src="../Imgs/NIDS.png" width=512>

We may also deploy a network based intrusion prevention system (NIPS) within a network.
A NIPS can use *active* rules to shutdown connections, not just *passively* detecting attacks. 
It can be integrated into firewalls to disable attackers.
It can use data mining techiques to analyze the traffic.

### Perimeter based intrusion detection system (PIDS)
The third type of intrusion detection system is called a perimeter based intrusion detection system.
It is often put beside a customer network's edge routers.
The edge routers handles all traffic into the customer network from the Internet and out of the customer network to the Internet.
The PIDS forms our first line of defense.

<img src="../Imgs/PIDS.png" width=512>

We may deploy a perimeter based intrusion prevention (PIPS) at edge routers. 
A PIPS can actively block known malicious attacks and perform eero-latency blocking. 
Zero latency blocking is not easy because there is so much traffic
going through the router.
Can you actually inspect all the network packets one by one?
Sometimes that is impossible. So it's very challenging to perform zero latency blocking.

## Emergence of Intrusion Prevention
Intuition detection is apprently not enough since it only detects attacks.
We also want to actually prevent the attack.
However, three problems are apparent. 
1. False Positives (false alarm). False alarms are a great challenge to IDS. Given the variety of network traffic, an IDS always generates false alarms, trating normal traffic as attacks. If all traffic generating flase alarms is blocked, the customers for sure will not be happy since their use of Internet will be disrupted.
2. Denial Of Service – Blocking spoofed hosts. Will you be happy if your computer is blocked even if it is compremised? ISP will have to handle too many phone calls from angry customers.
3. Latency – Delays in blocking limit effectiveness. It takes time to find the attack and block it. At the time of blocking, maybe it is already too late. 
Evolution of the technology, and merging of firewall and IDS and IPS functionalitare will help solve these problems.

One thing we need to understand is there is no absolute security. With firewalls, IPS and IDS, computers can still be compromised because all the defense measures cannot detect all the attacks. 

# Real-World Examples

### SQL Slammer worm
We now see a real-world attack, <a href="https://www.giac.org/paper/gsec/3091/ms-sql-slammer-sapphire-worm/105136">SQL slammer worm</a>.
On July 24th 2002, Microsoft announced a vulnerability in their SQL server.
On January 25th 2003, the SQL Slammer worm was unleashed.
At 05:29:36GMT, the the SQL Slammer worm was detected for the first time.
It infected more than 90 percent of vulnerable hosts within 10 minutes.

The worm has 376 byte viral payload in a single UDP packet.
It infects machines with a single packet over UDP/1434.
UDP is a broadcast protocol. So it is possible to infect multiple hosts with 1 packet.

What is a computer worm? It is a malware program.
A worm can send itself to a vulnerable server and compromise it.
Once the worm compromises the server, the worm code runs again, trying to find other vulnerable computers on the Internet.
Therefore, the worm can propagate itself to many computers, from one computer to another computer.
The number of infected computers grows exponentially.
That's why we call this as a worm because this type of malware program can propagate itself autonomously.

### How to stop SQL Slammer?
The vulenrable SQL server shall be patched. In 2002, patching was not so smart. Today, pacthing is made automatic.

Firewall can be used to block SQL worm packets to UDP/1434. We may use a VPN for access to sensitive services, not exposing servers to the internet.

We may use intrusion detection and prevention techniques. UDP/1434 is a well known protocol. It was a well known vulnerability and known 6 months before exploit. People just did not care!
IDP signatures can detect and block exploits of this vulnerability.
The size of the packet is anomalous behavior.
Zero-Latency Active IDS/IDP is the only way of blocking this worm.

## Wireshark
let's talk about wireshark.
It is a software program.
It can capture network packets coming into and going out of your computer and show all the packets.\
The picture below is the Wireshark interface.
There are different network cards.
For example, we choose to monitor the *Ethernet* card. All packets into and out of this card will be captures.

<img src="../Imgs/Wireshark-Ethernet.png" width=640>

Double click on the network interface, e.g., *Ethernet*. The capturing starts.
The picture below shows the interface of the capturing window, command menus, display filter. listing of
captured packets, details of selected packet header, and binary packet content.

<img src="../Imgs/Wireshark-Panels.png" width=640>

The display filter is useful because there's so much traffic sometimes.
You don't want to see all the packets sometimes.
You can actually set up a filter to show what you want to see.
In the filer expression, ip.source refers to the source ip (10.0.2.16).
The destination ip is the 10.0.2.13.

The details of a selected packet header are shown in a panel.
When you click a packet, Wireshark will show you the headers of the packet.
You can see here there's a lot of headers.
A header can have many fields. For example, the IP header has the source and destination IP addresses.
That is one power of Wireshark.
It shows your the names of those fields to help you understand the protocols a bit easier.
When you learn the Internet, Wireshark will help you a lot telling you
what each field means and what is the the name.

The binary content of the entire packet is shown in the bottom panel, including all the headers.

## Hands-on
Deploy knock attack against Windows VM. 
Use Wireshark to capture the attack traffic.
Can you find the attack packets sent from Kali VM to Windows VM?

