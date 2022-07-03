## Hands-on
Although the hands-on lab can be done by one person, we highly recommend one student signs the message, and another student verifies the signature.

### Hands-on 1: Windows 10 Certificate Store
- Please click on the Windows *Start* icon. In *Type here to search*, type and search *certmgr.msc*, which is the Windows 10 certificate store
- All people check content of a certificate from Trusted Root Certificate Authorities
- Discussion: why are these certificates needed?

### Hands-on 2: Generate Public and Private Key Pair
- If done before, no need 
- Generate public and private key pair
```
openssl genpkey -out privkey.pem -algorithm rsa
```
Note: privkey.pem can be used as the private key although it contains the public key.

- Extract the public key from privkey.pem
```
openssl rsa -in privkey.pem -outform PEM -pubout -out pubkey.pem
```

- Publish your pubkey.pem, e.g. via our chat server
- Never share privkey.pem

### Hands-on 3: Sign a file at Your Computer
- Sign a file called changelog or messages saved in a file
```
openssl dgst -sha256 -sign privkey.pem -out sign.sha256 changelog
```
The output sign.sha256 is binary

- Encode the binary signature with base64
```
openssl enc -base64 -in sign.sha256 -out sign.sha256.base64
```
Not really needed. It is needed here since we can send the base64 encoded message to our chat server

- Send both message and base64 encoded signature to our chat server

### Hands-on 4: Verify the Signature
- Save received signature into a file, e.g., called sign.sha256.base64

- Decode sign.sha256.base64 and get the binary signature
```
openssl enc -base64 -d -in sign.sha256.base64 -out sign.sha256
```

- Verify the signature with the public key
```
openssl dgst -sha256 -verify pubkey.pem -signature sign.sha256 changelog
```
