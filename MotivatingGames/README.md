## Motivating game - Denial of service (DoS)

In our lecture on <a href="https://github.com/xinwenfu/GenCyber/tree/main/SoftwareSecurity">Penetration Testing and Software Security</a>, we have exploited the vulnerable chat server (vchat) and deployed the buffer overflow attack against vchat. We were able to hack into the Windows VM through vchat.

The same vulnerability can be exploited for denial of service (DoS) attack. In the DoS attack, we send a long message with garbage content and overwrite the buffer and contents above the buffer. This messes up the function return address and with garbage data. Now when the function returns, it returns to nowhere and vchat actually crashes because of this.   

<img src="../Imgs/BufferOverflow-junk.png" width=512>
