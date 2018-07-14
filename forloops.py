#for loops

#string="hello world"
#for i in string:
	#print i

#string=["hello world",45,23,'d','a']
#for i in string:
	#print i
#for x in string[1]:
	#	print x	

		
string=["hello world",[45,23],[0,'d','a']]
index = 0
for i in string:
	print i, index
	index += 1
	for x in i:
		print x	