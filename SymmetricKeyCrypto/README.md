# Introduction to symmetrical key crypto
To be editted
here is a the outline of this lecture
we will first introduce
what is cryptography
next we are going to introduce some
retrieval codes
now we are going to introduce a modern
secret key cryptography
at the last we are going to introduce
hands-on labs
original meaning of cryptography is
secret writing however secret writing is
an art
so here i guess you guys played with
invisible ink and if you put
the writing
in invisible ink and
ultraviolet light now you can see it
but really the security of
secret writing
is not so good
cryptography becomes a science because
of the mathematics for example number
theory algebra
let's see one example
encryption
when we encrypt data we process data
into an intelligible form
however
this encrypted data is reversible means
we can decrypt the data and
obtain the original data
without any data loss
so this is a the
basic idea for cryptography
here is a big picture
for encryption and decryption one
critical
cryptographic
application
so here you can see on the left we have
bob on the left
we have the bob on the right we have
alice
so bob has a message which we call
as plain text
bob
will use an encrypted account
and
an encryption key to encrypt this plain
text
and
the output is called ciphertext
so the ciphertext is the encrypted data
so these separate text can go through
the internet
and even somebody intercepts cipher text
we should
be able to
think our data is secure the attacker
cannot actually recover the original
data
so now the separate text arrives at the
receiver
receiver here edits
will use
the corresponding decryption algorithm
and the corresponding decryption key
to decrypt the cipher text and obtain
the original plain text
so this is a big picture
how we actually use encryption
decryption
of course when we do encryption the
anime will try to
actually defeat the encryption and
obtain
the original message
this process is called crypt analysis
this is a definition of a crypto
analysis so we assume
the encryption and decryption errors are
known
then the goal of the attacker is to get
the keys
so there are many different ways of
crypt analysis we are going to see
one example later
now let's look at some trivial codes to
have a
some understanding of cryptography
particularly encryption and decryption
so the first
encryption approach is called
molar alphabetical sample
with a molar of a better server
we map one letter
in
the plain text
to another letter
in the cipher text
so here we are talking about
the ancient letters
so you can imagine right
and
we map letters
in
plain text to letters
as a separate text
of course the mapping must be one-to-one
otherwise we cannot reverse
the mapping procedure
okay
and
so this is the kind of mole of a better
server and you can imagine how many
different mappings do we have for 26
league letters
and we have 26 factories
one
molar alpha beta server is called a
scissor sampler
so in cedar cipher
you can see here
we use a
you know one letter in the
outer ring
we map one letter in the outer ring
to another letter in
the inner ring
so
we call this as a substitution separator
because we substitute
one letter in a plain
text
with a lot of letter in a separate text
and
so you can see here if we rotate
the inner
ring here then we will get a different
mappings totally
there are 26 possibilities
then we call this a
shift here that in here
is the key right so let's look at the
one system sample example
so in this case
we
have a key
of three it means
we replace each letter with the one
three letters later
so you can see here
we replace a with d
b with e
we use
this key
of 3
to
encrypt a message
hello what is the output and the output
will be
t h o o
because you can see here
so h will be mapped to key here
okay
so that's how
we
do see the sample with a key of three
now let's look at how can we defeat
cedar cipher actually
it's pretty easy and uh so let's look at
this a crypt analysis approach which is
called
frequency analysis as you know
ink letters have frequencies so here
this picture shows the frequency of
inclinators if your message is very long
and roughly that we got these kind of
frequencies of different letters
and so
in this case
so basically we assume we know
you know
somebody is using the c the separator
with a key we don't know the key
okay
however you know
if we get the ciphertext message now we
can count the frequency
of
all the letters in a separate text
then as we know
we can count the frequencies that we can
identify
which letter in a cipher text has
the most frequency then another letter
must be
e here so once you know actually that
letter was mapped from e
then you can actually use
the property of scissor server to obtain
the whole map
okay
so that's
the cryptic analysis against the scissor
server
so of course you can see the
mono african assembler is not very kind
of
secure that's why people invented the
polar upper beta centers
so in polar our webinar servers a letter
may be encrypted into different letters
from time to time so let's look at one
example this one is called a
clam
glamor transportation
okay
and uh so
let's look at one example here so we
have a plain text message attack
postponed until
2 a.m x y z here called padding because
in this
calendar transposition
we are going to align
you know
all the letters
in
rows so each o here is the seven letters
and then you can see here the last row
doesn't have
seven letters that's why we put x y z
over there as a padding
okay so our key is a four three one two
five one six
what does this mean
this means you know
okay
here
you know
the
first
row
the first column in original message
will be
actually
read
the first time
okay
and
so here three means
the
second column here
will be red in a third time
so in this way that we know
if we use a calendar transportation
then
the output will be like this
okay
so basically
the third column here
will be read first
as the separate text
so t t and a
then here
the fourth column
will be read second
as the seventh text
so it's aptm
so in this way you can see
you know
the original message is scrambled
allot
so here is a
another example of a calendar
transportation
so in this case
we have a keyword
z-e-b-r-a-s
zebras
okay so here basically the permutation
is defined by the alphabetical order of
the letters within the keyword
so you can see the zebras z
the order is six within
the keyword their brush
and so basically z is corresponding to 6
e correspond to 3
b correspond to 2 r comma 4 equal to 1 s
1 0 5
and what is the output if we use a
zebras to
encrypt this message we are
discovered
4d
at once
okay
qkgeu actually is a
the padding letters
and then what is the output the output
will be you know you can see here we are
going to
read
the fifth column first right e v and e
so by doing this then you can
obtain
the ciphertext
okay so we have introduced
the model alphabet server that is the
substitution server we also introduce
the transportation
ways of
encrypting data
so now let's look at
the modern secret key crypto
so in modern sequential
when we use
an encryption algorithm to encrypt
the message
the encryption
key is same as decryption key
we haven't seen that
right so you can see you can see the
cipher once we know that the key is
shift
and then basically you can use that
key for encryption and decryption in
calendar
transposition server and if we know the
keyword then we can use the keyword for
encryption and decryption okay
so in sql key crypto
the encryption key is the same as
decryption key
of course
what is a modern
secret key crypto
the basic technique is
we are going to use substitutions
and permutations
interleaved
and
so we are going to perform multiple
applications of interleaved
substitutions and the permutations
okay so this is a
the picture to show this process so
the plain text message is on the left it
will go through substitution permutation
supposition permutation a lot of rounds
finally it will produce a separate text
then the substitution implementation
in each round
will be controlled by the key so without
knowing the key
you don't know how exactly the
substitution and the permutation
is performed
right so basically it will be very hard
for you to guess the plain text
based on the cipher text
so here is one
example of a symmetric key crypto
ds
so ds is also called a block ciphers
so basically
each time ds can encrypt
eight bytes of a message okay so it's
like eight captures
and uh so you can see
in this case right
and uh
the
ds
uses a key and then
ds also has a 16 rounds
and then for each round we are going to
derive a sub key from the master key and
this muscle key will control
how exhausted
substitution and the permutations
are done
to the original data
so you can imagine right after so many
rounds 16 rounds
then
the input is really scrambled a lot
so
the problem of ds
is it it's key size is only like a
seven letters that's not very long
in terms of today's
computer power that's why people later
invented
the advanced equipment standard this is
a the current
standard for
secret key crypto encryption okay and
then here
the key size of es can be 128 192 or 256
and you know the ks is very secure
and
so basically if you choose a long es key
and use es to include message you can
assume your message is very secure
so here i have a question how you
encrypt a long message so as we said you
know
in ds right in es2 and each time
we only process
a block and in ds
each block is a
8 letters of 64 bits
and in es
each block is a 128 bits okay
and so
basically if a message is more than like
a one million
characters how do you encrypt a long
message so that's my question
let's look at the applications of a
secret key crypto
and
of course one critical
application is a
secret data transformation so
when you send a message to your friend
youtube can first
share a secret key and you can use the
key
to encrypted message in the decrypt
message without the key doubling out
will be able to decrypt your encrypted
message
of course if
you want actually securely to
store a file on your hard disk you can
use the es
to encrypt
the data right but you have to remember
the key
and that you cannot actually put the key
on a hard disk you have to remember it
and put it somewhere
securely
and then another application is called
integrity check so here i'm showing
a very naive
message integrated code it means
if we use this approach and if the
message is changed by somebody that will
be able to find it
so here is how i'm going to actually do
this kind of integrity so check you know
and so first when you send a message i'm
going to first send a message
then
i'm going to append the message with the
include message
so when i send to you right
then you'll be able to actually find if
the message is changed or not how can
you do that
can anybody tell me away
of course and it's very easy right when
you receive the message because you have
the key then you can actually
decrypt this incorrect message right and
then compare
the ticket message with the
message
and then if they are equal it means the
message is not changed
and uh
this
secret key crypto can also be used for
authentication what is authentication it
means we want to know
we are talking to
the right person so here we have edis we
have bob let's assume they share a
secret key first
so
one
wants to
check if she's talking with bob she can
pick up a random number whatever that
member is is random nobody
can guess what you are using and so you
send the number to bob and bubba can use
the shared key between
and is the bob to include message
then bumper will send
the encrypt message back the one and it
receives this incorrect message and it
can decrypt it
then if the secret message is same as
rna it must be bob because only bob has
not
shared a secret key and
so that's the reason
of course bob can use the same approach
to authenticate ns
okay so now let's introduce our hands-on
exercise
okay so first i want to introduce open
ssl
so
this
open ssl actually is a crypto library
but
this leverage comes with a
command line 2
with the same name
but it's just all lower letters open ssl
and this command line two uses
all the cryptographic graphic functions
of
the open ssls crypto library so you can
see here this command line too can be
used for encryption decryption can be
used for message digest basically
message integrity code and many other
things so we will see more
as we
talk more about
our topics in this gen server program
so here is our hands-on one
decipher scissor sever encrypted text
so in this case you know
the plain text i'm going to provide you
a message the plain text is an english
paragraph
encrypt we succeeded several of a
particular shift with a particular key
here
and i don't tell you the key so but you
have to use a frequency analysis and i'm
also giving you another tool which can
produce the scissor
sephora shifter table and then you can
use another tool
for see the sampler to actually
decrypt
the separate text
okay
and so i'm going to give you that
so the hands-on two here
is an encryption with a aes so here this
is wrong
okay
and
so
this is a command you can actually use
anchor open ssl apko is a
linux command so we usually perform this
hands-on
within candidates okay our candy vm and
so you can see here we do ankle open sl
this message
and then
here
this bar here
is uh
called actually redirection
okay so basically the input the output
of the first command this angle command
will be the input
of the second
command open ssl
and so you can see here we are using
openssl the encryption
function
and
here
our key will be generated from
a passcode called hello
and then
we are going to generate a key
with 100 1000
round of
operation and uh so to make you know
the
general key very random okay
and also we are going to use a
an encryption algorithm called es 256
means here to this is a key lens cpc is
a special
uh
way of aes
okay and here
the e is a b64 output
it means you know if you don't have this
dash aim the output will be boundary
numbers with a dash a
the output will be printable itself so
basically
the binary output the binary server text
is encoded
in base64 one kind of encoding approach
so that the output is printable
okay
so then once you get
the
separate text then you can use open ssl
to decrypt
the output
right the ciphertext so this is how you
do it again you can see we use echo
and here
the message
echoed by
anchor here is a
separate text
so
you know so basically the output of the
echo command will be input off of this
open ssl command
so
within the open ssl enc command
dash d means decryption so again we have
to provide a hello
and
we had to provide the iteration
times
right so that we can create
the correct
key from hello
and uh so dash a means you know the
input message is encoded with bits 64.
so in this way you know we can use
openssl enc command
to decrypt
the ciphertext
and then so here it's a
handout
three encryption
and the decryption
of a file with es so you basically
once you understand the previous command
you can understand this very well
and we are using
the es
algorithm
to actually
encrypt
a file okay so the input of the file
i mean the input file is sequencer.tkc
the other project is a
secrets.txt enc of course you can give
any name
to
the output file
okay
and then
so once uh
you
got to
your encrypted file
then you can do the decryption
and uh
so here is how you do the decryption i
think
you can understand that the command
easily
our hands-on form is a
we want to send the server text
through our chat server so one student
encrypts the messages and send out the
server text
via the chat server that's why you can
see why we want a b64 encoding
otherwise you know
our channel server cannot take a battery
input right and you can send you cannot
send the banner messages
and uh with base64
you know the separate text will be in
the big k4 format which is printable
okay and uh so once you
encrypt the message and send on the
separate text the other person
can receive
the cipher text and then perform the
decryption so you need to actually
select
the
message that was sent over
and then you right click and copy it and
then you can use the previous approaches
for decryption


