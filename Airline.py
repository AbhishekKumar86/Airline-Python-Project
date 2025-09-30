#!/usr/bin/env python
# coding: utf-8

# # Airline Analysis

# #### Import essentials libariers

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# #### import our datatsets

# In[2]:


df=pd.read_csv(r"D:\airlines_flights_data.csv")


# In[3]:


df.head()


# # Clean the dataset

# #### remove the index column

# In[4]:


df.drop(columns="index", inplace=True)


# In[10]:


df.head()


# #### Get the some info about dataset

# In[6]:


df.info()


# #### Get some statistical summary

# In[7]:


df.describe()


# # What are the airline in the dataset, accompanied by their frequencies?
# 

# #### Checing how many airlines in the dataset?
# 

# In[8]:


df["airline"].nunique()


# In[9]:


df["airline"].unique()


# #### "There are six airlines in this dataset, and the names of the airlines are: SpiceJet, AirAsia, Vistara, GO_FIRST, Indigo, and Air_India".

# #### Show all the Airlines with their numbers of flights in Bar Graph

# In[12]:


df_1=df["airline"].value_counts()
df_1


# In[14]:


colors=['red', 'magenta', 'blue', 'orange', 'purple', 'cyan', 'Green']
plt.bar(df_1.index, df_1.values, color=colors)
plt.xlabel("Airline")
plt.ylabel("No of flights")
plt.title("Flight Count by Airline")
plt.tight_layout()
plt.show()


# #### "We found that Vistara has the highest number of flights, with approximately 127,859, while SpiceJet has the lowest."

# # Show Bar Graph Representing the Deparature time and Arrival Time.

# In[15]:


df_2=df["departure_time"].value_counts()
df_2


# #### Showing the Arrival time for the flights.

# In[16]:


df_3=df["arrival_time"].value_counts()
df_3


# #### Create Subolots

# In[17]:


plt.figure(figsize=(16,4))
plt.subplot(1,2,1)
plt.bar(df_3.index, df_3.values, color=["r","b"])
plt.title("Arrival Time with counts")
plt.ylabel("No of counts")
plt.subplot(1,2,2)
plt.bar(df_2.index, df_2.values, color=["g","black"])
plt.title("Deparature Time with counts")
plt.show()


# #### Most flights are scheduled to Arrival during "Night" and Deparature during Morning, based on the frequency of arrival and departure time categories.

# # Show  the Bar Graphs representing the  Source City & Destination City

# In[19]:


df.head()


# #### Showing the Source City of the flights

# In[20]:


df["source_city"].value_counts()


# #### Showing the Destination City of the flights

# In[21]:


df["destination_city"].value_counts()


# #### Showing the Source City & Destination City for the flights with their counts

# In[22]:


plt.figure(figsize=(16,4))
plt.subplot(1,2,1)
plt.barh(df["source_city"].value_counts().index, df["source_city"].value_counts().values, color=["r","g"] )
plt.title("Source City with no.of flights")
plt.xlabel("No of flights")
plt.subplot(1,2,2)
plt.barh(df["destination_city"].value_counts().index, df["destination_city"].value_counts().values, color=["y","b"] )
plt.title("Destination City with no.of flights")
plt.show()



# #### The dataset shows that the most common source city is "Delhi" with 61343 flights, while the most frequent destination city is Mumbai with 59097 flights.

# # Does the ticket price change based on deprature time and arrival time?

# ##### Checking the Mean Ticket Price based on the Departure Time

# In[23]:


df.groupby("departure_time")["price"].mean()


# ##### Checking the Mean Ticket Price based on the Arrival Time
# 

# In[24]:


df.groupby("arrival_time")["price"].mean()


# In[25]:


plt.figure(figsize=(10,4))
sns.barplot(x="departure_time", y="price", data = df, hue= "airline", palette="magma")

plt.show()


# In[27]:


df.head()


# In[28]:


plt.figure(figsize=(10,4))
sns.barplot(x="arrival_time", y="price", data = df, hue="airline", palette="viridis")

plt.show()


# In[ ]:





# # How  the price changes with change in Source and Destination?
# 

# In[29]:


df.groupby("source_city")["price"].mean()


# In[30]:


df.groupby("destination_city")["price"].mean()


# In[31]:


sns.relplot(x="destination_city", y="price", data=df, col="source_city", kind="line")
plt.show()


# # How the price affected when ticket are brought in just 1 or 2 days before departure?
# 

# In[32]:


df.groupby("days_left")["price"].mean()


# In[33]:


sns.relplot(x="days_left", y="price", data=df, kind="line")
plt.show()


# #### The ticket prices are generally highest when purchased 1 or 2 days before the departure date. Interestingly, tickets bought just 1 day before departure tend to be slightly cheaper than those purchased 2, 3, or 4 days in advance. This may be due to the presence of last-minute vacant seats, which airlines often discount to ensure full occupancy.

# # How does the ticket price vary between Economy and Business class?

# In[34]:


df.groupby("class")["price"].mean()


# #### We have notice that Business class tickets are on average approximately 8 times more expensive than economy class tickets.

# # What will be the average price of Vistara Airline for a flight from Delhi to Hyderabad in Business Class?
# 

# In[35]:


df[(df["airline"]=="Vistara") & (df["source_city"] == "Delhi") 
   & (df["destination_city"]=="Hyderabad") & (df["class"]=="Business")]["price"].mean()


# #### The result — ₹47,939.84 — is the average price of Vistara Airline.

#  

# In[ ]:





# In[ ]:




