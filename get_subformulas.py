from Formula import *

formula1 = Or(Atom('p'), Atom('s'))
formula2 = Implies(Atom('s'), Or(Atom('p'), Atom('s')))
formula3 = Implies(Or(Atom('r'),Not(Atom('p'))),Not(Atom('q')))
    

'''
    This function must return a set with all subformulas of a formula


    example:
               formula1 = Or(Atom('p'), Atom('l'))   # (p ∨ l)

               get_subformulasformulas(formula1)
               the function must return   {p V l,p,l}

'''

def get_subformulas(formula):
    if isinstance(formula, Atom):
        return {formula}
    
    elif isinstance(formula, Not):
        return {formula} | get_subformulas(formula.inner)
    
    elif isinstance(formula, Implies)  or isinstance(formula, And) or isinstance(formula, Or):
        return {formula} | get_subformulas(formula.left) | get_subformulas(formula.right)
        
    else:
        return{None}


subs = get_subformulas(22)

for subformula in subs:
    print(subformula)

'''
# another way to implement the function

def get_subformulas(formula):
    if isinstance(formula, Atom):
        return {formula}      
    
    elif isinstance(formula, Not):
        subformulas = get_subformulas(formula.inner)
        subformulas.add(formula)  
        return subformulas
    
    elif isinstance(formula, Implies)  or isinstance(formula, And) or isinstance(formula, Or):

        subformulas = {formula}
        subformulas.update(get_subformulas(formula.left))
        subformulas.update(get_subformulas(formula.right))
        return subformulas
    else:
        return{None}


subs = get_subformulas(formula3)
for subformula in subs:
    print(subformula)
'''
