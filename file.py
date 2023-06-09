import tkinter
import customtkinter
import webbrowser
from PIL import Image


customtkinter.set_appearance_mode("system")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

file1=open("conf.txt","r")
conf=file1.read()
file1.close
loginget=open("log.txt","r")
logg=loginget.read()

loginget.close
"Получаение логина"
passget=open("log.txt","r")
pas=passget.read()
passget.close
"Получение пароля"
mail="test@mail.ru"
name="Name"
status="Status:"
stat="Basic"
status=status+" "+stat
Secname="Second name"
borderc="#1B1B1B"
textc="#2F2F2F"
Menuca=open("Menuc.txt","r")
Menuc=Menuca.read()
Menuca.close
"Получение цвета меню"
butts=open("butt.txt","r")
butt=butts.read()
butts.close()
"Получение цвета кнопок"
fons=open("fon.txt","r")
fon=fons.read()
fons.close()
"Получение цвета фона"
texts=open("text.txt","r")
text=texts.read()
texts.close()
"Получение цвета текста"
Labels=open("labla.txt","r")
Labla=Labels.read()
Labels.close()
"Получение получения цвета лейлба"
def app():
    'создание окна входа'

   
    app = customtkinter.CTk(fg_color="#2F2F2F")  # create CTk window like you do with the Tk window
    app.geometry("414x409")
    def google():
       webbrowser.open("https://www.google.com/?hl=%27")
    def button_function1():
        "Проверка на правильность пароля и логина"
        log=Login.get()
        pasw=Parol.get()
        if log==logg and pasw==pas:
            app.destroy()
            two()
        pr=open("conf.txt",'w+')
        pr.write("1")
        pr.close()
        "сохранения входа и переход на главную форму"
        if log!=logg or pasw!=pas:
            Login.delete(0,100)
            Parol.delete(0,100)
            pr1=open("conf.txt",'w+')
            pr1.write("0")
            pr1.close()
            borderc="#680101"
            Login.configure(border_color=borderc)
            Parol.configure(border_color=borderc)
            Oshibka.configure(text_color=borderc)
            Zabil.configure(text_color="#6D6D6D")
        "Сохранение неправельности входа, появление кнопки забыл пароль"
    def vv():
            app.destroy()
            vost()
    logo = customtkinter.CTkLabel(app, text="Wise Gate",fg_color="transparent",font=("Edu NSW ACT Foundation",24))
    logo.place(relx=0.5, rely=0.075, anchor=tkinter.CENTER)
    Login = customtkinter.CTkEntry(app, placeholder_text="Логин",text_color="#6D6D6D",fg_color=borderc,border_width=2,border_color=borderc,width=221,height=50,corner_radius=30)
    Login.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)
    Vxod = customtkinter.CTkButton(master=app, text="Sing in",text_color="#6D6D6D", command=button_function1,fg_color="#1C1B1B",width=141,height=33,corner_radius=30)
    Vxod.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)
    Reg= customtkinter.CTkButton(master=app, text="Sing up", text_color="#6D6D6D",command=google,fg_color="#1C1B1B",width=94.5,height=22.5,corner_radius=30)
    Reg.place(relx=0.5, rely=0.65, anchor=tkinter.CENTER)     
    Parol = customtkinter.CTkEntry(app, placeholder_text="Пароль",text_color="#6D6D6D",fg_color="#1B1B1B",border_color="#1B1B1B",width=221,height=50,corner_radius=30)
    Parol.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
    Oshibka = customtkinter.CTkLabel(app, text="Неверный Логин или пароль повторите ввод",height=6,text_color=textc,font=("Edu NSW ACT Foundation",12))
    Oshibka.place(relx=0.5, rely=0.48, anchor=tkinter.CENTER)
    Zabil = customtkinter.CTkButton(master=app, text="forgot password",text_color=textc, command=vv,fg_color="#2F2F2F",font=("Edu NSW ACT Foundation",12,"underline"),
    hover_color='#2F2F2F',width=141,height=33,corner_radius=30)
    Zabil.place(relx=0.5, rely=0.73, anchor=tkinter.CENTER)
    
    app.resizable(0, 0)
    app.mainloop()
def button_function():
    print("button pressed")
