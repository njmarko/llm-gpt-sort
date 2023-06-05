#!/usr/bin/env python
# coding: utf-8

# # LLM-GPT-SORT
# 

# ## Setup
# #### Load the API key and relevant Python libaries.

# In[1]:


import os
import openai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.environ['OPENAI_API_KEY']


# In[2]:


def get_completion_from_messages(messages, 
                                 model="gpt-3.5-turbo", 
                                 temperature=0, 
                                 max_tokens=1000):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, 
        max_tokens=max_tokens, 
    )
    return response.choices[0].message["content"]


# # Generate a random list of numbers and sort it with GPT

# In[3]:


import random
import ast

to_sort =  random.sample(range(0, 200), 200)
direction = 'Ascending'
print(to_sort)


sys_msg = f"""
Response should only contain the sorted data in the direction specified by the user.
Do not say anything else, just return a same structure with the sorted information.
You role is to only return the data.
"""

collection_type = f"""
list
"""

prompt_nums = f"""
Sort the elements in the given collection in the {direction} order, and return only the sorted collection in the {collection_type} format:
{to_sort}
"""



messages = [
    {'role': 'system',
    'content': sys_msg},
    {'role':'user',
    'content': prompt_nums}
]

res = get_completion_from_messages(messages)
print(res)
sorted_list = ast.literal_eval(res)


# # Evaluation

# In[4]:


to_sort.sort()
print(f"\nOriginal sorted collection:\n{to_sort}")
print(f"\nLLM sorted collection:\n{sorted_list}")
print(f"\nAre these two list the same? {to_sort == sorted_list}")


# # Generate a random list of words and sort it with GPT

# In[5]:


import random
import ast
import urllib.request

word_url = "https://www.mit.edu/~ecprice/wordlist.10000"
response = urllib.request.urlopen(word_url)
long_txt = response.read().decode()
words = long_txt.splitlines()

to_sort =  random.sample(words, 15)
print(to_sort)

sys_msg = f"""
Response should only contain the sorted data in the direction specified by the user.
Do not say anything else, just return a same structure with the sorted information.
You role is to only return the sorted data.
You should make sure to always return the same number of elements that were given to you in the collection.
"""

collection_type = f"""
list
"""

prompt = f"""
Sort the elements in the given collection in the {direction} order, and return only the sorted collection in the {collection_type} format:

{to_sort}
"""

messages = [
    {'role': 'system',
    'content': sys_msg},
    {'role':'user',
    'content': prompt}
]

res = get_completion_from_messages(messages)
print(res)
sorted_list = ast.literal_eval(res)


# # Evaluation

# In[6]:


to_sort.sort()
print(f"\nOriginal sorted collection:\n{to_sort}")
print(f"\nLLM sorted collection:\n{sorted_list}")
print(f"\nAre these two list the same? {to_sort == sorted_list}")

