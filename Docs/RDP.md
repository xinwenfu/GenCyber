This doc instroduces the installation and use of the Remote Desktop Protocol (RDP) app on Windows and MacOS.

# Install RDP

## Windows

1. Click and run Microsoft Store
2. Search and install "Microsoft Remote Desktop"
3. Launch the installed "Microsoft Remote Desktop"

## Mac OS X
Download and install “Microsoft Remote Desktop” from the Apple App Store

# Use RDP

1. Open the RDP app
2. Click on the + icon in the top panel to “Add PC”
3. Enter the IP address for the VM you want to connect to in the “PC name” box
4. Click “Add”
5. To connect to the VM over RDP, simply double click on the saved PC and then enter credentials when prompted

If the connection is very slow, you may need to change the resolution of the remote desktop. Here is how to do so:
1. Exit your RDP session
2. Click on the edit icon on the saved PC to “Edit PC”
3. Click the “Display” tab
4. Under “Resolution”, move the bar so that it says “1280 by 1024” and click “Save”
5. Now connect to the VM again, following the steps from earlier

# References

[How to Setup Xrdp over Xorg in Linux with Multi Sessions](https://c-nergy.be/blog/?p=16698)
[xRDP – Allow multiple sessions (local and remote) for the same user – HowTo]()
