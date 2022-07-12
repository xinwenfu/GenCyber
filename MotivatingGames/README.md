## Motivating game - Denial of service (DoS)

In our lecture on <a href="https://github.com/xinwenfu/GenCyber/tree/main/SoftwareSecurity">Penetration Testing and Software Security</a>, we have exploited the vulnerable chat server (vchat) and deployed the buffer overflow attack against vchat. We were able to hack into the Windows VM through vchat.

The same vulnerability can be exploited for denial of service (DoS) attack. In the DoS attack, the attacker sends a long message with garbage content, which overwrites the buffer and contents above the buffer as shown in the figure below. This messes up the function return address with garbage data. Now when the function returns, it returns to nowhere and vchat actually crashes because of this.   

<img src="../Imgs/BufferOverflow-junk.png" width=480>

Play the DoS game

1. The instructor or volunteer starts a vulnerable chat server C:\Tools\vchat\Server\vchat.exe
   - Announce the IP of Windows VM running *vchat*
2. Everybody runs /home/kali/GenCyber/vchat/Client/client.py to chat with each other
   - Wait for everybody to send at least one message
3. Do not proceed further without the instructor's permission
4. Now anybody can deploy the DoS attack
   - Use armitage to scan the target Windows VM and find attacks
   - Click the found Windows VM (IP)
   - Deploy auxillary/dos/vchat/DoS
