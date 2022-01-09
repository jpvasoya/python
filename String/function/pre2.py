#predifined function 2
#1.isalpha()
print ('1.')
s='Jaydip vasoya'
print(s.isalpha())#space not allowed
s1="jaydip"
print(s1.isalpha())#checking function
s2='jp9099'
print (s2.isalpha())
print('\n2.')
#2.isnumeric(), isdigit()
print(s2.isnumeric())
s3='9099'#spqce not allowed
print(s3.isnumeric())#check strings are digit? 
print('\n3.')
#3.isalnum()
print (s.isalnum())
print (s2.isalnum())#space not allowed
#4.isspace()
print ("\n4.")
s4=" "
print (s4.isspace())
print (s.isspace())#only space
#5.istitle()
print ("\n5.")
s5='Jaydip Vasoya'
print (s5.istitle())#starting 1st char capital
print(s.istitle())
s6="Jaydip vasoya"
print(s6.istitle())
print("\n6.")
#6.islower()/isupper()
print(s.islower())#check upper or lower
print(s2.islower())
print (s.isupper())