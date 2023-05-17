import customtkinter
import guiLib
import conn
import voice

app = customtkinter.CTk()

menuMainSimpleActive = False

def windowStart():
    guiLib.prepareNewWindow(app, 300, 350, False)
    a = ''

    label = { "name" : customtkinter.CTkLabel(app,text= guiLib.projectName, font = ("Poppins", 30)),
              "error": customtkinter.CTkLabel(app, text = a, font=("Poppins", 30), text_color = "red")
             }

    entry = {
        "login" : customtkinter.CTkEntry(master=app, placeholder_text="Login"),
        "password" : customtkinter.CTkEntry(master=app, placeholder_text="Password")
    }

    def logdans():
        logs = entry["login"].get()
        pas = entry["password"].get()
        conn.login(logs, pas)
        print(logs, pas)

        asid = conn.curent()
        print(asid)
        if asid == 1:
            windowMainExtended()
        else:
             windowSinginInError()

    def error_pass():
        global a 
        a = 'Нвереные данные'

    button = {
        "signIn" : customtkinter.CTkButton(master=app, corner_radius= 20,  text="Sign in", command=logdans),
        "signUp" : customtkinter.CTkButton(master=app, corner_radius= 20,  text="Sign Up", command=windowSignUp)
    }
    

    guiLib.configure(label["name"], placeX= 85, placeY= 40)
    guiLib.configure(label["error"], placeX= 93, placeY= 300)

    guiLib.configure(entry["login"], width=200, height=40, placeX= 50, placeY= 90)
    guiLib.configure(entry["password"], width=200, height=40, placeX= 50, placeY= 150)

    guiLib.configure(button["signIn"], width=130, height=30, placeX= 85, placeY= 215)
    guiLib.configure(button["signUp"], width=130, height=30, placeX= 85, placeY= 260)

def windowSinginInError():
    guiLib.prepareNewWindow(app, 300, 350, False)

    label = { "name" : customtkinter.CTkLabel(app,text= guiLib.projectName, font = ("Poppins", 30)),
              "error": customtkinter.CTkLabel(app, text = "Неверные данные!", font=("Poppins", 30), text_color = "red")
             }
    
    button = {
        "retry" : customtkinter.CTkButton(master=app, corner_radius= 20,  text="Повторить   ", command=windowStart),
    }
    
    guiLib.configure(label["name"], placeX= 85, placeY= 40)
    guiLib.configure(label["error"], placeX= 20, placeY= 300)

    guiLib.configure(button["retry"], width=130, height=30, placeX=85, placeY=215)

def windowSignUp():
    guiLib.prepareNewWindow(app, 500, 320, True, windowStart)

    entry = {
        "login" : customtkinter.CTkEntry(master=app, placeholder_text="Login"),
        "password" : customtkinter.CTkEntry(master=app, placeholder_text="Password"),
        "confirmPassword" : customtkinter.CTkEntry(master=app, placeholder_text="Confirm password"),
        "mail" : customtkinter.CTkEntry(master=app, placeholder_text="Mail"),
        "name" : customtkinter.CTkEntry(master=app, placeholder_text="Name"),
        "lastName" : customtkinter.CTkEntry(master=app, placeholder_text="Last name")
    }

    def reg_dans():

        

        logs = entry["login"].get()
        pas = entry["password"].get()
        pas2 = entry["confirmPassword"].get()
        mail = entry["mail"].get()
        fname = entry["name"].get()
        secondName = entry["lastName"].get()

        if pas == pas2:

            conn.reg(logs, fname, secondName, mail, pas)
            print(logs, fname, secondName, mail, pas)
            
            asid = conn.curent()
            print(asid)
            if asid == 1:
                windowMainSimple() 
            else:
                registrationError("Уже существует!")

        else: 
            registrationError("Пароли")


    # checkbox = { "license" : customtkinter.CTkCheckBox(master=app, text="License agreement", cursor = "hand2") }

    # button = { "confirm" : customtkinter.CTkButton(master=app, text="Confirm", state="disabled", command = lambda: guiLib.checkSignUp(app, entry, checkbox))  }
    button = { "confirm" : customtkinter.CTkButton(master=app, text="Confirm", command = reg_dans)  }

    guiLib.configure(object = entry["login"], width = 200, height = 40, placeX = 33, placeY = 80)
    guiLib.configure(object = entry["password"], width = 200, height = 40, placeX = 266, placeY = 80)

    guiLib.configure(object = entry["mail"], width = 200, height = 40, placeX = 33, placeY = 140)
    guiLib.configure(object = entry["confirmPassword"], width = 200, height = 40, placeX = 266, placeY = 140)

    guiLib.configure(object = entry["name"], width = 200, height = 40, placeX = 33, placeY = 200)
    guiLib.configure(object = entry["lastName"], width = 200, height = 40, placeX = 266, placeY = 200)

    guiLib.configure(object = button["confirm"], width=200, height=30, placeX=266, placeY=260)


def registrationError(what):
    guiLib.prepareNewWindow(app, 500, 320, True, windowStart)

    label = { "name" : customtkinter.CTkLabel(app,text= guiLib.projectName, font = ("Poppins", 30)),
              "error": customtkinter.CTkLabel(app, text = "Ошибка с " + what, font=("Poppins", 30), text_color = "red")
             }
    
    button = {
        "retry" : customtkinter.CTkButton(master=app, corner_radius= 20,  text="Повторить   ", command=windowSignUp),
    }
    
    guiLib.configure(label["name"], placeX= 85, placeY= 40)
    guiLib.configure(label["error"], placeX= 20, placeY= 270)

    guiLib.configure(button["retry"], width=130, height=30, placeX=85, placeY=215)

def changeMainMenuSimpleActive(window = lambda: windowMainSimple()):
    global menuMainSimpleActive
    if menuMainSimpleActive: menuMainSimpleActive = False
    else: menuMainSimpleActive = True
    window()

def windowMainSimple():
    guiLib.prepareNewWindow(app, 300, 300, False)

    frame = {"assistantActive" : customtkinter.CTkFrame(app),
                    "menu" : customtkinter.CTkFrame(app, 0, 0)}

    label = { "name" : customtkinter.CTkLabel(app,text= guiLib.projectName, font = ("Poppins", 24))}

    guiLib.configure(frame["assistantActive"], width = 200, height = 60, placeX= 50, placeY= 120)

    guiLib.configure(label["name"], placeX= 165, placeY= 45)

    if menuMainSimpleActive:
        label = { "menu" : customtkinter.CTkLabel(frame["menu"],text= "Menu", font = ("Poppins", 20))}

        button = { "menu" : customtkinter.CTkButton(master=frame["menu"], image= guiLib.imagePull["menu"], text = "", fg_color = "transparent", hover = False, command= changeMainMenuSimpleActive),
                            "settings": customtkinter.CTkButton(master=frame["menu"], text="Settings", command=lambda: changeMainMenuSimpleActive(windowSettingsSimple)),
                            "information" : customtkinter.CTkButton(master=frame["menu"],  text="Information", command=lambda: changeMainMenuSimpleActive(windowInformationSimple)),
                            "account" : customtkinter.CTkButton(master=frame["menu"],  text="Account", command= lambda: changeMainMenuSimpleActive(windowAccountSimple))}

        guiLib.configure(label["menu"], placeX= 50, placeY= 20)

        guiLib.configure(button["menu"], placeX= 110, placeY= 10, changeColorButton=False)
        guiLib.configure(button["settings"], width= 130, height= 30, placeX= 10, placeY= 60)
        guiLib.configure(button["information"], width= 130, height= 30, placeX= 10, placeY= 100)
        guiLib.configure(button["account"], width= 130, height= 30, placeX= 10, placeY= 140)

        guiLib.configure(frame["menu"], 150, 180, placeY=30)
    else:
        button = { "menu" : customtkinter.CTkButton(master=app, image= guiLib.imagePull["menu"], text = "", fg_color = "transparent", hover = False, command= changeMainMenuSimpleActive)}
        guiLib.configure(button["menu"], placeX= 0, placeY= 40, changeColorButton=False)
        guiLib.configure(frame["menu"], 0, 0)

