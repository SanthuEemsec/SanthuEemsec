#Fundamental data Types

#int and float
print(4 + 5)
var = 9+1
print(var)
print(type(var)) #type is int
print(type(2 / 4)) #type is float

print( 2 ** 3) # 2^3 = 8
print( 5 // 4)
print( 5 % 4 )

#math functions
print(round(3.1))
print(abs(-50))

#operator precedence
print( (4 + 5) + 2 ** 2)
#()
# **
# * /
# + -
#float
#bool
#str
#list
#tuple
#set
#dict


print(bin(5))
print(int('0b101', 2))

#variable
iq = 190
print(iq)
#Constant
PI =3.14
#PI = 0 we should not change the constant value
print(PI)

a,b,c = 1,2,3
print(a)
#Argumented assignment operator
some_value = 5
some_value = some_value + 5
some_value += 2
print(some_value)

#Strings
print(type("Hi Hello there !!"))
username = 'santhosha'
long_str = ''' wow
great '''
print(long_str)

#string concatenation
first_name = 'Santhosha'
last_name = ' D S'
full_name = first_name + ' ' + last_name
print(full_name)


#Type conversion
print(type(str(100)))

weather = 'it\'s sunny'
print(weather)

name = "Santhosh"
age = 27
print('hi ' + name + ' your age is ' + str(age))
#formated string works in python3  earlier .formate was there
print(f' hi {name}. you are {age} years old')

#string indexes
selfish = '0123456'
print(selfish[0])
#[start:stop:stepover]
print(selfish[0:3])
#to reverse an order [::-1]

name = input('What is your name?\n')     # \n ---> newline  ---> It causes a line break
print(name)



#List

li = [1,2,3,4]
li2 = ['a', 'b']
li3 = [1,2,'a',True]

#Data structure
amazon_cart = ['notebooks', 'sunglasses']
print(amazon_cart[0])

#list slicing creating new list/cart or copy of a list
amazon_cart[0 :2 :1]