print('Comparing File Size:')
f=open("SomeFile.txt","r")
contents=f.read()
contents=contents.split('Printing Num array:')[1]
new=(contents.replace('\n','')).split('\t')
#print(new)

chardict={}
i=0
while (i <len(new)):
	if(len(new[i])>0 and new[i][:9]=='Character'):
		for j in range(len(new[i])):
			#print(new[i][j])
			if new[i][j]==' ':
				key=new[i][j+1:]
				break
		
		while i<len(new) and not(new[i][:7]=='Encoded'):
			i=i+1
		for j in range(len(new[i])):
			#print(new[i][j])
			if new[i][j]=='1':
				value=new[i][j+1:]
				break
		chardict.update({key:value})		
	i=i+1	

#print(chardict)	

f.close()

f=open("file1.txt","r")
g=open("Original.txt","w")
h=open("Compressed.txt","w")

data=f.read()

for i in data:
	g.write(bin(ord(i))[2:].zfill(7))
	h.write(chardict[str(ord(i))])
f.close()
g.close()
h.close()

g=open("Original.txt","r")
h=open("Compressed.txt","r")
print('Binary Bits in Original file:')
s1=len(g.read())
print(s1)
print('Binary Bits in Compressed file:')
s2=len(h.read())
print(s2)

print('We achieved {} % compression using huffman coding scheme on our text file'.format((s1-s2)/s1*100))