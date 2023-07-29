from yargy import Parser, rule, and_
from yargy.predicates import gram, dictionary, type as t1

INT = t1('INT')
R_1 = rule (dictionary({'заказ'}), dictionary({'номер', '№'}), INT.repeatable())
parser = Parser(R_1)
text = '''
Просьба дать обратную связь по статусу заказа номер 12535.
В личном кабинете третий день стасус "Ожидает отправки".
Заказ № 54321 уже получен.
'''
for match in parser.findall(text):
    print ([x.value for x in match.tokens])