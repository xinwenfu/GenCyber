# Penetration Testing

In penetration testing, an ehtical hacker (or security consultant) hacks computers per the request of the owner of the computers. The goal is to find vulnerabilities of the target computers so that the owner can perform remedies, for example, patching the software of interest and enhancing network security.

Penetration testing has three phases
- Information collecting. Find the information of the target computers, e.g., IP addresses of those computers.
- Exploitation. Exploit the computers and find real vulnerabilities
- Post exploitation. Perform post exploitation of the compromised computers, e.g. collecting passwords to show evidences of vulnerabilities.

# Field Trip

In this field trip, students will use a tool called *Armitage* to perform the three phases of penetration testing. Our lab is set up as follows. 
- We use two virtual machines (VMs), *Kali-Fu* (Kali Linux) and *Metasploitable* (Linux full of vulnerabilities), managed by *Oracle VM VirtualBox Manager*. Virutal machines work like real computers, but they are not physical computers and run on a real physical computer. For example, in our setup, a computer running the Kubuntu Linux actually hosts and runs Kali-Fu and Metasploitable.
- Kali-Fu will be the attacking computer and Metasploitable will be the target.
- Armitage is launched from Kali-Fu and exploits a vulnerability in Metasploitable.

## Lab Setup: Start Kali-Fu and Metasploitable on Host Computer
The host computer runs the [operating system](https://en.wikipedia.org/wiki/Operating_system) called [Kubuntu](https://en.wikipedia.org/wiki/Kubuntu). Kali-Fu runs [Kali Linux](https://en.wikipedia.org/wiki/Kali_Linux). [Metasploitable](https://docs.rapid7.com/metasploit/metasploitable-2-exploitability-guide/) is a version of Ubuntu Linux and intentionally made vulnerable.

1. Log into a Cyber Range PC with the provided username and password.

2. Click *Application Launcher*.

<img src="imgs/KubuntuScreen.PNG">

3. Click *Search...*, type "Virtual" and Click "VirtualBox" in the search results to launch *Oracle VM VirtualBox Manager*.

<img src="imgs/KubuntuSearch.PNG">

4. *Oracle VM VirtualBox Manager* now shows up. 
   - Click to select the virtual machine *Kali-Fu* and then click "Start" to start the Kali Linux virtual machine.
   - Click to select the virtual machine *Metasploitable* and then click "Start" to start the Metasploitable Linux virtual machine.

<img src="imgs/KubuntuVirtualBox.PNG">

5. Log into the Kali Linux with the following credentials. 
   - Username: kali
   - Password: kali
   - Note: Click Kali on the taskbar if you cannot find it

<img src="imgs/KubuntuKali.PNG">

## Collecting Information about Metasploitable

6. Log into the Metasploitable Linux with the following credentials. In real world, we can use a variety of tools such as *nmap* to find the IP address of Metasploitable. For simplicity, we will just log into Metasploitable and use a command to find its IP address.
   - Username: msfadmin
   - Password: msfadmin
   - Note: Click Metasploitable on the taskbar if you cannot find it

<img src="imgs/KubuntuMetasploitable.PNG">

7. Within the Metasploitable console, enter the command *ifconfig* and then press the *Enter* key to find the IP address of Metasploitable

<img src="imgs/KubuntuMetasploitable-ifconfig.PNG">

8. Within the Kali GUI (Graphical User Interface), click *Applications*, then *08 - Exploitation Tools*, and then *Armitage* to start the software *Armitage*. We are going to use Armitage to find what networking services/applications are running on Metasploitable.

<img src="imgs/KubuntuKali-StartArmitage.PNG">

9. A few dialog windows show up one by one
   - In the dialog window *Authentication is needed ...*, enter the password *kali*
   - In the dialog window "Connect...", click the "Connect" button
   - In the dialog window "Start Metasploit?", click the "Yes" button
   - Wait for the "Progress..." to disappear and Armitage window to show up

10. Within the Armitage window, click *Hosts* and then *MSF Scans...*

<img src="imgs/KubuntuKali-ArmitageWindow.PNG">

11. In the dialog window *Input*, enter the IP address of the "Metasploitable" Linux and click the *Ok* button

<img src="imgs/KubuntuKali-ArmitageInput.PNG">

Armitage shows the found computer icon (with the IP address of Metasploitable) and what network applications/services (programs that can accept messages from the Internet/network) are running.

<img src="imgs/KubuntuKali-ArmitageFoundServices.PNG">

## Exploitation

Metasploitable has a vulnerability called *UnrealIRCD 3.2.8.1 Backdoor*. We will exploit it so as to log into Metasploitable later.

12. Click *Attacks* and then *Find Attacks*. Wait for the dialog window *Progress...* to disappear. A dialog Window *Message* shows up then. Click *Ok*.

<img src="imgs/KubuntuKali-ArmitageFindAttacks.PNG">

13. Right click the found computer icon, Click *Attack* -> *irc* -> *unreal_ircd_3281_backdoor*

<img src="imgs/KubuntuKali-ArmitageIRC.PNG">

14. In the dialog window *UnrealIRCD 3.2.8.1 Backdoor Command Execution*, check the checkbox *Use a reverse connection* and then click the *Launch* button

<img src="imgs/KubuntuKali-Armitage-IRCConfig.PNG">

If thigns go well, a lighting icon shows on the found computer icon and it means the found computer is compromsied.

<img src="imgs/KubuntuKali-Armitage-IRCResult.PNG">

## Post Exploitation

The Metasploitable VM is now compromised. We can log into Metasploitable and do a lot of things. For example, we can list what contents the computer has. Even worse, we can fetch the password file.

15. Right click the found computer icon, then click *Shell 1* -> *Interact*

<img src="imgs/KubuntuKali-Armitage-IRC-Shell.PNG"> 

A *Shell 1* console appears

<img src="imgs/KubuntuKali-Armitage-IRC-Shell1-Console.PNG"> 

16. Within the *Shell 1* console, type the following command. The purpose is to show we can list the content of a folder in the compromised computer.
```
ls /home/msfadmin
```

What is the output of this command?