def windowInformationSimple():
    guiLib.prepareNewWindow(app, 300, 300, False, windowMainSimple)

    label = { "version" : customtkinter.CTkLabel(app,text= guiLib.projectVersion, font = ("Poppins", 16))}

    button = {"developers" : customtkinter.CTkButton(master=app, text="Developers", command=windowDevelopersSimple),
                    "donate" : customtkinter.CTkButton(master=app, text="Donate"),
                    "report a bag": customtkinter.CTkButton(master=app, text="Report a bag")}

    guiLib.configure(button["developers"], width= 130, height= 30, placeX= 85, placeY= 70)
    guiLib.configure(button["donate"], width= 130, height= 30, placeX= 85, placeY= 120)
    guiLib.configure(button["report a bag"], width= 130, height= 30, placeX= 85, placeY= 170)

    guiLib.configure(label["version"], placeX= 85, placeY= 260)

    frame = {"menu" : customtkinter.CTkFrame(app, 0, 0)}

    if menuMainSimpleActive:
        label = { "menu" : customtkinter.CTkLabel(frame["menu"],text= "Menu", font = ("Poppins", 20))}

        button = { "menu" : customtkinter.CTkButton(master=frame["menu"], image= guiLib.imagePull["menu"], text = "", fg_color = "transparent", hover = False, command=lambda: changeMainMenuSimpleActive(windowInformationSimple)),
                            "settings": customtkinter.CTkButton(master=frame["menu"], text="Settings", command=lambda: changeMainMenuSimpleActive(windowSettingsSimple)),
                            "main" : customtkinter.CTkButton(master=frame["menu"], text="Main", command=lambda: changeMainMenuSimpleActive(windowMainSimple)),
                            "information" : customtkinter.CTkButton(master=frame["menu"],  text="Information", command=lambda: changeMainMenuSimpleActive(windowInformationSimple)),
                            "account" : customtkinter.CTkButton(master=frame["menu"],  text="Account", command= lambda: changeMainMenuSimpleActive(windowAccountSimple))}

        guiLib.configure(label["menu"], placeX= 50, placeY= 20)

        guiLib.configure(button["menu"], placeX= 110, placeY= 10, changeColorButton=False)
        guiLib.configure(button["main"], width= 130, height= 30, placeX= 10, placeY= 60)
        guiLib.configure(button["settings"], width= 130, height= 30, placeX= 10, placeY= 100)
        guiLib.configure(button["information"], width= 130, height= 30, placeX= 10, placeY= 140)
        guiLib.configure(button["account"], width= 130, height= 30, placeX= 10, placeY= 180)

        guiLib.configure(frame["menu"], 150, 220, placeY=30)
    else:
        button = { "menu" : customtkinter.CTkButton(master=app, image= guiLib.imagePull["menu"], text = "", fg_color = "transparent", hover = False, command= lambda: changeMainMenuSimpleActive(windowInformationSimple))}
        guiLib.configure(button["menu"], placeX= 0, placeY= 40, changeColorButton=False)
        guiLib.configure(frame["menu"], 0, 0)

def windowDevelopersSimple():
    guiLib.prepareNewWindow(app, 300, 300, True, windowInformationSimple)

def donateSimple():
    guiLib.prepareNewWindow(app, 300, 300)

def reportABagSimple():
    guiLib.prepareNewWindow(app, 300, 300)

