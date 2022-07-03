## Hands-on

### Hands-on 1: Common Linux command line terminal commands
Refer to <a href="https://linuxconfig.org/linux-commands-cheat-sheet">Linux commands cheat sheet</a>. Try the following Linux command line terminal commands and understand what they do. *Terminal Emulator* is Kali Linux's terminal program. 
1. <a href="https://man7.org/linux/man-pages/man1/touch.1.html">touch</a>: change file timestamps or create a new file
```
touch test1 # create an empty file called test1
```
2. <a href="https://man7.org/linux/man-pages/man1/ls.1.html">ls</a>: list files in a folder; current folder by default
```
ls # show files in current workng folder
```
where # indicates a comment and does not need to be entered
2. <a href="https://man7.org/linux/man-pages/man1/pwd.1.html">pwd</a>: print full path name of current working folder
```
pwd # show the name of current working folder 
```
3. <a href="https://man7.org/linux/man-pages/man1/cd.1p.html">cd</a>: change the working folder to another folder
```
cd .. # go to parent folder of current working folder
cd GenCyber # go to the GenCyber folder, which is a sub-folder of current working folder
cd /home/kali # go to folder /home/kali, which is a full path name
```
4. <a href="https://man7.org/linux/man-pages/man1/mkdir.1.html">mkdir</a>: create folders
```
mkdir mine # create a folder called mine in the current working folder
```
5. <a href="https://man7.org/linux/man-pages/man1/rm.1.html">rm</a>: remove files
```
rm test # remove a file called test
rm -r mine # remove a folder called mine and all its subfolders in the current working folder
```
6. <a href="https://linux.die.net/man/1/mv">mv</a>: move files or folders
```
mv test1 tset2 # move test1 to test2; no test1 any more
```
7. <a href="https://man7.org/linux/man-pages/man1/cp.1.html">cp</a>: copy files or folders
```
cp test2 test3 # copy test2 to test3; test2 still exists
```
8. <a href="https://man7.org/linux/man-pages/man8/ifconfig.8.html">ifconfig</a>: configure or show info of a network interface
```
ifconfig # show information of network interfaces
```
