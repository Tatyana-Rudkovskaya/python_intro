# run with
# nodemon .\index.py


""" print(5+2)  
print(20)
print("Hello World")
name = "Tatyana"
print (name)
print ("Welcom "+name )
user=["Tatyana", "Tommy", "Yakov"] #arrays
print(user)
print(user[1:]) # array slicing
"""
 
#conditionals

""" h=18
if h > 18:
    print("To old")
elif h == 18:
    print("Gleich")
else:
    print("Klein") """

#for loop with conditional

""" users=["Tatyana", "Tommy", "Yakov"]
index = 0
for user in users:
    if len(user) > 5:
        print("Ganz schoen lang er name " + user)
        print (user, len(user), len(users), index)
    index+=1

for i in range(5, 10):
    print(i)


for i in range(len(users)):
    print(users[i]) """

#for loop with brakestatmens
""" for i in range(5, 10):
    if i==7:
        continue
    print(i) """

""" for i in range(5, 10):
    if i==7:
        dreak
    print(i) """

#function
""" def sum(x,y):
    print(x+y)
sum(3,4)

def sum2(x,y=0):
    print(x+y)

sum2(10)
sum2(10,6) """

#datestraktures
""" users=["Tatyana", "Tommy", "Yakov"]
users.append("Lena")
users.insert(2,"Peter")
users[0]="Tanya"
print(users)
users[2:4] = ["Niklar", "Alan"]
print(users)
users.reverse()
print(users) """

#stacks
""" stack=[3,4,5]
stack.append(6)
stack.append(7)
stack.append(8)
print(stack) # stack gets biger

stack.pop()
stack.pop()
stack.pop()

print(stack) # stack gets biger """


# queues
""" users=["Tatyana", "Tommy", "Yakov"]
users.append("erik")
print(users)
users.pop(0)
print(users)
users.pop(0)
print(users)
users.pop(0)
print(users) """

#complex/multidimensional data-strukturs
""" matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix)

for i in range(len(matrix)):
    for j  in matrix[i]:
        print(j)
print("########")
for i in matrix:
    for j  in i:
        print(j) """

# sets
user= ["string", 66, "kdlsf"]
users =[
    {"name": "Tatyana", "age": 66},
    {"name": "Tommy", "age": 89}
 ]
print(users[1]["name"])