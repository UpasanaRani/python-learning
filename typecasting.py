# a="1"
# # a=1
# b="2"
# # b=2
# print(int(a)+int(b))
string ="15"
number=7
string_number=int(string)
sum=number+ string_number
print("The Sum of both the numbers is:",sum)

#python automatically converts
#a to int
a=7
print(type(a))
#python automatically converts  b to float
b=0.78
print(type(b))
#python automatically converts c to float as it is a float addition
c=a+b
print(c)
print(type(c))

# another implicit casting
c=1.9
d=8
print(c+d)