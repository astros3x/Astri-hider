from cryptography.fernet import Fernet
from tkinter import messagebox
import customtkinter as ctk
from PIL import Image
import customtkinter
from random import *
import string
import base64
import webbrowser
import shutil
import requests
import json
import secrets,random
import sys
import os

def function_clear(path):
    with open(path, "rb+") as f:
        content = f.read()
        off = content.index(bytes.fromhex("FFD9"))
        if off != -1:
            f.seek(off + 2)
            f.truncate()

def check_ext(path):
    if path.endswith('.jpg'):
        return True
    
    else:
        return False

def get_filename(path):
    available = ["\\","/"]

    for z in available:
        if z in path:
            return path.split(z)[-1]

def file_present(path):
    try:
        open(path,"r")
        return True
    except FileNotFoundError:
        return False

def asset_downloader():
    try:
        os.remove(assetsfolder)
    except:
        os.system(f"mkdir {assetsfolder} > NUL 2>&1")

    for x in files:
        x = x.replace("\\","/")
        r = requests.get(f"https://raw.githubusercontent.com/astros3x/astri-hider/main/{x}")
        open(x,"wb").write(r.content)
    
    print("Download Done !")

def folders_checker():
    for x in folders:
        if not os.path.exists(x): 
            os.system(f"mkdir {x} > NUL 2>&1")


def assetschecker():
    try:
        for x in files:
            open(x)
            
        return True
    
    except FileNotFoundError:
        return False


def openbin():
    os.startfile(binfolder)


def opendiscord():
    webbrowser.open('https://discord.com/invite/GDMVrNF8Gr')


def opengithub():
    webbrowser.open('https://github.com/astros3x')


def credits():
    messagebox.showinfo("Credits", "This program was made by:\n- @astros3x\n- @CaptainBeluga\n\nCheck our Githubs.\nJoin discord for support.")


class App(customtkinter.CTk):
    def __init__(mini):
        super().__init__()

        #WINDOW CONFIG
        mini.overrideredirect(True)

        mini.title("Astri@Hider | by Astri Devs")
        mini.geometry("690x440")

        mini.bind('<ButtonPress-1>', mini.drag)
        mini.bind('<B1-Motion>', mini.move)
        mini.bind('<ButtonRelease-1>', mini.stop)


        
        #MAIN WINDOW
        mini.bar = customtkinter.CTkFrame(mini, 
                                        corner_radius = 0, 
                                        fg_color = 'black')
        
        mini.bar.grid_rowconfigure((1, 2), weight=1)        
        mini.bar.grid(sticky="nsew")



        #WINDOW TITLEBAR
        mini.title = customtkinter.CTkLabel(mini.bar, 
                                            text="Astri@Hider", 
                                            text_color= 'white', 
                                            font=('Papyrus', 20))
        
        mini.title.grid(padx=30)


        mini.titlebar = customtkinter.CTkFrame(mini.bar, 
                                            width=10, 
                                            corner_radius=0, 
                                            fg_color = 'black') 
        
        mini.titlebar.grid(row=0, column=4, sticky="nsew")


        mini.titlebar = customtkinter.CTkButton(mini.titlebar,
                                                text="✕", 
                                                fg_color=color, 
                                                text_color='black', 
                                                hover_color=seccolor, 
                                                width=4,
                                                command = mini.close,)
        
        mini.titlebar.grid(padx=(465 , 30), pady=15)



        #WINDOW LEVEL
        mini.background = ctk.CTkFrame(mini, 
                                    width=800, 
                                    corner_radius=0)

        mini.background.grid(row = 1, sticky="nsew")



        #BUTTONS
        mini.git_button = customtkinter.CTkButton(mini.background, 
                                                    width = 10, height = 25,
                                                    fg_color = ftransparent, 
                                                    hover_color = ftransparent,
                                                    text = None, 
                                                    image = ds_logo, 
                                                    command= opendiscord)
        
        mini.git_button.place(relx = 0.01, rely = 0.915) 


        mini.git_button = customtkinter.CTkButton(mini.background, 
                                                    width = 10, 
                                                    height = 25,
                                                    fg_color = ftransparent, 
                                                    hover_color = ftransparent,
                                                    text = None, 
                                                    image = gh_logo, 
                                                    command = opengithub)
        
        mini.git_button.place(relx = 0.065, rely = 0.9)      
       

        mini.git_button = customtkinter.CTkButton(mini.background, 
                                                    width = 10, 
                                                    height = 25,
                                                    fg_color = ftransparent, 
                                                    hover_color = ftransparent,
                                                    text = None, 
                                                    image = info_logo, 
                                                    command = credits)
        
        mini.git_button.place(relx = 0.12, rely = 0.9)



        def writemsg():

            def writer():
                
                try:
                    getpath = input_path.get()
                    pass

                except Exception as e:
                    messagebox.showerror('Error', f'{e}')
                
                try:
                    if file_present(getpath):

                        if check_ext(getpath):
                            msg = input_text.get().encode()

                            #SCRIPT TO ADD THE MESSAGE TO THE JPG
                            filename = get_filename(getpath)

                            shutil.copy(getpath,res_default)

                            PATH = f"{res_default}\\{filename}"

                            function_clear(PATH)

                            f = open(PATH, "ab")
                            f.write(msg)

                            messagebox.showinfo("DONE !",f"Message successfully hide => `{filename}` ")

                        else:
                            messagebox.showerror("ERROR", f"Your Image is NOT a JPG !")
                    else:
                        messagebox.showerror("ERROR", f"`{getpath}` NOT found !")

                    


                    
                    #checkboxresult
                    val = checkbox.get()

                    if val == 1:
                        os.startfile(res_default)

                except Exception as e:
                    messagebox.showerror('Error', f'{e}')


            for widget in mini.main.winfo_children():
                widget.destroy()

            
            wtitle = customtkinter.CTkLabel(mini.main, 
                                                text = 'MESSAGE HIDER', 
                                                font=tfont)
            
            wtitle.place(relx = 0.357, rely = 0.06)


            qm_button = customtkinter.CTkButton(mini.main, 
                                width = 8, 
                                height = 11,
                                fg_color = stransparent, 
                                hover_color = stransparent,
                                text = None, 
                                image = qm_logo, 
                                command = exwriter)

            qm_button.place(relx = 0.9, rely = 0.05)


            input_path = customtkinter.CTkEntry(mini.main, 
                                                    placeholder_text='File path')
            
            input_path.place(relx = 0.35, rely = 0.30)


            input_text = customtkinter.CTkEntry(mini.main,
                                                    placeholder_text='Message')
            
            input_text.place(relx = 0.35, rely = 0.50)


            backbutton = customtkinter.CTkButton(mini.main, 
                                                    text = None, 
                                                    image = back, width=25, 
                                                    height=20, 
                                                    font = bfont,
                                                    fg_color = stransparent, 
                                                    hover=stransparent, 
                                                    command=mainmenu)
            
            backbutton.place(relx = 0.34, rely = 0.85)


            start = customtkinter.CTkButton(mini.main, 
                                                text = "Hide", 
                                                width=100, 
                                                height=20, 
                                                font = bfont,
                                                text_color = 'black',
                                                fg_color = color, 
                                                hover_color=seccolor, 
                                                command=writer)
            
            start.place(relx = 0.43, rely = 0.85)


            checkbox = customtkinter.CTkCheckBox(mini.main,
                                                    onvalue=1, 
                                                    text = None,
                                                    checkbox_width = 15, 
                                                    checkbox_height =15,
                                                    border_width=2, 
                                                    fg_color=color, 
                                                    checkmark_color='black')
            
            checkbox.place(relx = 0.60, rely = 0.63)


            checktext = customtkinter.CTkLabel(mini.main,
                                                    text = 'Open path',
                                                    font = ('Bahnschrift', 10))
            checktext.place(relx = 0.50, rely = 0.62)



        def msgreader():

            def reader():
                try:
                    getpath = input_path.get()
                except Exception as e:
                    messagebox.showerror('Error', f'{e}')
                
                try:

                    if(check_ext(getpath)):

                        #SCRIPT TO EXTRACT THE MESSAGE FROM THE JPG

                        f = open(getpath,"rb")

                        content = f.read()
                        off = content.index(bytes.fromhex('FFD9'))
                        f.seek(off + 2)

                        msg = f.read().decode('utf-8')


                        filename = get_filename(getpath)


                        #insert the result in the textbox
                        result.insert('1.0', msg)

                    else:
                        messagebox.showerror("ERROR", f"Your Image is NOT a JPG !")

                        
                except Exception as e:
                    messagebox.showerror('Error', f'{e}')


            for widget in mini.main.winfo_children():
                widget.destroy()


            rtitle = customtkinter.CTkLabel(mini.main, 
                                                text = 'JPG MSG READER', 
                                                font=tfont)
            
            rtitle.place(relx = 0.35, rely = 0.06)


            qm_button = customtkinter.CTkButton(mini.main, 
                                width = 8, 
                                height = 11,
                                fg_color = stransparent, 
                                hover_color = stransparent,
                                text = None, 
                                image = qm_logo, 
                                command = exreader)

            qm_button.place(relx = 0.9, rely = 0.05)


            input_path = customtkinter.CTkEntry(mini.main, 
                                                    placeholder_text='File path',
                                                    width=170)
            
            input_path.place(relx = 0.31, rely = 0.20)


            result = customtkinter.CTkTextbox(mini.main,
                                            text_color='white',
                                            state="normal",
                                            activate_scrollbars=True, 
                                            width=333,
                                            height=110,
                                            corner_radius=0,
                                            border_width=2,
                                            scrollbar_button_color = color,
                                            scrollbar_button_hover_color = seccolor,
                                            font = bfont)
            
            result.place(relx = 0.15, rely = 0.35)


            read = customtkinter.CTkButton(mini.main, 
                                                text = "Extract",
                                                text_color = 'black',
                                                width=190, 
                                                height=20, 
                                                font = bfont,
                                                fg_color = color, 
                                                hover_color=seccolor, 
                                                command=reader)
            
            read.place(relx = 0.44, rely = 0.85)


            clear = ctk.CTkButton(mini.main,
                                  text='Clear',
                                  command=lambda: [result.delete('1.0', ctk.END)],
                                  width=85,
                                  height=20,
                                  fg_color=color, 
                                  text_color='black',
                                  hover_color=seccolor,
                                  font=bfont)
            
            clear.place(relx = 0.23, rely = 0.85)


            backbutton = customtkinter.CTkButton(mini.main, 
                                                    text = None, 
                                                    image = back, width=25, 
                                                    height=20, 
                                                    font = bfont,
                                                    fg_color = stransparent, 
                                                    hover=stransparent, 
                                                    command=mainmenu)
            
            backbutton.place(relx = 0.14, rely = 0.85)

        

        def clearjpg():

            def cleaner():
                try:                
                    getpath = input_path.get()
                except Exception as e:
                    messagebox.showerror('Error', f'{e}')

                try:
                    if (file_present(getpath)):
                        if(check_ext(getpath)):
                            #SCRIPT TO CLEAR THE HIDDEN CONTENT FROM THE JPG

                            filename = get_filename(getpath)
                            shutil.copy(getpath,res_cleared)

                            with open(f"{res_cleared}\\{filename}", "rb+") as f:

                                content = f.read()
                                off = content.index(bytes.fromhex("FFD9")) #this function delet only the content at the end of the hex code

                                if off != -1:
                                    f.seek(off + 2)
                                    f.truncate()
                                    messagebox.showinfo("DONE !",f"Image Cleared => `{filename}` ")
                                else:
                                    messagebox.showerror('Error', 'No hidden content in this file!')
                            
                            
                            val = checkbox.get() #if checkbox is flagged open the results folder

                            if val == 1:
                                os.startfile(res_cleared)
                        else:
                            messagebox.showerror("ERROR", f"Your Image is NOT a JPG !")
                    else:
                        messagebox.showerror("ERROR", f"`{getpath}`found !")

                except Exception as e:
                    messagebox.showerror('Error', f'{e}')



            for widget in mini.main.winfo_children():
                widget.destroy()


            ctitle = customtkinter.CTkLabel(mini.main, 
                                                text = 'CLEAR JPG HIDDEN CONTENT', 
                                                font=tfont)
            
            ctitle.place(relx = 0.25, rely = 0.06)


            qm_button = customtkinter.CTkButton(mini.main, 
                                width = 8, 
                                height = 11,
                                fg_color = stransparent, 
                                hover_color = stransparent,
                                text = None, 
                                image = qm_logo, 
                                command = excleaner)

            qm_button.place(relx = 0.9, rely = 0.05)


            input_path = customtkinter.CTkEntry(mini.main, 
                                                    placeholder_text='File path',
                                                    width=170)
            
            input_path.place(relx = 0.30, rely = 0.42)


            checkbox = customtkinter.CTkCheckBox(mini.main,
                                                    onvalue=1, 
                                                    text = None,
                                                    checkbox_width = 15, 
                                                    checkbox_height =15,
                                                    border_width=2, 
                                                    fg_color=color, 
                                                    checkmark_color='black')
            
            checkbox.place(relx = 0.62, rely = 0.56)


            checktext = customtkinter.CTkLabel(mini.main,
                                                    text = 'Open path',
                                                    font = ('Bahnschrift', 10))
            
            checktext.place(relx = 0.50, rely = 0.55)


            clear = ctk.CTkButton(mini.main,
                        text='clear',
                        command=cleaner,
                        width=140,
                        height=20,
                        fg_color=color, 
                        text_color='black',
                        hover_color=seccolor,
                        font=bfont)
            
            clear.place(relx = 0.36, rely = 0.85)

            backbutton = customtkinter.CTkButton(mini.main, 
                                                    text = None, 
                                                    image = back, width=25, 
                                                    height=20, 
                                                    font = bfont,
                                                    fg_color = stransparent, 
                                                    hover=stransparent, 
                                                    command=mainmenu)
            
            backbutton.place(relx = 0.28, rely = 0.85)        



        def key_gen():
            def db_mixer():
                db = dict(json.loads(open(db_base_path,"r").read()))

                body = '{'


                keys = []

                for k in db:
                    keys.append(db[k])

                for x in range(len(db) +1):
                    if x != 0:
                        delimiter = ""

                        choice = secrets.choice(keys)
                        keys.remove(choice)

                        if choice == "":
                            choice = " "
                        
                        elif x != len(db):
                            delimiter = ","

                        body += f'"{x}" : "{choice}"{delimiter}\n'


                body += '}'

                open(db_path,"w").write(body)

            def keygen():
                numbers = string.digits

                def gen_number():
                    while True:

                        x = ""

                        for _ in range(3):
                            x+= secrets.choice(numbers)

                        x = int(x)

                        if(isPrime(x)):
                            return x


                def isPrime(n, k=5):
                    if n <= 1:
                        return False
                    if n <= 3:
                        return True

                    r, s = 0, n - 1
                    while s % 2 == 0:
                        r += 1
                        s //= 2

                    for _ in range(k):
                        a = random.randint(2, n - 1)
                        x = pow(a, s, n)
                        if x == 1 or x == n - 1:
                            continue
                        for _ in range(r - 1):
                            x = pow(x, 2, n)
                            if x == n - 1:
                                break
                        else:
                            return False

                    return True




                def mcd(a,b):
                    while b:
                        a, b = b, a % b
                    return a

                        
                p = gen_number()
                q = gen_number()
                sm = ""

                for _ in range(3):
                    sm+= secrets.choice(numbers)

                sm = int(sm)


                n = p * q

                z = (p-1) * (q-1)
                while True:
                    e = ""

                    for _ in range(5):
                        e+= secrets.choice(numbers)
                    
                    e = int(e)

                    if mcd(e,z) == 1:
                        break


                d = pow(e,-1,z)


                if((d*e) % z == 1):

                    PUBLIC_KEY = f"KKK_{e}_{n}_{sm}_KKK"

                    PRIVATE_KEY = f"KKK_{d}_{n}_{sm}_KKK"



                    to_write = f"{PUBLIC_KEY}\n{PRIVATE_KEY}"

                    open(key_path,"w").write(to_write)
                            
            def gen():
                    keygen()
                    db_mixer()

                    messagebox.showinfo("DONE !",f"New Keys Pair and JSON SCHEME set SUCCESSFULLY !")

                    val = checkbox.get() #if checkbox is flagged open the results folder
                    if val == 1:
                        os.startfile(encryptionfolder)

            for widget in mini.main.winfo_children():
                widget.destroy()


            ktitle = customtkinter.CTkLabel(mini.main, 
                                                text = 'KEYS PAIR & JSON SCHEME GENERATOR', 
                                                font=tfont)
            
            ktitle.place(relx = 0.25, rely = 0.06)


            qm_button = customtkinter.CTkButton(mini.main, 
                                width = 8, 
                                height = 11,
                                fg_color = stransparent, 
                                hover_color = stransparent,
                                text = None, 
                                image = qm_logo, 
                                command = excryption)

            qm_button.place(relx = 0.9, rely = 0.05)

            checkbox = customtkinter.CTkCheckBox(mini.main,
                                                    onvalue=1, 
                                                    text = None,
                                                    checkbox_width = 15, 
                                                    checkbox_height =15,
                                                    border_width=2, 
                                                    fg_color=color, 
                                                    checkmark_color='black')
            
            checkbox.place(relx = 0.62, rely = 0.56)


            checktext = customtkinter.CTkLabel(mini.main,
                                                    text = 'Open path',
                                                    font = ('Bahnschrift', 10))
            
            checktext.place(relx = 0.50, rely = 0.55)


            genbutton = ctk.CTkButton(mini.main,
                        text='Generate',
                        command=gen,
                        width=90,
                        height=20,
                        fg_color=color, 
                        text_color='black',
                        hover_color=seccolor,
                        font=bfont)
            
            genbutton.place(relx = 0.40, rely = 0.85)


            backbutton = customtkinter.CTkButton(mini.main, 
                                                    text = None, 
                                                    image = back, width=25, 
                                                    height=20, 
                                                    font = bfont,
                                                    fg_color = stransparent, 
                                                    hover=stransparent, 
                                                    command=mainmenu)
            
            backbutton.place(relx = 0.25, rely = 0.85)
        


        def encryptedwriter():
            def cb_rsa_encrypt(k,m):
                key_split = k.split("_")

                e = int(key_split[1])
                n = int(key_split[2])
                sm = int(key_split[3])


                db = dict(json.loads(open(db_path,"r").read()))

                reverse_db = dict(zip(db.values(),db.keys()))

                encrypted_msg = "$$$_"

                for char in m:

                    try:
                        enc = int(reverse_db[char])

                    except: #KeyError
                        enc = int(reverse_db["$_$_$_$_$"])

                    c = int(pow((enc*sm),e) % n)

                    encrypted_msg+= f"{c}_"

                encrypted_msg+= "$$$"

                return base64.b64encode(encrypted_msg.encode())

            def encwriter():
                try:
                    get_path = input_path.get()
                    path = get_path.strip('"')
                except Exception as e:
                    messagebox.showerror('Error', f'{e}')

                try:

                    if(file_present(get_path)):

                        if(check_ext(get_path)):

                            filename = get_filename(get_path)

                            PATH = f"{res_encrypted}\\{filename}"

                            shutil.copy(get_path,res_encrypted)

                            function_clear(PATH)

                            f = open(PATH, "ab")
                            f.write(cb_rsa_encrypt(open(key_path,"r").read().split("\n")[0],input_text.get()))

                            messagebox.showinfo("DONE !",f"Encrypted Message successfully hide => `{filename}` ")

                            #checkboxresult
                            val = checkbox.get()

                            if val == 1:
                                os.startfile(res_encrypted)
                        
                        else:
                            messagebox.showerror("ERROR", f"Your Image is NOT a JPG !")
                    else:
                        messagebox.showerror("ERROR", f"`{path}`found !")

                except Exception as e:
                    print(e)
                    if "No such file" in str(e):
                        messagebox.showinfo("Create a KEYS PAIR","You need to GENERATE a Keys Pair and a JSON SCHEME !")
                        key_gen()
                    else:
                        messagebox.showerror('Error', f'{e}')

            for widget in mini.main.winfo_children():
                widget.destroy()

            
            wtitle = customtkinter.CTkLabel(mini.main, 
                                                text = 'ENCRYPTED MESSAGE HIDER', 
                                                font=tfont)
            
            wtitle.place(relx = 0.25, rely = 0.06)


            qm_button = customtkinter.CTkButton(mini.main, 
                                width = 8, 
                                height = 11,
                                fg_color = stransparent, 
                                hover_color = stransparent,
                                text = None, 
                                image = qm_logo, 
                                command = exencwriter)

            qm_button.place(relx = 0.9, rely = 0.05)


            input_path = customtkinter.CTkEntry(mini.main, 
                                                    placeholder_text='File path')
            
            input_path.place(relx = 0.35, rely = 0.30)


            input_text = customtkinter.CTkEntry(mini.main,
                                                    placeholder_text='Message')
            
            input_text.place(relx = 0.35, rely = 0.50)


            backbutton = customtkinter.CTkButton(mini.main, 
                                                    text = None, 
                                                    image = back, width=25, 
                                                    height=20, 
                                                    font = bfont,
                                                    fg_color = stransparent, 
                                                    hover=stransparent, 
                                                    command=mainmenu)
            
            backbutton.place(relx = 0.34, rely = 0.85)


            start = customtkinter.CTkButton(mini.main, 
                                                text = "Hide", 
                                                width=100, 
                                                height=20, 
                                                font = bfont,
                                                text_color = 'black',
                                                fg_color = color, 
                                                hover_color=seccolor, 
                                                command=encwriter)
            
            start.place(relx = 0.43, rely = 0.85)


            checkbox = customtkinter.CTkCheckBox(mini.main,
                                                    onvalue=1, 
                                                    text = None,
                                                    checkbox_width = 15, 
                                                    checkbox_height =15,
                                                    border_width=2, 
                                                    fg_color=color, 
                                                    checkmark_color='black')
            
            checkbox.place(relx = 0.60, rely = 0.63)


            checktext = customtkinter.CTkLabel(mini.main,
                                                    text = 'Open path',
                                                    font = ('Bahnschrift', 10))
            checktext.place(relx = 0.50, rely = 0.62)



        def encmsgreader():
            def cb_rsa_decrypt(k,m):
                key_split = k.split("_")
                d = int(key_split[1])
                n = int(key_split[2])
                sm = int(key_split[3])

                db = dict(json.loads(open(db_path,"r").read()))

                m = base64.b64decode(m).decode().split("_")

                message = ""

                for val in m:
                    if val != "$$$":

                        c = round((int(val)**d % n) / sm)
                        
                        message+= db[str(c)]

                return message

            def reader():
                try:
                    getpath = input_path.get()
                except Exception as e:
                    messagebox.showerror('Error', f'{e}')
                
                try:
                    if check_ext(getpath):

                        #SCRIPT TO EXTRACT THE ENCRIPTED MESSAGE FROM THE JPG
                        f = open(getpath,"rb")
                        content = f.read()

                        off = content.index(bytes.fromhex('FFD9'))
                        f.seek(off + 2)

                        original_msg = f.read().decode('utf-8')

                        #insert the result in the textbox
                        result.insert('1.0', cb_rsa_decrypt(open(key_path,"r").read().split("\n")[1],original_msg))
                        
                    else:
                        messagebox.showerror("ERROR", f"`{getpath}`found !")

                except Exception as e:
                    if "No such file" in str(e):

                        if "db.json" in str(e):
                            messagebox.showerror("SCHEME MISSING", f"GENERATE A JSON SCHEME !")
                        
                        else:
                            messagebox.showerror("ERROR", f"`{getpath}` NOT found !")

                    else:
                        messagebox.showerror('Error', f'Private Key NOT CORRECT !')



            for widget in mini.main.winfo_children():
                widget.destroy()


            rtitle = customtkinter.CTkLabel(mini.main, 
                                                text = 'ENCRYPTED JPG MSG READER', 
                                                font=tfont)
            
            rtitle.place(relx = 0.25, rely = 0.06)


            qm_button = customtkinter.CTkButton(mini.main, 
                                width = 8, 
                                height = 11,
                                fg_color = stransparent, 
                                hover_color = stransparent,
                                text = None, 
                                image = qm_logo, 
                                command = exencreader)

            qm_button.place(relx = 0.9, rely = 0.05)


            input_path = customtkinter.CTkEntry(mini.main, 
                                                    placeholder_text='File path',
                                                    width=170)
            
            input_path.place(relx = 0.31, rely = 0.20)


            result = customtkinter.CTkTextbox(mini.main,
                                            text_color='white',
                                            state="normal",
                                            activate_scrollbars=True, 
                                            width=333,
                                            height=110,
                                            corner_radius=0,
                                            border_width=2,
                                            scrollbar_button_color = color,
                                            scrollbar_button_hover_color = seccolor,
                                            font = bfont)
            
            result.place(relx = 0.15, rely = 0.35)


            read = customtkinter.CTkButton(mini.main, 
                                                text = "Read Encrypted",
                                                text_color = 'black',
                                                width=190, 
                                                height=20, 
                                                font = bfont,
                                                fg_color = color, 
                                                hover_color=seccolor, 
                                                command=reader)
            
            read.place(relx = 0.44, rely = 0.85)


            clear = ctk.CTkButton(mini.main,
                                  text='clear',
                                  command=lambda: [result.delete('1.0', ctk.END)],
                                  width=85,
                                  height=20,
                                  fg_color=color, 
                                  text_color='black',
                                  hover_color=seccolor,
                                  font=bfont)
            
            clear.place(relx = 0.23, rely = 0.85)


            backbutton = customtkinter.CTkButton(mini.main, 
                                                    text = None, 
                                                    image = back, width=25, 
                                                    height=20, 
                                                    font = bfont,
                                                    fg_color = stransparent, 
                                                    hover=stransparent, 
                                                    command=mainmenu)
            
            backbutton.place(relx = 0.14, rely = 0.85)



        #MAIN MENU
        mini.main = customtkinter.CTkFrame(mini.background, 
                                        width=140)
        
        mini.main.grid(sticky="nsew", row = 1, padx=(100,100), pady = (70, 70))
        mini.main.grid_rowconfigure((1,2,3), weight=1)



        #main menu widgets
        def mainmenu():
            for widget in mini.main.winfo_children():
                widget.destroy()


            write = customtkinter.CTkButton(mini.main, 
                                                text="Hide Msg", 
                                                fg_color=color, 
                                                text_color='black', 
                                                font=bfont, 
                                                hover_color=seccolor, 
                                                command = writemsg)
            
            write.grid(row=1, column=1, padx = 50, pady = (50, 30))


            read = customtkinter.CTkButton(mini.main, 
                                                text="Read Jpg", 
                                                fg_color=color, 
                                                text_color='black', 
                                                font=bfont, 
                                                hover_color=seccolor,
                                                command = msgreader)
            
            read.grid(row=1, column=2, padx = 50, pady = (50, 30))


            obfuscated = customtkinter.CTkButton(mini.main, 
                                                    text="Encrypted Msg",
                                                    fg_color=color, 
                                                    text_color='black',
                                                    font=bfont,
                                                    hover_color=seccolor,
                                                    command=encryptedwriter)
            
            obfuscated.grid(row=2, column=1, pady = (0, 30))


            key = customtkinter.CTkButton(mini.main,
                                               text="Read Encrypted",
                                               fg_color=color, 
                                               text_color='black', 
                                               font=bfont, 
                                               hover_color=seccolor,
                                               command=encmsgreader)
            
            key.grid(row=2, column=2, pady = (0, 30))


            key = customtkinter.CTkButton(mini.main, 
                                               text="Encryption Key", 
                                               fg_color=color, 
                                               text_color='black',
                                               font=bfont, 
                                               hover_color=seccolor,
                                               command=key_gen)
            
            key.grid(row=3, column=1, pady = (0, 50))


            key = customtkinter.CTkButton(mini.main,
                                               text="Cleaner",
                                               fg_color=color, 
                                               text_color='black',
                                               font=bfont,
                                               hover_color=seccolor,
                                               command = clearjpg)
            
            key.grid(row=3, column=2, pady = (0, 50))

            folderbutton = customtkinter.CTkButton(mini.main, 
                                width = 8, 
                                height = 11,
                                fg_color = stransparent, 
                                hover_color = stransparent,
                                text = None, 
                                image = folder_ico, 
                                command = openbin)

            folderbutton.place(relx = 0.9, rely = 0.87)

        

        #START THE MAIN MENU
        mainmenu()


        #EXPLAINATIONS OPTIONS
        def exwriter():
            messagebox.showinfo("Message Hider Info", "This option allows you to hide a secret text message in a JPG file without actually changing the look of the image.")
        def exreader():
            messagebox.showinfo("Message Reader Info", "This option allows you to read a secret text message hidden in a JPG file.")
        def excleaner():
            messagebox.showinfo("JPG Cleaner Info", "This option allows you to clean a JPG file from hidden content.")
        def excryption():
            messagebox.showinfo("Encryption Key Gen Info", "This option allows you to create your own .key file to encrypt your messsage in the JPG file with your own decryption password.")
        def exencwriter():
            messagebox.showinfo("Encryped Message Hider Info", "This option allows you to hide a secret text message encrypted with you own .key in a JPG file without actually changing the look of the image.\n\n(Modify the '.key' file with the 'Encryption Key Gen' from the menu before to use this option).")
        def exencreader():
            messagebox.showinfo("Encryped Message Reader Info", "This option allows you to read an encrypted text message hidden in a JPG file using the '.key' file used to crypt it.")

    #MOVMENT SYSTEM
    def drag(mini, event):
        mini._x = event.x
        mini._y = event.y
    def move(mini, event):
        new_x = mini.winfo_x() - mini._x + event.x
        new_y = mini.winfo_y() - mini._y + event.y
        mini.geometry(f'+{new_x}+{new_y}')
        mini.attributes('-alpha', 0.3)
    def stop(mini, event):
        mini.geometry(f'+{mini.winfo_x()}+{mini.winfo_y()}')
        mini.attributes('-alpha', 1.0)

    def close(mini):
        if messagebox.askokcancel("Exit", "Are you sure to close astri@hider?"):
            sys.exit()



            
