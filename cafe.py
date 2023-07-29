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
#from yargy.pipelines import morph_pipeline
#from yargy.tokenizer import QUOTES

from yargy import Parser, rule
from yargy.predicates import gram, dictionary

R_1 = rule(or_(
    rule(gram('ADJF')
            ,dictionary({'сок', 'морс','компот'})
            )
    ,
    (rule(gram('ADJF').optional()
            ,normalized('два').optional()
            ,dictionary({'чай'})
            ,caseless('с')
            ,normalized('сахаром')
            )
        )
    ))
            

parser = Parser(R_1)
text = 'В заказ на доставку входили апельсиновый сок, вишнёвый морс и абрикосовый компот и два Чая с сахаром.'
for match in parser.findall(text):
    print ([x.value for x in match.tokens])