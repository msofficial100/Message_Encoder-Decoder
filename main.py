
from tkinter import *
import base64
from PIL import ImageTk, Image




root = Tk()

root.resizable(0,0)

root.title("Encryption - Decryption")


img =Image.open('C:\\Users\\MAYANK\\Desktop\\project 2\\bg.jpg')
bg = ImageTk.PhotoImage(img)

root.geometry("850x650")

# Add image
label = Label(root, image=bg)
label.place(x = 0,y = 0)




#label

Label(root, text ='Encrypt and Decrypt Your message ', font = 'arial 30 bold').pack()
Label(root, text ='Encryption - Decryption', font = 'arial 10 bold').pack(side =BOTTOM)


#define variables

Text = StringVar()
private_key = StringVar()
mode = StringVar()
Encrpyted_message = StringVar()


#function to encode

def Encode(key,message):
    enc=[]
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
        
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

#function to decode

def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
        
    return "".join(dec)

#function to set mode
def Mode():
    if(mode.get() == 'e'):
         Encrpyted_message.set(Encode(private_key.get(), Text.get()))
    elif(mode.get() == 'd'):
         Encrpyted_message.set(Decode(private_key.get(), Text.get()))
    else:
         Encrpyted_message.set('Invalid Mode')



#Function to exit window
        
def Exit():
    root.destroy()


#Function to reset
def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Encrpyted_message.set("")

#Message
Label(root, font= 'arial 15 bold', text='MESSAGE').place(x= 60,y=60)
Entry(root, font = 'arial 10', textvariable = Text, bg = 'light yellow').place(x=290, y = 60)

#key
Label(root, font = 'arial 15 bold', text ='KEY',bg ='orange').place(x=60, y = 90)
Entry(root, font = 'arial 10', textvariable = private_key , bg ='light yellow').place(x=290, y = 90)


#mode
Label(root, font = 'arial 15 bold', text ='MODE').place(x=60, y = 120)
Entry(root, font = 'arial 10', textvariable = mode , bg= 'light yellow').place(x=290, y = 120)



#result
Entry(root, font = 'arial 15 bold', textvariable = Encrpyted_message, bg ='#e3c3c3').place(x=290, y = 150)

######result button
Button(root, font = 'arial 10 bold', text = 'Encrpyt / Decrypt', width =20 ,padx =10,bg ='#e36464' ,command = Mode).place(x=60, y = 150)


#reset button
Button(root, font = 'arial 10 bold' ,text ='RESET' ,width =20, command = Reset,bg = '#65d4f0', padx=2).place(x=200, y = 240)

#exit button
Button(root, font = 'arial 10 bold',text= 'EXIT' , width = 20, command = Exit,bg = 'OrangeRed', padx=2, pady=2).place(x=400, y = 240)
root.mainloop()
