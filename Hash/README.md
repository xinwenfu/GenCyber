## Hands-on

### Hands-on 1: MD5 Hash

#### One student as Sender
- Compute hash of a *message* you choose
```
echo -n "message" | md5sum
```
- Send message and its hash to chat server in the format of message>>>hash or chosen format to ensure you can tell which part is message and which part is hash.

#### Another student as Receiver
- Compute hash of received message locally (md5sum)
```
echo -n "received-message" | md5sum
```
Replace *received-message* with the actual message that was sent over
- Compare newly computed hash with the hash sent over
- Discuss why hash only is not good for message integrity verification

### Hands-on 2: HMAC
#### One student as Sender
- Share a secret key (a string) with Receiver offline (e.g., Discord private message)
- Compute hmac of a message
```
echo -n "message" | openssl sha1 -hmac "key"
```
*sha1* refers to the sha1 hash algorithm; "key" is the chosen key.
- Send the message and hmac to the chat server in the format of message>>>hmac or your chosen format 

#### Another student with the key as Receiver
- Compute hmac of received message locally
```
echo -n "received-message" | openssl sha1 -hmac "key"
```
- Compare newly computed hmac with the received hmac

## Hands-on 3: Password Cracking
John the ripper---password cracking tool. Refer to <a href="https://www.openwall.com/john/doc/EXAMPLES.shtml">Example use</a>

Run the following command, where mypasswd is the password hash file in the required format, to crack password hashes and obtain original password.
```
john mypasswd
```
This command will try the *single crack* mode first, then use a wordlist (i.e. a dictionary of password; default password list at /usr/share/john/password.lst), and finally go for "incremental" mode
Please refer to MODES for more information on these modes.

If you ran the command before and got some passwords cracked, use the following command to show cracked passwords
```
john --show mypasswd
```
- Cracked passwords are stored in $JOHN/john.pot (~/.john/john.pot in kali) in a specific format.
- Delete john.pot in order to crack again
```
rm ~/.john/john.pot
```

- Test security of your own password
Create your password hash by replacing abc123 with your own password
```
openssl passwd -1 -salt RnYtvEVV abc123
```
Replace a hash in mypasswd with the output above
