Under construction

# Digital Forensics

We are going to talk about digital forensics. We first introduce what is digital forensics. Then we are going to talk about one critical technique used in
digital forensics---disk imaging. At last we'll talk about why we can recover deleted files.

## Introduction
Digital forensics includes computer forensics and network forensics. 
In computer forensics we focus on getting evidence from Individual computer systems.
In network forensics we focus on evidence connection, analysis and suspect identification in a networked environment.
Network forensics can be complicated since the Internet is complex. 
Why do we want to digital forensics? It is because the number of cyber crimes has been increasing all the time and the Internet is now a battle field of a cyber war and cyber crimes. Digital forensics education meets the urgent need of cyberspace operation professionals.

Here is FBI's list of cyber crime categories. There are many varieties, including 
advance fee fraud, auction fraud, blackmail/extortion, charity fraud, consumer complaint, counterfeiting/forgery,
credit/debit card fraud, computer damage, drug/narcotic offenses, business/employment fraud, fbi scams, gambling offenses, id theft,
illegal business, intimidation, investment fraud, miscellaneous fraud, non-delivery of merchandise, overpayment fraud, pornography/obscene material,
prostitution, relationship fraud, rental fraud, spam, stolen property offenses, and terrorist threat.

## Cyber crime cases
Let's look at a few cases of cyber crimes.
### Case Study 1 - Stolen property offenses

This is a case of stolen property offense. In 2010, A Dutch national Joey Vogelaar hacked into a company involved in the production release and stole digital versions of three Hollywood movies:  *How Do You Know* by Sony Pictures Entertainment,
*Rango* by the Paramount production  and *Megamind* by Dreamworks.
In this case the bad guy used the the hiking technology, got into a computer server and stole a few Hollywood movies.

### Case Study 2 - illegal business
This is a case of illegal online business.
Ross William Ulbricht created a website called Silk Road in approximately January 2011.
It was a black market on the internet, selling illegal goods and the
services including controlled substances, hiking software and services.
Bitcoin was used as the currency.

## Disk imaging
To defeat cyber crimes and prosecute bad guys, we often need disk imaging.
What is a disk imaging?
A bit stream copy of the original storage media is an exact copy of the original disk.
The result of a bit stream copy is often a file called bit stream image, which contains all data on the disk.
That's why we call this file as an image or image file.

When we collect evidence, we want to be very careful, not damaging evidence.
For example when a suspect computer is on, how can you perform imaging?
What factors should we consider?
Should we turn the computer off?
There are a lot of trade-offs here.
If we turn the computer off, the good thing is that the bad guys cannot remotely operate their computer any more and erase evidences.
That's the benefit. The downside is we lose all the content in the computer memory, which may have a lot of data and thus evidences.

## Recovering deleted files
A suspect may delete evidences from a disk.
We may be able to recover such deleted files.
Let's look at why and how we recover deleted files.
We will use a conventional magnetic hard drive as the example. Today we have other types of hard disks such as solid state drives. The principle of recovering deleted files is the same since it is only related with the operating system and file system.

### Magnetic hard disk
A magnetic hard disk has a lot of platters, on which data is stored.
All the platters are concentric around the spindle.
the spindle rotates the platters and the read-write head moves along the radius of the platters so as to access all the data.

![https://i.stack.imgur.com/y5wtm.jpg](https://user-images.githubusercontent.com/69218457/193344618-955ef94a-22f0-41b7-84ff-5104b27d783c.png)

There are a few concepts about the hard disk, including track, sector, cylinder and head.
The hard disk formatted as concentric circles on the platter surfaces known as tracks.
A platter has two surfaces. A read-write head is used to access each surface. 
A sector is a curved section of a track and can contain 512 bits of data.
Corresponding tracks on all plantar surfaces of a hard disk form a cylinder.
A sector has a coordinate of (cylinder, head, sector).

Why can a magnetic hard drive store data?
What is a bit on the hard disk?
For a magnetic hard drive, we use a group of magnetized metal greens to store a bit.
1 or 0 is indicated by the alignment of magnetization.
For example if the group of magnetized metal grains is aligned to the right, we call that allignment as 1.
Otherwise, it is a 0.
Changing data on a hard drive is basically changing the alignments of groups of magnetized metal grains.
Recall a sequene of 0s and 1s is a binary number, which can be converted into a decimal number.

![image](https://user-images.githubusercontent.com/69218457/193349270-6a068f88-7190-43a2-920b-879a99149431.png)

### File Allocation Table (FAT)

Now we discuss how a file system is used to organize files on a hard disk.
The figure belows show an example of the file system, file allocation table (FAT).
table here and the one column here
corresponding to 1
track
and then the first track contains
something called the MBR it's called a
master booted record and it contains the
first piece of code that the computer
will run from your hard disk
then the rest of
the disk here
will contain your files okay and so here
you can see we have some vbr that's
called the volume booted record and this
maybe like your state disk on your
computer and this is just one example
and the partitions of a disk can be very
complicated okay and let's just use this
one to show how we write a file on disk
and how we did the file on disk so here
we see a few regions we see Factor one
Fighter 2 root c and a file here so
Factor one Fighter 2 are called file and
location tables
and within the file allocation table
it contains entries indicating if
part of the disks
is a used and uh so the minimum
foreign
cluster so basically the file allocation
table indicates if
a cluster is used and uh what is the
next cluster
file
occupies okay
and then the root C here is just one
example for the root directory so in
this region of the hard disk it contains
the entries
Alpha
file information so for example when you
create one file on the disk then we
create one entry within this root
directory and
one entry indicates the file name and
there also contains a
start cluster of your file on the disk
okay finally we have the file region
this is where the data is stored
so we already discussed the file
allocation table so we said
the fact is a list of entries that map
to each cluster on the partition
and each entry reports one of the file

![image](https://user-images.githubusercontent.com/69218457/193351059-a6541b44-d489-47bd-861f-ca9808973374.png)


scenes the address of the next cluster
in a chain a special end of a file UF
character that indicates the end of a
chain
a special character to Mark a better
cluster a special character to Mark a
reserved cluster a zero to note that
that cluster is unused
so let's look at the
what happens when we write a file
when we write a file the first thing
that will be changed is the direct entry
the direct entry for this file will be
created within
the root generated region here okay so
you can see here right and in this
example we created the file that's the
file name and it will also indicate
where the file starts so in this case
the start cluster is 2 and it also shows
the file size
and then
the file and location tables are updated
you may wonder why do we need two file
allocation tables
we need another
file and location table for the purpose
of redundancy and so that's why we need
another file allocation table
so you can see
when we write the file after we create
the direct entry
in the root Direction region then we are
going to update the file allocation
tables and so basically uh
we are going to record which
clusters are used for this file within
the file allocation tables
finally
after we update
the directory and also file allocation
tables we are going to write the data
onto the disk and to the Clusters
indicated by the file allocation tables
okay so we have understood
what happens when we write a file to a
disk now let's look at how we did it a
file on the disk what happens when we
did the file on the disk
okay
and uh so here is what happens
so the first thing that happens after
you
delete a file as
the file
directory entry will be updated
so this is a the example of the thoughts
and early version of a
operating system and you can see so in
this case the first character of the
direct entry is changed to third time
okay and that indicates basically this
file is deleted
and also the corresponding entries
within the file allocation tables are
zeroed okay okay so once
the file allocation table entries become
zero
it indicates
those clusters
are used and they can be reused again
however
you can see here basically we are not
going to remove the data on the hard
disk
why because think about this
if you did the file we have to zero out
all the files all the contents
if your file is big
this will take a long time this is not
very convenient so therefore we just
actually
update
the file
directory entry
and also the file addiction tables to
indicate
the Clusters used by the old file
uh
available now so in this way the
performance of the computer will be
improved
however
you can see here because the data area
of the file is not changed this gives us
a chance that
this file can be recovered so this is
the reason why you can recover a file

## Autopsy—open source digital forensics platform
Autopsy is an open source digital forensics software that implements varieties of forensic technologies. We will show how it can be used for loading a disk image and performing forensics. 

When Autopsy is started, it gives three choices: *New Case*, *Open Recent Case*, and *Open Case* as shown below. 
![image](https://user-images.githubusercontent.com/69218457/193131150-2b5c60c8-998b-43af-9e07-140996f9cfe6.png)

When *New Case* is chosen, the *New Case Information* dialog shows up. Enter *Case Name* and *Browse* to choose a folder to save analytical results. Then presss *Next* to continue as follows.
![image](https://user-images.githubusercontent.com/69218457/193132272-e2ab3fa8-29bb-4dee-8648-38085d7e0008.png)

Fill out *Optional Information* and click *Finish*.
![image](https://user-images.githubusercontent.com/69218457/193132605-49f51840-0f6e-4abc-bd33-535cc8707216.png)

In the *Select Host* dialog window, you can use *Gnenerate host name based on data source name* and click *Next*.
![image](https://user-images.githubusercontent.com/69218457/193133334-9e01cef2-2b69-49ef-ac95-2a11e7b86c82.png)

In the *Select data source type*, we choose *Disk Image or VM FIle* since we will analyze a disk image. Click *Next*.
![image](https://user-images.githubusercontent.com/69218457/193133626-0f239546-5554-4609-84a8-c84ab3223c9c.png)

In the *Select data source* dialog window, *Browse* to choose the disk image file
![image](https://user-images.githubusercontent.com/69218457/193134049-613f0918-39ca-4487-8276-9806e244ebe9.png)

In the *Configure Injest* dislog window, click *Next* to run injest modules to retrieve default data from the image. Click *Next*.
![image](https://user-images.githubusercontent.com/69218457/193134775-8211834d-c10d-4c2f-bd3c-17ebdc57c287.png)

The next dialog window is *Add Data Source*. We do not have more data soures and thus just click *Finish*. After a while of analysis, Autopsy shows the analytical results.
![image](https://user-images.githubusercontent.com/69218457/193172925-bc202e89-c22a-45bc-8a13-63ef59001c38.png)

## Hands-on
### Hands-on 2 FTK Imager
*AccessData FTK Imager* can be used to mount a disk image and show files with the image. Start *FTK Imager*. Use *File* -> *Image Mounting* -> *Add Image* to mouse the image usb-case.E01. One the image mouted, a logical drive is created for the image. Open *File Explorer* of Windows.
* What can you observe from the logical drive corresponding to the image?

### Hands-on 2 Autopsy
Please load usb-case.E01 into *Autopsy*.
* Can you see files found in the logical drive in Hands-on 1 within Autopsy?

* Can Autospy recover deleted files? Why?

* What deleted files can you recover with Autopsy?
