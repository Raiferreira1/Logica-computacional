from Formula import *

formula1 = Or(Atom('p'), Atom('l'))
formula2 = Implies(Atom('s'), Or(Atom('p'), Atom('s')))
formula3 = Atom('s')
formula4 = Implies(Or(Atom('r'),Not(Atom('p'))),Not(Atom('q')))
print(formula1)
print(formula2)

'''
    the following function serves to replace a subformula with another formula
    it will receive as a parameter a formula A, a subformula B of A,
    and a new formula C that will replace B
    

    example:
            formula1 = Or(Atom('p'), Atom('l')) #(p ∨ l)
            formula2 = Implies(Atom('s'), Or(Atom('p'), Atom('s'))) # (p ∨ l)
            formula3 = Atom('s') #  s

            substitution (formula2,formula3,formula1) 
            return (p ∨ l) → (p ∨ (p ∨ l)))  

    if B is not a subformula of A the function must Return A
'''
def substitution(formula, old_subformula, new_subformula):

    if formula == old_subformula:
        return new_subformula
    
    elif isinstance(formula,Atom):
        return formula
    
    elif isinstance(formula, Not):
        formula.inner = substitution(formula.inner, old_subformula, new_subformula)
        return formula
    
    elif isinstance(formula, (And, Or, Implies)):
        formula.left = substitution(formula.left, old_subformula, new_subformula)
        formula.right = substitution(formula.right, old_subformula, new_subformula)
        return formula
    
    else:
        return formula
    
