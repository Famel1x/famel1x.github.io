"""Main activity and maybe sidbar"""


#import modelues
from typing import Any, List, Optional, Union
import flet
from flet import * 
from functools import partial
import time
import threading



class NavBar(UserControl):
    def __init__(self, func):
        self.func = func
        super().__init__()

    def HightLight(self, e):
        if e.data == 'true':
            e.control.bgcolor = 'white10'
            e.control.update()

            e.control.content.controls[0].icon_color = 'white'
            e.control.content.controls[1].color = 'white'
            e.control.content.update()
        else:
            e.control.bgcolor = None
            e.control.update()

            e.control.content.controls[0].icon_color = 'white54'
            e.control.content.controls[1].color = 'white54'
            e.control.content.update()

        

    def UserData(self, initials:str, name:str, description:str):
        #Строка 

        return Container(
            content=Row(
                controls=[
                    Container(
                        width=42,
                        height=42,
                        bgcolor="bluegrey900",
                        alignment=alignment.center,
                        border_radius = 42,
                        content=Text(
                            value=initials,
                            size=20,
                            weight="bold", 
                            # передай аргументы ниже
                        )
                    ),
                    Column(
                        spacing=1,
                        alignment="center",
                        controls=[
                            Text(
                                value=name,
                                size=11, 
                                weight="bold",

                                # здесь нам нужно включить некоторые детали 
                                # для анимации   
                                opacity=1, # От 0 - 1
                                animate_opacity=200, #Скорость анимаии
                            ),
                            Text(
                                value=description,
                                size=9,
                                weight="w400",
                                color= "white54",

                                # здесь нам нужно включить некоторые детали 
                                # для анимации   
                                opacity=1, # От 0 - 1
                                animate_opacity=200, #Скорость анимаии
                            )
                        ]
                    )
                ]
            )
        )

    # теперь перейдем к главной строке боковой панели и значкам
    def ContainedIcon(self, icon_name:str, text:str):
        return Container(
            width=180,
            height=45,
            border_radius=10,
            on_hover=lambda e: self.HightLight(e),
            content=Row(
                controls=[
                    IconButton(
                        icon=icon_name,
                        icon_size=18,
                        icon_color='white54',
                        style=ButtonStyle(
                            shape={
                                "": RoundedRectangleBorder(radius=7),
                            },
                            overlay_color={
                                "": 'transparent'
                            },
                        )                                      
                    ),
                    Text(
                        value=text,
                        color="white54",
                        size=11,
                        opacity=1, 
                        animate_opacity=200,
                    )
                ]
            ),
        )


    def build(self):
        return Container(
                height=580,
                width=200,
                padding=padding.only(top=10),
                alignment=alignment.center,
                content=Column(
                    alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment='center',
                    controls=[
                        self.UserData("SH", 'Shishin Ilia','Designer'),
                        Container(
                            width=24,   
                            height=24, 
                            bgcolor="bluegrey800",
                            border_radius=8,
                            on_click=partial(self.func)
                            ),
                        
                        #Добавляем делитель
                        Divider(height=5, color="transparent"),
                        self.ContainedIcon(icons.SEARCH, "Search"),
                        self.ContainedIcon(icons.DASHBOARD_ROUNDED, "Plagins"),
                        self.ContainedIcon(icons.BAR_CHART, "Statisics"),
                        self.ContainedIcon(icons.NOTIFICATIONS, "Notifocations"),
                        self.ContainedIcon(icons.PIE_CHART_ROUNDED, "Analytics"),
                        self.ContainedIcon(icons.SETTINGS_ROUNDED, "Settings"),
                        self.ContainedIcon(icons.WALLET_ROUNDED, "Wallet"),
                        Divider(height=5, color="white24"),
                        self.ContainedIcon(icons.LOGIN_ROUNDED, "Logout"),
                    ]
                )
            )
    


def main(page: Page):
    page.title  = 'Flet'

    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'

    def AnimatedSidebar(e):
        # существует несколько шагов для анимации боковой панели
        # сначала мы проверяем, соответствует ли ширина желаемой конечной ширине,
        # page.controls[0] - это класс, который мы вызвали. Класс находится в позиции
        #controls[0] и напомним, что класс возвращает
        #контейнер, который мы будем сворачивать и расширять
        if page.controls[0].width !=  62:
            # поскольку боковая панель (т.е. контейнер) имеет номер 62,
            # будет запущен этот оператор if.
            # итак, нам нужно сначала уменьшить непрозрачность, прежде чем сворачивать
            for item in (
                #нам нужно выполнить итерацию по строкам и значкам, которые
                #были возвращены классом NavBar
                # итак, класс находится в таком положении:
                page.controls [0]
                #далее идет содержимое контейнера
                .content.controls [0]
                #  далее идет строка controls
                .content.controls [0]
                #Здесь иной лейер (!)
                .content.controls [1]
                # тогда позиция text
                .controls[:] # : означает весь список элементов управления
            ):
                item.opacity = (
                    0  # таким образом, каждый элемент теперь ссылается на элемент управления Text()
                    #на боковой панели
                )
                item.update()
            
            for items in page.controls[0].content.controls[0].content.controls[3:]:
                if isinstance(items, Container):
                    items.content.controls[1].opacity = 0
                    items.content.update()

            time.sleep(0.2)

            page.controls[0].width = 62
            page.controls[0].update()


        else:
            page.controls[0].width = 200
            page.controls[0].update()

            time.sleep(0.2)

            for item in (
                
                page.controls [0]
                .content.controls [0]
                .content.controls [0]
                .content.controls [1]
                .controls[:] 
            ):
                item.opacity = 1
                item.update()
            
                for items in page.controls[0].content.controls[0].content.controls[3:]:
                    if isinstance(items, Container):
                        items.content.controls[1].opacity = 1
                        items.content.update()
    page.add(
          
        Container(
            width=200,
            height=580,
            bgcolor='black',
            border_radius=10,
            animate=animation.Animation(500, "decelerate"),
            alignment=alignment.center,
            padding=10,

            content=NavBar(AnimatedSidebar),
        ), 
        Container(
            width=600,
            height=580,
            bgcolor="black",
            alignment=alignment.center,
            
            padding=10,
            content= None
        )       

        
        
    )
    
    page.update()


if __name__ == '__main__':
    flet.app(target=main)