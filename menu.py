from main import *
import sys


with open('categories.json') as kat:
    categories = json.loads(kat.read())


def show_categories():
    for key, value in categories.items():
        print(key, ':', value)

def show_menu():
    print("### MENU: ###\n")
    menu = {
        1: "Pokaz wydatki na dzien dzisiejszy",
        2: "Zaksiegowac wydatek",
        3: "Zapisz",
        4: "Wyjsc z programu"
    }

    for key, value in menu.items():
        print(key, ':', value)



def execute_menu(position):
    if position == 1:
        print('\n')
        print(user.show_spent_money().strip())
    elif position == 2:
        show_categories()
        cat = input('Z ktorej kategorii jest to wydatek? ')

        amount = int(input('Ile dzis wydales? '))
        user.add_spending(amount)
    elif position == 3:
        user.save_to_file()
    elif position == 4:
        print('\nDo zobaczenia! ')
        sys.exit()







