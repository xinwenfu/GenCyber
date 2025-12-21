# Lab environment
We use Virtual Machines (VMs) or all the labs. All VMs are tested for [VirtualBox](https://www.virtualbox.org/wiki/Downloads).

## Install VirtualBox 

VirtualBox can be installed on a personal computer like Windows. It is a challenge to install VirtualBox on new Apple computers. Therefore, we use Windows as the example to show how the installation can be done.

Here are the steps to start (Click the links embedded in the blue and unlined text to watch videos):
1.	Install VirtualBox on [Windows](https://www.youtube.com/watch?v=8mns5yqMfZk).
2.	Download the .ova ((Open Virtual Appliance) file
   * [Kali]() 
4.	Import .ova file into VirtualBox
5.	If a student feels the VM is slow, please watch How to Speed up your VMs in VirtualBox! For Windows and How to improve Linux performance in a VirtualBox VM.

Try the following four networking options on these two VMs [3]: 
1.	Network Address Translation (NAT)
2.	NAT Network
3.	Bridged Adapter
4.	Internal Network
5.	Host-only Adaptor


## Download VMs
- <a href="[https://www.cs.uml.edu/~xinwenfu/VMs/Kali-CR-25G.ova](https://www.cs.uml.edu/~xinwenfu/VMs/Kali-40G-2025.ova)">Customized Kali VM</a>, which incldues customized Armitage and our Metasploit modules against the <a href="https://github.com/xinwenfu/vchat">vulnerable chat server</a>
  - Username: kali
  - Password: kali
  - Sudo password: kali

- Windows VM cannot be shared. But really only the vulnerable chat server <a href="https://github.com/xinwenfu/vchat">vchat</a> is needed. For demo purpose, Windows defense shall be disabled.
  - Turn off Windows Defenser Firewall.
  - Turn off Windows Exploit Protection.
  - Turn off the virus <a href="https://support.microsoft.com/en-us/windows/turn-off-defender-antivirus-protection-in-windows-security-99e6004f-c54c-8509-773c-a4d776b77960">real time protection</a>. The real-time protection is automatically turned on frequently by Windows, for example at a restart or after some time it was turned on.

## Import VMs into VirtualBox
Here are the steps to start (Click the links embedded in the blue and unlined text to watch videos):
1.	Install VirtualBox on [Windows 10](https://www.youtube.com/watch?v=8mns5yqMfZk) and [Mac OS X](https://www.youtube.com/watch?v=lEvM-No4eQo).
2.	[Import .ova](https://youtu.be/us5N0X75v-o) file into VirtualBox
3.	If a student feels the VM is slow, please watch [How to Speed up your VMs in VirtualBox](https://www.youtube.com/watch?v=2z7icd0vm0M)! For Windows and [How to improve Linux performance in a VirtualBox VM](https://www.youtube.com/watch?v=tbF8jNjD_IE).
