from yargy import (
    rule,
    or_, and_
)

from yargy.interpretation import fact, attribute
from yargy.predicates import (
    eq, lte, gte, gram, type, tag,
    length_eq,
    in_, in_caseless, dictionary,
    normalized, caseless,
    is_title,
    
)

from yargy import Parser, rule
from yargy.predicates import gram, dictionary, type as t1

INT = t1('INT')

NZAKAZ = rule (INT.repeatable(),caseless('a').optional())
ZAKAZ = rule (dictionary({'заказ'}), dictionary({'номер', '№'}), NZAKAZ)

R_1 = rule(
    or_(
        rule(gram('ADJF')
                ,dictionary({'сок', 'морс','компот'})
                )
        ,
        (rule(dictionary({'заказ'}),
                gram('ADJF').optional()
                ,normalized('два').optional()
                ,dictionary({'чай'})
                ,caseless('с')
                ,normalized('сахаром')
                )
            )
        )
    )
 



parser = Parser(R_1)
text = 'В заказ № 12453a на доставку входили апельсиновый сок, вишнёвый морс и абрикосовый компот и два Чая с сахаром.'

for match in parser.findall(text):
    print ([x.value for x in match.tokens])

parser = Parser(ZAKAZ)
for match in parser.findall(text):
    print ([x.value for x in match.tokens])