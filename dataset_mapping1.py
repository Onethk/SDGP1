#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
marks_data=pd.read_csv("marksdata2.csv")
marks_data


# In[2]:


dataMapping={
    "By public vehicle":1,
    "By private vehicle":0
}


# In[3]:


marks_data["TravelMethod"]=marks_data["TravelMethod"].map(dataMapping)
marks_data


# In[4]:


dataMapping={
    "Male":1,
    "Female":0
}


# In[5]:


marks_data["Gender"]=marks_data["Gender"].map(dataMapping)
marks_data


# In[6]:


dataMapping={
    "Yes":1,
    "No":0
}


# In[7]:


marks_data["PartTimeJob"]=marks_data["PartTimeJob"].map(dataMapping)
marks_data


# In[8]:


dataMapping={
    "Less than 15 minutes":1,
    "Less than 30 minutes":2,
    "Less than 1 hour":3,
    "More than 1 hour":4
}


# In[9]:


marks_data["TravelTime"]=marks_data["TravelTime"].map(dataMapping)
marks_data


# In[10]:


dataMapping={
    "Yes":1,
    "No":0
}


# In[11]:


marks_data["Relationship"]=marks_data["Relationship"].map(dataMapping)
marks_data


# In[12]:


dataMapping={
    "Holds a degree":1,
    "Secondary school (grade 6 - 12)":2,
    "Primary school (grade 1 - 5)":3
}


# In[13]:


marks_data["Father's_education"]=marks_data["Father's_education"].map(dataMapping)
marks_data["Mother's_education"]=marks_data["Mother's_education"].map(dataMapping)
marks_data


# In[14]:


dataMapping={
    "Less than 1 hour":1,
    "Less than 2 hours":2,
    "Less than 5 hours":3,
    "More than 5 hours":4,
    "None":5
}


# In[15]:


marks_data["StudyHours"]=marks_data["StudyHours"].map(dataMapping)
marks_data


# In[16]:


dataMapping={
    "Sometimes":1,
    "Always":2,
    "Never":3
}


# In[17]:


marks_data["AttendenceLecs"]=marks_data["AttendenceLecs"].map(dataMapping)
marks_data["Concentrate"]=marks_data["Concentrate"].map(dataMapping)

marks_data


# In[18]:


dataMapping={
    "Yes":1,
    "No":0
}


# In[19]:


marks_data["Friends"]=marks_data["Friends"].map(dataMapping)
marks_data["extra curricular"]=marks_data["extra curricular"].map(dataMapping)

marks_data


# In[20]:


dataMapping={
    "Less than 1 hour":1,
    "Less than 2 hours":2,
    "More than 2 hours":3,
    "None":4
}


# In[21]:


marks_data["SocialMediaTime"]=marks_data["SocialMediaTime"].map(dataMapping)
marks_data


# In[22]:


dataMapping={
    "Self studying":1,
    "Group studying along with friends":2,
    "Help of a tutor":3,
    "Self studying, Group studying along with friends":4,
    "Self studying, Help of a tutor":5,
    "Group studying along with friends, Help of a tutor":6,
    "Self studying, Group studying along with friends, Help of a tutor":7
}


# In[23]:


marks_data["HowYouPrepare"]=marks_data["HowYouPrepare"].map(dataMapping)
marks_data


# In[24]:


dataMapping={
    "I study regularly":1,
    "Closest date to the exam":2,
}


# In[25]:


marks_data["StudyPattern"]=marks_data["StudyPattern"].map(dataMapping)
marks_data


# In[26]:


dataMapping={
    "Topper student (85-100)":1,
    "Above average (65 - 85)":2,
    "Average (40 - 65)":3,
    "Below average (less than 40)":4
}


# In[27]:


marks_data["Rate yourself"]=marks_data["Rate yourself"].map(dataMapping)
marks_data


# In[31]:


from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

marks_data.drop(marks_data.columns[[0]], axis=1, inplace=True)
X=marks_data.drop(columns=['Marks'])
y=marks_data['Marks']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
model = DecisionTreeClassifier()
model.fit(X_train,y_train)
predictions=model.predict(X_train)

score=accuracy_score(y_train,predictions)
score


# In[ ]:




