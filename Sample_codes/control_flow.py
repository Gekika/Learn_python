
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