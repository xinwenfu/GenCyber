# Introduction to asymmetric cryptography

TO BE EDITTED

We are first going to discuss different type of cryptography.
Next we introduce the public key crypto.
One example of public key crypto is RSA. So we are
going to discuss a little bit more about RSA and see how it works.
OpenSSL implements a lot of cryptographic functions.
We are going to discuss openssl, a command line tool that uses OpenSSL to implement a lot of cryptographic functions, for our hands-on exercises.

## Different types of cryptography

We have discussed the secret key cryptography, i.e., symmetric crypto.
Based on the number of keys we can actually categorize cryptography into three types.
One is the hash functions, which will be introduced in another tutorial.
When we use hash functions, there's no key over there.
The second type of cryptography is a the secret key crypto, in which there's only one key shared by
the sender and the receiver.
The third type is a public key crypto.
In public key crypto, each person or each entity has two keys, (public key, private key).

Before we introduce public key crypto, let's review what we have learned about the secret key crypto.
In the picture below, we have Bob on the left and Alice on the right.
Bob is sending out a message, which is called plaintext, to Alice.
Bob is going to use an encryption algorithm, for example AES, and a secret key
to encrypt the plaintext.
This procedure produces theciphertext.
The ciphertext goes through the Internet and finally arrives at the receiver, Alice.
Alice uses a decryption algorithm and the same
key as the key used by Bob to decrypt the ciphertext and obtain the original plaintext.
This is a basically how we use a secret key crypto algorithm to encrypt a message

<img src="../Imgs/SecretKeyCrypto.png" width=512>

Secret key crypto is also called symmetrical crypto (because of the same key for encryption and decryption by sender and receiver) or conventional crypto (because that was conventionally used by people).

## Public Key Cryptography

### Encryption and Decryption
The picture below shows how encryption and decryption are done in public key crypto.
We have again Bob on the left and Alice  is on the right.
In any scenario of public key crypto, each person or entity has two keys.
Here Bob has the public and private key pair (e<sub>B</sub>, d<sub>B</sub>),
where e<sub>B</sub> is Bob's public key and d<sub>B</sub> is his private key.
Like Bob, Alice has her own public and private key pair (e<sub>A</sub>, d<sub>A</sub>), which is different from (e<sub>B</sub>, d<sub>B</sub>).

<img src="../Imgs/AsymmetricCrypto.png" width=512>

Bob is going to send a message *M*, which is the plaintext, to Alice.
Pay attention to how the encryption is done.
Bob needs an encryption algorithm.
But in this case Bob is going to use Alice's public key e<sub>A</sub> for the encryption.
Alice's public key is supposed to be known by anyone.
That is why it is called *public* key.
Bob uses an encryption algorithm and Alice's public key to encrypt the message.
The encryption produces the ciphertext, i.e., e<sub>A</sub>(M), 
which means e<sub>A</sub> is used to encrypt the message *M*.
The ciphertext goes through the Internet and arrives at the receiver Alice.
Alice then uses a decryption algorithm and her private key d<sub>A</sub>, which is different
from her public key, to decrypt the ciphertext and produce the original plaintext, that is, 

d<sub>A</sub>(e<sub>A</sub>(M))=M.

You can see here in public key crypto, 
the encryption and the decryption use different keys.
That's why public key is also called
asymmetrical crypto

Pay attention to the fact that Bob uses Alice's public key (not Bob's keys)
to encrypt the plaintext.

The public key crypto often involve a lot of mathematical calculations, which are time consuming for computers.
As we have learned, encrypton in secret key crypto uses substitutions and permutations, which can be done fast by computers. 
Secret key crypto performs the encryption that doesn't
involve a lot of mathematical calculation.
But public key crypto often involves a lot of
mathematical mathematics, and is often much slower than secret key crypto.

