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
	print("INPUT : ",listline)
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

listline = list()
for line in keyfile :
	line = line.rstrip()
	listline = line.split()
	amount = int(listline[1])
	froms = int(listline[3])
	tos = int(listline[5])
	print("key INPUT", amount, froms, tos)
	for i in range (0,9) :
		print(i+1, stack[i])

	for i in range(0, amount):
		print(i)
		print(stack[froms-1])
		print(stack[froms-1][-1])
		stack[tos-1].append(stack[froms-1][-1])
		print(stack[tos-1])
		del stack[froms-1][-1]
		print(stack[froms-1])

for i in range (0,9) :
	print(i+1, stack[i][-1])
