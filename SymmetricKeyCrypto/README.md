Hands-on 1: Encryption with AES
Encrypt a message like "OpenSSL"
```
echo "OpenSSL" | openssl enc -iter 1000 -aes-256-cbc -a -k hello
```
- -k hello: The key will be generated from hello 
Without -k hello, the command will ask for a password, which will be translated into a key 
- -iter 1000 is related to creating a strong key from the password 
- -a: means BASE64 output
