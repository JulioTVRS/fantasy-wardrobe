import os
import subprocess
from datetime import date

def menu(titulo, opcoes):
    borda_cima = "┏" + "┅" * 45 + "┓"
    borda_centro = "┣" + "┅" * 45 + "┫"
    borda_baixo = "┗" + "┅" * 45 + "┛"

    menu = borda_cima + "\n"
    menu += "┃" + " " * 45 + "┃\n"
    menu += "┃" + titulo.center(45) + "┃\n"
    menu += "┃" + " " * 45 + "┃\n"
    menu += borda_centro + "\n"

    for opcao in opcoes:
        menu += f"┃ {opcao:<43} ┃\n"
    menu += borda_baixo

    return menu

def submenu(titulo):
    borda_cima = "┏" + "┅" * 35 + "┓"
    borda_baixo = "┗" + "┅" * 35 + "┛"

    menu = borda_cima + "\n"
    menu += "┃" + " " * 35 + "┃\n"
    menu += "┃" + titulo.center(35) + "┃\n"
    menu += "┃" + " " * 35 + "┃\n"
    menu += borda_baixo

    return menu

def mostrar_menu(titulo, opcoes):
    print(menu(titulo, opcoes))

def mostrar_submenu(titulo):
    print(submenu(titulo))

def limpar():
    if os.name == "nt":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear", shell=True)
        
def data_atual():
    return str(date.today().day) + "/" + str(date.today().month) + "/" + str(date.today().year)