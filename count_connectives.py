from Formula import *

formula1 = Or(Atom('p'), Atom('l'))
formula2 = Implies(Atom('s'), Or(Atom('p'), Atom('s')))
formula3 = Implies(Or(Atom('r'),Not(Atom('p'))),Not(Atom('q')))

'''
    The following function should return the number of connectives in a formula

    example_1 :
               formula1 = Or(Atom('p'), Atom('l'))   # (p ∨ l)

               count_connectives(formula1)
               It must return 1 because there is only one connector in formula1 # ∨

    example_2 :
               formula2 = Implies(Atom('s'), Or(Atom('p'), Atom('s')))  # (s → (p ∨ s))

               count_connectives(formula2)
               Must return 2 because there are two connectives in formula 2  # →,∨
    
    example_3 :
               formula3 = Implies(Or(Atom('r'),Not(Atom('p'))),Not(Atom('q')))  # ((r ∨ (¬p)) → (¬q))

               count_connectives(formula3)
               Must return 4 because there are four connectives in formula 3  # →,∨,¬,¬
'''

def count_connectives(formula):
    if isinstance(formula, Atom):
        return 0
    
    elif  isinstance(formula, Not):
        return 1 + count_connectives(formula.inner)
    
    elif isinstance(formula, (Implies,Or,And)):

        return 1 + count_connectives(formula.left) + count_connectives(formula.right)
    else:
        return 0 
    
print(count_connectives(formula3))
