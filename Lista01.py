from Formula import *

formula1 = Not(Or(Atom('p'), Atom('l')))
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
    
# print(count_connectives(formula3))


'''
2. Conforme a definicão de fórmula da lógica proposicional, os conectivos binários devem
ser escritos na forma infixa, ou seja, devem ser escritos entre duas fórmulas. Essa
definição poderia ser modificada possibilitando escrever os conectivos na notacão
polonesa, conforme indicado pelas correspondências a seguir:


• A formula A atomica corresponde à formula A na notaçao polonesa,
• (¬A) corresponde à ¬A,
• (A ∧ B) corresponde à ∧AB,
• (A ∨ B) corresponde à ∨AB,
• (A → B) corresponde à → AB.

Escreva as formulas a seguir utilizando a notação polonesa:

(a) ¬(p → ¬q)  RESPOSTA: ¬→p¬q   N I p N q

(b) ((¬¬p ∨ q) → (p → q))   RESPOSTA: →V¬¬pq→pq     I O N N p q I p q





   
    notacão polonesa foi criada por jam tukasiewicz
'''





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
# formulasAtoms = get_formulas_atoms(formula1)
# for formulaAtom in formulasAtoms:
#     print(formulaAtom)


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
    


# #iterating between the set of formulas for print

# formulasAtoms = get_formulas_atoms(formula1)
# for formulaAtom in formulasAtoms:
#     print(formulaAtom)
# '''

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
    

'''
5. Conforme a definição de fórmula da lógica proposicional, os conectivos binários devem
ser escritos na forma infixa, ou seja, devem ser escritos entre duas formulas. Essa
definição poderia ser modificada possibilitando escrever os conectivos na notação
polonesa, conforme indicado pelas correspondencias a seguir:


• A formula A atomica corresponde à formula A na notaçao polonesa,
• (¬A) corresponde à ¬A,
• (A ∧ B) corresponde à ∧AB,
• (A ∨ B) corresponde à ∨AB,
• (A → B) corresponde à → AB.

As f ormulas a seguir est ̃ao na nota ̧c ̃ao polonesa. Reescreva-as na nota ̧c ̃ao convencio-
nal:

(a) ∨ → p q → r → ∨ p q ¬ s  RESPOSTA:    ((p → q)  V  (r → ((p V q ) → (¬s)) ))
(b) → → p q ∨ → p q → ¬ r r   RESPOSTA:      ((p → q ) →  (  (p → q) V ( ¬r → r)))
'''



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
    
    
print(substitution(formula1,Atom('p'),Atom('flavia')))


def atomic_occurrences(formula):

    if isinstance(formula, Atom):
        return 1

    elif isinstance(formula, Not):
        if isinstance(formula.inner,Atom):
            return 1
        return atomic_occurrences(formula.inner)

    elif isinstance(formula, (Implies,Or,And)):
        return atomic_occurrences(formula.left) + atomic_occurrences(formula.right)
        
    else:
        return{None}
    




def occurrences_binary_connections (formula):
    if isinstance(formula, Atom):
        return 0
    
    elif  isinstance(formula, Not):
        return occurrences_binary_connections(formula.inner)
    
    elif isinstance(formula, (Implies,Or,And)):

        return 1 + occurrences_binary_connections(formula.left) + occurrences_binary_connections(formula.right)
    else:
        return 0 
    

# print(formula1)
# print(occurrences_binary_connections(formula1))
# print(formula2)
# print(occurrences_binary_connections(formula2))
# print(formula3)
# print(occurrences_binary_connections(formula3))