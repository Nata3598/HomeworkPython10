import operations_rational as opRat
import operations_complex as opComp

type = input('Выберите режим работы? (рациональные/комплексные): ').lower()

while type ==  'рациональные':
    opRat.mainRat()
    
if type == 'комплексные':
    opComp.mainComp()