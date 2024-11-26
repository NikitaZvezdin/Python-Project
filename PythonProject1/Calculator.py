class Caculator:
    def __init__(self):
       print('### Здраствуйте уважаемый пользователь!###\n###  Это мой первый в мире калькулятор ###\n###     Пользуйся им на здоровье!      ###')
       continuation = input('   |Продолжим?(Y или N)|\n>>')
       if continuation == 'Y':
           self.start()
       else:
           print('   |...Завершение программы...|')
           pass
    def start(self):
       print('   |Какую арифметическую операцию вы хотите провести?|   ')
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
           print('   |Ваше число не соответствует выбору! Перезапустите калькулятор!|   ')
    def addition(self):
        pass
    def subtraction(self):
        pass
    def multiplication(self):
        pass
    def division(self):
        pass
Caculator()







