import textanalysis
def count_char(text1,char):
	count=0
	for c in text:
		if c==char:
			count+=1
	return count
text=input("file name:")
char=input("which char you find:")
with open(text) as t1:
	text1=t1.read()

print(count_char(text1,char))
print(text1)
help(textanalysis)