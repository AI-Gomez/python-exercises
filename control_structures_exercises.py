#!/usr/bin/env python
# coding: utf-8

# In[2]:


#A) prompt the user for a day of the week, print out whether the day is Monday or not

dayweek = input("What is today dummy: ")

if dayweek == 'Monday' or dayweek == 'monday':
    print ('Wow, suprised you knew that')
else:
    print ('go home, youre drunk')


# In[5]:


#B) prompt the user for a day of the week, print out whether the day is a 
#weekday or a weekend

dwd = input("What is today dummy: ")
if dwd == 'Sunday' or dwd == 'Saturday':
    print ('Wow, suprised you knew that... its a weekend')
elif dwd == 'Monday' or dwd == 'Tuesday' or dwd == 'Wednesday' or dwd == 'Thursday' or dwd == 'Friday':
    print ('yes, thats a weekday dummy')

else:
    print ('go home, youre drunk')
    


# In[29]:


#C create variables and make up values for number of hours worked in one week
#the hourly rate how much the weeks check is going to be
#time and a half if you work more than 40hrs

hrs = 98
h= float(hrs)
rate = float(121)

if h <= 40:
    pay = h * rate
elif h > 40:
    pay = ((h-40)*rate*1.5)+rate*40   

print('I worked', hrs, 'hours last week and only made $', pay )


# In[30]:


#2A Create an integer variable i with a value of 5.

i = 5

#Create a while loop that runs so long as i is less than or equal to 15
#Each loop iteration, output the current value of i, then increment i by one.

while i <= 15:
    print(i)
    i += 1
    


# In[31]:


##2A CTD Create a while loop that will count by 2's starting with 0 and ending at 100. 
##Follow each number with a new line.
i = 0
while i <= 100:
    print(i)
    i += 2
    


# In[32]:


#Alter your loop to count backwards by 5's from 100 to -10.

i = 100
while i >= -10:
    print(i)
    i -= 5


# In[2]:


##Create a while loop that starts at 2, and displays the number squared on each line
##less than 1000000
i = 2
while i <= 1000000:
    print(i)
    i = i ** 2


# In[5]:


#Write a loop that uses print to create the output shown below.

i = 100
while i >= 5:
    print(i)
    i -= 5


# In[2]:


#B Write some code that prompts the user for a number, then shows 
#a multiplication table up through 10 for that number.
num = int(input("Hurry up, Pick a number, ANY number: "))

for i in range(1, 11):
   print(num,"X",i,"=",num * i)


# In[6]:


#Create a for loop that uses print to create the output shown below.
n=9
for num in range(n+1):
    for i in range (num):
        print(num,end="")
    print("\r")
    
#also
for i in range(1, 10):
    print(str(i) * i)


# In[12]:


#C Prompt the user for an odd number between 1 and 50. Use a loop and a break 
#statement to continue prompting the user if they enter invalid input. 
#(Hint: use the isdigit method on strings to determine this). Use a 
#loop and the continue statement to output all the odd numbers between 
#1 awhile True:
while True:

     start_odd = input("Please input an odd number between 1 and 50: ")

     if not start_odd.isdigit():
         print("\nPlease input a positive integer value without decimals. ")
         continue

     if int(start_odd) < 1 or int(start_odd) > 50:
         print("\nYou have entered a number outside of the specified range. Please try again. ")
         continue

     if int(start_odd) % 2 != 1:
         print("\nYou have failed to enter an odd number. Please try again. ")
         continue

     else:
         break

     print(f"\nNumber to skip is: {start_odd}\n")

for num in range(1, 51):
     if num == int(start_odd):
         print(f"Yikes! Skipping number: {start_odd}")
         continue
     if num % 2 == 1:
         print(f"Here is an odd number: {num}")




# In[17]:


#The input function can be used to prompt for input and use that input in your 
#python code. Prompt the user to enter a positive number and write a loop that 
#counts from 0 to that number. (Hints: first make sure that the value the user 
#entered is a valid number, also note that the input function returns a string, 
#so you'll need to convert this to a numeric type.)
while True:
     count_to_num = input("Pick a positive number: ")

     if not int(count_to_num.isdigit()):
         print("Follow the instructions")
         continue
     if int(count_to_num) < 0:
         print("Please enter a positive number. ")
         continue
     else:
         break

if int(num) > 0:
     for i in range (0, int(count_to_num) + 1):
         print(i)
    


# In[14]:


#Write a program that prompts the user for a positive integer. Next write a loop 
#that prints out the numbers from the number the user entered down to 1.
while True:
    try:
        pos = int(input("Pick a positive number: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        break
i = pos
while i >= 1:
    print(i)
    i -= 1


# In[6]:


#One of the most common interview questions for entry-level programmers is the 
#FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic 
#looping and conditional logic skills.
#Write a program that prints the numbers from 1 to 100.
#For multiples of three print "Fizz" instead of the number
#For the multiples of five print "Buzz".
#For numbers which are multiples of both three and five print "FizzBuzz".
for fizzbuzz in range(101):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)


# In[18]:


#Display a table of powers.
#Prompt the user to enter an integer.
#Display a table of squares and cubes from 1 to the value entered.
#Ask if the user wants to continue.
#Assume that the user will enter valid data.
#Only continue if the user agrees to.

while True:    
     table_target = int(input("What number would you like to go up to? "))
     if table_target > 0:
         print("\nHere is your table!\n")
         print("number | squared | cubed")
         print("------ | ------- | -----")
         number_lst = []
         for i in list(range(1, table_target + 1, 1)):
             number_lst.append(i)
         for n in range(0, len(number_lst), 1):
             normal = number_lst[n]
             squared = number_lst[n] ** 2
             cubed = number_lst[n] ** 3
             print(f"{normal:<7}| {squared:<8}| {cubed:<5}")
     user_continue = input("\nWant another one? (y/n): ")
     if user_continue == "y":
         continue
     if user_continue == "n":
         print("\nOk, bye")
         break
     else:
         print("\nYou are not making sense")
         break


# In[23]:


#Convert given number grades into letter grades.
#Prompt the user for a numerical grade from 0 to 100.
#Display the corresponding letter grade.
#Prompt the user to continue.
#Assume that the user will enter valid integers for the grades.
#The application should only continue if the user agrees to.
while True:
    
    grade = int(input("What was your grade?\t"))
    print()
    if grade >= 88 and grade <= 100:
        print("You received an A")

    elif grade >= 80 and grade <= 87:
        print("You received a B")

    elif grade >= 67 and grade <= 79:
        print("You received a C")

    elif grade >= 60 and grade <= 66:
        print("You received a D")

    elif grade >=0 and grade <= 59:
        print("You failed with an F")
        
    wants_to_continue = input("Do you want to continue? y/n\n")
    if wants_to_continue not in ["y"]:
        break
        
print("We are done here")


# In[27]:


#Create a list of dictionaries where each dictionary represents a 
#book that you have read. Each dictionary in the list should 
#have the keys title, author, and genre. Loop through the 
#list and print out information about each book.

books = [
    {'title': 'Left of Boom', 'author': 'Some CIA Dude', 'genre': 'non fiction'},
    {'title': 'American Spartan', 'author': 'Some SF guy', 'genre': 'non fiction'},
    {'title': 'No Easy Day', 'author': 'Some SEAL', 'genre': 'non fiction'},
]
selected_genre = input('Enter a genre: ')
selected_books = [book for book in books if book ['genre'] == selected_genre]

for book in selected_books:
    print('----')
    print('title: ' + book['title'])
    print('author: ' + book['author'])
    print('genre: ' + book['genre'])
    


# In[ ]:




