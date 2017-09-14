
# coding: utf-8

# # 1. Introduction

# ## Guidelines
# Please complete the assignment inside this notebook. Make sure the code can be executed easily.
# 
# - Write production-ready code.
# - Create unit tests for your code where applicable.
# - Add comments and documentation strings for all methods. Also discuss your design choices.
# - Discuss the complexity (Big O notation) of your solutions, both memory wise and performance wise.
# - Try to stick to the most popular scientific Python libraries.

# ## Input data
# You should have received three csv files. Each csv-file represents the locations where a person was stationary for a certain amount of time. 
# The csv-files contain the following fields:
# 
# - Latitude: The latitude of the detected GPS coordinates Longitude: The longitude of the detected GPS coordinates
# - Timestamp: The start time of the stationary in the following format:
#     - YYYY = year
#     - MM = month of year
#     - dd = day of month
#     - HH=hourofday
#     - mm = minute of hour
#     - Z = timezone offset
# - Duration: The length of time the person was stationary (in milliseconds)
#     
# All questions in this assignment are related to this data.

# In[15]:

# import statements go here.
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib  import cm
import numpy as np
import random
import math
from sklearn.neighbors import KDTree
# get_ipython().magic(u'matplotlib inline')


# # 2. Programming skills

# ## Question 1: Data parsing
# - Create the code needed to read and parse the data.
# - Print out some summary statistics of the data
#     - e.g. Average number of places visited per day
#     - e.g. Median distance traveled between two subsequent stationary locations
#     - ...

# In[16]:

def read_csv (filename):
    df = pd.read_csv (filename, sep = ';')
    # convert string to datetime
    df['time'] = pd.to_datetime (df['start_time(YYYYMMddHHmmZ)'])
    df.rename (columns={'start_time(YYYYMMddHHmmZ)':'start_time'}, inplace = True)
    return df


# In[17]:

# read CSV files
person1 = read_csv ("person.1.csv")
person2 = read_csv ("person.2.csv")
person3 = read_csv ("person.3.csv")


# In[18]:

# print first few lines of each data
print (person1.head (n=2))
print (person2.head (n=2))
print (person3.head (n=2))


# In[19]:

# visualize the visited place in one day of one person
def visualize_visits (df):
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(111)
    ax.set_xlabel("latitude",fontsize=12)
    ax.set_ylabel("longitude",fontsize=12)
    ax.grid(True,linestyle='-',color='0.75')
    z = df.time.apply(lambda x:x.hour)
    z = z/8
    ax.scatter(x = df['latitude'], y = df['longitude'], s=40,
               c = z, marker = 'o', cmap = cm.jet );
    plt.show()


# In[20]:

def sample(df, n):
    # sample n rows from a pandas dataframe
    return df.ix[random.sample(df.index, n)]


# In[21]:

# visualize moves of a person
visualize_visits (person1)


# In[22]:

visualize_visits (person2)


# In[23]:

visualize_visits (person3)


# In[24]:

def get_distances (df):
    # get travelled distances
    N = len (df.index)
    distances = []
    days = df.time.apply (lambda x:x.day)
    for i in xrange (N - 2):
        if days[i] == days[i+1]:
            distance = math.sqrt ((df['latitude'][i] - df['latitude'][i + 1])**2 
                                  + (df['longitude'][i] - df['longitude'][i + 1])**2)
            distances.append (distance)
    return distances


# In[25]:

# get median
print ('Median of moving distances of person 1: ' + str(np.median (get_distances (person1))))
print ('Median of moving distances of person 2: ' + str(np.median (get_distances (person2))))
print ('Median of moving distances of person 3: ' + str(np.median (get_distances (person3))))


# ## Question 2: Data lookup
# Create a method that generates a lookup table allowing us to effiently check whether or not a user has ever visited a location even if the new location is not exactly the same as the visited location (some noise is added to the longitude/latitude pairs).

# In[26]:

def build_visited_database (df):
    # using KDTree to store the visited information
    latitude = df['latitude'].tolist()
    longitude = df['longitude'].tolist()
    X = [list(a) for a in zip(latitude, longitude)]
    tree = KDTree (X, leaf_size =10)
    return tree

def check_visited (place, kdTree, distance_threshold = 1):
    # check if a person visited place within the distance threshold
    dist, ind = kdTree.query(place, k=1) 
    if dist[0] < distance_threshold:
        return True
    return False


# In[27]:

# test the solution
db1 = build_visited_database (person1)
place1 = np.array ([49,73])
print (check_visited(place1, db1))
place1 = np.array ([-49,-73])
print (check_visited(place1, db1))


# # 3. Machine learning skills

# ## Question 1: Home and work detection
# The goal of this question, is to design an algorithm that allows us to distinguish the likely home locations of a user from his likely work locations.
# 
# Note that a person might have multiple home and work locations, or might not have a work location at all. Also note that the data might be noise, incorrect and/or incomplete.
# 
# Discuss your choice of algorithms, rules, methods, distance measures, etc.

# In[28]:


    


# In[ ]:

cluster_visited (person1)


# ## Question 2: Social graph
# - Try to uncover the geo-spatial similarities between the users' data. Do users visit similar places? Are they likely to know each other?
# - Figure out a way to describe how 'socially active' each user is, by designing some kind of action radius metric. This metric should should take into account how many places a user visits, how far these places are away from each other, and how long the user stays there. The metric should allow us to compare users and to flag the most socially active one.

# In[ ]:



