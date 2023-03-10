import argparse
import secrets
class Password:
    def __init__(self, tuple_of_strs, length):
        self.length = length
        self.tuple_of_strs = tuple_of_strs
        self.signs_list = ''
        for i in tuple_of_strs:
            self.signs_list += ''.join(i)
        self.signs_list = list(self.signs_list) #нумерация
    
    def generate(self):
        password = ''
        for stroka in self.tuple_of_strs:               #три символа
            password += ''.join(secrets.choice(stroka))
        for i in range(self.length - len(self.tuple_of_strs)): 
            password += ''.join(secrets.choice(self.signs_list)) #остальные символы
        return password   
parser = argparse.ArgumentParser(
    prog = 'PasswordGeneration',
    description = 'Programma generiruet paroli',
    epilog = 'Ykajite colichestvo paroley, ih dlinu i alphaviti'
    )
parser.add_argument('-q', '--quantity', #сколько паролей генерировать
                            type = int,
                            required = True,
                            help = 'quantity of passwords')
parser.add_argument('-l', '--length', #длина паролей
                            type = int,
                            required = True,
                            help = 'passwords length')
parser.add_argument('Aa1',                     #параметр генерации
                        type = str,
                        help = 'using alphabet')
abc = 'abcdefghijklmnopqrstuvwxyz'
abc_upper = abc.upper()
numbers = '0123456789'
lst = []
for i in parser.parse_args().Aa1:
    if i == 'A':
        lst.append(abc_upper)
    elif i == 'a':
        lst.append(abc)
    elif i == '1':
        lst.append(numbers)
    else:
        print('Введён непредусмотренный символ')
parol = Password(tuple_of_strs=tuple(lst), length=parser.parse_args().length)
for i in range(parser.parse_args().quantity):  #сгенирировать заданное кол-во паролей
    print(parol.generate())
