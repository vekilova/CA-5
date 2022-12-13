#!/usr/bin/env python3
loadfile = open("input5.1.txt")
liststa = list()

stack = dict()
for i in range(0, 9) :
	stack[i] = list()
listline = list()

for line in loadfile :
	line = line.rstrip()
	listline = line.split()
	#print("INPUT : ",listline)
	for j in range (0, 9):
		if listline[j] == 'X' :
			continue
		else :
			stack[j].append(listline[j])

#print(stack)
#print(stack[1])

for i in range(0, 9) :
	del stack[i][-1]
	stack[i].reverse()
#print(stack[1])

keyfile = open("input5.txt")
movelist = []
listline = list()

for i in range (0,9) :
	print(i+1, stack[i])

for line in keyfile :
	line = line.rstrip()
	listline = line.split()
	amount = int(listline[1])
	froms = int(listline[3])
	tos = int(listline[5])
	#print("key INPUT", amount, froms, tos)
	#amount = 2
	#froms = 7
	#tos = 8
	movelist = []
	print("key INPUT", amount, froms, tos)

	print("from stack ", stack[froms-1])
	print("to stack ", stack[tos-1])
	print("to be moved", stack[froms-1][-amount:])
	movelist = stack[froms-1][-amount:]
	print("movelist", movelist)
	for i in range(0, len(movelist)):
		stack[tos-1].append(movelist[i])
	del stack[froms-1][-amount:]

	print("from stack NEW ",stack[froms-1])
	print("to stack NEW ",stack[tos-1])
	for i in range (0,9) :
	#print(i+1, stack[i][-1])
		print(i+1, stack[i])


print('##################FINAL##############')
for i in range (0,9) :
	print(i+1, stack[i][-1])
	#print(i+1, stack[i])
