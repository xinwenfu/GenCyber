## Hands-on

### Hands-on 1: Use RSA to Encrypt and Decrypt a Message
1. Generate Public and Private Key Pair
```
openssl genpkey -out privkey.pem -algorithm rsa
```
- *<a href="https://www.openssl.org/docs/manmaster/man1/openssl-genpkey.html">openssl genpkey</a>*: Generate a private key
- The created privkey.pem can be used as the private key although it contains the public key
- *-out outfile*: Output file, privkey.pem in this case, which stores the private key
- *-algorithm val*: The public key algorithm, *rsa* in this case 

2. Extract public key from privkey.pem and save it in pubkey.pem
```
openssl rsa -in privkey.pem -outform PEM -pubout -out pubkey.pem
```
- *<a href="https://www.openssl.org/docs/manmaster/man1/openssl-rsa.html">openssl rsa</a>*: RSA related operations
- *-in filename/uri*: the input to read a key from, privkey.pem in this case
- *-outform DER/PEM*: The key output format, PEM in this case
- *-pubout*: a public key will be output
- *-out filename*: The output filename to write a key, pubkey.pem in this case

3. Create a file
```
echo "Welcome to LinuxCareer.com" > encrypt.txt
```
- *<a href="https://www.guru99.com/linux-redirection.html"> > </a>*: Redirect the output, in this case to a file, encrypt.txt

4. Encryption
```
openssl rsautl -encrypt -inkey pubkey.pem -pubin -in encrypt.txt -out encrypt.dat
```
- *<a href="https://linux.die.net/man/1/rsautl">rsautl</a>*: sign, verify, encrypt and decrypt data using the RSA algorithm
- *-encrypt*: encrypt the input data using an RSA public key
- *-inkey file*: input key file
- *-pubin*: input file is an RSA public key
- *-in filename*: input filename to read
- *-out filename*: output filename to write to

5. Encode the binary ciphertext with base64
Encoding with base64 is not necessary, but needed for sending the ciphertext through our chat server
```
openssl enc -base64 -in encrypt.dat -out encrypt.dat.base64
```
- encrypt.dat is binary 
- encrypt.dat.base64 is printable

6. Decryption with RSA
- Decode encrypt.dat.base64 and get the binary ciphertext 
```
openssl enc -base64 -d -in encrypt.dat.base64 -out encrypt.dat
```
- Decryption
```
openssl rsautl -decrypt -inkey privkey.pem -in encrypt.dat -out new_encrypt.txt
```

### Hands-on 2: RSA Encrypted Message through Chat Server
- Use OpenSSL and RSA to encrypt a message
  - The message can be saved in a file first
- Send the message via the chat server
- Use OpenSSL and RSA to decrypt the ciphertext

### Hands-on 3: RSA
Consider RSA with p = 5 and q = 11.
- What are n and z?
- Let e be 3. Find d such that de = 1 (mod z). 
- Encrypt the message m = 8 using the key (n, e). Let c denote the corresponding ciphertext.
- Decrypt the ciphertext. 
