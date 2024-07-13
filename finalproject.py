import cv2
import os
d={} #dictonary for charecter to ASCII converted data
c={} #dictonary for ASCII to character converted data
def dataconv(): #conversion of the data from ASCII to characters and vice versa
    for i in range (256):
        d[chr(i)]=i #character to ASCII
        c[i]=chr(i) #ASCII to character
def encode(): #encoding function
    img_path=input("Enter the image file path here :")
    img=cv2.imread(img_path)
    if img is None:
        print("\n\nImage not found, or check the given file path") 
        return None
    key=input("\n\nEnter the password to encode :")
    text=input("\n\nEnter the message here :") + "#####" #an end marker to the message for better encryption
    l=len(text)
    kl=0 #key lenght index
    #here n,m,z are the index RGB colour channels of the picture 
    n=0  
    m=0
    z=0
    height,width,_=img.shape
    for i in range (l): #encoding loop
        img[n,m,z]=d[text[i]]^d[key[kl]] #XOR operation to encode the data into the pixel data
        n=(n+1) % height #move to next pixel
        if n==0:
            m=(m+1) % width
        kl=(kl+1) % len(key) #cycle through the key characters
    #save the image and open the generated image
    encrypted_image_path="picture.png"
    cv2.imwrite(encrypted_image_path,img)
    os.startfile("picture.png")
    print("\n\nSUCCESSFULLY ENCRYPTED")
def decode(): #decoding function 
    img_path=input("\nEnter the image file path here : ")
    img=cv2.imread(img_path)
    if img is None:
        print("\nImage not found, or check the given file path")
        return None
    key=input("\nEnter the password to decode : ")
    kl=0 #key lenght index
    # same as before index for the RGB colour channels of the picture
    n=0
    m=0
    z=0
    decrypt=""
    for _ in range(img.shape[0]*img.shape[1]): # for the range of the image resolution of pixels
            decrypt_char= c[img[n,m,z]^d[key[kl]]] #decoding of the character data from the pixel data
            decrypt +=decrypt_char
            if decrypt.endswith("#####"): # checking for the data with end marker
                print("\n\nTHE SECRET MESSAGE IS : ",decrypt[:-5])
                return
            n=(n+1) % img.shape[0] # move to the next pixel
            if n==0:
                m=(m+1) % img.shape[1]
            kl=(kl+1) % len(key) #cycel through the key characters
    print("\n\nWORNG PASSWORD OR NO HIDDEN MESSAGE FOUND") # incase if there is no hidden message in the picture of the password is wrong   
def main():
    dataconv() #caling the data conversion function
    a=int(input("Choose your steganography operation \n1.Encode\n2.Decode\nENTER YOUR CHOISE HERE(enter the number) :"))
    if a==1:
        encode()
    elif a==2:
        decode()
    else:
        print("\n\nENTER A VALID INPUT")
    input("\n\nPress enter to exit....")
if __name__=='__main__':
    main()