def vost():
      "восстановление пароля"
      vosta = customtkinter.CTk(fg_color=fon)  
      vosta.geometry("731x414")

      logo = customtkinter.CTkLabel(vosta, text="Wise Gate",fg_color="transparent",font=("Edu NSW ACT Foundation",24))
      logo.place(relx=0.5, rely=0.075, anchor=tkinter.CENTER)
      vosta.mainloop()
def three():
     
      three = customtkinter.CTk(fg_color=fon)  
      three.geometry("731x414")
      my_image = customtkinter.CTkImage(light_image=Image.open("horse.jpg"),
                                  dark_image=Image.open("horse.jpg"),
                                  size=(130, 120))
      "Переход на другие формы"
      def infm():
        three.destroy()
        inf()
      def Main():
          three.destroy()
          two()
      def set():
          three.destroy()
          four()
      labelim = customtkinter.CTkLabel(three, image=my_image, text="")
      labelim.place(relx=0.47, rely=0.4, anchor=tkinter.CENTER)
      Danii=customtkinter.CTkFrame(three,width=173,height=251,fg_color=Menuc,corner_radius=20)
      Danii.place(relx=0.87, rely=0.36, anchor=tkinter.CENTER)
      Mail=customtkinter.CTkLabel(Danii,text="Mail:",font=("Edu NSW ACT Foundation",14),width=100,height=10,text_color=text,fg_color=Menuc,anchor="nw")
      Mail.place(relx=0.13,rely=0.07)
      Mailviv=customtkinter.CTkLabel(Danii,text=mail,font=("Edu NSW ACT Foundation",14),width=153,height=27,text_color=text,fg_color=butt,corner_radius=25)
      Mailviv.place(relx=0.07,rely=0.16)
      Name=customtkinter.CTkLabel(Danii,text="Name:",font=("Edu NSW ACT Foundation",14),width=100,height=10,text_color=text,fg_color=Menuc,anchor="nw")
      Name.place(relx=0.13,rely=0.3)
      Nameviv=customtkinter.CTkLabel(Danii,text=name,font=("Edu NSW ACT Foundation",14),width=153,height=27,text_color=text,fg_color=butt,corner_radius=25)
      Nameviv.place(relx=0.07,rely=0.39)
      SecondName=customtkinter.CTkLabel(Danii,text="Secoond Name:",font=("Edu NSW ACT Foundation",14),width=100,height=10,text_color=text,fg_color=Menuc,anchor="nw")
      SecondName.place(relx=0.13,rely=0.53)
      SecondNameviv=customtkinter.CTkLabel(Danii,text=Secname,font=("Edu NSW ACT Foundation",14),width=153,height=27,text_color=text,fg_color=butt,corner_radius=25)
      SecondNameviv.place(relx=0.07,rely=0.63)
      Status=customtkinter.CTkLabel(Danii,text=status,font=("Edu NSW ACT Foundation",14),width=120,height=27,text_color=text,fg_color=butt,corner_radius=25)
      Status.place(relx=0.15,rely=0.8)
      Menu = customtkinter.CTkFrame(three, width=150, height=414,fg_color=Menuc)
      Menu.place(relx=0.09, rely=0.5, anchor=tkinter.CENTER)
      Logomenu = customtkinter.CTkLabel(Menu, text="Wise Gate",fg_color="transparent",font=("Edu NSW ACT Foundation",20))
      Logomenu.place(relx=0.5, rely=0.075, anchor=tkinter.CENTER)
      Setting =customtkinter.CTkButton(master=Menu, text="Setting",text_color=text, command=set,fg_color=butt,width=120,height=33,corner_radius=30)
      Setting.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
      Inform =customtkinter.CTkButton(master=Menu, text="Information",text_color=text, command=infm,fg_color=butt,width=120,height=33,corner_radius=30)
      Inform.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
      Acc =customtkinter.CTkButton(master=Menu, text="Account",text_color=text, command=button_function,fg_color=butt,width=120,height=33,corner_radius=30)
      Acc.place(relx=0.5 , rely=0.8, anchor=tkinter.CENTER)
      Mains =customtkinter.CTkButton(master=Menu, text="Main",text_color=text, command=Main,fg_color=butt,width=120,height=33,corner_radius=30)
      Mains.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
      ChangeInfo=customtkinter.CTkButton(master=three, text="Change info",text_color=text, command=button_function,fg_color=butt,width=120,height=33,corner_radius=30)
      ChangeInfo.place(relx=0.47, rely=0.6, anchor=tkinter.CENTER)
      "Логаут"
      def logut():
        conf=open("conf.txt",'w+')
        conf.write("0")
        conf.close()
        three.destroy()
        app()
      Logout=customtkinter.CTkButton(master=three, text="Log out",text_color=text, command=logut,fg_color=butt,width=80,height=33,corner_radius=30)
      Logout.place(relx=0.47, rely=0.7, anchor=tkinter.CENTER)
       
      three.resizable(0, 0)
      three.mainloop()
     
