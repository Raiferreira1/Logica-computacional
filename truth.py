from Formula import *

formula0 = Or(Atom('s'),Atom('r'))
def valuation(A:Atom):
    valuation_set= {
        "P": True,
        "Q": False,
        "S": False,
        "R":True
    }

    if isinstance(A, Atom) and A.name.upper() in valuation_set:
        return valuation_set[A.name.upper()]
    
    

def truth_value(Formula:Formula,v = valuation ):
    
    if isinstance(Formula,Atom):
       return v(Formula) 
    
    if isinstance(Formula,Not):
        return truth_value(Formula.inner,v)
    
    if isinstance(Formula, And):
        return truth_value(Formula.left) and truth_value(Formula.right)
    
    if isinstance(Formula,Or):
        return truth_value(Formula.left) or truth_value(Formula.right)
    
    if isinstance(Formula,Implies):
        return (not truth_value(Formula.left,v)) or truth_value(Formula.right)

print(truth_value(formula0))