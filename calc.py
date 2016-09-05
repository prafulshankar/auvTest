import sys
from pythonds.basic.stack import Stack
import argparse
import readline
import re

#---------------START OF CALCULATOR METHODS-----------------#
def inToPostfix(expression):
	expression = expression.replace(" ","")
	new_exp = []
	numeric_buffer = []
	prev = ''
	for each in expression:
		if each not in "1234567890+-/()*":
			print("invalid expression")
			return "invalid syntax"
		if prev in "+-*/" and each in "+-*/":
			print("invalid expression")
			return "invalid syntax"
		if each in "+-()*/":
			if numeric_buffer!=[]:
				new_exp.append(int(''.join(numeric_buffer)))
			numeric_buffer = []
			new_exp.append(each)
		else:
			numeric_buffer.append(each)
		prev = each
	if numeric_buffer!=[]:
		new_exp.append(int(''.join(numeric_buffer)))
	expression = new_exp
	print("INFIX: " +str(expression))

	dict_exp = {'/':4, '*':3, '+':2, '-':1, '(':0}

	operations = Stack()
	output = []

	for ch in expression:
		if ch=='(':
			operations.push(ch)
		elif type(ch)==int:
			output.append(ch)
		elif ch==')':
			chMain = operations.pop()
			while chMain!='(':
				output.append(chMain)
				chMain = operations.pop()
		else:
			while(not operations.isEmpty()) and (dict_exp[operations.peek()]\
				>= dict_exp[ch]):
				output.append(operations.pop())
			operations.push(ch)

	while not operations.isEmpty():
		output.append(operations.pop())

	return output

def evaluate(postfix):
	output = Stack()
	def calculate(a,b,ch):
		if ch == "+":
			return a+b
		elif ch == "*":
			return a*b
		elif ch == "/":
			return int(a/b)
		elif ch == "-":
			return a-b
	for ch in postfix:
		if str(ch) in "*+/-":
			b = output.pop()
			a = output.pop()
			output.push(calculate(a,b,ch))
		else:
			output.push(ch)
	return output.pop()


#---------------END OF CALCULATOR METHODS-----------------#

#---------------BUILDING COMMAND LINE INTERFACE-----------------#
print("In my calculator interface, enter any expression with or without brackets"\
	+"\nYou will get three outputs on the screen:\n(1)Parsed Infix\n(2)Postfix\n3)Evalu"\
	+"ated Postfix\n\nCtrl+d to quit\n\n*NOTE: Division is floored")
while(True):
	inp = raw_input("Calc$ ")
	h=inToPostfix(inp)
	print("POSTFIX: "+str(h))
	print("RESULT: " +str(evaluate(h)))