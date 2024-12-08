#identity is unique
from z3 import *

e = Int('e')
c = Int('c')
f = Function('f', IntSort(), IntSort(), IntSort())
g = Function('g', IntSort(),IntSort())

#for associativity, identity, inverse axioms and the  formula that says identity is unique, instantiate with terms of depth 0, ie constants c,e

#associativity
#associativity = ForAll([x,y,z],f(f(x,y),z)==f(x,f(x,y)))
as_1 = f(f(e,e),e) == f(e,f(e,e))
as_2 = f(f(e,e),c) == f(e,f(e,c))
as_3 = f(f(e,c),e) == f(e,f(c,e))
as_4 = f(f(e,c),c) == f(e,f(c,c))
as_5 = f(f(c,e),e) == f(c,f(e,e))
as_6 = f(f(c,e),c) == f(c,f(e,c))
as_7 = f(f(c,c),e) == f(c,f(c,e))
as_8 = f(f(c,c),c) == f(c,f(c,c))
#identity
#identity = ForAll(x, And(f(x,e)==x,f(e,x)==x))
ident_1 = And(f(e,e)==e,f(e,e)==e)
ident_2 = And(f(c,e)==c,f(e,c)==c)
#inverse
#inverse = ForAll(x, And(f(x,g(x))==e,f(g(x),x)==e))
inv_1 = And(f(e,g(e))==e,f(g(e),e)==e)
inv_2 = And(f(c,g(c))==e,f(g(c),c)==e)
#identity is unique
#unique = ForAll(x,And((f(x,c)==x),f(c,x)==x,Not(e=c)))
uniq_1 = And((f(e,c)==e),f(c,e)==e,Not(e==c))
uniq_2  = And((f(c,c)==c),f(c,c)==c,Not(e==c))

#solver
solver = Solver()
solver.add(as_1)
solver.add(as_2)
solver.add(as_3)
solver.add(as_4)
solver.add(as_5)
solver.add(as_6)
solver.add(as_7)
solver.add(as_8)

solver.add(ident_1)
solver.add(ident_2)

solver.add(inv_1)
solver.add(inv_2)

solver.add(uniq_1)
solver.add(uniq_2)


if solver.check()== unsat:
    print('The obtained formula is unsatisfiable')
else:
    print('The obtained formula is satisfiable')