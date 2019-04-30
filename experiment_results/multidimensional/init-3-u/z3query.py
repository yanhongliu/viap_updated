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
	j9=Function('j9',IntSort(),IntSort())
	_n6=Int('_n6')
	j1=Int('j1')
	_x4=Int('_x4')
	_n5=Int('_n5')
	_x1=Const('_x1',arraySort)
	_x2=Int('_x2')
	_x3=Int('_x3')
	k14=Function('k14',IntSort(),IntSort(),IntSort())
	k18=Function('k18',IntSort(),IntSort())
	A1=Const('A1',arraySort)
	_N2=Function('_N2',IntSort(),IntSort())
	k1=Int('k1')
	k5=Function('k5',IntSort(),IntSort(),IntSort())
	C1=Int('C1')
	A=Const('A',arraySort)
	C=Int('C')
	i1=Int('i1')
	_N3=Const('_N3',IntSort())
	_N1=Function('_N1',IntSort(),IntSort(),IntSort())
	_N6=Const('_N6',IntSort())
	_N4=Function('_N4',IntSort(),IntSort(),IntSort())
	_N5=Function('_N5',IntSort(),IntSort())
	d3array5=Function('d3array5',arraySort,IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	d3array2=Function('d3array2',arraySort,IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	j18=Function('j18',IntSort(),IntSort())
	d3array1=Function('d3array1',arraySort,IntSort(),IntSort(),IntSort(),IntSort())
	k9=Function('k9',IntSort(),IntSort())
	d3array9=Function('d3array9',arraySort,IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	d3array14=Function('d3array14',arraySort,IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	d3array11=Function('d3array11',arraySort,IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	_n2=Int('_n2')
	_n3=Int('_n3')
	_n1=Int('_n1')
	d3array18=Function('d3array18',arraySort,IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	_n4=Int('_n4')
	n=Int('n')
	n1=Int('n1')
	d3array=Function('d3array',arraySort,IntSort(),IntSort(),IntSort(),IntSort())
	main=Int('main')
	_k1=Int('_k1')
	_k2=Int('_k2')
	_k3=Int('_k3')
	_k4=Int('_k4')
	_k6=Int('_k6')
	_k5=Int('_k5')
	_s=Solver()
	_s.add(ForAll([_n],Implies(_n>=0, _f(_n)==_n)))
	_s.set("timeout",50000)
	_s.add(A1 == A)
	_s.add(C1 == C)
	_s.add(n1 == n)
	_s.add(i1 == _N6)
	_s.add(k1 == k18(_N6))
	_s.add(j1 == j18(_N6))
	_s.add(ForAll([_x3,_x2,_x4],Implies(And(_x3>=0,And(_x2>=0,_x4>=0)),d3array1(A,_x2,_x3,_x4) == d3array18(A,_x2,_x3,_x4,_N6))))
	_s.add(ForAll([_n1,_n3,_n2],Implies(And(_n1>=0,And(_n3>=0,_n2>=0)),d3array2(A,_n3,_n2,_n1,_n1 + 1,_n2,_n3) == C)))
	_s.add(ForAll([_x3,_x2,_n3,_n2,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_n3>=0,And(_n2>=0,_x4>=0)))),d3array2(A,_x2,_x3,_x4,0,_n2,_n3) == d3array5(A,_x2,_x3,_x4,_n2,_n3))))
	_s.add(ForAll([_n3,_n2],Implies(And(_n3>=0,_n2>=0),_N1(_n2, _n3) >= n)))
	_s.add(ForAll([_n1,_n3,_n2],Implies(And(_n1 < _N1(_n2, _n3),And(_n1>=0,And(_n3>=0,_n2>=0))),_f(_n1) < n)))
	_s.add(ForAll([_n3,_n2],Implies(And(_n3>=0,_n2>=0),Or(_N1(_n2, _n3)==0,_N1(_n2, _n3) - 1 < n))))
	_s.add(ForAll([_n3,_n2],Implies(And(_n3>=0,_n2>=0),k5(_n2 + 1, _n3) == _N1(_n2, _n3))))
	_s.add(ForAll([_x3,_x2,_n3,_n2,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_n3>=0,And(_n2>=0,_x4>=0)))),d3array5(A,_x2,_x3,_x4,_n2 + 1,_n3) == d3array2(A,_x2,_x3,_x4,_N1(_n2,_n3),_n2,_n3))))
	_s.add(ForAll([_n3],k5(0, _n3) == 0))
	_s.add(ForAll([_x3,_x2,_n3,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_n3>=0,_x4>=0))),d3array5(A,_x2,_x3,_x4,0,_n3) == d3array9(A,_x2,_x3,_x4,_n3))))
	_s.add(ForAll([_n3],Implies(_n3>=0,_N2(_n3) >= n)))
	_s.add(ForAll([_n3,_n2],Implies(And(_n2 < _N2(_n3),And(_n3>=0,_n2>=0)),_f(_n2) < n)))
	_s.add(ForAll([_n3],Implies(_n3>=0,Or(_N2(_n3)==0,_N2(_n3) - 1 < n))))
	_s.add(ForAll([_n3],Implies(_n3>=0,k9(_n3 + 1) == k5(_N2(_n3), _n3))))
	_s.add(ForAll([_n3],Implies(_n3>=0,j9(_n3 + 1) == _N2(_n3))))
	_s.add(ForAll([_x3,_x2,_n3,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_n3>=0,_x4>=0))),d3array9(A,_x2,_x3,_x4,_n3 + 1) == d3array5(A,_x2,_x3,_x4,_N2(_n3),_n3))))
	_s.add(k9(0) == 0)
	_s.add(j9(0) == 0)
	_s.add(ForAll([_x3,_x2,_x4],Implies(And(_x3>=0,And(_x2>=0,_x4>=0)),d3array9(A,_x2,_x3,_x4,0) == d3array(A,_x2,_x3,_x4))))
	_s.add(_N3 >= n)
	_s.add(ForAll([_n3],Implies(And(_n3 < _N3,_n3>=0),_f(_n3) < n)))
	_s.add(Or(_N3==0,_N3 - 1 < n))
	_s.add(ForAll([_x3,_x2,_x4,_n5,_n4,_n6],Implies(And(_x3>=0,And(_x2>=0,And(_x4>=0,And(_n5>=0,And(_n4>=0,_n6>=0))))),d3array11(A,_x2,_x3,_x4,_n4 + 1,_n5,_n6) == d3array11(A,_x2,_x3,_x4,_n4,_n5,_n6))))
	_s.add(ForAll([_x3,_x2,_n6,_n5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_n6>=0,And(_n5>=0,_x4>=0)))),d3array11(A,_x2,_x3,_x4,0,_n5,_n6) == d3array14(A,_x2,_x3,_x4,_n5,_n6))))
	_s.add(ForAll([_n5,_n6],Implies(And(_n5>=0,_n6>=0),_N4(_n5, _n6) >= n)))
	_s.add(ForAll([_n5,_n4,_n6],Implies(And(_n4 < _N4(_n5, _n6),And(_n5>=0,And(_n4>=0,_n6>=0))),_f(_n4) < n)))
	_s.add(ForAll([_n5,_n6],Implies(And(_n5>=0,_n6>=0),Or(_N4(_n5, _n6)==0,_N4(_n5, _n6) - 1 < n))))
	_s.add(ForAll([_n5,_n6],Implies(And(_n5>=0,_n6>=0),k14(_n5 + 1, _n6) == _N4(_n5, _n6))))
	_s.add(ForAll([_x3,_x2,_n6,_n5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_n6>=0,And(_n5>=0,_x4>=0)))),d3array14(A,_x2,_x3,_x4,_n5 + 1,_n6) == d3array11(A,_x2,_x3,_x4,_N4(_n5,_n6),_n5,_n6))))
	_s.add(ForAll([_n6],k14(0, _n6) == 0))
	_s.add(ForAll([_x3,_x2,_n6,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_n6>=0,_x4>=0))),d3array14(A,_x2,_x3,_x4,0,_n6) == d3array18(A,_x2,_x3,_x4,_n6))))
	_s.add(ForAll([_n6],Implies(_n6>=0,_N5(_n6) >= n)))
	_s.add(ForAll([_n5,_n6],Implies(And(_n5 < _N5(_n6),And(_n5>=0,_n6>=0)),_f(_n5) < n)))
	_s.add(ForAll([_n6],Implies(_n6>=0,Or(_N5(_n6)==0,_N5(_n6) - 1 < n))))
	_s.add(ForAll([_n6],Implies(_n6>=0,k18(_n6 + 1) == k14(_N5(_n6), _n6))))
	_s.add(ForAll([_n6],Implies(_n6>=0,j18(_n6 + 1) == _N5(_n6))))
	_s.add(ForAll([_x3,_x2,_n6,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_n6>=0,_x4>=0))),d3array18(A,_x2,_x3,_x4,_n6 + 1) == d3array14(A,_x2,_x3,_x4,_N5(_n6),_n6))))
	_s.add(k18(0) == 0)
	_s.add(j18(0) == 0)
	_s.add(ForAll([_x3,_x2,_x4],Implies(And(_x3>=0,And(_x2>=0,_x4>=0)),d3array18(A,_x2,_x3,_x4,0) == d3array9(A,_x2,_x3,_x4,_N3))))
	_s.add(_N6 >= n)
	_s.add(ForAll([_n6],Implies(And(_n6 < _N6,_n6>=0),_f(_n6) < n)))
	_s.add(Or(_N6==0,_N6 - 1 < n))
	_s.add(ForAll([_n1,_n3,_n2],Implies(And(_n1>=0,And(_n3>=0,_n2>=0)),d3array2(A,_n3,_n2,_n1,_N1(_n2,_n3),_n2,_n3) == C)))
	_s.add(ForAll([_n1,_n3,_n2],Implies(And(_n1>=0,And(_n3>=0,_n2>=0)),d3array9(A,_n3,_n2,_n1,_N3) == C)))
	_s.add(ForAll([_n1,_n3,_n2],Implies(And(_n1>=0,And(_n3>=0,_n2>=0)),d3array5(A,_n3,_n2,_n1,_N2(_n3),_n3) == C)))
	_s.add(ForAll([_n5,_n6,_n1,_n3,_n2],Implies(And(_n5>=0,And(_n6>=0,And(_n1>=0,And(_n3>=0,_n2>=0)))),d3array11(A,_n3,_n2,_n1,_N4(_n5,_n6),_n5,_n6) == C)))
	_s.add(ForAll([_n1,_n3,_n2],Implies(And(_n1>=0,And(_n3>=0,_n2>=0)),d3array18(A,_n3,_n2,_n1,_N6) == C)))
	_s.add(ForAll([_n6,_n1,_n3,_n2],Implies(And(_n6>=0,And(_n1>=0,And(_n3>=0,_n2>=0))),d3array14(A,_n3,_n2,_n1,_N5(_n6),_n6) == C)))
	_s.add(ForAll([_n1,_n3,_n2],Implies(And(_n1>=0,And(_n3>=0,_n2>=0)),d3array2(A,_n3,_n2,_n1,_N1(_n2,_n3),_n2,_n3) == C)))
	_s.add(ForAll([_n1,_n3,_n2],Implies(And(_n1>=0,And(_n3>=0,_n2>=0)),d3array2(A,_n3,_n2,_n1,_N1(_n2,_n3),_n2,_n3) == C)))
	_s.add(ForAll([_n1,_n3,_n2],Implies(And(_n1>=0,And(_n3>=0,_n2>=0)),d3array9(A,_n3,_n2,_n1,_N3) == C)))
	_s.add(ForAll([_n1,_n3,_n2],Implies(And(_n1>=0,And(_n3>=0,_n2>=0)),d3array9(A,_n3,_n2,_n1,_N3) == C)))
	_s.add(ForAll([_n1,_n3,_n2],Implies(And(_n1>=0,And(_n3>=0,_n2>=0)),d3array5(A,_n3,_n2,_n1,_N2(_n3),_n3) == C)))
	_s.add(ForAll([_n1,_n3,_n2],Implies(And(_n1>=0,And(_n3>=0,_n2>=0)),d3array5(A,_n3,_n2,_n1,_N2(_n3),_n3) == C)))
	_s.add(ForAll([_n5,_n6,_n1,_n3,_n2],Implies(And(_n5>=0,And(_n6>=0,And(_n1>=0,And(_n3>=0,_n2>=0)))),d3array11(A,_n3,_n2,_n1,_N4(_n5,_n6),_n5,_n6) == C)))
	_s.add(ForAll([_n5,_n6,_n1,_n3,_n2],Implies(And(_n5>=0,And(_n6>=0,And(_n1>=0,And(_n3>=0,_n2>=0)))),d3array11(A,_n3,_n2,_n1,_N4(_n5,_n6),_n5,_n6) == C)))
	_s.add(ForAll([_n1,_n3,_n2],Implies(And(_n1>=0,And(_n3>=0,_n2>=0)),d3array18(A,_n3,_n2,_n1,_N6) == C)))
	_s.add(ForAll([_n1,_n3,_n2],Implies(And(_n1>=0,And(_n3>=0,_n2>=0)),d3array18(A,_n3,_n2,_n1,_N6) == C)))
	_s.add(ForAll([_n6,_n1,_n3,_n2],Implies(And(_n6>=0,And(_n1>=0,And(_n3>=0,_n2>=0))),d3array14(A,_n3,_n2,_n1,_N5(_n6),_n6) == C)))
	_s.add(ForAll([_n6,_n1,_n3,_n2],Implies(And(_n6>=0,And(_n1>=0,And(_n3>=0,_n2>=0))),d3array14(A,_n3,_n2,_n1,_N5(_n6),_n6) == C)))
	_s.add(A1 == A)
	_s.add(C1 == C)
	_s.add(n1 == n)
	_s.add(_k1>=0)
	_s.add(_k4>=0)
	_s.add(ForAll([_n2 ,_n3],_N1(_n2, _n3)>=0))
	_s.add(ForAll([_n3],_N2(_n3)>=0))
	_s.add(_N3>=0)
	_s.add(ForAll([_n5 ,_n6],_N4(_n5, _n6)>=0))
	_s.add(ForAll([_n6],_N5(_n6)>=0))
	_s.add(_N6>=0)
	_s.add(Not(ForAll([_n5,_n4,_n6],Implies(And(_n5<_N5(_n6),And(_n4<_N4(_n5, _n6),And(_n6<_N6,And(_n5>=0,And(_n4>=0,_n6>=0))))),((d3array18(A,_n6,_n5,_n4,_N6))==(C))))))

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
