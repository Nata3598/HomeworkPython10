import operations_rational as op
import sys

def x():
    firstnum = float( input('Введите первое число с плавающей запятой: ').replace(',', '.') )
    return firstnum

def y():
    secondnum = float( input('Введите второе число с плавающей запятой: ').replace(',', '.') )
    return secondnum

def selectoperation():
    global operation
    operation = ( input(f'Выберите операцию: +, -, *, /: ') )
    if operation == '+' or '-' or '/' or '*':
        return operation
    else:
        print('Неверный синтаксис')

def res(firstnum, secondnum):
    if  operation == '+':
        res = firstnum + secondnum
        result = round(res, 3)
        return result
    elif operation == '-':
        res = firstnum - secondnum
        result = round(res, 3)
        return result
    elif operation == '*':
        res = firstnum * secondnum
        result = round(res, 3)
        return result
    elif operation == '/':
        res = firstnum / secondnum
        result = round(res, 3)
        return result
    else:
        print('Неверный синтаксис')

def mainRat():
    x = op.x()
    while True:
        y = op.y()
        oper = op.selectoperation()
        res = op.res(x, y)
        with open('results.txt', 'a') as f:
            f.write(f'{x} {oper} {y} = {res}\n')
            f.close()
        print(f'Результат {x} {oper} {y} = {res}\n(записано в results.txt)' )
        again = input('Вы хотите рассчитать другие числа? (y/n) : ').lower()
        if again == 'y':
            useresult = input('Вы хотите использовать результат последней операции? (y/n): ').lower()
            if useresult == 'y':
                x = res
                continue
            elif useresult == 'n':
                break
            else:
                sys.exit()           
        else:   
            sys.exit()