if __name__ == "__main__":

    #PROGRAM PROPERTIES
    version = "1.0.0"
    release = "https://github.com/astros3x/astri-hider/releases"

    binfolder = "bin"

    resfolder = "bin\\results"
    res_encrypted = "bin\\results\\encrypted"
    res_cleared = "bin\\results\\cleared"
    res_default = "bin\\results\\default"

    assetsfolder = "bin\\assets\\"
    encryptionfolder = "bin\\encryption\\"

    key_path = "bin\\encryption\\key.key"

    db_base_path = "bin\\encryption\\db_BASE.json"
    db_path = "bin\\encryption\\db.json"

    folders = [binfolder, 
            resfolder, 
            res_encrypted, 
            res_cleared, 
            res_default,
            assetsfolder,
            encryptionfolder]

    files = [f"{assetsfolder}back.png",
             f"{assetsfolder}ds_logo.png",
             f"{assetsfolder}folder_ico.png",
             f"{assetsfolder}gh_logo.png",
             f"{assetsfolder}info_logo.png",
             f"{assetsfolder}qm_logo.png",
             f"{encryptionfolder}db_BASE.json"
             ]


    #VERSION CHECKER
    try:
        r = requests.get("https://raw.githubusercontent.com/astros3x/astri-hider/main/version.txt").text.strip()

        if r == version:
            pass

        else:
            if messagebox.askokcancel("Update Available", "A new version is available. Wanna download it?"):
                webbrowser.open(release)
            
            else:
                pass

    except Exception as e:
        messagebox.showerror('ERROR', "Version check failed http error/offline.\nPress 'Ok' to continue.")
        pass


    # ASSETS CHECKER
    try:
        folders_checker() #Checks the presence of the required folders
        
        if assetschecker() == True: #Check the assets
            pass

        else:
            try:
                print("Downloading Assets....")
                asset_downloader() #Download the assets if not found

            except Exception as e:
                messagebox.showerror('Error', f'{e}')

    except Exception as e:
        messagebox.showerror('Error', f'{e}')


    #ASSETS
    color = '#00f71c'
    seccolor = '#01aa15'
    thirdcolor = 'black'
    ftransparent = '#2b2b2b'
    stransparent = '#333333'

    tfont = ("Impact", 21)
    bfont = ('Bahnschrift', 15)

    logo = (assetsfolder + "ico.png")
    folder_ico = customtkinter.CTkImage(Image.open(assetsfolder + "folder_ico.png"), size=(20, 15))
    ds_logo = customtkinter.CTkImage(Image.open(assetsfolder + "ds_logo.png"), size=(20, 15))
    gh_logo = customtkinter.CTkImage(Image.open(assetsfolder + "gh_logo.png"), size=(22, 22))
    info_logo = customtkinter.CTkImage(Image.open(assetsfolder + "info_logo.png"), size=(20, 20))
    qm_logo = customtkinter.CTkImage(Image.open(assetsfolder + "qm_logo.png"), size=(12, 16))
    back = customtkinter.CTkImage(Image.open(assetsfolder + "back.png"), size=(23, 19))


    app = App()
    app.mainloop()