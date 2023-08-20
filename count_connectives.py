from Formula import *

formula1 = Or(Atom('p'), Atom('s'))
formula2 = Implies(Atom('p'), Or(Atom('p'), Atom('s')))

print(f'1° {formula1}')
print(f'2° {formula2}')

def count_connectives(formula):
    if isinstance(formula, Atom):
        return 0
    elif isinstance(formula, Implies) or isinstance(formula, Not) or isinstance(formula, And) or isinstance(formula, Or):
        return 1 + count_connectives(formula.left) + count_connectives(formula.right)
    else:
        return 0  


print(count_connectives(formula1))
print(count_connectives(formula2))