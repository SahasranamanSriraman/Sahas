#1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.
for i in range(2000,3201):
    if (i%7==0) and (i%5!=0):
        print(i,end=',')

#2. Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name.
first_name=input('Enter the first_name: ')
last_name=input('Enter the last_name: ')
print('{} {}'.format(last_name[::-1],first_name[::-1]))
#3. Write a Python program to find the volume of a sphere with diameter 12 cm
def vol_sphere(diameter):
    return 4/3*3.14*(diameter/2)**3
print(vol_sphere(8))