## Hands-on

### Hands-on 1: Decipher Caesor cipher encrypted text

#### Ciphertext
The plaintext is English paragraphs, encrypted with Caesar Cipher of a particular shift. Ciphertext is shown below.
```
Qb qa i xmzqwl wn kqdqt eiza qv bpm oitifg. I jzidm ittqivkm wn cvlmzozwcvl nzmmlwu nqopbmza pia kpittmvoml bpm bgzivvg ivl wxxzmaaqwv wn bpm iemawum OITIKBQK MUXQZM.

Abzqsqvo nzwu i nwzbzmaa pqllmv iuwvo bpm jqttqwv abiza wn bpm oitifg, zmjmt axikmapqxa pidm ewv bpmqz nqzab dqkbwzg qv i jibbtm eqbp bpm xwemznct Quxmzqit Abizntmmb. Bpm MUXQZM nmiza bpib ivwbpmz lmnmib kwctl jzqvo i bpwcaivl uwzm awtiz agabmua qvbw bpm zmjmttqwv, ivl Quxmzqit kwvbzwt wdmz bpm oitifg ewctl jm twab nwzmdmz.

Bw kzcap bpm zmjmttqwv wvkm ivl nwz itt, bpm MUXQZM qa kwvabzckbqvo i aqvqabmz vme jibbtm abibqwv. Xwemznct mvwcop bw lmabzwg iv mvbqzm xtivmb, qba kwuxtmbqwv axmtta kmzbiqv lwwu nwz bpm kpiuxqwva wn nzmmlwu.
```