def two():
       "Главная форма"
       two = customtkinter.CTk(fg_color=fon)  
       two.geometry("731x414")
       "Переход на другие формы"
       def button_function3():
        two.destroy()
        three()
       def infm():
           two.destroy()
           inf()
       def set():
           two.destroy()
           four()
       Yourpc = customtkinter.CTkFrame(two, width=127, height=100,corner_radius=25,fg_color=Menuc)
       Yourpc.place(relx=0.9, rely=0.15, anchor=tkinter.CENTER)
       Plagun = customtkinter.CTkFrame(two, width=127, height=100,corner_radius=25,fg_color=Menuc)
       Plagun.place(relx=0.9, rely=0.45, anchor=tkinter.CENTER)
       Time = customtkinter.CTkFrame(two, width=127, height=23.5,corner_radius=25,fg_color=Menuc)
       Time.place(relx=0.9, rely=0.65, anchor=tkinter.CENTER)
       Date = customtkinter.CTkFrame(two, width=127, height=42.5,corner_radius=15,fg_color=Menuc)
       Date.place(relx=0.9, rely=0.8, anchor=tkinter.CENTER)
       Menus = customtkinter.CTkFrame(two, width=150, height=414,fg_color=Menuc)
       Menus.place(relx=0.09, rely=0.5, anchor=tkinter.CENTER)
       Logo = customtkinter.CTkLabel(Menus, text="Wise Gate",fg_color="transparent",font=("Edu NSW ACT Foundation",20))
       Logo.place(relx=0.5, rely=0.075, anchor=tkinter.CENTER)
       setting =customtkinter.CTkButton(master=Menus, text="Setting",text_color=text, command=set,fg_color=butt,width=120,height=33,corner_radius=30)
       setting.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
       Inform =customtkinter.CTkButton(master=Menus, text="Information",text_color=text, command=infm,fg_color=butt,width=120,height=33,corner_radius=30)
       Inform.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
       Acc =customtkinter.CTkButton(master=Menus, text="Account",text_color=text, command=button_function3,fg_color=butt,width=120,height=33,corner_radius=30)
       Acc.place(relx=0.5 , rely=0.8, anchor=tkinter.CENTER)
       Main =customtkinter.CTkButton(master=Menus, text="Main",text_color=text, command=button_function,fg_color=butt,width=120,height=33,corner_radius=30)
       Main.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
       Nizn=customtkinter.CTkLabel(two,width=362,text="",height=144.5,fg_color=Labla,corner_radius=25,anchor="nw")
       Nizn.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
       Verh=customtkinter.CTkLabel(two,width=362,text="",height=36,fg_color=Labla,corner_radius=25,anchor="nw")
       Verh.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
       Record = customtkinter.CTkButton(master=two, text="Record",text_color=text, command=button_function,fg_color=butt,width=141,height=33,corner_radius=30)
       Record.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
       

     
       two.resizable(0, 0)
       two.mainloop()
        
