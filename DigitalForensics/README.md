
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
![image](https://user-images.githubusercontent.com/69218457/193135852-7b42a031-96a3-4e66-9779-e27a07a8fc8c.png)

## Hands-on
