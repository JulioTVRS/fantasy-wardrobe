import os
import subprocess
from datetime import date

def menu(titulo, opcoes):
    borda = "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"

    menu = borda + "\n"
    menu += "|" + " " * 35 + "|\n"
    menu += "|" + titulo.center(35) + "|\n"
    menu += "|" + " " * 35 + "|\n"
    menu += borda + "\n"

    for opcao in opcoes:
        menu += f"| {opcao:<33} |\n"
    menu += borda

    return menu

def submenu(titulo):
    borda = "-------------------------------------"

    menu = borda + "\n"
    menu += "|" + " " * 35 + "|\n"
    menu += "|" + titulo.center(35) + "|\n"
    menu += "|" + " " * 35 + "|\n"
    menu += borda

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