def windowAccountSimple():
    guiLib.prepareNewWindow(app, 300, 300)

    label = { "profileIcon" : customtkinter.CTkLabel(app, text="", image=guiLib.imagePull["profileIcon"]),
                    "nickName" : customtkinter.CTkLabel(app, text="NickName", font = ("Poppins", 16)),
                    "UID" : customtkinter.CTkLabel(app, text="UID: 000000000001", font = ("Poppins", 14))}
    
    button = { "status" : customtkinter.CTkButton(app, text="Status: basic", corner_radius=50),
                    "information" : customtkinter.CTkButton(app, text="Change info", corner_radius=50),
                    "signOut" : customtkinter.CTkButton(app, text="Sign out", corner_radius=50, command=windowStart) }

    guiLib.configure(label["profileIcon"], placeX= 100, placeY=60)

    guiLib.configure(label["nickName"],100, 30, placeX= 100, placeY=170)
    guiLib.configure(label["UID"],100, 30, placeX= 165, placeY=270)

    guiLib.configure(button["status"],100, 30, placeX= 20, placeY=215)
    guiLib.configure(button["information"],100, 30, placeX= 160, placeY=215)
    guiLib.configure(button["signOut"], 40, 20, placeX= 200, placeY=50)

    frame = {"menu" : customtkinter.CTkFrame(app, 0, 0)}
    if menuMainSimpleActive:
        label = { "menu" : customtkinter.CTkLabel(frame["menu"],text= "Menu", font = ("Poppins", 20))}

        button = { "menu" : customtkinter.CTkButton(master=frame["menu"], image= guiLib.imagePull["menu"], text = "", fg_color = "transparent", hover = False, command=lambda: changeMainMenuSimpleActive(windowAccountSimple)),
                            "settings": customtkinter.CTkButton(master=frame["menu"], text="Settings", command=lambda: changeMainMenuSimpleActive(windowSettingsSimple)),
                            "main" : customtkinter.CTkButton(master=frame["menu"], text="Main", command=lambda: changeMainMenuSimpleActive(windowMainSimple)),
                            "information" : customtkinter.CTkButton(master=frame["menu"],  text="Information", command=lambda: changeMainMenuSimpleActive(windowInformationSimple)),
                            "account" : customtkinter.CTkButton(master=frame["menu"],  text="Account", command= lambda: changeMainMenuSimpleActive(windowAccountSimple))}

        guiLib.configure(label["menu"], placeX= 50, placeY= 20)

        guiLib.configure(button["menu"], placeX= 110, placeY= 10, changeColorButton=False)
        guiLib.configure(button["main"], width= 130, height= 30, placeX= 10, placeY= 60)
        guiLib.configure(button["settings"], width= 130, height= 30, placeX= 10, placeY= 100)
        guiLib.configure(button["information"], width= 130, height= 30, placeX= 10, placeY= 140)
        guiLib.configure(button["account"], width= 130, height= 30, placeX= 10, placeY= 180)

        guiLib.configure(frame["menu"], 150, 220, placeY=30)
    else:
        button = { "menu" : customtkinter.CTkButton(master=app, image= guiLib.imagePull["menu"], text = "", fg_color = "transparent", hover = False, command= lambda: changeMainMenuSimpleActive(windowAccountSimple))}
        guiLib.configure(button["menu"], placeX= 0, placeY= 40, changeColorButton=False)
        guiLib.configure(frame["menu"], 0, 0)

def checkTypeOfWindow(object):
    if object.get() == "Simple":
        windowSettingsSimple()
    else:
        windowSettingsExtended()

