'''print("hellow world")
print("print('hellow world')")
print("hellow world\nmy name\nmy father")
print("hellow world"+"my name")
input("what is your name")
name=input("what is your name")
print(name)
aman="jenny"
print(aman)'''
#logical operater
#a,b=5,4
#print(a>4 and b<10)
#c=True
#print(not(c))
#bitwise operattor
#&and,|or,^xor,~not,<< left shift,>> right sift
#a=5
#b=4
#print(a&b)
#print(a|b)
#print(a^b)
#print(a-b)
#identity opertors is,is not
#a=5
#b=5
#print(a is b) 
#print(id(a))
#print(id(b))
#membersip operator "in" an "not in"
'''str='deepak'
print('d'in str)
print('dee'in str)
print('d'not in str)
l=[1,3,4,5,6,]
print(1 in l)
weight=input("enter weight in kg:")
height=input("enter heigh in m:")
bmi=int(weight)/float(height)**2
print(bmi)'''
#round function round()
#round(number,no of digits)
#print(round(23.3233,3))
#print(round(23.3233))
#f-strings
'''name='deepak'
age=30
height=1.6
print(name+str(age)+str(height))
print(f"my name is{name}.I am {age} yer old.myheight is {height} meter")'''
#if else statements
##a=int(input("enter the age"))
'''if(a>4):
    print("passs")
else:
    print("fail")
if a>5:
    print("good")
elif(a>4):
     print("not good")
else:
     print("good bye")
#list in python mutable
number=[1,2,88,65 ,7,9]
print(number)
print(number[3])
print(number[1:5])
print(number[1:5:2])
number.sort()
print(number)
number.reverse()
print(number)
number.append(45)
number.insert(2,4)
number.extend([2,,34,5,6,7,])
import random
random.randint(1,4)
list1=[1,2,3,5,[2,34,5],5]
print(len(list1))
print(list1[4][2])
#tuple in python immutable
tuple1=(1,2,3,4,5)
print(tuple1[-2])
#sets in python
a={10,3,4,5,9,'deepak'}
print(a)
a.add(10)
print(a)
a.remove(10)
print(a)
a.clear()
#operations on sets
set1={'ram ','deepak','anil'}
set2={'aman','deepak',2}
set3={1,3,4,5}
print(set1.union(set2))
print(set1 | set2 | set3)
print(set1.union(set2,set3))
set1.update(set2)
print(set1)
print(set1.intersection(set2))
#for loop in python
name=['aman','raman','deepak']
for names in name:
    print(names)
    if names=='deepak':
        print("good name")
else:
    print("nice job")   
#a=range(10,0,-1)
for i in a:
    print(i)
for i in range(1,9):
      print(i,end='')
cont=0
while cont >=9:
    print(cont)
    cont+=1
else:
print("aman")
#loop control statements
count=0
while count<=10:
    print(count)
    count+=1
    if count==7:
        break
    print("hi")
print("out from loop")   
count=1
while count<=10:
    print(count)
    count+=1
    if count==7:
        continue
    print("hii")
    
print("out from loop")
for i in range(1,19):
    if(i==10):
        continue
    else:
        print(i)
        what is indentation===:
        
#functions in python
def fun_name(parameter):
    fun body
    return expression
#callig
fun_name()
def greet():
    print("hii")
    print("jenny")
greet() 
greet()
#function with argument
def greet():
    print("hii")
    print("bye")
greet()  
def add(a,b):
    c=a+b
    print(c)
add(3,4)
add(4,5)    
#type of argument in function
# 1.default
# 2.positinal .3 keyword 4. arbitary
#positional
#def greet(name,dept):


 ##
 #   print(f"are you form{dept} department")  
#greet("deepak","css")
#keyword
def greet(name,dept):
   print(f"hi {name}")
   print(f"are you form{dept} department")  
greet(name="deepak",dept="css")
#arbitrary
def add(*numbers):
    c=0
    for i in numbers:
      c=c+i
    print(f"sum is{c}")
add(4,5,6)    
def infoperson(**kwargs):
    for i,j in kwargs.items():
        print(i,j)
infoperson(name="ram",age=30,dept="cse")
#dictionary in python orderd and mutable keys are imutable no dublicaes allowed
phone_no={"name":886854,"class":10}
print(phone_no["name"])        
#phone_no["name"]=464575
#print(phone_no)
#phone_no["aman"]={13214,34,54}

#print(phone_no)
del phone_no['name']
print(phone_no)
phone_no.pop("class")
phone_no.popitem("class")
phone_no.clear("class")
phone_no.keys()
phone_no.values()
phone_no(len(phone_no))'''


