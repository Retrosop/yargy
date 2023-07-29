#парсер простых математических выражений:

from yargy import Parser, rule, or_, forward
from yargy.predicates import in_


SYMBOL = rule(
                 in_('AB')
            ).named('SYMBOL')
TERM = rule(
            SYMBOL,
            in_('/*'),
            SYMBOL
           ).named('TERM')
EXPR = forward()
EXPR.define(or_(
    SYMBOL,
    TERM,
    rule(
        EXPR,
        in_('+-'),
        EXPR
    )
).named('EXPR'))


parser = Parser(EXPR)
match = parser.match('A * A + B * B')
for i in match:
    print(i,'\n')
match.tree.as_dot