def windowSettingsSimple():
    guiLib.prepareNewWindow(app, 300, 300)

    tab = {"settings" : customtkinter.CTkTabview(app)}
    tab["settings"].add("App")
    tab["settings"].add("Assistant")
    tab["settings"].add("Plugins")

    button = {  "changeTheme" : customtkinter.CTkButton(master=tab["settings"].tab("App"), text = "Change themes", command=lambda : windowChangeTheme (windowSettingsSimple)),
                    "save" :  customtkinter.CTkButton(master=app, text = "Apply changes", command= lambda: checkTypeOfWindow(optionMenu["changeTypeWindow"])) }
    
    optionMenu = {  "changeTypeWindow" : customtkinter.CTkOptionMenu(master=tab["settings"].tab("App"), values=["Simple", "Extended"]) }

    label = {"typeWindow" : customtkinter.CTkLabel(tab["settings"].tab("App"),text= "Window type", font = ("Poppins", 16)),}

    guiLib.configure(tab["settings"], 220, 200, 40, 35)

    guiLib.configure(label["typeWindow"], 130, 30, 45, 15)

    guiLib.configure(optionMenu["changeTypeWindow"], 130, 25, 45, 45)
    optionMenu["changeTypeWindow"].set("Simple")

    guiLib.configure(button["changeTheme"], 130, 30, 45, 95)
    guiLib.configure(button["save"], 130, 25, 90, 250)

    frame = {"menu" : customtkinter.CTkFrame(app, 0, 0)}
    if menuMainSimpleActive:
        label = { "menu" : customtkinter.CTkLabel(frame["menu"],text= "Menu", font = ("Poppins", 20))}

        button = { "menu" : customtkinter.CTkButton(master=frame["menu"], image= guiLib.imagePull["menu"], text = "", fg_color = "transparent", hover = False, command=lambda: changeMainMenuSimpleActive(windowSettingsSimple)),
                            "settings": customtkinter.CTkButton(master=frame["menu"], text="Settings", command=lambda: changeMainMenuSimpleActive(windowSettingsSimple)),
                            "main" : customtkinter.CTkButton(master=frame["menu"], text="Main", command=lambda: changeMainMenuSimpleActive(windowMainSimple)),
                            "information" : customtkinter.CTkButton(master=frame["menu"],  text="Information", command=lambda: changeMainMenuSimpleActive(windowInformationSimple)),
                            "account" : customtkinter.CTkButton(master=frame["menu"],  text="Account", command= lambda: changeMainMenuSimpleActive(windowAccountSimple))}

        guiLib.configure(label["menu"], placeX= 50, placeY= 20)

        guiLib.configure(button["menu"], placeX= 110, placeY= 10, changeColorButton=False)
        guiLib.configure(button["main"], width= 130, height= 30, placeX= 10, placeY= 60)
        guiLib.configure(button["settings"], width= 130, height= 30, placeX= 10, placeY= 100)
        guiLib.configure(button["information"], width= 130, height= 30, placeX= 10, placeY= 140)
        guiLib.configure(button["account"], width= 130, height= 30, placeX= 10, placeY= 180)

        guiLib.configure(frame["menu"], 150, 220, placeY=30)
    else:
        button = { "menu" : customtkinter.CTkButton(master=app, image= guiLib.imagePull["menu"], text = "", fg_color = "transparent", hover = False, command= lambda: changeMainMenuSimpleActive(windowSettingsSimple))}
        guiLib.configure(button["menu"], placeX= 0, placeY= 40, changeColorButton=False)
        guiLib.configure(frame["menu"], 0, 0)

import threading
import time
def updateWindow(answer, otvet):
    for i in range(10):
        time.sleep(2)

        answer.delete("0.0", "end")
        otvet.delete("0.0", "end")
        
        answer.insert("0.0", f"{voice.record_result}")
        otvet.insert("0.0", f"{voice.gpt_result}")
        

def voiceRecord(answer, otvet):
    t = threading.Thread(target=voice.record)
    t.start() 
    
    f = threading.Thread(target=lambda: updateWindow(answer, otvet))
    f.start()

