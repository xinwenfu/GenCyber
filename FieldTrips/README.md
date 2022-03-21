1. Log into a Cyber Range PC with the username *cyberadmin* and provided password
2. Click Application Launcher 

<img src="imgs/KubuntuScreen.PNG">

3. Click *Search...*, type "Virtual" and Click "VirtualBox" in the search results

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

6. Log into the Metasploitable Linux with the following credentials
   - Username: msfadmin
   - Password: msfadmin
   - Note: Click Metasploitable on the taskbar if you cannot find it

<img src="imgs/KubuntuMetasploitable.PNG">

7. Within the Metasploitable console, enter the command *ifconfig" and *Enter* to find the IP address of the Metasploitable VM

<img src="imgs/KubuntuMetasploitable-ifconfig.PNG">

8. Within the Kali GUI (Graphical User Interface), click *Applications*, then *08 - Exploitation Tools*, and then *Armitage* to start the software *Armitage*

<img src="imgs/KubuntuKali-StartArmitage.PNG">

9. A few dialog windows show up
   - In the dialog window *Authentication is needed ...*, enter the password *kali*
   - In the dialog window "Connect...", click the "Connect" button
   - In the dialog window "Start Metasploit?", click the "Yes" button
   - Wait for the "Progress..." to disappear and Armitage window to show up

10. Within the Armitage window, click *Hosts* and then *MSF Scans...*

<img src="imgs/KubuntuKali-ArmitageWindow.PNG">

11. In the dialog window *Input*, enter the IP address of the "Metasploitable" Linux and click the *Ok* button

<img src="imgs/KubuntuKali-ArmitageInput.PNG">

Armitage shows what services (programs that can accept messages from the Internet/network) are running.

<img src="imgs/KubuntuKali-ArmitageFoundServices.PNG">

12. Click *Attacks* and then *Find Attacks*. Wait for the dialog window *Progress...* to disappear. A dialog Window *Message* shows up then and click *Ok*.

<img src="imgs/KubuntuKali-ArmitageFindAttacks.PNG">

13. Right click the computer icon, Click *Attack* -> *irc* -> *unreal_ircd_3281_backdoor*

<img src="imgs/KubuntuKali-ArmitageIRC.PNG">

14. In the dialog window *UnrealIRCD 3.2.8.1 Backdoor Command Execution*, check the checkbox *Use a reverse connection* and then click the *Launch* button

<img src="imgs/KubuntuKali-Armitage-IRCConfig.PNG">

If thigns go well, a lighting icon shows on the found computer icon

<img src="imgs/KubuntuKali-Armitage-IRCResult.PNG">

15. Right click the found computer icon, then *Shell 1* -> *Interact*

<img src="imgs/KubuntuKali-Armitage-IRC-Shell.PNG"> 

A *Shell 1* console appears

<img src="imgs/KubuntuKali-Armitage-IRC-Shell1-Console.PNG"> 

16. Within the *Shell 1* console, type the following command
```
ls /home/msfadmin

