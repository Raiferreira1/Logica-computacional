from Formula import *

formula1 = Or(Atom('p'), Atom('l'))
formula2 = Implies(Atom('s'), Or(Atom('p'), Atom('s')))
formula3 = Implies(Or(Atom('r'),Not(Atom('p'))),Not(Atom('q')))

'''
this function should return the total size of a formula

    example_1 :
               formula1 = Or(Atom('p'), Atom('l'))   # (p ∨ l)

               formula_size(formula1)
               the return must be 3 because formula1 has three elements  # p,l,V

    example_2 :
               formula2 = Implies(Atom('s'), Or(Atom('p'), Atom('s')))  # (s → (p ∨ s))

               formula_size(formula2)
               the return must be 5 because formula2 has five elements  # s,→,p,∨,s
'''

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
print(formula_size(formula3))
