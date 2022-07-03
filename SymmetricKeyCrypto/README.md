## Hands-on

### Hands-on 1: Decipher Caesor cipher encrypted text

#### Ciphertext
The plaintext is English paragraphs, encypted with Caesar Cipher of a particular shift. Ciphertext is shown below.
```
Qb qa i xmzqwl wn kqdqt eiza qv bpm oitifg. I jzidm ittqivkm wn cvlmzozwcvl nzmmlwu nqopbmza pia kpittmvoml bpm bgzivvg ivl wxxzmaaqwv wn bpm iemawum OITIKBQK MUXQZM.

Abzqsqvo nzwu i nwzbzmaa pqllmv iuwvo bpm jqttqwv abiza wn bpm oitifg, zmjmt axikmapqxa pidm ewv bpmqz nqzab dqkbwzg qv i jibbtm eqbp bpm xwemznct Quxmzqit Abizntmmb. Bpm MUXQZM nmiza bpib ivwbpmz lmnmib kwctl jzqvo i bpwcaivl uwzm awtiz agabmua qvbw bpm zmjmttqwv, ivl Quxmzqit kwvbzwt wdmz bpm oitifg ewctl jm twab nwzmdmz.

Bw kzcap bpm zmjmttqwv wvkm ivl nwz itt, bpm MUXQZM qa kwvabzckbqvo i aqvqabmz vme jibbtm abibqwv. Xwemznct mvwcop bw lmabzwg iv mvbqzm xtivmb, qba kwuxtmbqwv axmtta kmzbiqv lwwu nwz bpm kpiuxqwva wn nzmmlwu.
```

#### Tools to use for decryption
- <a href="https://www.dcode.fr/frequency-analysis">Frequency analysis</a>
- <a href="https://www.usna.edu/Users/cs/wcbrown/courses/si110AY13S/resources/ceasar-shift/shiftTable.html">Ceasar Shift Table</a>

What is the plaintext message?

### Hands-on 2: Encryption with AES
Encrypt a message like "OpenSSL"
```
echo "OpenSSL" | openssl enc -iter 1000 -aes-256-cbc -a -k hello
```
- *echo "OpenSSL"*: display a message, in this case, "OpenSSL"
- *|*:  with the pipe character ‘|’, the output of one command (*echo "OpenSSL"* in this case) acts as input to another command (*openssl ...* in this case)
- *<a href="https://wiki.openssl.org/index.php/Command_Line_Utilities">openssl</a> <a href="https://wiki.openssl.org/index.php/Enc">enc</a>*: *Enc* is used for block and stream ciphers using password based keys or explicitly provided keys. Can be used for Base64 encoding or decoding.
- *-k hello*: The key will be generated from hello 
Without -k hello, the command will ask for a password, which will be translated into a key 
- *-iter 1000* is related to creating a strong key from the password 
- *-a*: means BASE64 output

### Hands-on 3: Decryption with AES
Decrypt the encrypted message
```
echo "U2FsdGVkX1+lVCnMEVpKXisqA1IlycMvDFkv72ILasg=" | openssl enc -aes-256-cbc -iter 1000 -a -d -k hello
```
- *-d*: means decryption
- *-a*: means BASE64 encoded input
- *-k hello*: hello was used to generate the key

### Hands-on 4: Encrypting and Decrypting File with AES
Encrypt a file
```
openssl aes-256-cbc -a -salt -in secrets.txt -out secrets.txt.enc -iter 1000 -k hello
```
Decrypt the encrypted file
```
openssl aes-256-cbc -d -a -in secrets.txt.enc -out secrets.txt.new -iter 1000 -k hello
```

### Hands-on 4: Send Encrypted Message via Chat Server
- One person encrypts messages and sends
- The other person receives encrypted messages and decrypts

## References
- <a href="https://cryptii.com/pipes/caesar-cipher">Caesar cipher tools</a>
