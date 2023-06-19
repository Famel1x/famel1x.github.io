import customtkinter
from PIL import Image
from ctypes import windll

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

defaultTheme = {"buttonFgColor": "#2F4F4F", "buttonHoverColor": "#155263", "textColor":"#FFFFFF" ,"frameColor": "#2A2A2A"} 

blueTheme={"buttonFgColor": "#0081C9", "buttonHoverColor": "#2A709D", "textColor":"#000000" ,"frameColor": "#93C6E7"}

yellowTheme={"buttonFgColor": "#FFD495", "buttonHoverColor": "#FFB26B", "textColor":"#070707" ,"frameColor": "#FFEBB7"}

sageTheme={"buttonFgColor": "#A3BB98", "buttonHoverColor": "#939B62", "textColor":"#000000" ,"frameColor": "#E1EEDD"}

currentTheme = defaultTheme

imagePull = {
    "exit": customtkinter.CTkImage(Image.open ("Data\\Image\\exit.png"), size = (18,18)),
    "back": customtkinter.CTkImage(Image.open ("Data\\Image\\back.png"), size = (18,18)),
    "hide": customtkinter.CTkImage(Image.open ("Data\\Image\\hide.png"), size = (18,18)),
    "menu": customtkinter.CTkImage(Image.open ("Data\\Image\\iconMenu.png"), size = (24,24)),
    "QR_Ichise": customtkinter.CTkImage(Image.open ("Data\\Image\\QR_ichise.png"), size = (120,120)),
    "QR_HirikaYato": customtkinter.CTkImage(Image.open ("Data\\Image\\QR_hirikayato.png"), size = (120,120)),
    "profileIcon" : customtkinter.CTkImage(Image.open ("Data\\Image\\profileIcon.png"), size= (100, 100))
}

projectName = "Wise Gate"
projectVersion = "Version: 0.0000001"

def prepareNewWindow(root = customtkinter.CTk, windowWidth = int, windowHeight = int, buttonBack = False, buttonBackFunction = "if buttonBack == True"):
    root.iconbitmap(r'Data\\Image\\logo.ico')
    root.geometry(str(windowWidth) + "x" + str(windowHeight))
    destroyAllWidgets(root)

    frame = customtkinter.CTkFrame(master=root, width= windowWidth, height= 27, corner_radius= 0)
    frame.pack(anchor="n")
    frame.bind('<ButtonPress-1>', clickwin)
    frame.bind('<B1-Motion>', lambda x: dragwin(root))

    buttonExit = customtkinter.CTkButton(master=frame, image= imagePull["exit"], text = "", fg_color = "transparent", hover = False, hover_color= ['#979DA2', '#565B5E'], width=18, height=18, command=lambda: root.quit())
    buttonExit.place(x = windowWidth - 35)

    buttonHide = customtkinter.CTkButton(master=frame, image= imagePull["hide"], text = "", fg_color = "transparent", hover = False, hover_color= ['#979DA2', '#565B5E'], width=18, height=18, command=lambda: minimizeGUI(root))
    buttonHide.place(x = windowWidth - 70)

    if buttonBack:
        buttonBack = customtkinter.CTkButton(master=frame, image= imagePull["back"], text = "", fg_color = "transparent", hover = False, hover_color= ['#979DA2', '#565B5E'], width=18, height=18, command=buttonBackFunction)
        buttonBack.place(x = 0)

def destroyAllWidgets(root):
    for widget in root.winfo_children():
        widget.destroy()

def windowSetup(root):
    style = windll.user32.GetWindowLongW(windll.user32.GetParent(root.winfo_id()), -20)
    style = style & ~0x00400080
    style = style | 0x00040000
    res = windll.user32.SetWindowLongW(windll.user32.GetParent(root.winfo_id()), -20, style)
    root.wm_withdraw()
    root.after(10, lambda: root.wm_deiconify())
    root.overrideredirect(True)
    root.bind("<Map>", lambda x: frameMapped(root))
    root.title("Wisegate")

minGui = 1

def minimizeGUI(root):
    global minGui
    minGui = 1
    root.state('withdrawn')
    root.overrideredirect(False)
    root.state('iconic')

def frameMapped(root  = "master", event=None):
    global minGui
    root.overrideredirect(True)
    if minGui == 1:
        windowSetup(root)
        minGui = 0

def clickwin(event):
    global lastClickX
    global lastClickY
    lastClickX = event.x
    lastClickY = event.y

def dragwin(root  = "master", event = None):
    x = root.winfo_pointerx() - lastClickX
    y = root.winfo_pointery() - lastClickY
    root.geometry('+{x}+{y}'.format(x=x,y=y))

def configure(object, width = 0, height = 0, placeX = 0, placeY = 0, changeColorButton = True):
    object.configure(width = width, height = height)
    object.place(x = placeX, y = placeY)

    if changeColorButton:
        if isinstance(object, customtkinter.CTkButton):
            object.configure(hover_color = currentTheme["buttonHoverColor"], fg_color = currentTheme["buttonFgColor"], text_color = currentTheme["textColor"],font = ("Poppins", 16))
    if isinstance(object, customtkinter.CTkTabview):
        object.configure(segmented_button_fg_color = currentTheme["buttonFgColor"], 
                         segmented_button_selected_color= currentTheme["buttonHoverColor"],
                         segmented_button_selected_hover_color = currentTheme["buttonHoverColor"],
                         segmented_button_unselected_color = currentTheme["buttonFgColor"],
                         segmented_button_unselected_hover_color = currentTheme["buttonHoverColor"])
    if isinstance(object, customtkinter.CTkOptionMenu):
        object.configure(fg_color = currentTheme["buttonFgColor"], button_color =  currentTheme["buttonHoverColor"],text_color = currentTheme["textColor"])

def checkSignUp(root, entryList, checkbox):
    sucsess = {"login": False, "password": False, "mail": False, "confirmPassword": False, "name": False, "lastName": False, "license": False}
    
    labelFaildedSignUp = customtkinter.CTkLabel(root,text="check the entered information", font = ("Poppins", 16))
    labelFaildedSignUp.configure(corner_radius = 20, fg_color = "#A52A2A")
    labelFaildedSignUp.place(x=135, y=35)

def licenseAgreement(checkbox):
    licenseAgreement = customtkinter.CTkToplevel()
    licenseAgreement.geometry("500x320")
    licenseAgreement.title("license Agreement")

    textbox = customtkinter.CTkTextbox(licenseAgreement)
    textbox.insert("0.0", "new text to insert")
    textbox.configure(state="disabled", width = 400, height = 500)
    textbox.grid(row=0, column=0)
    license_button = customtkinter.CTkButton(licenseAgreement, text = "I accept")
    license_button.configure()
    license_button.place(relx = 0, rely = 0.5)
    license_button.bind('<ButtonPress-1>', command = lambda x: checkbox.configure(state = "normal"))