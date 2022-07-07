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

This is the big picture of a public
key crypto so in public key crypto then
we have again bob on the left and that
is on the right so let's look at this
example
so in this example
actually in any scenario of a public key
crypto so each person
is going to have two keys
so here you can see in a parenthesis
i put two
symbols here eb and db so eb is the
public key of bob db is his private key
same
as bob here nsa has a two keys
so
ea is a
analysis
public key and d a is a
and this is a private key
okay
so in this case again
bob
is going to send a message
that is the plain text to
alice so pay attention to the difference
so again
okay bob needs an encryption algorithm
but in this case you can see here
what happens is that bob is going to use
it and this is a public key
which is public and known by anyone
okay
and uh so bob is going to use an
encryption agreement and analysis
public key to encrypt the message
so
the encryption produces the separate
text
so again the cipher text goes through
the internet and arouse enter address
so in this case
alice
again
uses a
decryption algorithm
and her private key which is different
from
her public key to decrypt
the cipher text
and
the decryption will produce the plain
text
so you can see here
in public crypto
the encryption and the decryption use
different keys and then also pay
attention
how baba
uses
any as a public key
to encrypt the plain text
okay
and so this is a basically how
public key crypto encryption works 

<img src="../Imgs/AsymmetricCrypto.png" width=512>

so we
are going to look at an example later
and
you know
most of the public key crypto aggregates
involve a lot of mathematical
you know calculations
and as we have learned in secretly key
crypto when we do secret key crypto
encryption most of time we use a
permutation
and
also
you know substitutions
to perform the encryption that doesn't
involve a lot of mathematical
calculation but
as we just said
publicly crypto often involves a lot of
mathematical agreements
and the mathematical calculations
and the mathematical calculations
are much slower compared
with
permutations and substitutions
because
alice and bob use different keys for
decryption encryption
and
that's why
here property crypto is also called
asymmetrical crypto
so let's look at the one application of
the public crypto
so of course again we can use a public
key crypto
for
data transformation
and so in this case let's look at an
example here right and then you can see
here i'm using a different example let's
look at this example again
so in this example here alice has a
message to send
to
bob
and many alice is going to use
bob's public key eb here to encrypt this
message
so and this will send this message over
and when bob receives this server text
bob is going to use
his private key to decrypt this separate
text
and the bubble will recover the original
message
so this is how
property crypto is used for data
transmission and we already saw the
example
in last slide
and of course here
you can also use a
public crypto for
secure storage so you can use
your public key
to
actually encrypt files other data
and then put
the encrypted data on your hard disk
then because you
and only you have the private key
so only you can actually decrypt the
encrypted data so that's the idea of a
secure storage
so as we mentioned you know
most of the time if you have a lot of
data to transmit across the internet
we actually do not use public crypto
because it's too slow you don't want to
wait for your message to arrive
after a long delay
right so
that's
why
you know
when we send
messages
if we need interaction with our receiver
most of the time we are going to use
secret key crypto
however in secret key crypto when we do
encryption decryption
we need
actually share the key between the
standard and the receiver
but on the internet you know
it's not so easy to share a key with
somebody right
and uh
so how do we address
this issue how do we actually share a
secret key
in secret key crypto
across the internet this problem is
called key exchange
actually it can be solved by the public
crypto easily so let's look at this
example here so here again we have edis
we have bob
right and
so let's see here the key here is i mean
this electric key here is a the secret
key in secret key crypto
and while alice wants to
share this key with bob
edis can just use bob's public key to
encrypt this key
and send it over to bob when bubble
receive it and bubba can use
his private key to decrypt this
encrypted key
then bubble
can recover
the
secret key
so once this secret key is a
shared
between anything above
and the editor bubble can use
this
key to encrypt the message so here i'm
giving you
an example here and alice has a message
m here so here
and it uses
the shared key here to encrypt this
message
and
send it over so when bubble receive it
bubble can use
the same key to decrypt
the cipher text so here key
to the power of a minus one means that
bob uses the same key
to decrypt
the message
okay
so this is the idea of key exchange so
now you can see
so we use
the publicly crypto to share the key and
we can use the key
to encrypt the message
with a secret key crypto and uh so
actually secret key crypto is pretty
fast it's a at least a
fit for
interaction between
sender and receiver so you can send the
messages
and you can talk with your friends
with encryption
so actually
public crypto has two problems we
already saw one so
we already saw when you have a message
here you can use
somebody's public key to encrypt the
message and the data somebody can use a
it's a private key to decrypt this step
for the case except for text and the
receiver
i mean recover the original message
okay
and
so actually there's a lot of property
and uh so you can also use the
i mean somebody's private key
to
include the message and that that
somebody can use it it's
a key to decrypt
this encrypted message by
somebody's private key you can still
recover the
original message
here i have a question for you
so the second problem here can we use
this property
to
secretly send a message across the
internet
okay very good so we already understand
the basic idea of a public key crypto so
let's look at uh
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
and uh so let's look at
a nail digital signature
strategy here so in this case bob
actually wants
to publish an announcement or contract
here
singing okay i want to give professor
foo 1 million dollars of course i'm
joking and but anyway and he wants
everybody to know
i mean
he's doing it
but how can everybody
verify
it's really him who wants to do it
okay
so this is how it works
so bob has a
the public and the proud key pair right
eb is a public key db is
the private key
so what
he will do is he will sign the contract
what is this a signing procedure
actually the signing means
he is going to use his private key here
to encrypt this contract
so now when bob
delivers
the contract
alongside this contract i publish this
contract
he will actually publish two parts
the first part is the contract itself
the second part is
this digital signature which is the
encrypted contract by bob's publicly can
anybody tell me
so
how can actually bob
i mean how can you for example let's
assume you have a bubbles public key
how can you actually prove
this contract
is
released by
bob
okay
so this is how we do it
and so basically anybody can use
bob's public key
to decrypt
this encrypted contract by bob's private
key
if the decrypted contract is the same as
the published contract it is from bob
because only bob's
public key can decrypt this encrypted
contract right
right so then we are sure it is from bob
so this is a deny you digital signature
why is it now you because you can see
here we encrypt the whole tr contract
as a bob's
digital signature so that's not very
efficient it's too long okay
and so that's basically what we are
doing here
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
