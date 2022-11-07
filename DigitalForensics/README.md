# Digital Forensics

We first introduce what is digital forensics and a couple of cyber crime cases. Then we are going to talk about one critical technique used in
digital forensics&mdash;disk imaging. At last we'll talk about why we can recover deleted files and the use of the open source software Autopsy on Windows to recover deleted files.

## Introduction
Digital forensics includes computer forensics and network forensics. 
In computer forensics, we focus on getting evidence from individual computer systems.
In network forensics, we focus on evidence connection, analysis and suspect identification in a networked environment.
Network forensics can be complicated since the Internet is complex. 
Why do we want digital forensics? It is because the number of cyber crimes has been increasing all the time and the Internet is now a battle field of a cyber war and cyber crimes. Digital forensics education meets the urgent need of cyberspace operation professionals.

Here is FBI's list of cyber crime categories, including 
advance fee fraud, auction fraud, blackmail/extortion, charity fraud, consumer complaint, counterfeiting/forgery,
credit/debit card fraud, computer damage, drug/narcotic offenses, business/employment fraud, FBI scams, gambling offenses, ID theft,
illegal business, intimidation, investment fraud, miscellaneous fraud, non-delivery of merchandise, overpayment fraud, pornography/obscene material, prostitution, relationship fraud, rental fraud, spam, stolen property offenses, and terrorist threat.

## Cyber crime cases
Let's look at a couple of cyber crime cases.
### Case Study 1 - A case of Stolen property offense

This is a case of stolen property offense. In 2010, A Dutch national Joey Vogelaar hacked into a company involved in the production release and stole digital versions of three Hollywood movies:  *How Do You Know* by Sony Pictures Entertainment,
*Rango* by the Paramount production and *Megamind* by Dreamworks.
In this case the suspect used the computer hiking technologies, got into a computer server and stole a few Hollywood movies.

### Case Study 2 - A case of illegal business

This is a case of illegal online business.
Ross William Ulbricht created a website called *Silk Road* over Tor, which provides anonymity service, in approximately January 2011.
It was a black market on the Internet, selling illegal goods and
services including controlled substances, hiking software and services.
Bitcoin was used as the currency.
In this case, the suspect abused the anonymity service offered by Tor and opened an online black market.

## Disk imaging
To defeat cyber crimes and prosecute cyber criminals, we often need disk imaging.
What is a disk imaging?
In disk imaging, we perform a bit stream copy of the original storage media, creating an exact copy of the original disk.
The result of a bit stream copy is often a file called bit stream image, which contains all data on the disk.
That's why we call this file as an image or image file.

When we collect evidence, we want to be very careful, not damaging evidence.
For example when a suspect computer is on, how can we perform disk imaging?
What factors should we consider?
Should we turn the computer off?
There are a lot of trade-offs here.
If we turn the computer off, the good thing is that the bad guys cannot remotely operate their computer any more and erase evidences.
The downside is we lose all the contents in the computer memory, which may have a lot of data and thus evidences.

## Recovering deleted files

A suspect may delete files that contain evidences from a disk.
We want to recover such deleted files.
Let's look at why and how we may recover deleted files.
We will use a conventional magnetic hard drive as the example. Today we have other types of hard disks such as solid state drives. The principle of recovering deleted files is the same since the principle is only related with the operating system and file system. But for fun, we will talk about how the magnetic disk works too.

### Magnetic hard disk
A magnetic hard disk has a number of platters, on which data is stored.
All the platters are concentric around the spindle as shown in the image below.
the spindle rotates the platters and the read-write head moves along the radius of a platter so as to access the data.

![https://i.stack.imgur.com/y5wtm.jpg](https://user-images.githubusercontent.com/69218457/193344618-955ef94a-22f0-41b7-84ff-5104b27d783c.png)

Why can a magnetic hard drive store data?
What is a bit on the hard disk?
For a magnetic hard drive, we use a group of magnetized metal greens to store a bit.
1 or 0 is indicated by the alignment of magnetization.
For example, if the group of magnetized metal grains is aligned to the right, we call that allignment as 1.
Otherwise, it is a 0.
Changing data on a hard drive is basically changing the alignments of groups of magnetized metal grains.
Recall a sequene of 0s and 1s is a binary number, which can be converted into a decimal number.

<img src="https://user-images.githubusercontent.com/69218457/193349270-6a068f88-7190-43a2-920b-879a99149431.png" width=320>

There are a few concepts about the hard disk, including track, sector, cylinder and head.
The hard disk is formatted as concentric circles, called tracks, on the platter surfaces.
Each platter has two surfaces. A read-write head is used to access a surface. 
A sector is a curved section of a track and contains 512 bits of data.
Corresponding tracks on all platter surfaces of a hard disk form a cylinder.
Therefore, a sector has a coordinate of (cylinder, head, sector).
A cluster is one or more contiguous sectors.
Cluster is the minimum unit used by an operating system (OS) to allocate disk space to files.
An OS allocates clusters of disk space to a file.

<img src="https://user-images.githubusercontent.com/69218457/193436132-9fe45a0e-1e86-4d2e-8261-6b5d2a0d329d.png" width=320>


### File Allocation Table (FAT)

Now we discuss how a file system is used to organize files on a hard disk.
The figure below shows an example file system, file allocation table (FAT), used by operating systems such as DoS and Windows.
DOS is an early OS from Microsoft and IBM.
The grid surface represents the hard disk surface. A grid represents a sector.
A column of grids corresponds to a track.
In this example, the first sector of the hard disk contains the master boot record (MBR),
which contains master boot code and master partition table.
The master boot code is the first piece of code on the hard disk that the computer will run.
The master partition table tells how the disk is partitioned and on which partition an operating system is installed.

<img src="https://user-images.githubusercontent.com/69218457/193351059-a6541b44-d489-47bd-861f-ca9808973374.png" width=512>

In this example, the OS is installed on the disk partition starting from the second track.
The first sector of this partition contains the Volume Boot Record (VBR), which is used to identify the files needed by the OS. The volume boot code in the VBR loads the OS to run.
The partitions of a disk can be complex. Let's just use this simple example to show how we write and delete a file on a disk.

It can be observed that there are a few regions after the VBR, including FAT1, FAT2, Root C and FILE. FAT referes to file location table. The FAT contains a list of entries that map to each cluster on the partition. Each entry records one of five things:
* the address of the next cluster in a chain 
* a special end of file (EOF) character that indicates the end of a chain 
* a special character to mark a bad cluster 
* a special character to mark a reserved cluster 
* a zero to note that that cluster is unused 
We have two FATs here and the second FAT is a backup in case that the first one is corrupt.

Root C is the Root Directory Table.
It represents the directory C:\. 
Each file or directory stored within the directory C:\ is represented by an entry in the table. Each entry records 
name, extension, attributes (archive, directory, hidden, read-only, system and volume), the date and time of creation, the address of the first cluster of the file/directory's data and finally the size of the file/directory.

FILE is the region where actual files are stored on the partition. The directory table and FAT together tell where file data is stored. The directory table indicates the first cluster occupied by a file. The corresponding cluster entry in the FAT tells the next cluster of the file and so on. The last cluster has a special end of file (EOF) character that indicates the end of a chain of clusters occupied by the file.

### Writing a file 
Let's look at what happens when we write a file onto a disk.
The first thing that will be changed is the direct table.
A directory entry for this file will be created within the root directory table in our example.
The figure below shows the directory entry, which includes file name, start cluster (i.e., the first cluster on disk allocated to the file) and file size.
The start cluster is 2. Next, we are going to update the FATs.
One cluster is enough to store the file of 1024 bytes. Recall a cluster may contain multiple sectors.
Therefore, one entry in the FAT is used and the entry has a label of E, indicating the end of the file. 
Finally after we create the directory entry and update the FATs, we write the file data onto the disk.

<img src="https://user-images.githubusercontent.com/69218457/193430136-49dc9db2-2551-49b5-8cb4-605b5fa5a5e9.png" width=512>

### Deleting a file 
Now let's look at what happens when we delete the file on the disk.
The first thing that happens after we delete a file is the file directory entry will be updated.
In this case the first character of file name in the direct entry is changed to &sigma;, which indicates this file is deleted.
The corresponding entries within the FATs are zeroed out.
This indicates those clusters are free and they can be reused.
However, data area is not changed.
The actual file data on the hard disk is not changed.
Why? What happens if we actually overwrite the file data, e.g., with zeroes or random numbers?
If the file is big, such a deletion operation will take a long time.
This is not very efficient.
This is why we just actually update the file directory entry and FATs to indicate the clusters used by the old file are free when we delete a file.
In this way the performance of the computer is improved. 

<img src="https://user-images.githubusercontent.com/69218457/193430325-0797de78-a30f-4863-aef9-50f702108017.png" width=512>

However, you can see because the data area of the file is not changed, this gives us a chance to recover this file.
This is the reason why you recover a file.

Question: can you always recover a deleted file?

## Autopsy—open source digital forensics platform
Autopsy is an open source digital forensics software that implements varieties of forensic technologies. We will show how it can be used for loading a disk image and performing forensics. 

When Autopsy is started, it gives three choices: *New Case*, *Open Recent Case*, and *Open Case* as shown below. 
<img src="https://user-images.githubusercontent.com/69218457/193131150-2b5c60c8-998b-43af-9e07-140996f9cfe6.png" width=512>

When *New Case* is chosen, the *New Case Information* dialog shows up. Enter *Case Name* and *Browse* to choose a folder to save analytical results. Then presss *Next* to continue as follows.

<img src="https://user-images.githubusercontent.com/69218457/193132272-e2ab3fa8-29bb-4dee-8648-38085d7e0008.png" width=720>

Fill out *Optional Information* and click *Finish*.

<img src="https://user-images.githubusercontent.com/69218457/193132605-49f51840-0f6e-4abc-bd33-535cc8707216.png" width=720>

In the *Select Host* dialog window, you can use *Gnenerate host name based on data source name* and click *Next*.

<img src="https://user-images.githubusercontent.com/69218457/193133334-9e01cef2-2b69-49ef-ac95-2a11e7b86c82.png" width=720>

In the *Select data source type*, we choose *Disk Image or VM FIle* since we will analyze a disk image. Click *Next*.

<img src="https://user-images.githubusercontent.com/69218457/193133626-0f239546-5554-4609-84a8-c84ab3223c9c.png" width=720>

In the *Select data source* dialog window, *Browse* to choose the disk image file

<img src="https://user-images.githubusercontent.com/69218457/193134049-613f0918-39ca-4487-8276-9806e244ebe9.png" width=720>

In the *Configure Injest* dislog window, click *Next* to run injest modules to retrieve default data from the image. Click *Next*.

<img src="https://user-images.githubusercontent.com/69218457/193134775-8211834d-c10d-4c2f-bd3c-17ebdc57c287.png" width=720>

The next dialog window is *Add Data Source*. We do not have more data soures and thus just click *Finish*. After a while of analysis, Autopsy shows the analytical results.

<img src="https://user-images.githubusercontent.com/69218457/193172925-bc202e89-c22a-45bc-8a13-63ef59001c38.png" width=720>

For a large image file, the analysis may take some time. Please wait for the analysis to finish. It is indicated on the status bar at the bottom, which shall show 100%.

![image](https://user-images.githubusercontent.com/69218457/200358165-39ad61a7-8093-45fd-847c-88582fb68f8c.png)



## Hands-on
### Hands-on 2 FTK Imager
*AccessData FTK Imager* can be used to mount a disk image and show files with the image. Start *FTK Imager*. Use *File* -> *Image Mounting* -> *Add Image* to mouse the image usb-case.E01. One the image mouted, a logical drive is created for the image. Open *File Explorer* of Windows.
* What can you observe from the logical drive corresponding to the image?

### Hands-on 2 Autopsy
Please load usb-case.E01 into *Autopsy*.
* Can you see files found in the logical drive in Hands-on 1 within Autopsy?

* Can Autospy recover deleted files? Why?

* What deleted files can you recover with Autopsy?
