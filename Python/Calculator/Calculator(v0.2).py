from colorama import *
init()
class Caculator:
    def __init__(self):
       print(Fore.GREEN + '###  Здраствуй уважаемый пользователь! ###\n###  Это мой первый в мире калькулятор ###\n###     Пользуйся им на здоровье!      ###')
       continuation = input(Style.BRIGHT + '   |Продолжим?(Y или N)|\n>>' + Style.RESET_ALL)
       if continuation == 'Y':
           self.start()
       else:
           print(Fore.BLACK +'   |...Завершение программы...|')
           pass
    def start(self):
       print(Fore.GREEN + '   |Какую арифметическую операцию вы хотите провести?|   ')
       print('>>Сложение:  1\n>>Вычитание: 2\n>>Умножение: 3\n>>Деление:   4')
       choice = int(input('>>'))
       if choice == 1:
           self.addition()
       elif choice == 2:
           self.subtraction()
       elif choice == 3:
           self.multiplication()
       elif choice == 4:
           self.division()
       else:
           print(Fore.LIGHTRED_EX + '   |Ваше число не соответствует выбору! Перезапустите калькулятор!|   ')
    def addition(self):
        print('   |Сложение|\n   |Введите в переменные A и B ваши значения|')
        a = int(input('>>A='))
        b = int(input('>>B='))
        print('>>Ответ:', a + b)
        Caculator()
    def subtraction(self):
        print('   |Вычитание|\n   |Введите в переменные A и B ваши значения|')
        a = int(input('>>A='))
        b = int(input('>>B='))
        print('>>Ответ:', a - b)
        Caculator()
    def multiplication(self):
        print('   |Умножение|\n   |Введите в переменные A и B ваши значения|')
        a = int(input('>>A='))
        b = int(input('>>B='))
        print('>>Ответ:', a * b)
        Caculator()
    def division(self):
        print('   |Деление|\n   |Введите в переменные A и B ваши значения|')
        a = int(input('>>A='))
        b = int(input('>>B='))
        print('>>Ответ:', a / b)
        Caculator()
Caculator()