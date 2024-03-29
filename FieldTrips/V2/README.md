# Penetration Testing

In penetration testing, an ehtical hacker (or security consultant) hacks computers per the request of the owner of the computers. The goal is to find vulnerabilities of the target computers so that the owner can perform remedies, for example, patching the software of interest and enhancing network security.

Penetration testing has three phases
- **Information collecting**. Find the information of the target computers, e.g., IP addresses of those computers.
- **Exploitation**. Exploit the computers and find real vulnerabilities
- **Post exploitation**. Perform post exploitation of the compromised computers, e.g. viewing contents of files and collecting passwords to show evidences of vulnerabilities.

Below is a video demo showing how to use a Kali VM to attack a Windows VM, which runs a vulnerbale chat server (vchat).

[![Armitage](https://img.youtube.com/vi/TJX__HPo9jQ/0.jpg)](https://youtu.be/TJX__HPo9jQ)


# Field Trip

In this field trip, students will use a tool called *Armitage* to perform the three phases of penetration testing. Our lab is set up as follows. 
- We use two virtual machines (VMs), *Kali* (Kali Linux) and *Windows 10*, managed by *Oracle VM VirtualBox Manager*. Virutal machines work like real computers, but they are not physical computers and run on a real physical computer. For example, in our setup, a computer running the Kubuntu Linux actually hosts and runs Kali and Windows VMs.
- Kali will be the attacking computer and Windows will be the target.
- Armitage is launched from Kali and exploits a vulnerability in a chat server called vchat.exe.

## Setting Up the Lab: Start Kali and Windows VMs on Host Computer
The host computer (i.e., the physical computer) runs the [operating system](https://en.wikipedia.org/wiki/Operating_system) called [Kubuntu](https://en.wikipedia.org/wiki/Kubuntu). Kali runs [Kali Linux](https://en.wikipedia.org/wiki/Kali_Linux), a version of Debian Linux.

1. Log into a Cyber Range PC with the **provided username and password**.

2. Click *Application Launcher*.

<img src="../imgs/KubuntuScreen.PNG" width="640">

3. Click *Search...*, type "Virtual" and Click "VirtualBox" in the search results to launch *Oracle VM VirtualBox Manager*.

<img src="../imgs/KubuntuSearch.PNG" width="640">

4. *Oracle VM VirtualBox Manager* now shows up. 
   - Click to select the virtual machine *Kali* and then click "Start" to start the Kali Linux virtual machine.
   - Click to select the virtual machine *Windows* and then click "Start" to start the Widnows VM.

<img src="../imgs/KubuntuVirtualBox.PNG" width="640">

5. Log into the Kali Linux with the following credentials. 
   - Username: kali
   - Password: kali
   - Note: Click Kali on the taskbar if you cannot find it

<img src="../imgs/KubuntuKali.PNG" width="640">

**Question**: 
- How can you find the IP address of Kali? 
  - Answer: Start a *Terminal Emulator* and type the command *ifconfig* and then enter.
- What is the IP address of the Kali VM?

## Collecting Information about Windows VM

6. Log into the Windows VM with provided password and then run the chat server
   - Click C:\Tools\vchat\Server\vchat.exe and run the chat server

8. Disable Windows *Real-time protection* against virus & threat:
   - Enter *Exploit* in *Type here to search* at the bottom left of the Windows desktop. 
   - Click *Exploit protection* system settings in found items. 
   - In the *Windows Security* window, click *Virus & threat protection* &rarr; *Virus & threat protection settings* &rarr; *Manage settings*
   - In the window of *Virus & threat protection settings*, turn off *Real-time protection* 
   - If the window of *User account control* pops up, click *Yes*

9. Within the Kali GUI (Graphical User Interface), click *Applications* &rarr; *08 - Exploitation Tools* &rarr; *Armitage* to start the software *Armitage*. We are going to use Armitage to find what networking services/applications are running on Metasploitable.

<img src="../imgs/KubuntuKali-StartArmitage.PNG" width="640">

10. A few dialog windows show up one by one
   - In the dialog window *Authentication is needed ...*, enter the password *kali*
   - In the dialog window "Connect...", click the "Connect" button
   - In the dialog window "Start Metasploit?", click the "Yes" button
   - Wait for the "Progress..." to disappear and Armitage window to show up

11. If there are previous results showing computer icons within Armitage, click *Hosts* &rarr; *Clear Database* for cleanup.

12. Within the Armitage window, click *Hosts* &rarr; *MSF Scans...*

13. In the dialog window titled *Input*, enter 10.0.2.0/24 and click the *Ok* button
    - 10.0.2.0/24 represents the IPv4 addresses from 10.0.2.0 to 10.0.2.255. That is, Armitage will check all those IP addresses and see which one is active.

Armitage shows the found computer icon (with the IP address of Metasploitable) and what network applications/services (programs that can accept messages from the Internet/network) are running.

<img src="https://user-images.githubusercontent.com/69218457/224392646-1f02980e-1aa3-4729-aa9a-05ae3fbe76aa.png" width="640">

**Question**: Which found IP belongs to the Windows VM?
- Click a found IP, perform *Hosts* &rarr; *Nmap Scan* &rarr; *Quick Scan (OS detect)* to find the OS running at an IP.

## Exploitation

vchat.exe on Windows VM has a vulnerability. We will exploit it so as to log into the Windows VM.

14. Click the Windows VM icon within Armitage. Click *Attacks* &rarr; *Find Attacks*. Wait for the dialog window *Progress...* to disappear. A dialog Window *Message* shows up then. Click *Ok*.

15. Right click the found computer icon, Click *Attack* &rarr; *vchat* &rarr; *knock*

16. In the dialog window *vulnserver Buffer Overflow-KNOCK command*, click *launch*

If things go well, a lighting icon shows on the found computer icon and it means the found computer is compromsied.

<img src="https://user-images.githubusercontent.com/69218457/224389016-da1c6992-5190-4b67-9e0b-42944cb17ef7.png" width="640">

**Note**: If the attack does not work, just try *launch* a number of times (e.g., 10 times), it will work.

## Post Exploitation

The Windows VM is now compromised. We can log into Windows VM and do a lot of things. We will just look at some files.

17. Right click the found computer icon, then click *Meterpreter xxx* &rarr; *Interact* &rarr; *Meterpreter Shell*, where *xxx* refers to a session number, e.g., 1. A Meterpreter shell shows up at the bottom of Armitage.

18. Within Meterpreter shell console, type the following commands. 
    - *ls*: show the files in the current folder
    - *cat LICENSE.TXT*. Show the content of LICENSE.TXT.

**Question**: According to LICENSE.TXT, who has the copyright (of vulnserver)?
