def Insert_Numbers():
    # Функция приглашения пользователя для вставки двух комплексых чисел и операции между ними
    print('Тип комплексного числа: a + bi\n')
    user_komplex1 = input('Введите первое комплексное число: ')
    user_komplex2 = input('Введите второе комплексное число: ')
    operation = input('Что вы хотите с этим делать? (+, -, *, /): ')
    with open('results.txt', 'a') as f:
        f.write(f'({user_komplex1}) {operation} ({user_komplex2}) = ')
        f.close()
    return [user_komplex1, user_komplex2, operation]

def Take_Rational_Part(user_number):
    # Функция возвращает рациональную часть из комплексного числа
    rational_part = []
    for k in range(0, len(user_number)):
        if user_number[k] != ' ':
            rational_part.append(user_number[k])
        else:
            break
    rational_part = float(''.join(rational_part))
    return rational_part

def Take_Imaginary_Part(user_number):
    # Функция возвращает мнимую часть
    imaginary_part = []
    for i in range(0, len(user_number)):
        if user_number[i] == 'i':
            while user_number[i] != ' ':
                imaginary_part.insert(0,user_number[i - 1])
                i-= 1
    imaginary_part.pop(0)
    imaginary_part = float(''.join(imaginary_part))
    return imaginary_part

def Take_Symbol(user_number):
    # Возврат функции - или + между рациональной и мнимой частями
    symbol = []
    for l in range(0, len(user_number)):
        if user_number[l] == '-' and l !=0 or user_number[l] == '+' and l != 0:
            symbol.append(user_number[l])
    symbol = ''.join(symbol)
    return symbol

def Addition(r1, s1, i1, r2, s2, i2):
    # Функция сложения двух комплексных чисел
    res = []
    res.append(r1+r2)
    if s1 == '+' and s2 == '+':
        res.append(i1+i2)
    elif s1 == '+' and s2 == '-':
        res.append(i1-i2)
    elif s1 == '-' and s2 == '+':
        res.append(i2-i1)
    else:
        res.append(-(i1+i2))
    return res

def Deduction(r1, s1, i1, r2, s2, i2):
    # Функция вычетания второго комплексного числа из первого
    res = []
    res.append(r1-r2)
    if s1 == '+' and s2 == '+':
        res.append(i1-i2)
    elif s1 == '+' and s2 == '-':
        res.append(i1+i2)
    elif s1 == '-' and s2 == '+':
        res.append(-i2-i1)
    else:
        res.append(i2-i1)
    return res

def Multiply(r1, s1, i1, r2, s2, i2):
    # Функция перемножения двух комплексных чисел
    res = []
    res.append(r1*r2)
    if s1 == "+" and s2 == "+" or s1 == "-" and s2 == "-":
        res.append(-i1*i2)
    else:
        res.append(i1*i2)
    if s1 == "+":
        res.append(r2*i1)
    else:
        res.append(-r2*i1)
    if s2 == "+":
        res.append(r1*i2)
    else:
        res.append(-r1*i2)
    res[0] = res[0] + res[1]
    res[1] = res[2] + res[3]
    res.pop(3)
    res.pop(2)
    return res    
    
def Division(r1, s1, i1, r2, s2, i2):
    # Функция деления двух комплексных чисел
    numerator = []
    denominator = []
    res = []
    numerator.append(r1*r2)
    if s1 == "+" and s2 == "+" or s1 == "-" and s2 == "-":
        numerator.append(i1*i2)
    else:
        numerator.append(-i1*i2)
    if s1 == "-":
        numerator.append(-r2*i1)
    else:
        numerator.append(r2*i1)
    if s2 == "+":
        numerator.append(-r1*i2)
    else:
        numerator.append(r1*i2)
    numerator[0] = numerator[0] + numerator[1]
    numerator[1] = numerator[2] + numerator[3]
    numerator.pop(3)
    numerator.pop(2)
    denominator.append(r2**2+i2**2)
    res.append(numerator[0]/denominator[0])
    res.append(numerator[1]/denominator[0])
    return res

def record_in_file(res):
    # Добавлены результаты в файл'''
    with open('results.txt', 'a') as f:
        if res[1] != 0:
            for i in range(0, 2):
                if res[i] > 0 and i == 1:
                    f.write('+ ')
                elif res[i] < 0 and i == 1:
                    res[i] = -res[i]
                    res[i] = str(res[i])
                    f.write('- ')
                    f.write(res[i])
                else:
                    res[i] = str(res[i])
                    f.write(res[i])
                if i != 1:
                    f.write(' ')
            f.write('i\n')
        else:
            res[0] = str(res[0])
            f.write(f'{res[0]}\n')
        print('(записано в results.txt)')
        f.close()

def Repeat_Or_No():
    '''Функцию запроса пользователя продолжить или нет'''
    user_choice = 'Неверный ответ'
    while user_choice.lower() != 'y' or user_choice.lower() != 'n':
        user_choice = input('Хотите продолжить работу с комплексными числами? (y/n) ')
        if user_choice == 'n':
            return False
        elif user_choice == 'y':
            return True
        else:
            print('Неверный ответ! Хотите продолжить работу с комплексными числами? (y/n) ')

def CalcComp(num1, num2, operation):
    if operation == "+":
        res = Addition(Take_Rational_Part(num1), Take_Symbol(num1), Take_Imaginary_Part(num1), Take_Rational_Part(num2), Take_Symbol(num2), Take_Imaginary_Part(num2))
    elif operation == "-":
        res = Deduction(Take_Rational_Part(num1), Take_Symbol(num1), Take_Imaginary_Part(num1), Take_Rational_Part(num2), Take_Symbol(num2), Take_Imaginary_Part(num2))
    elif operation == "*":
        res = Multiply(Take_Rational_Part(num1), Take_Symbol(num1), Take_Imaginary_Part(num1), Take_Rational_Part(num2), Take_Symbol(num2), Take_Imaginary_Part(num2))
    elif operation == "/":
        res = Division(Take_Rational_Part(num1), Take_Symbol(num1), Take_Imaginary_Part(num1), Take_Rational_Part(num2), Take_Symbol(num2), Take_Imaginary_Part(num2))
    else:
        res = [0]
    record_in_file(res)
    return res

def mainComp():
    repeat = True
    while repeat == True:
        num1, num2, op = Insert_Numbers()
        CalcComp(num1, num2, op)
        repeat = Repeat_Or_No()