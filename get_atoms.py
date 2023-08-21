from Formula import *

formula1 = Or(Atom('p'), Atom('l'))
formula2 = Implies(Atom('s'), Or(Atom('p'), Atom('s')))
formula3 = Implies(Or(Atom('r'),Not(Atom('p'))),Not(Atom('q')))


'''
    This function must return the set of atomic formulas contained in a formula

    example_1 :
               formula1 = Or(Atom('p'), Atom('l'))   # (p ∨ l)

               get_formulas_atoms(formula1)
               must return a set with the atomic ones Atom('p'), Atom('l').  # {p,l}

    example_2 :
               formula2 = Implies(Atom('s'), Or(Atom('p'), Atom('s')))  # (s → (p ∨ s))

               get_formulas_atoms(formula2)
               must return a set with the atomic ones Atom('p') , Atom('s').  # {s,p}
'''

def get_formulas_atoms(formula):

    if isinstance(formula, Atom):
        return {formula}

    elif isinstance(formula, Not):
        return get_formulas_atoms(formula.inner)

    elif isinstance(formula, (Implies,Or,And)):
        return get_formulas_atoms(formula.left) | get_formulas_atoms(formula.right)
        
    else:
        return{None}
    


#iterating between the set of formulas for print
formulasAtoms = get_formulas_atoms(formula1)
for formulaAtom in formulasAtoms:
    print(formulaAtom)


'''  
# another way to implement the function

def get_formulas_atoms(formula):
    if isinstance(formula, Atom):
        return {formula}
    
    elif isinstance(formula, Not):
        formulas_atoms = get_formulas_atoms(formula.inner)
        return formulas_atoms
    
    elif isinstance(formula, (Implies, Or,And)):
        formulas_atoms = set()
        formulas_atoms.update(get_formulas_atoms(formula.left))
        formulas_atoms.update(get_formulas_atoms(formula.right))
        return formulas_atoms
    else:
        return{None}
    


#iterating between the set of formulas for print

formulasAtoms = get_formulas_atoms(formula1)
for formulaAtom in formulasAtoms:
    print(formulaAtom)
'''
