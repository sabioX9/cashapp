#not so serious app
#github testing

import datetime
import json
import menu


with open('spent.txt') as spent:
    data = spent.read()

spent_money = int(data)


class Spending:

    def __init__(self, starting_cash):
        self.cash = starting_cash

    def add_spending(self, amount):
        self.cash += amount
        return self.cash

    def show_spent_money(self):
        today = datetime.date.today()
        exact_day = today.strftime("%d/%m/%Y")
        return 'Na dzien {} wydales {}'.format(exact_day, self.cash)

    def greetings(self):
        print('Witaj w CashApp. Twojej aplikacji do sledzenia wydatkow.')
        weekday = datetime.datetime.today().weekday()
        if weekday == 6:
            print('Dzis mamy niedziele')
        elif weekday == 0:
            print('Dzis mamy poniedzialek')
        elif weekday == 1:
            print('Dzis mamy wtorek')
        elif weekday == 2:
            print('Dzis mamy srode')
        elif weekday == 3:
            print('Dzis mamy czwartek')
        elif weekday == 4:
            print('Dzis mamy piatek')
        elif weekday == 5:
            print('Dzis mamy sobote')

    def save_to_file(self):
        cash = str(self.cash)
        with open('spent.txt', 'w') as spent:
            spent.write(cash)
        return None


user = Spending(spent_money)

if __name__ == "__main__":
    user.greetings()
    while True:
        menu.show_menu()
        user_input = int(input('Co chcialbys zrobic? '))
        menu.execute_menu(user_input)










