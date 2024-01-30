x=y=z="same"
print(x)
print(y)
print(z)


b1=True
b2=False
x=type(b1)
print(x)


x=1.0
z=type(x) is int
print(z)


x=1.0
z=isinstance(x,float)
print(z)


x=15
y=4
a=x+y
b=x-y
c=x/y
d=x//y
e=x**y
print(a)
print(b)
print(c)
print(d)
print(e)


x1=5
y1=5
x2="hello"
y2="hello"
x3=[1,2,3]
y3=[1,2,3]
print(x1 is not y1)


x="hello world"
y={1:"a",2:"b"}
print("h" in x)
print("Hello" not in x)
print(1 in y)


s="virat is best player in the nation"
s2=s.replace("nation","world")
print(s2)
print(s[5:])



my_list=[]
print(my_list)
my_list=[1,2,3,'example',3.132]
print(my_list)


my_list=[1,2,3]
print(my_list)
my_list.append([555,12])
print(my_list)
my_list.append([234])
print(my_list)
del my_list[2]
print(my_list)
my_list.append("example")
print(my_list)
my_list.remove("example")
print(my_list)
my_list.pop(2)
print(my_list)
my_list.clear()
print(my_list)

