### Applications: Data transmission and secure storate
Let's look at the one application of the public key crypto.
We can use public key crypto for data transformation as the example above shows.
Let's look at another example here.
In this example Alice has a message *M* to send to Bob.
Alice is going to use Bob's public key e<sub>B</sub> to encrypt this message *M*.
The ciphertext e<sub>B</sub>(M) is sent to Bob.
Bob is going to use his private key d<sub>B</sub>( to decrypt this ciphertext and recover the original message, that is,

d<sub>B</sub>(e<sub>B</sub>(M))=M.

You can also use public key crypto for secure storage, storing encrypted data such as files on a hard disk.
You can use your public key to encrypt files other data and then put the encrypted data on your hard disk.
Because only you have the private key, only you can actually decrypt the encrypted data.
That's the idea of secure storage with public key crypto.

## Key exchange
If we have a lot of data to transmit across the Internet,
we actually do not use public crypto because it's too slow.
You don't want to wait for your message to arrive after a long delay, right?
That's why when we need real-time interaction with our receiver,
we are going to use secret key crypto to encrypt messages.

However in secret key crypto when we do encryption and decryption
we need to share the secret key between the sender and the receiver.
But on the Internet, how can we share a key with somebody far away?
Calling somebody is really awkward, not convenient.
How do we actually share a secret key across the Internet?
This problem is called key exchange.

The problem of key exchange can be solved by the public crypto easily.
Let's look at this example here.
We have Alice on the left and Bob on the right.
Alice wants to send a secret key *K* for secret key crypto to Bob.
Alice can just use Bob's public key e<sub>B</sub> to
encrypt this secret key *K* and send e<sub>B</sub>(K) over to Bob.
When Bob receive its, he can use his private key d<sub>B</sub> to decrypt this encrypted secret key and  recover the secret key, that is,

d<sub>B</sub>(e<sub>B</sub>(K))=K.

Once this secret key *K* is shared between Alice and Bob, they can use this secret K to encrypt messages.
Here is an example.
Alice has a message M. She uses K to encrypt M with the AES algorithm.
K(M) is sent to Bob.
When Bob receives it, he can use the shared key K to decrypt the ciphertext, that is

K<sup>-1</sup>(K(M))=M.

Here K<sup>-1</sup> means that K is used to the encrypted message K(M).


### Two Properties of Public Key Crypto

#### d(e(M))=M

A message M can be encrypted with one’s public key e, i.e., e(M).
Only the one’s private key can be used to decrypt e(M), that is, d(e(M))=M.
We have been using this property for encryption and decret for secret message transmission.

#### e(d(M))=M
One can encrypt a message by its private key d, i.e., d(M).
Only the one’s public key can be used to decrypt d(M), that is, e(d(M))=M.

Here is a question for you.
With the second property, can we use this property for secret data transmission?
For example, Alice encrypts a message M with her private key and gets d<sub>A</sub>(M).
She sends the ciphertext to Bob, who can use Alice's public key to decrypt the ciphertext e<sub>A</sub>(d<sub>A</sub>(M))=M. Technically this is fine. Is this secure? If a bad guy over the Internet intercepts the ciphertext during its transmission, can the bad guys decrypt the ciphertext?

### Naive digital signature

The second property of public key crypto is actually the foundation of a critical application, digital signature.
Let's see a naive digital siganture scheme.
In this example Bob wants to publish an announcement M.
He wants to sign the message and let everybody know he makes that announcement.
Everybody can verify he makes that announcement.

How can we produce such a digital signature?
This is how it works.
Bob has the public and the private key pair (e<sub>B</sub>, d<sub>B</sub>).
e<sub>B</sub> is his public key and d<sub>B</sub> is his private key.
Signing the annnoucement M means Bob is going to use his private key to encrypt M.
That is, the digital siganture is d<sub>B</sub>(M).
When bob publishes the annoucement, 
he publishes both M and the digital signature d<sub>B</sub>(M), M | d<sub>B</sub>(M), where | means concatenation.

How can you verify the annoucement is from Bob?
Let's assume you have Bob's public key.
This is how we do it.
Basically anybody can use Bob's public key
to decrypt the digital signature, that is the encrypted annoucement M.
if the decrypted M is the same as the published M, the annoucement M is from Bob
because only Bob's public key can decrypt this encrypted M right.
Then we are sure it is from Bob.

This is a naive digital signature because you can see
here the whole annoucement is encrypted with Bob's private key as the digital signature.
That's not very efficient since the digital siganture too long.
When we discuss hash functions, we will see the real world digital siganture.


one example of a particular crypto and
see how it works so rsa
so rsa
is a one type of a
public key crypto very popular one
let's look at how we use rsa to encrypt
and decrypt message
so when we talk about the message
you know
all the messages all the
docs all the data
are sealed on computer
in final numbers
so whatever the message is just
a sequence of bits
okay
and of course
you can treat
the bs
as messages but
really they are also
final numbers so encrypting a message is
equivalent to encrypting a number
so here is an
example let's see m is one zero one zero
zero one we don't care about what it is
means in terms of messages but anyway so
this is a
equal to a decimal number 145
okay so when we say
we want encrypt m
we actually
encrypt the corresponding number and
this is a about rsa
okay so here
let's first look at
how do we
create
public key and the private key for a
person okay because in public key crypto
we said
everybody
must have a a pair of a public and
private key and so this is all just
calculations so step one we choose two
large prime numbers so what is prime
number a prime number
has only two factors one and itself
okay
then
step two you compute n
and n is equal to p times q that's easy
z is equal to p minus 1 times q minus 1.
that's not hard either
now we choose e
e shouldn't have
common factors with z
right
and so basically
e and z they have only one common
factor
which is one so sometimes we also call
this
e and z are relative prime okay
and then
finally
we choose d
so here the d should be chosen
this way
so
e times d
mod divided right by z
and
you know the remainder is one
okay so this is what we mean by e d
model z equal to one so this is just the
modular calculation means
e d times
e times d
divided by z
and the remainder
is one
remember everything here is like
integers
so we are done with creating the public
private key pair and the public key is n
e
and the private key is nd so you can see
here in rsa
for each key we have two numbers
and uh but anyway you can see here e and
the d
are the critical ones right and the n is
no
as a p times q okay
good so now we know
let's see
n and the e and and the d which are our
which are our public and private key
pair
so good
and now let's look at the encryption and
decryption so we already have an e as
public key and d as private key
so let's see how we
encrypt a message n
is actually quite straightforward so
basically
when we encrypt a message m
we just do the calculation
m to the power of e mod n this will
create the ciphertext c which is also a
number
so good well done with the encryption so
number two i mean step two here
and then to decrypt the received
c here right a number
you just do this you just do
c to the power of d mild m
okay
and then you will recover
the original m y
so when you go to college you will learn
why so this can be proved but
the process is just as simple as that
but you can see here
we involve
the exponential calculation right and so
that's very slow
in computers that's why we said
you know public key crypto is often slow
compared with a
secret key crypto
okay so you can see here we said the
magic happens you know and so that's the
decryption process okay
and uh
good
so this is a one earth example
in this case we use a very small
numbers so you can see p and q
are 5 and 7 respectively and they are
actually prime numbers so then we can
get n equal to 35 z equal to 24 and so
we choose e to equal to five you can see
here
e and z
right here 24 they are relative prime
they have only one common factor one
so then we choose d as 29
so if you actually
do the calculation file times 29
mod
z here it should be 1.
okay
and uh so so basically
the remainder
okay e times d
divided by z
okay and the remainder is one
so good so now we got
an e
and a n d
okay
and so we want to actually encrypt
this message okay and the zero zero
zero
zero one one zero zero okay so this is a
equal to what decimal number twice and
then we do
the encryption so
m
by 12 to the power of
5 right and so this is a the result
now if you do the decryption
right
here you know because uh
we have to do m
to the power of e
mod
n
so c here is a 17
okay and the separate text
so
unit decryption
we do the calculation
c to the power of
d mod n
if you don't believe it you can do the
calculation using
your
computer calculator and you will find
the result will be
actually
trial
so this is a the earth's example
okay
and uh good i forgot to talk about this
and uh so very good and uh
so actually
one critical
public key crypto
application is a digital signature
which uses a the second property
of a public key crypto so that is so
when you use
some when somebody uses them
it's a private key to encrypt
the message m here
you can still use it
i mean the guy can still use a
everybody can use his public key to
decrypt this include message to recover
the original app okay



very good so now let's look at to
open ssl so what is open ssl so open ssl
actually is a
a crypto library and it's open source
crypto library
and it implements all kinds of
you know
cryptographic
functions
including
public crypto sql crypto and also hash
functions so you can use
open ssl for everything and open sso
also comes with
one command application called the open
ssl or in lower case then
you can use this actually to do a lot of
things okay
and uh so you can see here we can use uh
this open ssl to generate public and
private key pair
okay and then we can use a
open ssl for encryption with rsa
and
we can also use a
open ssl for decryption and uh
right and uh so this is open ssl
so finally you know
uh here
our hands-on
and so the first hands down
i think we don't need to talk about this
okay
we'll talk about this in in the lecture
but we don't talk about this now



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
