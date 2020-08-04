#!/usr/bin/env python
# coding: utf-8

# In[21]:


#Define a function named is_two. It should accept one input and return 
#True if the passed input is either the number or the string 2, 
#False otherwise.

def is_two(num):
    return int(num) == 2
is_two(2)  


# In[23]:


#Define a function named is_vowel. It should return True if the 
#passed string is a vowel, False otherwise.
def is_vowel(let):
    vowels = 'aeiouAEIOU'
    return let in vowels
is_vowel('z')


# In[33]:


#Define a function named is_consonant. It should return True if 
#the passed string is a consonant, False otherwise. Use your 
#is_vowel function to accomplish this.
def is_consonant(con):
    consonants = 'bcdfghjklmnpqrstvxzwy'
    return con in consonants
is_consonant('c')


# In[88]:


#Define a function that accepts a string that is a word. 
#The function should capitalize the first letter of the word 
#if the word starts with a consonant.
def first_letterc(con):
    consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','z','w']
    if con in con for consonants:
        return con.capitalize()
first_letterc('alpha')


# In[64]:


#Define a function named calculate_tip. It should accept a 
#tip percentage (a number between 0 and 1) and the bill total, 
#and return the amount to tip.
def calculate_tip(tip, bill):
    return (tip * bill)
calculate_tip(.2, 78.99)


# In[ ]:




