import sys
import os
currentdirectory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(currentdirectory+"/packages/setuptools/")
currentdirectory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(currentdirectory+"/packages/z3/python/")
from z3 import *
init(currentdirectory+"/packages/z3")
set_param(proof=True)

try:
	_p1=Int('_p1')
	_p2=Int('_p2')
	_n=Int('_n')
	_bool=Int('_bool')
	arraySort = DeclareSort('arraySort')
	_f=Function('_f',IntSort(),IntSort())
	_ToReal=Function('_ToReal',RealSort(),IntSort())
	_ToInt=Function('_ToInt',IntSort(),RealSort())
	d1array14=Function('d1array14',arraySort,IntSort(),IntSort(),IntSort())
	_N5=Const('_N5',IntSort())
	d1array12=Function('d1array12',arraySort,IntSort(),IntSort(),IntSort())
	d1array10=Function('d1array10',arraySort,IntSort(),IntSort(),IntSort())
	_n5=Int('_n5')
	_x1=Const('_x1',arraySort)
	_x2=Int('_x2')
	__VERIFIER_nondet_int2=Function('__VERIFIER_nondet_int2',IntSort(),IntSort())
	a1_var=Const('a1_var',arraySort)
	a6_var1=Const('a6_var1',arraySort)
	a5_var1=Const('a5_var1',arraySort)
	a6_var=Const('a6_var',arraySort)
	_N2=Const('_N2',IntSort())
	a5_var=Const('a5_var',arraySort)
	main=Int('main')
	d1array=Function('d1array',arraySort,IntSort(),IntSort())
	a3_var=Const('a3_var',arraySort)
	i1=Int('i1')
	_N3=Const('_N3',IntSort())
	_N1=Const('_N1',IntSort())
	_N6=Const('_N6',IntSort())
	a4_var1=Const('a4_var1',arraySort)
	_N4=Const('_N4',IntSort())
	_N7=Const('_N7',IntSort())
	a1=Int('a1')
	a2_var=Const('a2_var',arraySort)
	d1array8=Function('d1array8',arraySort,IntSort(),IntSort(),IntSort())
	a1_var1=Const('a1_var1',arraySort)
	d1array4=Function('d1array4',arraySort,IntSort(),IntSort(),IntSort())
	d1array6=Function('d1array6',arraySort,IntSort(),IntSort(),IntSort())
	x1=Int('x1')
	d1array1=Function('d1array1',arraySort,IntSort(),IntSort())
	d1array2=Function('d1array2',arraySort,IntSort(),IntSort(),IntSort())
	_n2=Int('_n2')
	_n3=Int('_n3')
	_n1=Int('_n1')
	_n6=Int('_n6')
	_n7=Int('_n7')
	_n4=Int('_n4')
	a4_var=Const('a4_var',arraySort)
	a3_var1=Const('a3_var1',arraySort)
	a2_var1=Const('a2_var1',arraySort)
	_k1=Int('_k1')
	_k2=Int('_k2')
	_k3=Int('_k3')
	_k4=Int('_k4')
	_k5=Int('_k5')
	_k6=Int('_k6')
	_k7=Int('_k7')
	_s=Solver()
	_s.add(ForAll([_n],Implies(_n>=0, _f(_n)==_n)))
	_s.set("timeout",50000)
	_s.add(a3_var1 == a3_var)
	_s.add(a1_var1 == a1_var)
	_s.add(a4_var1 == a4_var)
	_s.add(a2_var1 == a2_var)
	_s.add(a5_var1 == a5_var)
	_s.add(a6_var1 == a6_var)
	_s.add(a1 == _N1)
	_s.add(i1 == _N6)
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array1(a1_var,_x2) == d1array14(a1_var,_x2,_N7))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array1(a6_var,_x2) == d1array14(a6_var,_x2,_N7))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array1(a5_var,_x2) == d1array14(a5_var,_x2,_N7))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array1(a3_var,_x2) == d1array14(a3_var,_x2,_N7))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array1(a2_var,_x2) == d1array14(a2_var,_x2,_N7))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array1(a4_var,_x2) == d1array14(a4_var,_x2,_N7))))
	_s.add(main == 0)
	_s.add(x1 == _N7)
	_s.add(ForAll([_n1],Implies(_n1>=0,d1array2(a1_var,_n1,_n1 + 1) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_x2,_n1],Implies(And(_x2>=0,_n1>=0),d1array2(a6_var,_x2,_n1 + 1) == d1array2(a6_var,_x2,_n1))))
	_s.add(ForAll([_x2,_n1],Implies(And(_x2>=0,_n1>=0),d1array2(a5_var,_x2,_n1 + 1) == d1array2(a5_var,_x2,_n1))))
	_s.add(ForAll([_x2,_n1],Implies(And(_x2>=0,_n1>=0),d1array2(a3_var,_x2,_n1 + 1) == d1array2(a3_var,_x2,_n1))))
	_s.add(ForAll([_x2,_n1],Implies(And(_x2>=0,_n1>=0),d1array2(a2_var,_x2,_n1 + 1) == d1array2(a2_var,_x2,_n1))))
	_s.add(ForAll([_x2,_n1],Implies(And(_x2>=0,_n1>=0),d1array2(a4_var,_x2,_n1 + 1) == d1array2(a4_var,_x2,_n1))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array2(a1_var,_x2,0) == d1array(a1_var,_x2))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array2(a6_var,_x2,0) == d1array(a6_var,_x2))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array2(a5_var,_x2,0) == d1array(a5_var,_x2))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array2(a3_var,_x2,0) == d1array(a3_var,_x2))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array2(a2_var,_x2,0) == d1array(a2_var,_x2))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array2(a4_var,_x2,0) == d1array(a4_var,_x2))))
	_s.add(_N1 >= 100000)
	_s.add(ForAll([_n1],Implies(And(_n1 < _N1,_n1>=0),_f(_n1) < 100000)))
	_s.add(Or(_N1==0,_N1 - 1 < 100000))
	_s.add(ForAll([_x2,_n2],Implies(And(_x2>=0,_n2>=0),d1array4(a1_var,_x2,_n2 + 1) == d1array4(a1_var,_x2,_n2))))
	_s.add(ForAll([_x2,_n2],Implies(And(_x2>=0,_n2>=0),d1array4(a6_var,_x2,_n2 + 1) == d1array4(a6_var,_x2,_n2))))
	_s.add(ForAll([_x2,_n2],Implies(And(_x2>=0,_n2>=0),d1array4(a5_var,_x2,_n2 + 1) == d1array4(a5_var,_x2,_n2))))
	_s.add(ForAll([_x2,_n2],Implies(And(_x2>=0,_n2>=0),d1array4(a3_var,_x2,_n2 + 1) == d1array4(a3_var,_x2,_n2))))
	_s.add(ForAll([_n2],Implies(_n2>=0,d1array4(a2_var,_n2,_n2 + 1) == d1array4(a1_var,_n2,_n2))))
	_s.add(ForAll([_x2,_n2],Implies(And(_x2>=0,_n2>=0),d1array4(a4_var,_x2,_n2 + 1) == d1array4(a4_var,_x2,_n2))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array4(a1_var,_x2,0) == d1array2(a1_var,_x2,_N1))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array4(a6_var,_x2,0) == d1array2(a6_var,_x2,_N1))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array4(a5_var,_x2,0) == d1array2(a5_var,_x2,_N1))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array4(a3_var,_x2,0) == d1array2(a3_var,_x2,_N1))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array4(a2_var,_x2,0) == d1array2(a2_var,_x2,_N1))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array4(a4_var,_x2,0) == d1array2(a4_var,_x2,_N1))))
	_s.add(_N2 >= 100000)
	_s.add(ForAll([_n2],Implies(And(_n2 < _N2,_n2>=0),_f(_n2) < 100000)))
	_s.add(Or(_N2==0,_N2 - 1 < 100000))
	_s.add(ForAll([_x2,_n3],Implies(And(_x2>=0,_n3>=0),d1array6(a1_var,_x2,_n3 + 1) == d1array6(a1_var,_x2,_n3))))
	_s.add(ForAll([_x2,_n3],Implies(And(_x2>=0,_n3>=0),d1array6(a6_var,_x2,_n3 + 1) == d1array6(a6_var,_x2,_n3))))
	_s.add(ForAll([_x2,_n3],Implies(And(_x2>=0,_n3>=0),d1array6(a5_var,_x2,_n3 + 1) == d1array6(a5_var,_x2,_n3))))
	_s.add(ForAll([_n3],Implies(_n3>=0,d1array6(a3_var,_n3,_n3 + 1) == d1array6(a2_var,_n3,_n3))))
	_s.add(ForAll([_x2,_n3],Implies(And(_x2>=0,_n3>=0),d1array6(a2_var,_x2,_n3 + 1) == d1array6(a2_var,_x2,_n3))))
	_s.add(ForAll([_x2,_n3],Implies(And(_x2>=0,_n3>=0),d1array6(a4_var,_x2,_n3 + 1) == d1array6(a4_var,_x2,_n3))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array6(a1_var,_x2,0) == d1array4(a1_var,_x2,_N2))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array6(a6_var,_x2,0) == d1array4(a6_var,_x2,_N2))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array6(a5_var,_x2,0) == d1array4(a5_var,_x2,_N2))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array6(a3_var,_x2,0) == d1array4(a3_var,_x2,_N2))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array6(a2_var,_x2,0) == d1array4(a2_var,_x2,_N2))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array6(a4_var,_x2,0) == d1array4(a4_var,_x2,_N2))))
	_s.add(_N3 >= 100000)
	_s.add(ForAll([_n3],Implies(And(_n3 < _N3,_n3>=0),_f(_n3) < 100000)))
	_s.add(Or(_N3==0,_N3 - 1 < 100000))
	_s.add(ForAll([_x2,_n4],Implies(And(_x2>=0,_n4>=0),d1array8(a1_var,_x2,_n4 + 1) == d1array8(a1_var,_x2,_n4))))
	_s.add(ForAll([_x2,_n4],Implies(And(_x2>=0,_n4>=0),d1array8(a6_var,_x2,_n4 + 1) == d1array8(a6_var,_x2,_n4))))
	_s.add(ForAll([_x2,_n4],Implies(And(_x2>=0,_n4>=0),d1array8(a5_var,_x2,_n4 + 1) == d1array8(a5_var,_x2,_n4))))
	_s.add(ForAll([_x2,_n4],Implies(And(_x2>=0,_n4>=0),d1array8(a3_var,_x2,_n4 + 1) == d1array8(a3_var,_x2,_n4))))
	_s.add(ForAll([_x2,_n4],Implies(And(_x2>=0,_n4>=0),d1array8(a2_var,_x2,_n4 + 1) == d1array8(a2_var,_x2,_n4))))
	_s.add(ForAll([_n4],Implies(_n4>=0,d1array8(a4_var,_n4,_n4 + 1) == d1array8(a3_var,_n4,_n4))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array8(a1_var,_x2,0) == d1array6(a1_var,_x2,_N3))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array8(a6_var,_x2,0) == d1array6(a6_var,_x2,_N3))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array8(a5_var,_x2,0) == d1array6(a5_var,_x2,_N3))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array8(a3_var,_x2,0) == d1array6(a3_var,_x2,_N3))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array8(a2_var,_x2,0) == d1array6(a2_var,_x2,_N3))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array8(a4_var,_x2,0) == d1array6(a4_var,_x2,_N3))))
	_s.add(_N4 >= 100000)
	_s.add(ForAll([_n4],Implies(And(_n4 < _N4,_n4>=0),_f(_n4) < 100000)))
	_s.add(Or(_N4==0,_N4 - 1 < 100000))
	_s.add(ForAll([_n5,_x2],Implies(And(_n5>=0,_x2>=0),d1array10(a1_var,_x2,_n5 + 1) == d1array10(a1_var,_x2,_n5))))
	_s.add(ForAll([_n5,_x2],Implies(And(_n5>=0,_x2>=0),d1array10(a6_var,_x2,_n5 + 1) == d1array10(a6_var,_x2,_n5))))
	_s.add(ForAll([_n5],Implies(_n5>=0,d1array10(a5_var,_n5,_n5 + 1) == d1array10(a4_var,_n5,_n5))))
	_s.add(ForAll([_n5,_x2],Implies(And(_n5>=0,_x2>=0),d1array10(a3_var,_x2,_n5 + 1) == d1array10(a3_var,_x2,_n5))))
	_s.add(ForAll([_n5,_x2],Implies(And(_n5>=0,_x2>=0),d1array10(a2_var,_x2,_n5 + 1) == d1array10(a2_var,_x2,_n5))))
	_s.add(ForAll([_n5,_x2],Implies(And(_n5>=0,_x2>=0),d1array10(a4_var,_x2,_n5 + 1) == d1array10(a4_var,_x2,_n5))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array10(a1_var,_x2,0) == d1array8(a1_var,_x2,_N4))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array10(a6_var,_x2,0) == d1array8(a6_var,_x2,_N4))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array10(a5_var,_x2,0) == d1array8(a5_var,_x2,_N4))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array10(a3_var,_x2,0) == d1array8(a3_var,_x2,_N4))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array10(a2_var,_x2,0) == d1array8(a2_var,_x2,_N4))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array10(a4_var,_x2,0) == d1array8(a4_var,_x2,_N4))))
	_s.add(_N5 >= 100000)
	_s.add(ForAll([_n5],Implies(And(_n5 < _N5,_n5>=0),_f(_n5) < 100000)))
	_s.add(Or(_N5==0,_N5 - 1 < 100000))
	_s.add(ForAll([_x2,_n6],Implies(And(_x2>=0,_n6>=0),d1array12(a1_var,_x2,_n6 + 1) == d1array12(a1_var,_x2,_n6))))
	_s.add(ForAll([_n6],Implies(_n6>=0,d1array12(a6_var,_n6,_n6 + 1) == d1array12(a5_var,_n6,_n6))))
	_s.add(ForAll([_x2,_n6],Implies(And(_x2>=0,_n6>=0),d1array12(a5_var,_x2,_n6 + 1) == d1array12(a5_var,_x2,_n6))))
	_s.add(ForAll([_x2,_n6],Implies(And(_x2>=0,_n6>=0),d1array12(a3_var,_x2,_n6 + 1) == d1array12(a3_var,_x2,_n6))))
	_s.add(ForAll([_x2,_n6],Implies(And(_x2>=0,_n6>=0),d1array12(a2_var,_x2,_n6 + 1) == d1array12(a2_var,_x2,_n6))))
	_s.add(ForAll([_x2,_n6],Implies(And(_x2>=0,_n6>=0),d1array12(a4_var,_x2,_n6 + 1) == d1array12(a4_var,_x2,_n6))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array12(a1_var,_x2,0) == d1array10(a1_var,_x2,_N5))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array12(a6_var,_x2,0) == d1array10(a6_var,_x2,_N5))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array12(a5_var,_x2,0) == d1array10(a5_var,_x2,_N5))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array12(a3_var,_x2,0) == d1array10(a3_var,_x2,_N5))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array12(a2_var,_x2,0) == d1array10(a2_var,_x2,_N5))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array12(a4_var,_x2,0) == d1array10(a4_var,_x2,_N5))))
	_s.add(_N6 >= 100000)
	_s.add(ForAll([_n6],Implies(And(_n6 < _N6,_n6>=0),_f(_n6) < 100000)))
	_s.add(Or(_N6==0,_N6 - 1 < 100000))
	_s.add(ForAll([_x2,_n7],Implies(And(_x2>=0,_n7>=0),d1array14(a1_var,_x2,_n7 + 1) == d1array14(a1_var,_x2,_n7))))
	_s.add(ForAll([_x2,_n7],Implies(And(_x2>=0,_n7>=0),d1array14(a6_var,_x2,_n7 + 1) == d1array14(a6_var,_x2,_n7))))
	_s.add(ForAll([_x2,_n7],Implies(And(_x2>=0,_n7>=0),d1array14(a5_var,_x2,_n7 + 1) == d1array14(a5_var,_x2,_n7))))
	_s.add(ForAll([_x2,_n7],Implies(And(_x2>=0,_n7>=0),d1array14(a3_var,_x2,_n7 + 1) == d1array14(a3_var,_x2,_n7))))
	_s.add(ForAll([_x2,_n7],Implies(And(_x2>=0,_n7>=0),d1array14(a2_var,_x2,_n7 + 1) == d1array14(a2_var,_x2,_n7))))
	_s.add(ForAll([_x2,_n7],Implies(And(_x2>=0,_n7>=0),d1array14(a4_var,_x2,_n7 + 1) == d1array14(a4_var,_x2,_n7))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array14(a1_var,_x2,0) == d1array12(a1_var,_x2,_N6))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array14(a6_var,_x2,0) == d1array12(a6_var,_x2,_N6))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array14(a5_var,_x2,0) == d1array12(a5_var,_x2,_N6))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array14(a3_var,_x2,0) == d1array12(a3_var,_x2,_N6))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array14(a2_var,_x2,0) == d1array12(a2_var,_x2,_N6))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array14(a4_var,_x2,0) == d1array12(a4_var,_x2,_N6))))
	_s.add(_N7 >= 100000)
	_s.add(ForAll([_n7],Implies(And(_n7 < _N7,_n7>=0),_f(_n7) < 100000)))
	_s.add(Or(_N7==0,_N7 - 1 < 100000))
	_s.add(ForAll([_n1],Implies(_n1>=0,d1array2(a1_var,_n1,_N1) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array2(a6_var,_x2,_N1) == d1array(a6_var,_x2))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array2(a5_var,_x2,_N1) == d1array(a5_var,_x2))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array2(a3_var,_x2,_N1) == d1array(a3_var,_x2))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array2(a2_var,_x2,_N1) == d1array(a2_var,_x2))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array2(a4_var,_x2,_N1) == d1array(a4_var,_x2))))
	_s.add(ForAll([_n1],Implies(_n1>=0,d1array4(a1_var,_n1,_N2) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array4(a6_var,_x2,_N2) == d1array(a6_var,_x2))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array4(a5_var,_x2,_N2) == d1array(a5_var,_x2))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array4(a3_var,_x2,_N2) == d1array(a3_var,_x2))))
	_s.add(ForAll([_n1,_n2],Implies(And(_n1>=0,_n2>=0),d1array4(a2_var,_n2,_N2) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array4(a4_var,_x2,_N2) == d1array(a4_var,_x2))))
	_s.add(ForAll([_n1],Implies(_n1>=0,d1array6(a1_var,_n1,_N3) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array6(a6_var,_x2,_N3) == d1array(a6_var,_x2))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array6(a5_var,_x2,_N3) == d1array(a5_var,_x2))))
	_s.add(ForAll([_n1,_n3],Implies(And(_n1>=0,_n3>=0),d1array6(a3_var,_n3,_N3) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1,_n2],Implies(And(_n1>=0,_n2>=0),d1array6(a2_var,_n2,_N3) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array6(a4_var,_x2,_N3) == d1array(a4_var,_x2))))
	_s.add(ForAll([_n1],Implies(_n1>=0,d1array8(a1_var,_n1,_N4) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array8(a6_var,_x2,_N4) == d1array(a6_var,_x2))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array8(a5_var,_x2,_N4) == d1array(a5_var,_x2))))
	_s.add(ForAll([_n1,_n3],Implies(And(_n1>=0,_n3>=0),d1array8(a3_var,_n3,_N4) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1,_n2],Implies(And(_n1>=0,_n2>=0),d1array8(a2_var,_n2,_N4) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n4,_n1],Implies(And(_n4>=0,_n1>=0),d1array8(a4_var,_n4,_N4) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1],Implies(_n1>=0,d1array10(a1_var,_n1,_N5) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array10(a6_var,_x2,_N5) == d1array(a6_var,_x2))))
	_s.add(ForAll([_n5,_n1],Implies(And(_n5>=0,_n1>=0),d1array10(a5_var,_n5,_N5) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1,_n3],Implies(And(_n1>=0,_n3>=0),d1array10(a3_var,_n3,_N5) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1,_n2],Implies(And(_n1>=0,_n2>=0),d1array10(a2_var,_n2,_N5) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n4,_n1],Implies(And(_n4>=0,_n1>=0),d1array10(a4_var,_n4,_N5) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1],Implies(_n1>=0,d1array12(a1_var,_n1,_N6) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n6,_n1],Implies(And(_n6>=0,_n1>=0),d1array12(a6_var,_n6,_N6) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n5,_n1],Implies(And(_n5>=0,_n1>=0),d1array12(a5_var,_n5,_N6) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1,_n3],Implies(And(_n1>=0,_n3>=0),d1array12(a3_var,_n3,_N6) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1,_n2],Implies(And(_n1>=0,_n2>=0),d1array12(a2_var,_n2,_N6) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n4,_n1],Implies(And(_n4>=0,_n1>=0),d1array12(a4_var,_n4,_N6) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1],Implies(_n1>=0,d1array14(a1_var,_n1,_N7) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n6,_n1],Implies(And(_n6>=0,_n1>=0),d1array14(a6_var,_n6,_N7) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n5,_n1],Implies(And(_n5>=0,_n1>=0),d1array14(a5_var,_n5,_N7) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1,_n3],Implies(And(_n1>=0,_n3>=0),d1array14(a3_var,_n3,_N7) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1,_n2],Implies(And(_n1>=0,_n2>=0),d1array14(a2_var,_n2,_N7) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n4,_n1],Implies(And(_n4>=0,_n1>=0),d1array14(a4_var,_n4,_N7) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1],Implies(_n1>=0,d1array2(a1_var,_n1,_N1) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1],Implies(_n1>=0,d1array2(a1_var,_n1,_N1) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array2(a6_var,_x2,_N1) == d1array(a6_var,_x2))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array2(a6_var,_x2,_N1) == d1array2(a6_var,_x2,_N1))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array2(a5_var,_x2,_N1) == d1array(a5_var,_x2))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array2(a5_var,_x2,_N1) == d1array2(a5_var,_x2,_N1))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array2(a3_var,_x2,_N1) == d1array(a3_var,_x2))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array2(a3_var,_x2,_N1) == d1array2(a3_var,_x2,_N1))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array2(a2_var,_x2,_N1) == d1array(a2_var,_x2))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array2(a2_var,_x2,_N1) == d1array2(a2_var,_x2,_N1))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array2(a4_var,_x2,_N1) == d1array(a4_var,_x2))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array2(a4_var,_x2,_N1) == d1array2(a4_var,_x2,_N1))))
	_s.add(ForAll([_n1],Implies(_n1>=0,d1array4(a1_var,_n1,_N2) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1],Implies(_n1>=0,d1array4(a1_var,_n1,_N2) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array4(a6_var,_x2,_N2) == d1array(a6_var,_x2))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array4(a6_var,_x2,_N2) == d1array4(a6_var,_x2,_N2))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array4(a5_var,_x2,_N2) == d1array(a5_var,_x2))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array4(a5_var,_x2,_N2) == d1array4(a5_var,_x2,_N2))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array4(a3_var,_x2,_N2) == d1array(a3_var,_x2))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array4(a3_var,_x2,_N2) == d1array4(a3_var,_x2,_N2))))
	_s.add(ForAll([_n1,_n2],Implies(And(_n1>=0,_n2>=0),d1array4(a2_var,_n2,_N2) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1,_n2],Implies(And(_n1>=0,_n2>=0),d1array4(a2_var,_n2,_N2) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array4(a4_var,_x2,_N2) == d1array(a4_var,_x2))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array4(a4_var,_x2,_N2) == d1array4(a4_var,_x2,_N2))))
	_s.add(ForAll([_n1],Implies(_n1>=0,d1array6(a1_var,_n1,_N3) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1],Implies(_n1>=0,d1array6(a1_var,_n1,_N3) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array6(a6_var,_x2,_N3) == d1array(a6_var,_x2))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array6(a6_var,_x2,_N3) == d1array6(a6_var,_x2,_N3))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array6(a5_var,_x2,_N3) == d1array(a5_var,_x2))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array6(a5_var,_x2,_N3) == d1array6(a5_var,_x2,_N3))))
	_s.add(ForAll([_n1,_n3],Implies(And(_n1>=0,_n3>=0),d1array6(a3_var,_n3,_N3) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1,_n3],Implies(And(_n1>=0,_n3>=0),d1array6(a3_var,_n3,_N3) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1,_n2],Implies(And(_n1>=0,_n2>=0),d1array6(a2_var,_n2,_N3) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1,_n2],Implies(And(_n1>=0,_n2>=0),d1array6(a2_var,_n2,_N3) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array6(a4_var,_x2,_N3) == d1array(a4_var,_x2))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array6(a4_var,_x2,_N3) == d1array6(a4_var,_x2,_N3))))
	_s.add(ForAll([_n1],Implies(_n1>=0,d1array8(a1_var,_n1,_N4) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1],Implies(_n1>=0,d1array8(a1_var,_n1,_N4) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array8(a6_var,_x2,_N4) == d1array(a6_var,_x2))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array8(a6_var,_x2,_N4) == d1array8(a6_var,_x2,_N4))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array8(a5_var,_x2,_N4) == d1array(a5_var,_x2))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array8(a5_var,_x2,_N4) == d1array8(a5_var,_x2,_N4))))
	_s.add(ForAll([_n1,_n3],Implies(And(_n1>=0,_n3>=0),d1array8(a3_var,_n3,_N4) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1,_n3],Implies(And(_n1>=0,_n3>=0),d1array8(a3_var,_n3,_N4) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1,_n2],Implies(And(_n1>=0,_n2>=0),d1array8(a2_var,_n2,_N4) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1,_n2],Implies(And(_n1>=0,_n2>=0),d1array8(a2_var,_n2,_N4) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n4,_n1],Implies(And(_n4>=0,_n1>=0),d1array8(a4_var,_n4,_N4) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n4,_n1],Implies(And(_n4>=0,_n1>=0),d1array8(a4_var,_n4,_N4) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1],Implies(_n1>=0,d1array10(a1_var,_n1,_N5) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1],Implies(_n1>=0,d1array10(a1_var,_n1,_N5) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array10(a6_var,_x2,_N5) == d1array(a6_var,_x2))))
	_s.add(ForAll([_x2],Implies(_x2>=0,d1array10(a6_var,_x2,_N5) == d1array10(a6_var,_x2,_N5))))
	_s.add(ForAll([_n5,_n1],Implies(And(_n5>=0,_n1>=0),d1array10(a5_var,_n5,_N5) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n5,_n1],Implies(And(_n5>=0,_n1>=0),d1array10(a5_var,_n5,_N5) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1,_n3],Implies(And(_n1>=0,_n3>=0),d1array10(a3_var,_n3,_N5) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1,_n3],Implies(And(_n1>=0,_n3>=0),d1array10(a3_var,_n3,_N5) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1,_n2],Implies(And(_n1>=0,_n2>=0),d1array10(a2_var,_n2,_N5) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1,_n2],Implies(And(_n1>=0,_n2>=0),d1array10(a2_var,_n2,_N5) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n4,_n1],Implies(And(_n4>=0,_n1>=0),d1array10(a4_var,_n4,_N5) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n4,_n1],Implies(And(_n4>=0,_n1>=0),d1array10(a4_var,_n4,_N5) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1],Implies(_n1>=0,d1array12(a1_var,_n1,_N6) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1],Implies(_n1>=0,d1array12(a1_var,_n1,_N6) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n6,_n1],Implies(And(_n6>=0,_n1>=0),d1array12(a6_var,_n6,_N6) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n6,_n1],Implies(And(_n6>=0,_n1>=0),d1array12(a6_var,_n6,_N6) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n5,_n1],Implies(And(_n5>=0,_n1>=0),d1array12(a5_var,_n5,_N6) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n5,_n1],Implies(And(_n5>=0,_n1>=0),d1array12(a5_var,_n5,_N6) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1,_n3],Implies(And(_n1>=0,_n3>=0),d1array12(a3_var,_n3,_N6) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1,_n3],Implies(And(_n1>=0,_n3>=0),d1array12(a3_var,_n3,_N6) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1,_n2],Implies(And(_n1>=0,_n2>=0),d1array12(a2_var,_n2,_N6) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1,_n2],Implies(And(_n1>=0,_n2>=0),d1array12(a2_var,_n2,_N6) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n4,_n1],Implies(And(_n4>=0,_n1>=0),d1array12(a4_var,_n4,_N6) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n4,_n1],Implies(And(_n4>=0,_n1>=0),d1array12(a4_var,_n4,_N6) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1],Implies(_n1>=0,d1array14(a1_var,_n1,_N7) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1],Implies(_n1>=0,d1array14(a1_var,_n1,_N7) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n6,_n1],Implies(And(_n6>=0,_n1>=0),d1array14(a6_var,_n6,_N7) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n6,_n1],Implies(And(_n6>=0,_n1>=0),d1array14(a6_var,_n6,_N7) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n5,_n1],Implies(And(_n5>=0,_n1>=0),d1array14(a5_var,_n5,_N7) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n5,_n1],Implies(And(_n5>=0,_n1>=0),d1array14(a5_var,_n5,_N7) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1,_n3],Implies(And(_n1>=0,_n3>=0),d1array14(a3_var,_n3,_N7) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1,_n3],Implies(And(_n1>=0,_n3>=0),d1array14(a3_var,_n3,_N7) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1,_n2],Implies(And(_n1>=0,_n2>=0),d1array14(a2_var,_n2,_N7) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n1,_n2],Implies(And(_n1>=0,_n2>=0),d1array14(a2_var,_n2,_N7) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n4,_n1],Implies(And(_n4>=0,_n1>=0),d1array14(a4_var,_n4,_N7) == __VERIFIER_nondet_int2(_n1))))
	_s.add(ForAll([_n4,_n1],Implies(And(_n4>=0,_n1>=0),d1array14(a4_var,_n4,_N7) == __VERIFIER_nondet_int2(_n1))))
	_s.add(a3_var1 == a3_var)
	_s.add(a1_var1 == a1_var)
	_s.add(a4_var1 == a4_var)
	_s.add(a2_var1 == a2_var)
	_s.add(a5_var1 == a5_var)
	_s.add(a6_var1 == a6_var)
	_s.add(_k1>=0)
	_s.add(_k2>=0)
	_s.add(_k3>=0)
	_s.add(_k4>=0)
	_s.add(_k5>=0)
	_s.add(_k6>=0)
	_s.add(_k7>=0)
	_s.add(_N1>=0)
	_s.add(_N2>=0)
	_s.add(_N3>=0)
	_s.add(_N4>=0)
	_s.add(_N5>=0)
	_s.add(_N6>=0)
	_s.add(_N7>=0)
	_s.add(Not(ForAll([_n7],Implies(And(_n7<_N7,_n7>=0),((d1array14(a1_var,_n7,_N7))==(d1array14(a6_var,_n7,_N7)))))))

except Exception as e:
	print "Error(Z3Query)"
	file = open('j2llogs.logs', 'a')

	file.write(str(e))

	file.close()

	sys.exit(1)

try:
	result=_s.check()
	if sat==result:
		print "Counter Example"
		print _s.model()
	elif unsat==result:
		result
		try:
			if os.path.isfile('j2llogs.logs'):
				file = open('j2llogs.logs', 'a')
				file.write("\n**************\nProof Details\n**************\n"+str(_s.proof().children())+"\n")
				file.close()
			else:
				file = open('j2llogs.logs', 'w')
				file.write("\n**************\nProof Details\n**************\n"+str(_s.proof().children())+"\n")
				file.close()
		except Exception as e:
			file = open('j2llogs.logs', 'a')
			file.write("\n**************\nProof Details\n**************\n"+"Error"+"\n")
			file.close()
		print "Successfully Proved"
	else:
		print "Failed To Prove"
except Exception as e:
	print "Error(Z3Query)"
	file = open('j2llogs.logs', 'a')

	file.write(str(e))

	file.close()
