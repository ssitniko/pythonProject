# Инкапсуляция

# уровни доступа
# 1 публичный, 2 защищенный, 3 приватный

class Bank(object):
    def __init__(self, name, age, balance):
        self.name = name
        self._validate_age(age)
        self._age = age
        self.__balance = balance

    def _validate_age(self,age):
        if age < 18:
            raise ValueError("Возраст должен быть 18+")

    def get_age(self):
        # print(self._age)
        return self._age

    def set_age(self, new_age):
        self._validate_age(new_age)
        self._age=new_age
        print(f'Возраст {self.name} изменен на {self._age} лет')

    def __str__(self):
        return (f'name:{self.name}\n'
                f'age:{self._age}\n'
                f'balance:{self.__balance}\n')


beka = Bank('beka', 18, 1000)
# beka.name = 'Bekbolot'
beka._age=99
beka.__balance = 2000
print(beka)
print(dir(beka))
# beka._age=199
# beka.set_age(19)
# print(beka)

# class Bank:
#     def __init__(self, name, balance):
#         self._name = name
#         self._balance = balance
#
#     def moneyX(self, add_sum):
#         self.add_sum = add_sum
#         if int(add_sum) <= 0:
#             raise ValueError('Вводите только положительное число!')
#         self._balance += add_sum
#
#     def _kill(self):
#         self._balance = 0
#
#     def __jackpot(self):
#         self._balance *= 10
#
#     def _uni_balance(self, other_balance):
#         self.other_balance = other_balance
#         self._balance += other_balance
#
#
# first_client = Bank('Arman', 1000)
# second_client = Bank('Alina', 5000)
#
# increase_balance = int(input('Enter the amount by which you would increase you balance: '))
# first_client.moneyX(increase_balance)
# print(f'The increased balance for {first_client._name} is {first_client._balance}')
#
# first_client._Bank__jackpot()
# print(f'The jackpot balance for {first_client._name} is {first_client._balance}')
#
# first_client._uni_balance(second_client._balance)
# print(f'The united balance for {first_client._name} is {first_client._balance}')
#
# first_client._kill()
# print(f'The current balance for {first_client._name} is {first_client._balance}')
#
# with open('bank.txt', 'a') as f:
#     f.write('Hello world\n')


# Калькулятор на классах, как я это понял
# class Calculator:
#     def __init__(self, value):
#         self.value = value
#
#     def __add__(self, other):
#         return Calculator(self.value + other.value)
#
#     def __sub__(self, other):
#         return Calculator(self.value - other.value)
#
#     def __mul__(self, other):
#         return Calculator(self.value * other.value)
#
#     def __truediv__(self, other):
#         if other.value == 0:
#             raise ZeroDivisionError('Делить на ноль нельзя!')
#         return Calculator(self.value / other.value)
#
#     def __str__(self):
#         return f'Result: {self.value}'
#
# def main():
#     while True:
#         input1 = input('Веберите одну из нужнных операций: сложение, вычитание, умножение, деление, стоп: ')
#         if input1 == 'стоп':
#             print('Калькулятор завершен')
#             break
#         if input1 not in ['сложение', 'вычитание', 'умножение', 'деление']:
#             print('Введите одну из предложенных операций.')
#             continue
#         try:
#             input_num1 = int(input('Введите первый операнд: '))
#             input_num2 = int(input('Введите второй операнд: '))
#         except ValueError:
#             print('Введите корректное число')
#             continue
#
#         num1 = Calculator(input_num1)
#         num2 = Calculator(input_num2)
#
#         if input1 == 'сложение':
#             print(num1 + num2)
#         elif input1 == 'вычитание':
#             print(num1 - num2)
#         elif input1 == 'умножение':
#             print(num1 * num2)
#         elif input1 == 'деление':
#             try:
#                 print(num1 / num2)
#             except ZeroDivisionError as e:
#                 print(e)
#
# if __name__ == '__main__':
#     main()