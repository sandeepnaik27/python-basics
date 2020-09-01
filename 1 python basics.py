#!/usr/bin/env python
# coding: utf-8

# # MACHINE LEARNING 
# ## python basics 
# 

# In[1]:


1+1


# In[2]:


6-5


# In[3]:


6*4


# In[4]:


10/2


# In[5]:


10%2


# ## strings

# In[6]:


"sandeep"


# In[9]:


type('sandeep')


# ## variable

# In[10]:


sandy=10


# In[13]:


type('sandy')


# In[14]:


a=10


# In[15]:


type(10)


# In[16]:


a='sandeep'


# In[17]:


type(a)


# In[19]:


a=10
b=20


# In[20]:


print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)


# In[22]:


#various ways of printing
print('hello')


# In[25]:


first_name='sandeep'
last_name='naik'


# In[28]:


print=("my first name is {} and last name is {}".format(first_name,last_name))


# In[35]:


print


# In[39]:


len(first_name)


# ## Data Structure and Boolean

# ### boolean

# In[2]:


print(True,False)


# In[3]:


type(True)


# In[5]:


type(False)


# In[11]:


my_str="Sandeep"


# In[18]:


print(my_str.isalnum())
print(my_str.isalpha())
print(my_str.isdigit())
print(my_str.istitle())
print(my_str.isupper())
print(my_str.islower())
print(my_str.endswith('d'))
print(my_str.startswith('S'))


# ## Boolean and Logical Operator

# In[19]:


True and False


# In[20]:


True and True


# In[21]:


False and False


# In[22]:


True or False


# In[23]:


True or True


# In[24]:


False and False


# In[34]:


str_example='hello world'
my_str="Sandeep"


# In[36]:


my_str.isalpha() or str_example.isnum()


# ## Lists

# In[37]:


type([])


# In[40]:


lst_example=[]


# In[41]:


type(lst_example)


# In[43]:


lst=list()


# In[44]:


type(lst)


# In[46]:


lst=['mathematics','chemistry',100,50,60,10]


# In[47]:


len(lst)


# In[49]:


type(lst)


# ## Append

# In[50]:


# Append is used to add elements in the list 
lst.append("sandeep")


# In[51]:


lst


# ## Indexing

# In[54]:


lst[2]


# In[55]:


lst[5]


# In[58]:


lst[1:6]


# ## Insert

# In[60]:


lst.insert(2,"car")


# In[61]:


lst


# In[62]:


lst=[1,2,3]


# In[67]:


lst.append([4,5])


# In[65]:


lst


# ## Extend Method

# In[70]:


lst.extend([6,7])


# In[71]:


lst


# ## Various Operations we can perform in the list

# In[72]:


lst=[1,2,3,4,5]


# In[73]:


sum(lst)


# In[91]:


lst*2


# In[96]:


lst*4


# ## pop() Method

# In[74]:


lst.pop()


# In[75]:


lst


# In[76]:


lst.pop(1)


# In[77]:


lst


# ## count(): calculate total  occurance of given element of list

# In[78]:


lst=[1,2,2,3,4,5]


# In[79]:


lst.count(2)


# In[80]:


lst


# In[81]:


len(lst)# calculate the totallength of the list


# In[86]:


#index(): Retuens the index of first occurance. Start and End index are not necessary parameters
lst.index(2)


# In[88]:


lst.index(2,1,4)


# In[89]:


# Min and Max
min(lst)


# In[90]:


max(lst)


#  ## Sets

# In[2]:


# Defining an empty set
set_var=set()
print(set_var)
print(type(set_var))


# In[3]:


set_var={1,2,3,4,3}#doesn't take duplicate elements


# In[4]:


set_var


# In[6]:


set_var={"avengers","ironman","hitman"}
print(set_var)
type(set_var)


# In[7]:


# Inbuilt function in sets
set_var.add("Hulk")


# In[8]:


print(set_var)


# In[14]:


set1={"Avengers","hitman","Ironman"}
set2={"Avengers","hitman","Ironman","Hulk2"}


# In[15]:


# Intersection
set2.intersection(set1)


# In[18]:


# Intersection update
set2.intersection_update(set1)


# In[19]:


set2


# In[10]:


# Difference
set2.difference(set1)


# In[11]:


## Difference update
set2.difference_update(set1)


# In[12]:


print(set2)


# ## Dictionaries

# In[20]:


dic={}


# In[21]:


type(dic)


# In[22]:


dic={1,2,3,4}


# In[23]:


type(dic)


# In[29]:


## Let create a dictionary
my_dict={"car1":"Audi","car2":"BMW","car3":"Mercidies Benz"}


# In[28]:


type(my_dict)


# In[32]:


## Access the items involved in keys
my_dict['car1']


# In[33]:


# We can even loop through the dictionaries keys
for x in my_dict:
    print(x)


# In[36]:


# We can even loop through the dictionaries values
for x in my_dict.values():
    print(x)


# In[37]:


# We can also check both keya and values
for x in  my_dict.items():
    print(x)


# In[38]:


## Adding items in Dictionaries
my_dict["car4"]="Audi 2.0"


# In[39]:


my_dict


# In[40]:


# Overridden
my_dict['car1']='maruthi'


# In[41]:


my_dict


# ## Nested Dictionary

# In[43]:


car1_model={"mercedes":1960}
car2_model={"audi":1970}
car3_model={"ambassador":1980}
car_type={'car1':car1_model,'car2':car2_model,'car3':car3_model}


# In[44]:


print(car_type)


# In[46]:


# Accessing the items in the dictionary
print(car_type['car1'])


# In[47]:


print(car_type['car1']['mercedes'])


# ## Tuple

# In[48]:


#  Create an empty tuple
my_tuple=tuple()


# In[49]:


type(my_tuple)


# In[50]:


my_tuple=()


# In[51]:


type(my_tuple)


# In[52]:


my_tuple=("sandeep","karthik","ram")


# In[ ]:


my_tuple[0]='naik'  # doesn't support item assignment


# In[54]:


print(type(my_tuple))
print(my_tuple)


# In[55]:


type(my_tuple)


# In[56]:


# Inbuilt function
my_tuple.count('sandeep')


# In[57]:


my_tuple.index('karthik')


# ## Numpy Tutorials

#    numpy is a general purpose processing package.It provides high performance multi-dimensional array object and tools for working with these arrays. It is ther fundamental package for scientific computing in python.
#    
#   ## ARRAY
# 
# An arrray is a data structure that stores of same data type. In python this is the main difference between arrays and lists.
# While python list can conatains values corresponding to different data types. Arrays in python can conatains values corresponding to same data types

# In[ ]:




