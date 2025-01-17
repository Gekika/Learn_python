
#  if statement

y = int(input("Enter the dimension of your shape"))
x = int(input("1.Square 2.Rectangle"))

if x == 1:
    print(f"The area of sqaure is: {y*4}")
elif x==2:
    print(f"The area of Rectangle is {y*y}")

# for statement
# we will measure the length of various strings
words = ["Martin" , 'Go' , 'into' ,'the ','woods']
for w in words:
    print(w,len(w))


# Code that modifies a collection while iterating over the same colection, a copy is created 1st
users = {'Ken': 'active' ,'Martin': 'inactive' ,'Joyce': 'active' ,'Mary': 'inactive' ,'Brenda': 'active' , }

# iterate over the copy 
for user, status in users.copy().items():
        if status == 'inactive':
            del users[user]
            print(users)


# the range function
for i in range(20):
     print(i)



users = ["Martin" , 'Go' , 'into' ,'the ','woods']
for us in range(len(users)):
     print(us, users[us])