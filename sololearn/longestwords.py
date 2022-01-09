#longestwords
txt=input("enter text: ")
text=txt.split(" ")
#print(text)
count=0
for t in text:
	count+=1
print("how many words in the text:",count)
print("longest words:",max(text,key=len))
print("which word biggest in by lexographics order:"+max(text))
