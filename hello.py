#input name
x=""
i=0
while(x=="") :
    x = input("Name ? ")
    i=i+1

x = x.strip().capitalize()
y=""
# y = x.capitalize()
""" 
now print your name  , multiple line comment.
"""
print("welcome ",x,y,i)

#----------------- split function ------------
b=input("write 2 words")
first,last=b.split(" ")
print(" you wrote {first} and {last}")



