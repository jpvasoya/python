#trick 2
u=500
m=100
t=600
s=200
condition=[
u>200,         #all condition true
                     #else atleast 1 condition mate
m>28,             #any
t>250,
s>50
]
if all(condition):
	print('done')