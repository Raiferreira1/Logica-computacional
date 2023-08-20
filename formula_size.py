from Formula import *

formula1 = Or(Atom('p'), Atom('s'))
formula2 = Implies(Atom('p'), Or(Atom('p'), Atom('s')))


print(f'1° {formula1}')
print(f'2° {formula2}')


def formula_size(formula):

    if isinstance(formula, Atom):
        return 1
    
    elif isinstance(formula, Not):
        return 1 + formula_size(formula.inner)
    
    elif isinstance(formula, And) or isinstance(formula, Or) or isinstance(formula, Implies) :
        return 1 + formula_size(formula.left) + formula_size(formula.right)
    
    else:
        return 0  
    
print(formula_size(formula1))
print(formula_size(formula2))