def windowMainExtended():
    guiLib.prepareNewWindow(app, 700, 400)

    frame = { "menu" : customtkinter.CTkFrame(master=app, corner_radius= 0)}

    label = { "name" : customtkinter.CTkLabel(frame["menu"],text= guiLib.projectName, font = ("Poppins", 20)),
              "answer": customtkinter.CTkTextbox(master=app),
              "otvet": customtkinter.CTkTextbox(master=app)
             }

    button = {"main" : customtkinter.CTkButton(master=frame["menu"], corner_radius= 20,  text="Main", command=windowMainExtended),
                    "settings" : customtkinter.CTkButton(master=frame["menu"], corner_radius= 20,  text="Settings", command=windowSettingsExtended),
                    "information" : customtkinter.CTkButton(master=frame["menu"], corner_radius= 20,  text="Information", command=windowInformationExtended),
                    "account" : customtkinter.CTkButton(master=frame["menu"], corner_radius= 20,  text="Account", command=windowAccounExtended), 
                    "speech": customtkinter.CTkButton(master=app, corner_radius=20, text="Record", command = lambda: voiceRecord(label["answer"], label["otvet"]))}

    guiLib.configure(frame["menu"], 140, 374, placeY=26)

    guiLib.configure(label["name"], placeX= 25, placeY= 10)
    
    guiLib.configure(label["answer"], placeX= 170, placeY= 90, width = 500, height = 50)
    guiLib.configure(label["otvet"], placeX= 170, placeY= 180, width = 500, height = 190)
    guiLib.configure(button["speech"], 130, 30, placeX=350, placeY=145)

    guiLib.configure(button["main"], 130, 30, placeX=5, placeY=50)
    guiLib.configure(button["settings"], 130, 30, placeX=5, placeY=95)
    guiLib.configure(button["information"], 130, 30, placeX=5, placeY=140)
    guiLib.configure(button["account"], 130, 30, placeX=5, placeY=185)

def windowSettingsExtended():
    guiLib.prepareNewWindow(app, 700, 400)

    frame = { "menu" : customtkinter.CTkFrame(master=app, corner_radius= 0)}

    optionMenu = {  "changeTypeWindow" : customtkinter.CTkOptionMenu(master=app, values=["Simple", "Extended"]) }

    label = { "name" : customtkinter.CTkLabel(frame["menu"],text= guiLib.projectName, font = ("Poppins", 20)),
                "app" : customtkinter.CTkLabel(app,text= "App", font = ("Poppins", 20)),
                "assistant" : customtkinter.CTkLabel(app,text= "Assistant", font = ("Poppins", 20)),
                "plugins" : customtkinter.CTkLabel(app,text= "Plugins", font = ("Poppins", 20)),
                "typeWindow" : customtkinter.CTkLabel(app,text= "Window type", font = ("Poppins", 16))}

    button = {"main" : customtkinter.CTkButton(master=frame["menu"], corner_radius= 20,  text="Main", command=windowMainExtended),
                    "settings" : customtkinter.CTkButton(master=frame["menu"], corner_radius= 20,  text="Settings", command=windowSettingsExtended),
                    "information" : customtkinter.CTkButton(master=frame["menu"], corner_radius= 20,  text="Information", command=windowInformationExtended),
                    "account" : customtkinter.CTkButton(master=frame["menu"], corner_radius= 20,  text="Account", command=windowAccounExtended),
                    "changeTheme" : customtkinter.CTkButton(master=app, text = "Change themes", command= lambda: windowChangeTheme(windowSettingsExtended)),
                    "save" :  customtkinter.CTkButton(master=app, text = "Apply changes", command= lambda: checkTypeOfWindow(optionMenu["changeTypeWindow"]))  }

    guiLib.configure(frame["menu"], 140, 374, placeY=26)

    guiLib.configure(label["name"], placeX= 25, placeY= 10)
    guiLib.configure(label["app"], placeX= 200, placeY= 40)
    guiLib.configure(label["assistant"], placeX= 365, placeY= 40)
    guiLib.configure(label["plugins"], placeX= 560, placeY= 40)

    guiLib.configure(button["main"], 130, 30, placeX=5, placeY=50)
    guiLib.configure(button["settings"], 130, 30, placeX=5, placeY=95)
    guiLib.configure(button["information"], 130, 30, placeX=5, placeY=140)
    guiLib.configure(button["account"], 130, 30, placeX=5, placeY=185)

    guiLib.configure(button["save"], 130, 30, placeX=155, placeY=300)

    guiLib.configure(label["typeWindow"], 130, 30, 155, 70)

    guiLib.configure(optionMenu["changeTypeWindow"], 130, 25, 155, 110)
    optionMenu["changeTypeWindow"].set("Extended")

    guiLib.configure(button["changeTheme"], 130, 30, 155, 150)

