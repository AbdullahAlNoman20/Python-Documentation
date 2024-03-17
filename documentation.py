

# print("Hello World")






# # Formatted String
# num1= 20
# num2= 30
# print(f"the Sum is {num1} + {num2} = {num1+num2} ")




# For Print Space after multiple line in add in a single line
# print("Abdullah AL Noman.", end=" ")
# print("01764308876")








# Use of if else or elif 
# marks = 74
# marks = int(input("Enter your mark"))
# if marks >=80 :
#     print("A+")
# elif marks >=60 :
#     print("A-")
# elif marks >=40 :
#     print("B")

# else:
#     print("Fail")

# num = 5

# if num%2==0:
#     print("Even")
# else:
#     print("Odd")











# to view any Type of a variable 
# Name= "Noman"
# print(type(Name))








# # Some useful Library

# a = "Hello, World!"
# print(a.upper())






# a = "Hello, World!"
# print(a.lower())






# a = "Hello, World!"
# print(a.replace("H", "J"))






# a = "Hello, World!"
# print(a.split(","))





# a = "Tony"
# print(a.find('n'))






# a = "Tony"
# print("T" in a)






# # Logical Operator
# # or,and,not






# # Variable Declaration
# Name = "Abdullah"
# print(Name)








# # Getting Input From User
# age = int(input("Enter Your Age "))
# print("Your age is",age)









# # Control statement
# if(age <= 18):
#     print("So, Ghumia Thako")

# else:
#     print("Vot Dite Jaw")








# # For Loop
# n = int(input("Enter Any Value"))
# list = []

# for i in range (1,n+1,2):
#     # 1 thake suru hoye n+1 porjonto jabe r protibar 2 kore barbe
#     list.append(i)

# print(list)


# for N in "Abdullah":
#   print(N)


#   for A in range(2, 30, 3):
#   print(A) 









# # Break & Continue





# math related function
# from math import *

# print(max(20,30))



# print(min(30,10))


# # minas value remove kore dibe
# print(abs(-5))



# print(pow(2,3))


# # Squr root
# print(sqrt(25))




# print(round(3.2))




# print(floor(3.8))



# print(ceil(3.9))













# User Defign Function 

# def functionName():
#     print("Someone Call me ")

# functionName()





# Range Function
# num = list(range(10))
# print(num)



# num = list(range(3,10))
# print(num)



# num = list(range(50,100,5))
# print(num)







# Recive any value and parform any operation and print the result
# def sunTwoNumber(x,y):
#     sum = x+y 
#     print(sum)
# sunTwoNumber(20,30)








# Return value from a Function

# def addFunction(a,b):
#     sum = a+b
#     return sum

# result = addFunction(20,30)
# print(result)







# def large(a,b):
#     if a>b:
#         return a
#     else :
#         return b

# result = large(20,30)
# print(result) 








# # List Operation
# list1 = [1,2,3,4,5]
# list2 = ["Noman","Sakib","Tanvir"]
# print(list1)
# print(list2)

# list3 = list1.copy()
# print(list3)

# print(list1[2:])




# in Operator
# print("Noman" in list2)
# print("Noman" not in list2)

# position = list.index(4)
# print(position)


# count = list.count(4)
# print(count)


# print(list[1])
# print(list[-1])




# list=[1,2,3,4,5,6,78,9]
# print(len(list))


# list.sort()
# print(list)



# list.reverse()
# print(list)





# list[1] = 20
# print(list)


# list.append(500)
# print(list)


# list.insert(3,"Name")



# list.pop()

# list.clear()



# Get input from user as a list

# n = input("Enter some value")

# list = n.split()
# sum = 0

# for num in list:
#     sum = sum + int(num)
# print(sum)



# list.remove(5)
# print(list)


# for L in list:
#   print(L)


# newlist = []

# for x in list:
#     if 3 in x:
#         newlist.append(x)

# print(newlist)



# list.sort()
# print(list)



# mylist = list.copy()
# print(mylist)



# list2 = [1, 2, 3]

# list3 = list + list2
# print(list3)




# list comprehension
# num = [1,2,3,4,5,6,8]

# result = [x*x for x in num]
# print(result)

# result = [x for x in num if x%2==0]
# print(result)








# Tuples same as list but its immuteble. that means tuples value can not change

# student = (
#     ("Ahmed",27,3.5),
#     "Sakib",
#     "Raju"
# )

# print(student)







# Set

# num1 = {1,2,3,4,5,6}

# num2 = set([2,3,4,5,6])


# num2.add(9)

# num2.remove(4)

# print(num2)

# print(7 in num2)
# print(7 not in num2)


# | is Union and & is intersection

# print (num1 | num2 )



# print(num1 & num2)


# # Difference
# print(num1 - num2)







# # dictionary

student = {


    "101": "Abdullah",
    "102": "Al",
    "103": "Noman",

}

print(student)
# print(student["101"])
# print(student.get("101"))
# print(student.get("109","Not a Valid Key"))





# student.pop("102")
print(student.pop("102"))


print(student.get("103"))


print(student)


print(student.keys())


print(student.values())


print(student.items())


for key, values in student.items():
    print(key,values)












