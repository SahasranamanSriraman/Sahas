#Create the below pattern using nested for loop in Python.
for i in range(6):
    print('*' * i,end='\n')
else:
    for j in range(1,5)[::-1]:
        print('*' * j,end='\n')
#Write a Python program to reverse a word after accepting the input from the user.
user_input=input('Enter the charecters: ')
print(user_input[::-1])
