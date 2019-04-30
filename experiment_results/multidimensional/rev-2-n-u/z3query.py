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
	j5=Function('j5',IntSort(),IntSort())
	j1=Int('j1')
	_x1=Const('_x1',arraySort)
	_x2=Int('_x2')
	_x3=Int('_x3')
	d2array2=Function('d2array2',arraySort,IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	d2array1=Function('d2array1',arraySort,IntSort(),IntSort(),IntSort())
	d2array7=Function('d2array7',arraySort,IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	d2array5=Function('d2array5',arraySort,IntSort(),IntSort(),IntSort(),IntSort())
	A1=Const('A1',arraySort)
	_N2=Const('_N2',IntSort())
	m1=Int('m1')
	A=Const('A',arraySort)
	B=Const('B',arraySort)
	d2array10=Function('d2array10',arraySort,IntSort(),IntSort(),IntSort(),IntSort())
	i1=Int('i1')
	_N3=Function('_N3',IntSort(),IntSort())
	_N1=Function('_N1',IntSort(),IntSort())
	_N4=Const('_N4',IntSort())
	d2array=Function('d2array',arraySort,IntSort(),IntSort(),IntSort())
	j10=Function('j10',IntSort(),IntSort())
	p1=Int('p1')
	_n2=Int('_n2')
	_n3=Int('_n3')
	_n1=Int('_n1')
	m=Int('m')
	_n4=Int('_n4')
	n=Int('n')
	p=Int('p')
	B1=Const('B1',arraySort)
	n1=Int('n1')
	main=Int('main')
	_k1=Int('_k1')
	_k2=Int('_k2')
	_k3=Int('_k3')
	_k4=Int('_k4')
	_s=Solver()
	_s.add(ForAll([_n],Implies(_n>=0, _f(_n)==_n)))
	_s.set("timeout",50000)
	_s.add(A1 == A)
	_s.add(p1 == p)
	_s.add(B1 == B)
	_s.add(m1 == m)
	_s.add(n1 == n)
	_s.add(i1 == _N4)
	_s.add(j1 == j10(_N4))
	_s.add(ForAll([_x3,_x2],Implies(And(_x3>=0,_x2>=0),d2array1(A,_x2,_x3) == d2array10(A,_x2,_x3,_N4))))
	_s.add(ForAll([_x3,_x2],Implies(And(_x3>=0,_x2>=0),d2array1(B,_x2,_x3) == d2array10(B,_x2,_x3,_N4))))
	_s.add(ForAll([_n1,_n2],Implies(And(_n1>=0,_n2>=0),d2array2(A,_n2,_n1,_n1 + 1,_n2) == d2array2(B,-_n2 + m - 1,-_n1 + n - 1,_n1,_n2))))
	_s.add(ForAll([_x3,_x2,_n1,_n2],Implies(And(_x3>=0,And(_x2>=0,And(_n1>=0,_n2>=0))),d2array2(B,_x2,_x3,_n1 + 1,_n2) == d2array2(B,_x2,_x3,_n1,_n2))))
	_s.add(ForAll([_x3,_x2,_n2],Implies(And(_x3>=0,And(_x2>=0,_n2>=0)),d2array2(A,_x2,_x3,0,_n2) == d2array5(A,_x2,_x3,_n2))))
	_s.add(ForAll([_x3,_x2,_n2],Implies(And(_x3>=0,And(_x2>=0,_n2>=0)),d2array2(B,_x2,_x3,0,_n2) == d2array5(B,_x2,_x3,_n2))))
	_s.add(ForAll([_n2],Implies(_n2>=0,_N1(_n2) >= n)))
	_s.add(ForAll([_n1,_n2],Implies(And(_n1 < _N1(_n2),And(_n1>=0,_n2>=0)),_f(_n1) < n)))
	_s.add(ForAll([_n2],Implies(_n2>=0,Or(_N1(_n2)==0,_N1(_n2) - 1 < n))))
	_s.add(ForAll([_n2],Implies(_n2>=0,j5(_n2 + 1) == _N1(_n2))))
	_s.add(ForAll([_x3,_x2,_n2],Implies(And(_x3>=0,And(_x2>=0,_n2>=0)),d2array5(A,_x2,_x3,_n2 + 1) == d2array2(A,_x2,_x3,_N1(_n2),_n2))))
	_s.add(ForAll([_x3,_x2,_n2],Implies(And(_x3>=0,And(_x2>=0,_n2>=0)),d2array5(B,_x2,_x3,_n2 + 1) == d2array2(B,_x2,_x3,_N1(_n2),_n2))))
	_s.add(j5(0) == 0)
	_s.add(ForAll([_x3,_x2],Implies(And(_x3>=0,_x2>=0),d2array5(A,_x2,_x3,0) == d2array(A,_x2,_x3))))
	_s.add(ForAll([_x3,_x2],Implies(And(_x3>=0,_x2>=0),d2array5(B,_x2,_x3,0) == d2array(B,_x2,_x3))))
	_s.add(_N2 >= m)
	_s.add(ForAll([_n2],Implies(And(_n2 < _N2,_n2>=0),_f(_n2) < m)))
	_s.add(Or(_N2==0,_N2 - 1 < m))
	_s.add(ForAll([_x3,_x2,_n4,_n3],Implies(And(_x3>=0,And(_x2>=0,And(_n4>=0,_n3>=0))),d2array7(A,_x2,_x3,_n3 + 1,_n4) == d2array7(A,_x2,_x3,_n3,_n4))))
	_s.add(ForAll([_x3,_x2,_n4,_n3],Implies(And(_x3>=0,And(_x2>=0,And(_n4>=0,_n3>=0))),d2array7(B,_x2,_x3,_n3 + 1,_n4) == d2array7(B,_x2,_x3,_n3,_n4))))
	_s.add(ForAll([_x3,_x2,_n4],Implies(And(_x3>=0,And(_x2>=0,_n4>=0)),d2array7(A,_x2,_x3,0,_n4) == d2array10(A,_x2,_x3,_n4))))
	_s.add(ForAll([_x3,_x2,_n4],Implies(And(_x3>=0,And(_x2>=0,_n4>=0)),d2array7(B,_x2,_x3,0,_n4) == d2array10(B,_x2,_x3,_n4))))
	_s.add(ForAll([_n4],Implies(_n4>=0,_N3(_n4) >= n)))
	_s.add(ForAll([_n4,_n3],Implies(And(_n3 < _N3(_n4),And(_n4>=0,_n3>=0)),_f(_n3) < n)))
	_s.add(ForAll([_n4],Implies(_n4>=0,Or(_N3(_n4)==0,_N3(_n4) - 1 < n))))
	_s.add(ForAll([_n4],Implies(_n4>=0,j10(_n4 + 1) == _N3(_n4))))
	_s.add(ForAll([_x3,_x2,_n4],Implies(And(_x3>=0,And(_x2>=0,_n4>=0)),d2array10(A,_x2,_x3,_n4 + 1) == d2array7(A,_x2,_x3,_N3(_n4),_n4))))
	_s.add(ForAll([_x3,_x2,_n4],Implies(And(_x3>=0,And(_x2>=0,_n4>=0)),d2array10(B,_x2,_x3,_n4 + 1) == d2array7(B,_x2,_x3,_N3(_n4),_n4))))
	_s.add(j10(0) == 0)
	_s.add(ForAll([_x3,_x2],Implies(And(_x3>=0,_x2>=0),d2array10(A,_x2,_x3,0) == d2array5(A,_x2,_x3,_N2))))
	_s.add(ForAll([_x3,_x2],Implies(And(_x3>=0,_x2>=0),d2array10(B,_x2,_x3,0) == d2array5(B,_x2,_x3,_N2))))
	_s.add(_N4 >= m)
	_s.add(ForAll([_n4],Implies(And(_n4 < _N4,_n4>=0),_f(_n4) < m)))
	_s.add(Or(_N4==0,_N4 - 1 < m))
	_s.add(ForAll([_n1,_n2],Implies(And(_n1>=0,_n2>=0),d2array2(A,_n2,_n1,_N1(_n2),_n2) == d2array(B,-_n2 + m - 1,-_n1 + n - 1))))
	_s.add(ForAll([_x3,_x2,_n2],Implies(And(_x3>=0,And(_x2>=0,_n2>=0)),d2array2(B,_x2,_x3,_N1(_n2),_n2) == d2array(B,_x2,_x3))))
	_s.add(ForAll([_n1,_n2],Implies(And(_n1>=0,_n2>=0),d2array5(A,_n2,_n1,_N2) == d2array(B,-_n2 + m - 1,-_n1 + n - 1))))
	_s.add(ForAll([_x3,_x2],Implies(And(_x3>=0,_x2>=0),d2array5(B,_x2,_x3,_N2) == d2array(B,_x2,_x3))))
	_s.add(ForAll([_n4,_n1,_n2],Implies(And(_n4>=0,And(_n1>=0,_n2>=0)),d2array7(A,_n2,_n1,_N3(_n4),_n4) == d2array(B,-_n2 + m - 1,-_n1 + n - 1))))
	_s.add(ForAll([_x3,_x2,_n4],Implies(And(_x3>=0,And(_x2>=0,_n4>=0)),d2array7(B,_x2,_x3,_N3(_n4),_n4) == d2array(B,_x2,_x3))))
	_s.add(ForAll([_n1,_n2],Implies(And(_n1>=0,_n2>=0),d2array10(A,_n2,_n1,_N4) == d2array(B,-_n2 + m - 1,-_n1 + n - 1))))
	_s.add(ForAll([_x3,_x2],Implies(And(_x3>=0,_x2>=0),d2array10(B,_x2,_x3,_N4) == d2array(B,_x2,_x3))))
	_s.add(ForAll([_n1,_n2],Implies(And(_n1>=0,_n2>=0),d2array2(A,_n2,_n1,_N1(_n2),_n2) == d2array(B,-_n2 + m - 1,-_n1 + n - 1))))
	_s.add(ForAll([_n1,_n2],Implies(And(_n1>=0,_n2>=0),d2array2(A,_n2,_n1,_N1(_n2),_n2) == d2array2(B,-_n2 + m - 1,-_n1 + n - 1,_N1(_n2),_n2))))
	_s.add(ForAll([_x3,_x2,_n2],Implies(And(_x3>=0,And(_x2>=0,_n2>=0)),d2array2(B,_x2,_x3,_N1(_n2),_n2) == d2array(B,_x2,_x3))))
	_s.add(ForAll([_x3,_x2,_n2],Implies(And(_x3>=0,And(_x2>=0,_n2>=0)),d2array2(B,_x2,_x3,_N1(_n2),_n2) == d2array2(B,_x2,_x3,_N1(_n2),_n2))))
	_s.add(ForAll([_n1,_n2],Implies(And(_n1>=0,_n2>=0),d2array5(A,_n2,_n1,_N2) == d2array(B,-_n2 + m - 1,-_n1 + n - 1))))
	_s.add(ForAll([_n1,_n2],Implies(And(_n1>=0,_n2>=0),d2array5(A,_n2,_n1,_N2) == d2array5(A,-_n2 + m - 1,-_n1 + n - 1,_n2 + 1))))
	_s.add(ForAll([_x3,_x2],Implies(And(_x3>=0,_x2>=0),d2array5(B,_x2,_x3,_N2) == d2array(B,_x2,_x3))))
	_s.add(ForAll([_x3,_x2,_n2],Implies(And(_x3>=0,And(_x2>=0,_n2>=0)),d2array5(B,_x2,_x3,_N2) == d2array5(B,_x2,_x3,_n2 + 1))))
	_s.add(ForAll([_n4,_n1,_n2],Implies(And(_n4>=0,And(_n1>=0,_n2>=0)),d2array7(A,_n2,_n1,_N3(_n4),_n4) == d2array(B,-_n2 + m - 1,-_n1 + n - 1))))
	_s.add(ForAll([_n4,_n1,_n2],Implies(And(_n4>=0,And(_n1>=0,_n2>=0)),d2array7(A,_n2,_n1,_N3(_n4),_n4) == d2array7(B,-_n2 + m - 1,-_n1 + n - 1,_N3(_n4),_n4))))
	_s.add(ForAll([_x3,_x2,_n4],Implies(And(_x3>=0,And(_x2>=0,_n4>=0)),d2array7(B,_x2,_x3,_N3(_n4),_n4) == d2array(B,_x2,_x3))))
	_s.add(ForAll([_x3,_x2,_n4],Implies(And(_x3>=0,And(_x2>=0,_n4>=0)),d2array7(B,_x2,_x3,_N3(_n4),_n4) == d2array7(B,_x2,_x3,_N3(_n4),_n4))))
	_s.add(ForAll([_n1,_n2],Implies(And(_n1>=0,_n2>=0),d2array10(A,_n2,_n1,_N4) == d2array(B,-_n2 + m - 1,-_n1 + n - 1))))
	_s.add(ForAll([_n4,_n1,_n2],Implies(And(_n4>=0,And(_n1>=0,_n2>=0)),d2array10(A,_n2,_n1,_N4) == d2array10(A,-_n2 + m - 1,-_n1 + n - 1,_n4 + 1))))
	_s.add(ForAll([_x3,_x2],Implies(And(_x3>=0,_x2>=0),d2array10(B,_x2,_x3,_N4) == d2array(B,_x2,_x3))))
	_s.add(ForAll([_x3,_x2,_n4],Implies(And(_x3>=0,And(_x2>=0,_n4>=0)),d2array10(B,_x2,_x3,_N4) == d2array10(B,_x2,_x3,_n4 + 1))))
	_s.add(A1 == A)
	_s.add(p1 == p)
	_s.add(B1 == B)
	_s.add(m1 == m)
	_s.add(n1 == n)
	_s.add(_k1>=0)
	_s.add(_k3>=0)
	_s.add(ForAll([_n2],_N1(_n2)>=0))
	_s.add(_N2>=0)
	_s.add(ForAll([_n4],_N3(_n4)>=0))
	_s.add(_N4>=0)
	_s.add(Not(ForAll([_n4,_n3],Implies(And(_n4<_N4,And(_n3<_N3(_n4),And(_n4>=0,_n3>=0))),((d2array10(A,_n4,_n3,_N4))==(d2array10(B,-_n4 + m - 1,-_n3 + n - 1,_N4)))))))

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