#### Tools to use for decryption
- <a href="https://www.dcode.fr/frequency-analysis">Frequency analysis</a>
- <a href="https://www.usna.edu/Users/cs/wcbrown/courses/si110AY13S/resources/ceasar-shift/shiftTable.html">Ceasar shift table</a>
- <a href="https://cryptii.com/pipes/caesar-cipher">Caesar cipher tools</a>

What is the plaintext message?

### Hands-on 2: Encryption with AES
Encrypt a message like "OpenSSL"
```
echo "OpenSSL" | openssl enc -iter 1000 -aes-256-cbc -a -k hello
```
- *echo "OpenSSL"*: display a message, in this case, "OpenSSL"
- *|*:  with the pipe character ‘|’, the output of one command (*echo "OpenSSL"* in this case) acts as input to another command (*openssl ...* in this case)
- *<a href="https://wiki.openssl.org/index.php/Command_Line_Utilities">openssl</a> <a href="https://wiki.openssl.org/index.php/Enc">enc</a>*: *Enc* is used for block and stream ciphers using password based keys or explicitly provided keys
  - Can be used for Base64 encoding or decoding.
- *-k hello*: The key will be generated from hello 
  - Without -k hello, the command will ask for a password, which will be translated into a key 
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
- *aes-256-cbc*. Use aes-256-cbc algorithm
- *-salt*. Use salt in strong key derivation

Decrypt the encrypted file
```
openssl aes-256-cbc -d -a -in secrets.txt.enc -out secrets.txt.new -iter 1000 -k hello
```

### Hands-on 4: Send Encrypted Message via Chat Server
- One person encrypts messages and sends
- The other person receives encrypted messages and decrypts

## References
