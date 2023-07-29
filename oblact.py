from yargy import Parser, rule, and_
from yargy.predicates import gram, is_capitalized, dictionary


GEO = rule(
    and_(
        gram('ADJF'),  # так помечается прилагательное, остальные пометки описаны в
                       # http://pymorphy2.readthedocs.io/en/latest/user/grammemes.html
        is_capitalized() #C заглавной буквы
        ),
    gram('ADJF').optional().repeatable(),
    dictionary({
        'федерация',
        'республика'
        })
    )


parser = Parser(GEO)
text = '''
В Чеченской республике на день рождения ...
Советская народная республика провозгласила ...
Башня Федерация — одна из самых высоких ...
'''
for match in parser.findall(text):
    print([_.value for _ in match.tokens])

#['Советская', 'народная', 'республика']
#['Чеченской', 'республике']