def four():
    
    four = customtkinter.CTk(fg_color=fon)  
    "Переход на другие формы"
    def infm():
        four.destroy()
        inf()
    four.geometry("731x414") 
    def acc():
        four.destroy()
        three()
    def theme():
        four.destroy()
        five()
    def main():
        four.destroy()
        two()
    "Создание бокового меню"
    Menus = customtkinter.CTkFrame(four, width=150, height=414,fg_color=Menuc)
    Menus.place(relx=0.09, rely=0.5, anchor=tkinter.CENTER)
    Logo = customtkinter.CTkLabel(Menus, text="Wise Gate",fg_color="transparent",font=("Edu NSW ACT Foundation",20))
    Logo.place(relx=0.5, rely=0.075, anchor=tkinter.CENTER)
    setting =customtkinter.CTkButton(master=Menus, text="Setting",text_color=text, command=button_function,fg_color=butt,width=120,height=33,corner_radius=30)
    setting.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
    Inform =customtkinter.CTkButton(master=Menus, text="Information",text_color=text, command=infm,fg_color=butt,width=120,height=33,corner_radius=30)
    Inform.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
    Acc =customtkinter.CTkButton(master=Menus, text="Account",text_color=text, command=acc,fg_color=butt,width=120,height=33,corner_radius=30)
    Acc.place(relx=0.5 , rely=0.8, anchor=tkinter.CENTER)
    Main =customtkinter.CTkButton(master=Menus, text="Main",text_color=text, command=main,fg_color=butt    ,width=120,height=33,corner_radius=30)
    Main.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
    label=customtkinter.CTkLabel(four,text="Сменить тему",fg_color="transparent",text_color=text,font=("Edu NSW ACT Foundation",20))
    label.place(relx=0.22,rely=0.1)
    Theme = customtkinter.CTkButton(master=four, text="Сменить тему",text_color=text, command=theme,fg_color=butt,width=141,height=33,corner_radius=30)
    Theme.place(relx=0.3, rely=0.3, anchor=tkinter.CENTER)    
    four.resizable(0, 0)
    four.mainloop()
# Use CTkButton instead of tkinter Button
def inf():
    "Переход на другие формы"
    def acc():
        six.destroy()
        three()
    def set():
        six.destroy()
        five()
    def main():
        six.destroy()
        two()
    six = customtkinter.CTk(fg_color=fon)  
    six.geometry("731x414")
    "Создание ссылок на вк"
    def link2():
        webbrowser.open_new("https://vk.com/dimasharov2015")
    def link1():
        webbrowser.open_new("https://vk.com/hirikayato")
    def link():
      webbrowser.open_new("https://vk.com/go_away_from_my_swam") 
    Menus = customtkinter.CTkFrame(six, width=150, height=414,fg_color=Menuc)
    Menus.place(relx=0.09, rely=0.5, anchor=tkinter.CENTER)
    Logo = customtkinter.CTkLabel(Menus, text="Wise Gate",fg_color="transparent",font=("Edu NSW ACT Foundation",20))
    Logo.place(relx=0.5, rely=0.075, anchor=tkinter.CENTER)
    setting =customtkinter.CTkButton(master=Menus, text="Setting",text_color=text, command=set,fg_color=butt,width=120,height=33,corner_radius=30)
    setting.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
    Inform =customtkinter.CTkButton(master=Menus, text="Information",text_color=text, command=button_function,fg_color=butt,width=120,height=33,corner_radius=30)
    Inform.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
    Acc =customtkinter.CTkButton(master=Menus, text="Account",text_color=text, command=acc,fg_color=butt,width=120,height=33,corner_radius=30)
    Acc.place(relx=0.5 , rely=0.8, anchor=tkinter.CENTER)
    Main =customtkinter.CTkButton(master=Menus, text="Main",text_color=text, command=main,fg_color=butt    ,width=120,height=33,corner_radius=30)
    Main.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)   
    Logo1 = customtkinter.CTkLabel(six, text="Wise Gate",fg_color="transparent",font=("Edu NSW ACT Foundation",20))
    Logo1.place(relx=0.57, rely=0.075, anchor=tkinter.CENTER)
    label=customtkinter.CTkLabel(six,text="Создатели приложения",fg_color="transparent",font=("Edu NSW ACT Foundation",20) )
    label.place(relx=0.43,rely=0.15)
    Ilia=customtkinter.CTkButton(six,text="Илья Шишин",command=link,text_color=text,fg_color=butt,corner_radius=25)
    Ilia.place(relx=0.47,rely=0.3) 
    Andrey=customtkinter.CTkButton(six,text="Андрей Архипов",command=link1,text_color=text,fg_color=butt,corner_radius=25)
    Andrey.place(relx=0.47,rely=0.5) 
    Dima=customtkinter.CTkButton(six,text="Дмитрий Шаров",command=link2,text_color=text,fg_color=butt,corner_radius=25)
    Dima.place(relx=0.47,rely=0.7) 
     
    six.resizable(0, 0)
    six.mainloop()

