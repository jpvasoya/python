#method 3
#1.getkeys()
dict={1:'jay®', 2:'',3:"",4:""}
print(dict.get(1))#get values into the keys in dictionary
#by default none
print(dict.get(5))
#all keys get below 
#2.keys()
print(dict.keys())
#3.setdefault()
dict.setdefault('jp','king')#set default values of the key
print(dict.keys())
print(dict.get('jp'))
dict.setdefault(2,'vasoya')#only used in new keys 
print(dict.get(2))