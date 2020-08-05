#!/usr/bin/env python
# coding: utf-8

# In[21]:


#1 Define a function named is_two. It should accept one input and return 
#True if the passed input is either the number or the string 2, 
#False otherwise.

def is_two(num):
    return int(num) == 2
is_two(2)  


# In[23]:


#2 Define a function named is_vowel. It should return True if the 
#passed string is a vowel, False otherwise.
def is_vowel(let):
    vowels = 'aeiouAEIOU'
    return let in vowels
is_vowel('z')


# In[33]:


#3 Define a function named is_consonant. It should return True if 
#the passed string is a consonant, False otherwise. Use your 
#is_vowel function to accomplish this.
def is_consonant(con):
    consonants = 'bcdfghjklmnpqrstvxzwy'
    return con in consonants
is_consonant('c')


# In[32]:


#4 Define a function that accepts a string that is a word. 
#The function should capitalize the first letter of the word 
#if the word starts with a consonant.
def is_consonant(con):
    consonants = 'bcdfghjklmnpqrstvxzwy'
    return con in consonants

def first_consonant(word):
    if str(word).isdigit():
        return(word)
    elif is_consonant(word[0]):
        return(word[0].upper() + word[1:])
    else:
        return word
first_consonant('bomb')


# In[64]:


#5 Define a function named calculate_tip. It should accept a 
#tip percentage (a number between 0 and 1) and the bill total, 
#and return the amount to tip.
def calculate_tip(tip, bill):
    return (tip * bill)
calculate_tip(.2, 78.99)


# In[4]:


#6 Define a function named apply_discount. It should accept a 
#original price, and a discount percentage, and return the 
#price after the discount is applied.
def apply_discount(disc, orig_price):
    return (1 - disc) * orig_price
apply_discount(.15, 45.65)


# In[14]:


#7 Define a function named handle_commas. It should accept a 
#string that is a number that contains commas in it as input, 
#and return a number as output.
def handle_commas(s):
    s = s.replace(',', '')
    return s
handle_commas('1,000,000,000')


# In[2]:


#8 Define a function named get_letter_grade. It should accept
#a number and return the letter grade associated with that 
#number (A-F).
def get_letter_grade():
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
            return grade
get_letter_grade()

#or

def get_letter_grade(num):
    if num >= 90:
        return 'A'
    elif num >= 80:
        return 'B'
    elif num >= 70:
        return 'C'
    elif num >= 60:
        return 'D'
    else:
        return 'F'
get_letter_grade(70)


# In[27]:


#9 Define a function named remove_vowels that accepts a 
#string and returns a string with all the vowels removed.
def remove_vowels(c):
    newstr = c
    vowels = ('a', 'e', 'i', 'o', 'u')
    for x in c.lower():
        if x in vowels:
            newstr = newstr.replace(x,"")

    return newstr
remove_vowels('apple')


# In[ ]:


#10 Define a function named normalize_name. It should accept a 
#string and return a valid python identifier, that is:
#anything that is not a valid python identifier should be removed
#leading and trailing whitespace should be removed
#everything should be lowercase
#spaces should be replaced with underscores
def normalize_name(string):
    normalized_string = ''
    stripped_string = string.strip()
    if stripped_string[0].isdigit():
        stripped_string = '_' + stripped_string
    for letter in stripped_string:
        if (letter.isalpha() or letter == '_') and not letter == ' ':
            normalized_string += letter.lower()
        elif letter.isdigit():
            normalized_string += letter
        elif letter == ' ':
            normalized_string += '_'
    return normalized_string
    


# In[3]:


#11 Write a function named cumulative_sum that accepts a list of 
#numbers and returns a list that is the cumulative sum of the 
#numbers in the list.
def cumulative_sum(lists):
    cu_list = []
    length = len(lists)
    cu_list = [sum(lists[0:x:1]) for x in range(0, length + 1)]
    return cu_list[1:]
cumulative_sum([1,5,10,56,99])


# In[ ]:




