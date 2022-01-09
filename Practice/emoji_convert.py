#emoji converter
msg=input("\>")
dict={":)":"😀",":(":"😔","def":"☺"}
words=msg.split(" ")
for word in words:
	print(dict.get(word,word),end=" ")
	