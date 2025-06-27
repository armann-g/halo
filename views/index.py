import flet as ft
from flet.core.alignment import center


def IndexView(page:ft.Page, params):
    def CreateAppBar():
        app_bar = ft.AppBar(
            leading=ft.Image("images/csc_logo_100.png"),
            leading_width=40,
            title=ft.Text("Flet Template"),
            #center_title=False,
            bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
            actions=[
                ft.IconButton(ft.Icons.RESTART_ALT, on_click=restart_clicked),
                ft.IconButton(ft.Icons.FILTER_3),

            ],
        )
        return app_bar

    def restart_clicked(e):
         dlg = ft.AlertDialog(title=ft.Text("You clicked restart"))
         page.open(dlg)
    def btn_question1_clicked(e):
        page.go("/question/1")

    def btn_question2_clicked(e):
        page.go("/question/2")

    def btn_simple_clicked(e):
        page.go("/simple_view")


    appbar = CreateAppBar()
    question_data={"question" : "Name 5 largest countries",
            "answers" : ["Russia","China","USA","Canada","Brazil"]}
    question_tb=ft.Text(value=question_data["question"],size=30)
    answer_column = ft.Column()
    i=1
    for answer in question_data["answers"] :
        number = ft.Container(content=ft.Text(value=i,size=20),
                              bgcolor=ft.Colors.BROWN,
                              width=25,
                              height=25,
                              alignment=ft.alignment.center,
                              border_radius=15
                              )#put thr number in a container so we can change the background colors and etc.
        a = ft.Text(value=answer,size=20)
        row = ft.Row(controls=[number,a])#to arrange the elememts in 1 single line use row
        answer_column.controls.append(row)#controls=list
        i += 1
        user_answer_tb = ft.TextField(label="Type here")
    page.views.append(ft.View(
        "/",
        [appbar,question_tb,answer_column,user_answer_tb],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,

    )
    )
    page.update()
