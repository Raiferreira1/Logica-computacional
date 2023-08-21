from Formula import *

formula1 = Or(Atom('p'), Atom('l'))
formula2 = Or(Atom('s'), Or(Atom('p'), Atom('s')))
formula3 = And(Or(Atom('r'),Not(Not(Atom('p')))),Not(Atom('q')))
formula4 = Or(Not(Atom('p')),Not(Or(Atom('p'),Atom('q'))))

'''
    The function Checks whether a logical formula is in Negative Normal Form (NNF).
    
'''
def is_negation_normal(formula):

    if isinstance(formula,Atom):
        return True

    elif isinstance(formula, Not):
         if isinstance(formula.inner, Not): 
            return is_negation_normal(formula.inner.inner)
         return isinstance(formula.inner, Atom)

    elif isinstance(formula,(Or,And)):
        return is_negation_normal(formula.left) and is_negation_normal(formula.right)

    else:
        return False
    

