import telebot
import operations_rational as opRat
import operations_complex as opComp

def get_token():
    file = open('token.csv', 'r')
    for i in file:
        token = i
    file.close()
    return token

ratx = 0
raty = 0
compx = ''
compy = ''
operation = '+'


bot = telebot.TeleBot( get_token() )

@bot.message_handler(content_types=['sticker', 'pinned_message', 'photo', 'audio', 'video'])
def warning(message):
    bot.send_message(message.chat.id, f'Я тебя не понимаю. Введи: /help.')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привет, *{message.from_user.first_name}!*\nВ любой непонятной ситуации введи\nкоманду: /help\nДа! кнопки скоро появятся ;)\nЧтобы вызвать главное меню введи: /main')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(
        message.chat.id, f'/start - начать сначала (перезапустить бота)\n/main - главное меню\n/help - вызвать справку')


@bot.message_handler(commands=['rational'])
def mainRat(message):
    # if (step == 1):
    bot.send_message(message.chat.id, f'Введите X: ')
    bot.register_next_step_handler(message, EnterRatX)
    
    # if (step == 2):
    #     bot.send_message(message.chat.id, f'Введите Y: ')
    #     bot.register_next_step_handler(message, raty)

    # if (step == 3):
        # print(ratx, raty)

@bot.message_handler(commands=['complex'])
def mainComplex(message):
    bot.send_message(message.chat.id, f'Введите первое комплексное число: ')
    bot.register_next_step_handler(message, EnterCompX)


@bot.message_handler(content_types=['text'])
def main(message):
    if message.text == '/main':
         bot.send_message(message.chat.id, f'Выберите режим работы? (рациональные/комплексные):\n/rational\n/complex')
         # opComp.init_data_base('results.txt')
    # elif message.text == '/rational':
    #     print('Пользователь выбрал рациональные числа')
    #     bot.register_next_step_handler(message, mainRat)
    # elif message.text == '/complex':
    #     print('Пользователь выбрал комплексные числа')
    #     bot.register_next_step_handler(message, mainComplex)
    # x = op.x()
    # while True:
    #     y = op.y()
    #     oper = op.selectoperation()
    #     res = op.res(x, y)
    #     with open('results.txt', 'a') as f:
    #         f.write(f'{x} {oper} {y} = {res}\n')
    #         f.close()
    #     print(f'Результат {x} {oper} {y} = {res}\n(записано в results.txt)' )
    #     again = input('Вы хотите рассчитать другие числа? (y/n) : ').lower()
    #     if again == 'y':
    #         useresult = input('Вы хотите использовать результат последней операции? (y/n): ').lower()
    #         if useresult == 'y':
    #             x = res
    #             continue
    #         elif useresult == 'n':
    #             break
    #         else:
    #             sys.exit()           
    #     else:   
    #         sys.exit()

def EnterRatX(message):
    global ratx
    ratx = float(message.text.replace(',', '.'))
    
    bot.send_message(message.chat.id, f'Введите Y: ')
    bot.register_next_step_handler(message, EnterRatY)

def EnterRatY(message):
    global raty
    raty = float(message.text.replace(',', '.'))

    bot.send_message(message.chat.id, f'Выберите операцию: +, -, *, /')
    bot.register_next_step_handler(message, RatOperation)

def RatOperation(message):
    global ratx, raty, ratop
    if message.text in ['+','-','*','/']:
        ratop = message.text
        res = opRat.res(ratx, raty, ratop)
        bot.send_message(message.chat.id, f'Результат {ratx} {ratop} {raty} = {res}')
        
        bot.send_message(
            message.chat.id, f'/main - возврат в главное меню\n/help - вызвать справку')
    else:
        bot.send_message(message.chat.id, f'Неверная операция')
        bot.register_next_step_handler(message, RatOperation)

def EnterCompX(message):
    global compx
    compx = message.text
    
    bot.send_message(message.chat.id, f'Введите второе комплексное число: ')
    bot.register_next_step_handler(message, EnterCompY)

def EnterCompY(message):
    global compy
    compy = message.text

    bot.send_message(message.chat.id, f'Выберите операцию: +, -, *, /')
    bot.register_next_step_handler(message, CompOperation)


def CompOperation(message):
    global compx, compy, operation
    if message.text in ['+','-','*','/']:
        operation = message.text
        r = opComp.CalcComp(compx, compy, operation)
        res = []
        for i in r:
            res.append(float(i))
        bot.send_message(message.chat.id, f'Результат ({compx}) {operation} ({compy}) = {CompResStr(res)}')
        
        bot.send_message(
            message.chat.id, f'/main - возврат в главное меню\n/help - вызвать справку')
    else:
        bot.send_message(message.chat.id, f'Неверная операция')
        bot.register_next_step_handler(message, CompOperation)


def CompResStr(res):
    s = ''
    if res[1] != 0:
        for i in range(0, 2):
            if res[i] > 0 and i == 1:
                s += '+ '
            elif res[i] < 0 and i == 1:
                res[i] = -res[i]
                res[i] = str(res[i])
                s += ('- ')
                s += (res[i])
            else:
                res[i] = str(res[i])
                s += (res[i])
            if i != 1:
                s += (' ')
        s += ('i\n')
    else:
        res[0] = str(res[0])
        s += (f'{res[0]}\n')
    return s

print('server start')
bot.infinity_polling()