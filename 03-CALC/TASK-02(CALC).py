#choose calculator mode an operation comlixtty
import math
import os
import time
x="1"

while x=='1':
	opr="`"
	op1=1

	op2=1
	co_op=0
	nu_sys=0
	print("your simple calculator")
	print("======================")
	mode=input("please enter [1] for scintific calc and [2] for programmer calc ")
	os.system('cls')
	op_comlixty=input("please enter [1] for normal operation and [2] for complix ")
	os.system('cls')
		#numerc system for programmer mode
	if (mode=='2')&(op_comlixty=='2'):
		print("from decimal to binary [1]")
		print("from decimal to hexa  [2]")
		print("for decimal to octal [3]")
		nu_sys=input("please choose numeric system: ")
		os.system('cls')
		op1=input('please enternumberto convert ')

		#incase of choosing complix operation
	if (mode=='1')&(op_comlixty=='2'):
		print("for exponintial [1]")
		print("for power [2]")
		print("for root [3]")
		print("for factorial [4]")
		print("for log [5]")
		co_op=input("please choose next operation ")
		os.system('cls')
		if (co_op=='2'):
			op1,op2=input('please enter op1 and power with space betweeen it ').split(" ",2)
		else:
			op1=input('please enter number ')

		#reading values from user
	if (op_comlixty=='1'):
		op1,opr,op2=input('please enter op1 operator op2 with space betweeen it ').split(" ",3)

	op1=int(op1)
	op2=int(op2)
	os.system('cls')

	
	cal_sc={
		'sum': op1+op2,
		'sub': op1-op2,
		'mult': op1*op2,
		'div': op1/op2,
		'exp': math.exp(op1),
		'fac': math.factorial(op1),
		'log': math.log(op1),
		'pow': math.pow(op1,op2),
		'sqrt': math.sqrt(op1)
	}

	if co_op=='1':
		print("e power %d = %d" %(op1,cal_sc['exp']))
	if co_op=='2':
		print(" %d power %d = %d" %(op1,op2,cal_sc['pow']))
	if co_op=='3':
		print("sqrt(%d) = %d" %(op1,cal_sc['sqrt']))
	if co_op=='4':
		print("%d! = %d" %(op1,cal_sc['fac']))
	if co_op=='5':
		print("log(%d) = %d" %(op1,cal_sc['log']))


	cal_pr={
		'and': op1&op2,
		'or': op1|op2,
		'sh_l': op1<<op2,
		'sh_r':op1>>op2,
		'bin': bin(op1),
		'hexa': hex(op1),
		'octal': oct(op1),
	}
	if nu_sys=='1':
		print("%d in binary = %s" %(op1,cal_pr['bin']))
	if nu_sys=='2':
		print("%d in hexa = %s" %(op1,cal_pr['hex']))
	if nu_sys=='3':
		print("%d in octal = %s" %(op1,cal_pr['oct']))

	if opr=='+':
		print(op1,opr,op2,"=",cal_sc['sum'])
	if opr=='-':
		print(op1,opr,op2,"=",cal_sc['sub'])
	if opr=='*':
		print(op1,opr,op2,"=",cal_sc['mult'])
	if opr=='/':
		print(op1,opr,op2,"=",cal_sc['div'])
	if opr=='&':
		print(op1,opr,op2,"=",cal_pr['and'])
	if opr=='|':
		print(op1,opr,op2,"=",cal_pr['or'])
	if opr=='<<':
		print(op1,opr,op2,"=",cal_pr['sh_l'])
	if opr=='>>':
		print(op1,opr,op2,"=",cal_pr['sh_r'])

	x=input("for another operation press 1 to exit press 0")
	os.system('cls')