def windowInformationExtended():
    guiLib.prepareNewWindow(app, 700, 400)

    frame = { "menu" : customtkinter.CTkFrame(master=app, corner_radius= 0)}
    
    label = { "name" : customtkinter.CTkLabel(frame["menu"],text= guiLib.projectName, font = ("Poppins", 20))}

    button = {"main" : customtkinter.CTkButton(master=frame["menu"], corner_radius= 20,  text="Main", command=windowMainExtended),
                    "settings" : customtkinter.CTkButton(master=frame["menu"], corner_radius= 20,  text="Settings", command=windowSettingsExtended),
                    "information" : customtkinter.CTkButton(master=frame["menu"], corner_radius= 20,  text="Information", command=windowInformationExtended),
                    "account" : customtkinter.CTkButton(master=frame["menu"], corner_radius= 20,  text="Account", command=windowAccounExtended) }
    
    guiLib.configure(frame["menu"], 140, 374, placeY=26)
    
    guiLib.configure(label["name"], placeX= 25, placeY= 10)
    guiLib.configure(button["main"], 130, 30, placeX=5, placeY=50)
    guiLib.configure(button["settings"], 130, 30, placeX=5, placeY=95)
    guiLib.configure(button["information"], 130, 30, placeX=5, placeY=140)
    guiLib.configure(button["account"], 130, 30, placeX=5, placeY=185)

def windowAccounExtended():
    guiLib.prepareNewWindow(app, 700, 400)

    frame = { "menu" : customtkinter.CTkFrame(master=app, corner_radius= 0),
                    "right" :  customtkinter.CTkFrame(master=app, corner_radius= 20)}
    
    label = { "projectName" : customtkinter.CTkLabel(frame["menu"],text= guiLib.projectName, font = ("Poppins", 20)),
                    "profileIcon" : customtkinter.CTkLabel(app, text="", image=guiLib.imagePull["profileIcon"]),
                    "nickName" : customtkinter.CTkLabel(app, text="NickName", font = ("Poppins", 16)),
                    "UID" : customtkinter.CTkLabel(app, text="UID: 000000000001", font = ("Poppins", 18)),
                    "bmail" : customtkinter.CTkButton(master=frame["right"], corner_radius= 20,  text="test@mail.ru"),
                    "bname" : customtkinter.CTkButton(master=frame["right"], corner_radius= 20,  text="Name"),
                    "bsecondName" : customtkinter.CTkButton(master=frame["right"], corner_radius= 20,  text="SecondName"),
                    "mail" : customtkinter.CTkLabel(master=frame["right"], text="Mail", font = ("Poppins", 18)),
                    "name" : customtkinter.CTkLabel(master=frame["right"], text="Name", font = ("Poppins", 18)),
                    "secondName" : customtkinter.CTkLabel(master=frame["right"],text="Second Name", font = ("Poppins", 18))}

    button = {"main" : customtkinter.CTkButton(master=frame["menu"], corner_radius= 20,  text="Main", command=windowMainExtended),
                    "settings" : customtkinter.CTkButton(master=frame["menu"], corner_radius= 20,  text="Settings", command=windowSettingsExtended),
                    "information" : customtkinter.CTkButton(master=frame["menu"], corner_radius= 20,  text="Information", command=windowInformationExtended),
                    "account" : customtkinter.CTkButton(master=frame["menu"], corner_radius= 20,  text="Account", command=windowAccounExtended),
                    "status" : customtkinter.CTkButton(master=app, corner_radius= 20,  text="Status: Basic"),
                    "signOut" : customtkinter.CTkButton(app, text="Sign out", corner_radius=50, command=windowStart),
                    "changeInfo" : customtkinter.CTkButton(master=frame["right"], corner_radius= 20,  text="Change info")}
    
    guiLib.configure(frame["menu"], 140, 374, placeY=26)

    guiLib.configure(label["projectName"], placeX= 25, placeY= 10)
    guiLib.configure(button["main"], 130, 30, placeX=5, placeY=50)
    guiLib.configure(button["settings"], 130, 30, placeX=5, placeY=95)
    guiLib.configure(button["information"], 130, 30, placeX=5, placeY=140)
    guiLib.configure(button["account"], 130, 30, placeX=5, placeY=185)

    guiLib.configure(label["profileIcon"], placeX= 275, placeY=90)

    guiLib.configure(label["nickName"],100, 30, placeX= 275, placeY=200)
    guiLib.configure(button["signOut"], 40, 20, placeX= 280, placeY=240)

    guiLib.configure(button["status"], 130, 30, placeX=150, placeY=360)
    guiLib.configure(label["UID"],100, 30, placeX= 515, placeY=360)

    guiLib.configure(frame["right"], 190, 300, placeX= 500, placeY=40)
    guiLib.configure(button["changeInfo"], 130, 30, placeX=30, placeY=10)

    guiLib.configure(label["mail"], placeX= 10, placeY=55)
    guiLib.configure(label["name"],placeX= 10, placeY=135)
    guiLib.configure(label["secondName"],placeX= 10, placeY=215)

    guiLib.configure(label["bmail"],160, 30, placeX= 15, placeY=90)
    guiLib.configure(label["bname"],160, 30, placeX= 15, placeY=170)
    guiLib.configure(label["bsecondName"],160, 30, placeX= 15, placeY=250)

def windowChangeTheme(window):
    guiLib.prepareNewWindow(app, 700, 400)

    guiLib.prepareNewWindow(app, 700, 400)

    frame = { "menu" : customtkinter.CTkFrame(master=app, corner_radius= 0)}
    
    label = { "name" : customtkinter.CTkLabel(frame["menu"],text= "Select theme", font = ("Poppins", 20))}

    button = {"Default" : customtkinter.CTkButton(master=frame["menu"], corner_radius= 20,  text="Default", command= lambda:switchTheme(guiLib.defaultTheme, window)),
                    "Blue" : customtkinter.CTkButton(master=frame["menu"], corner_radius= 20,  text="Blue", command=lambda:switchTheme(guiLib.blueTheme, window)),
                    "Yellow" : customtkinter.CTkButton(master=frame["menu"], corner_radius= 20,  text="Yellow", command=lambda:switchTheme(guiLib.yellowTheme, window)),
                    "Sage" : customtkinter.CTkButton(master=frame["menu"], corner_radius= 20,  text="Sage", command=lambda: switchTheme(guiLib.sageTheme, window)),
                    "custom" : customtkinter.CTkButton(master=frame["menu"], corner_radius= 20,  text="Custom"),
                    "apply" : customtkinter.CTkButton(master=frame["menu"], corner_radius= 20,  text="Apply", command= lambda: window()) }
    
    guiLib.configure(frame["menu"], 140, 374, placeY=26)
    
    guiLib.configure(label["name"], placeX= 10, placeY= 10)
    guiLib.configure(button["Default"], 130, 30, placeX=5, placeY=50)
    guiLib.configure(button["Blue"], 130, 30, placeX=5, placeY=95)
    guiLib.configure(button["Yellow"], 130, 30, placeX=5, placeY=140)
    guiLib.configure(button["Sage"], 130, 30, placeX=5, placeY=185)
    guiLib.configure(button["custom"], 130, 30, placeX=5, placeY=230)
    guiLib.configure(button["apply"], 130, 30, placeX=5, placeY=320)

def switchTheme(theme, window):
    # widgets =  app.winfo_children()
    # for i in range(3, len(widgets)):
    #     widgets[i].configure(fg_color=theme ["frameColor"])
    #     for widgetsFrame in widgets[i].winfo_children():
    #         if i == 6:  widgetsFrame.configure(fg_color =theme["buttonFgColor"], text_color=theme["textColor"], hover_color=theme["buttonHoverColor"])
    #         elif isinstance(widgetsFrame, customtkinter.CTkLabel): widgetsFrame.configure(text_color=theme["textColor"])

    guiLib.currentTheme = theme
    windowChangeTheme(window)

def start():
    app.after(10, lambda: guiLib.windowSetup(app))
    windowStart()
    app.geometry(f"+{(app.winfo_screenwidth() - 400) // 2}+{(app.winfo_screenheight() - 400) // 2}")
    app.mainloop()

start()