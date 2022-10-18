# Lab environment
We use VMs for all the labs. All VMs are tested for VirtualBox.

- <a href="https://www.cs.uml.edu/~xinwenfu/VMs/Kali-CR-25G.ova">Customized Kali VM</a>, which incldues customized Armitage and our Metasploit modules against the <a href="https://github.com/xinwenfu/vchat">vulnerable chat server</a>
  - Username: kali
  - Password: kali
  - Sudo password: kali
- <a href="https://www.cs.uml.edu/~xinwenfu/VMs/Metasploitable-CR.ova">Metasploitable 2</a>
  - Username: msfadmin
  - Password: msfadmin
  - Sudo password: msfadmin
- Windows VM cannot be shared. But really only the vulnerable chat server <a href="https://github.com/xinwenfu/vchat">vchat</a> is needed. For demo purpose, Windows defense shall be disabled.
  - Turn off Windows Defenser Firewall
  - Turn off the virus <a href="https://support.microsoft.com/en-us/windows/turn-off-defender-antivirus-protection-in-windows-security-99e6004f-c54c-8509-773c-a4d776b77960">real time protection</a>. The real-time protection is automatically turned on frequently by Windows, for example at a restart or after some time it was turned on.
