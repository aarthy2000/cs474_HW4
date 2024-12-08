#identity is unique
from z3 import *

c = Int('c')
d = Int('d')
e = Int('e')
f = Function('f', IntSort(), IntSort(), IntSort())
g = Function('g', IntSort(),IntSort())

#for associativity, identity, inverse axioms and the  formula that says inverse is unique, instantiate with terms of depth 0, ie constants c,d,e

#associativity
#associativity = ForAll([x,y,z],f(f(x,y),z)==f(x,f(x,y)))
#for this formula, instantiate with terms of depth 0, ie constants c,d,e
as_1 = f(f(e,e),e) == f(e,f(e,e))
as_2 = f(f(e,e),c) == f(e,f(e,c))
as_3 = f(f(e,e),d) == f(e,f(e,d))
as_4 = f(f(e,c),e) == f(e,f(c,e))
as_5 = f(f(e,c),c) == f(e,f(c,c))
as_6 = f(f(e,c),d) == f(e,f(c,d))
as_7 = f(f(e,d),e) == f(e,f(d,e))
as_8 = f(f(e,d),c) == f(e,f(d,c))
as_9 = f(f(e,d),d) == f(e,f(d,d))
as_10 = f(f(c,e),e) == f(c,f(e,e))
as_11 = f(f(c,e),c) == f(c,f(e,c))
as_12 = f(f(c,e),d) == f(c,f(e,d))
as_13 = f(f(c,c),e) == f(c,f(c,e))
as_14 = f(f(c,c),c) == f(c,f(c,c))
as_15 = f(f(c,c),d) == f(c,f(c,d))
as_16 = f(f(c,d),e) == f(c,f(d,e))
as_17 = f(f(c,d),c) == f(c,f(d,c))
as_18 = f(f(c,d),d) == f(c,f(d,d))
as_19 = f(f(d,e),e) == f(d,f(e,e))
as_20 = f(f(d,e),c) == f(d,f(e,c))
as_21 = f(f(d,e),d) == f(d,f(e,d))
as_22 = f(f(d,c),e) == f(c,f(c,c))
as_23 = f(f(d,c),c) == f(d,f(c,c))
as_24 = f(f(d,c),d) == f(d,f(c,d))
as_25 = f(f(d,d),e) == f(d,f(d,e))
as_26 = f(f(d,d),c) == f(d,f(d,c))
as_27 = f(f(d,d),d) == f(d,f(d,d))
#identity
#identity = ForAll(x, And(f(x,e)==x,f(e,x)==x))
ident_1 = And(f(e,e)==e,f(e,e)==e)
ident_2 = And(f(c,e)==c,f(e,c)==c)
ident_3 = And(f(d,e)==d,f(e,d)==d)
#inverse
#inverse = ForAll(x, And(f(x,g(x))==e,f(g(x),x)==e))
inv_1 = And(f(e,g(e))==e,f(g(e),e)==e)
inv_2 = And(f(c,g(c))==e,f(g(c),c)==e)
inv_3 = And(f(d,g(d))==e,f(g(d),d)==e)
#identity is unique
#unique = ForAll(x,And((f(x,c)==x),f(c,x)==x,Not(e=c)))
uniq_1 = And((f(e,c)==e),f(c,e)==e,Not(e==c))
uniq_2  = And((f(c,c)==c),f(c,c)==c,Not(e==c))
uniq_3  = And((f(d,c)==d),f(c,d)==d,Not(e==c))

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
solver.add(as_9)
solver.add(as_10)
solver.add(as_11)
solver.add(as_12)
solver.add(as_13)
solver.add(as_14)
solver.add(as_15)
solver.add(as_16)
solver.add(as_17)
solver.add(as_18)
solver.add(as_19)
solver.add(as_20)
solver.add(as_21)
solver.add(as_22)
solver.add(as_23)
solver.add(as_24)
solver.add(as_25)
solver.add(as_26)
solver.add(as_27)

solver.add(ident_1)
solver.add(ident_2)
solver.add(ident_3)

solver.add(inv_1)
solver.add(inv_2)
solver.add(inv_3)

solver.add(uniq_1)
solver.add(uniq_2)
solver.add(uniq_3)


if solver.check()== unsat:
    print('The obtained formula is unsatisfiable')
else:
    print('The obtained formula is satisfiable')