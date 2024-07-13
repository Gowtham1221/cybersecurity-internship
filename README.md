This repository contains the project that i did for my cybersecurity internship.
This project mainly focuses on the encryption of text into an image file and extraction of the encrypted text data from tha image file. This process is called as steganography.
So, what is the aim of this project?
The aim of this project is to provide a platform for communication of highly secreative, sensitive and classified information with the highest degree of security and convinence.
This is how the project works.
In some specific detail the program takes an image file as an input, a message and a password, the text is converted into ASCII values and sotred in the RGB pixel data of the image.
The program uses LSB insertion, means the LSB bits of the RGB channel values are modified to store the ASCII data. As only the LSB's are modified the image dosent seem to be changed to the naked eye.
The decoding process is simple enough that it is the reverse process of the encoding, the ASCII values are converted back into characters only if the password is correct.
If there is no hidden data or the password is wrong the message will not be shown.