def five():
    five = customtkinter.CTk(fg_color=fon)  
    five.geometry("731x414")  
    "функция для кнопки назад"  
    def naz():
        five.destroy()
        four()
    "Изменение окна с выбором темы"
    def cof():
         defaul.configure(fg_color=butt,text_color=text)
         Menus.configure(fg_color=Menuc)
         darcblue.configure(fg_color=butt,text_color=text)
         nazq.configure(fg_color=butt,text_color=text)
         blues.configure(fg_color=butt,text_color=text)
         darkgr.configure(fg_color=butt,text_color=text)
         five.configure(fg_color=fon)
         Nizn.configure(fg_color=Labla)
         Primer.configure(text_color=text)
         Primerbut.configure(text_color=text,fg_color=butt)
    "запись данных темы в файлы"
    def men(mens,fons,buts,texts,label):
         ff=open("fon.txt",'w+')
         ff.write(fons)
         ff.close()
         mm=open("Menuc.txt",'w+')
         mm.write(mens)
         mm.close()
         bb=open("butt.txt",'w+')
         bb.write(buts)
         bb.close()
         tt=open("text.txt","w+")
         tt.write(texts)
         tt.close()
         ll=open("labla.txt","w+")
         ll.write(label)
         ll.close()
    "Выбор темы и запись"
    def blue():
         global Menuc
    
         Menuc="#091589"
         global butt
         butt="#040937"
         global fon
         fon="#060A7B"
         global text
         text="#4C48FF"
         global Labla
         Labla="#000347"
         men(Menuc,fon,butt,text,Labla)
         cof()
    def vib():
         global Menuc
        
         Menuc="#030621"
         global butt
       
         butt="#040937"
         global fon
         
         fon="#000227"
         global text
         text="#030084"
         global Labla
         Labla="#000347"
         men(Menuc,fon,butt,text,Labla)
         cof()
   
    def defu():
        global Menuc
        Menuc="#242424"
        global butt
        butt="#1C1B1B"
        global fon
        fon="#2F2F2F"

        global text
        text="#857F7F"
        global Labla
        Labla="#676767"
        men(Menuc,fon,butt,text,Labla)
        cof()
    def dGreen():

        global Menuc
        Menuc="#001C03"
        global butt
        butt="#05331A"
        global fon
        fon="#061600"

        global text
        text="#038400"
        global Labla
        Labla="#073000"
        men(Menuc,fon,butt,text,Labla)
        cof()
    def buton():
        print("butt pressed")
    Menus = customtkinter.CTkFrame(five, width=150, height=414,fg_color=Menuc)
    Menus.place(relx=0.09, rely=0.5, anchor=tkinter.CENTER)
    Logo = customtkinter.CTkLabel(Menus, text="Wise Gate",fg_color="transparent",font=("Edu NSW ACT Foundation",20))
    Logo.place(relx=0.5, rely=0.075, anchor=tkinter.CENTER)
    defaul=customtkinter.CTkButton(master=Menus, text="Default",text_color=text, command=defu,fg_color=butt,width=120,height=33,corner_radius=30)
    defaul.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
    blues=customtkinter.CTkButton(master=Menus, text="Blue",text_color=text, command=blue,fg_color=butt,width=120,height=33,corner_radius=30)
    blues.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)
    darcblue=customtkinter.CTkButton(master=Menus, text="Darc Blue",text_color=text, command=vib,fg_color=butt,width=120,height=33,corner_radius=30)
    darcblue.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    darkgr=customtkinter.CTkButton(master=Menus, text="Dark green",text_color=text, command=dGreen,fg_color=butt,width=120,height=33,corner_radius=30)
    darkgr.place(relx=0.5, rely=0.65, anchor=tkinter.CENTER)
    Nizn=customtkinter.CTkLabel(five,width=362,text="",height=144.5,fg_color=Labla,corner_radius=25,anchor="nw")
    Nizn.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
    Primer=customtkinter.CTkLabel(five,text='Пример текста',text_color=text,fg_color="transparent",font=("Edu NSW ACT Foundation",16))
    Primer.place(relx=0.3,rely=0.2)
    Primerbut=customtkinter.CTkButton(five, text="Пример кнопки",text_color=text, command=buton,fg_color=butt,width=120,height=33,corner_radius=30)
    Primerbut.place(relx=0.37, rely=0.36, anchor=tkinter.CENTER)
    nazq =customtkinter.CTkButton(master=Menus, text="back",text_color=text, command=naz,fg_color=butt,width=120,height=33,corner_radius=30)
    nazq.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)
    five.resizable(0, 0)
    five.mainloop()

'Проверка на то зашел ли пользователь до этого'
if conf=="1":
      two()
elif conf=="0":
    app()