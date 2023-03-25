#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
marks_data=pd.read_csv("marksdata2.csv")
marks_data


# In[4]:


dataMapping={
    "By public vehicle":1,
    "By private vehicle":0
}


# In[5]:


marks_data["TravelMethod"]=marks_data["TravelMethod"].map(dataMapping)
marks_data


# In[6]:


dataMapping={
    "Male":1,
    "Female":0
}


# In[7]:


marks_data["Gender"]=marks_data["Gender"].map(dataMapping)
marks_data


# In[8]:


dataMapping={
    "Yes":1,
    "No":0
}


# In[9]:


marks_data["PartTimeJob"]=marks_data["PartTimeJob"].map(dataMapping)
marks_data


# In[10]:


dataMapping={
    "Less than 15 minutes":1,
    "Less than 30 minutes":2,
    "Less than 1 hour":3,
    "More than 1 hour":4
}


# In[11]:


marks_data["TravelTime"]=marks_data["TravelTime"].map(dataMapping)
marks_data


# In[12]:


dataMapping={
    "Yes":1,
    "No":0
}


# In[13]:


marks_data["Relationship"]=marks_data["Relationship"].map(dataMapping)
marks_data


# In[14]:


dataMapping={
    "Holds a degree":1,
    "Secondary school (grade 6 - 12)":2,
    "Primary school (grade 1 - 5)":3
}


# In[15]:


marks_data["Father's_education"]=marks_data["Father's_education"].map(dataMapping)
marks_data["Mother's_education"]=marks_data["Mother's_education"].map(dataMapping)
marks_data


# In[16]:


dataMapping={
    "Less than 1 hour":1,
    "Less than 2 hours":2,
    "Less than 5 hours":3,
    "More than 5 hours":4,
    "None":5
}


# In[17]:


marks_data["StudyHours"]=marks_data["StudyHours"].map(dataMapping)
marks_data


# In[18]:


dataMapping={
    "Sometimes":1,
    "Always":2,
    "Never":3
}


# In[19]:


marks_data["AttendenceLecs"]=marks_data["AttendenceLecs"].map(dataMapping)
marks_data["Concentrate"]=marks_data["Concentrate"].map(dataMapping)

marks_data


# In[20]:


dataMapping={
    "Yes":1,
    "No":0
}


# In[21]:


marks_data["Friends"]=marks_data["Friends"].map(dataMapping)
marks_data["extra curricular"]=marks_data["extra curricular"].map(dataMapping)

marks_data


# In[22]:


dataMapping={
    "Less than 1 hour":1,
    "Less than 2 hours":2,
    "More than 2 hours":3,
    "None":4
}


# In[23]:


marks_data["SocialMediaTime"]=marks_data["SocialMediaTime"].map(dataMapping)
marks_data


# In[24]:


dataMapping={
    "Self studying":1,
    "Group studying along with friends":2,
    "Help of a tutor":3,
    "Self studying, Group studying along with friends":4,
    "Self studying, Help of a tutor":5,
    "Group studying along with friends, Help of a tutor":6,
    "Self studying, Group studying along with friends, Help of a tutor":7
}


# In[25]:


marks_data["HowYouPrepare"]=marks_data["HowYouPrepare"].map(dataMapping)
marks_data


# In[26]:


dataMapping={
    "I study regularly":1,
    "Closest date to the exam":2,
}


# In[27]:


marks_data["StudyPattern"]=marks_data["StudyPattern"].map(dataMapping)
marks_data


# In[28]:


dataMapping={
    "Topper student (85-100)":1,
    "Above average (65 - 85)":2,
    "Average (40 - 65)":3,
    "Below average (less than 40)":4
}


# In[29]:


marks_data["Rate yourself"]=marks_data["Rate yourself"].map(dataMapping)
marks_data


# In[30]:


x= marks_data.drop(columns='Marks')
y= marks_data['Marks']


# In[31]:


get_ipython().system('pip install imblearn')


# In[32]:


from imblearn import over_sampling


# In[33]:


import numpy as np
import seaborn as sns
from sklearn import preprocessing
from collections import Counter


# In[34]:


from imblearn.over_sampling import RandomOverSampler
ros = RandomOverSampler(random_state=0)
x_resampled,y_resampled=ros.fit_resample(x,y)
print(sorted(Counter(y_resampled).items()),y_resampled.shape)


# In[35]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x_resampled,y_resampled,test_size=0.2)


# In[36]:


from sklearn.preprocessing import StandardScaler


# In[37]:


scaler = StandardScaler()


# In[38]:


x_train_scaled = scaler.fit_transform(x_train)


# In[39]:


x_test_scaled = scaler.transform(x_test)


# In[40]:


x_test_scaled


# In[41]:


from sklearn.linear_model import LogisticRegression


# In[42]:


log_reg = LogisticRegression(random_state =0).fit(x_train_scaled, y_train)


# In[43]:


log_reg.predict(x_train_scaled)


# In[44]:


log_reg.score(x_train_scaled, y_train)


# In[45]:


log_reg.score(x_test_scaled, y_test)


# In[46]:


x_resampled['Marks'] = y_resampled


# In[47]:


x_resampled


# In[48]:


x_resampled.to_csv('/Users/kamilthenuwara/Desktop/data10.csv')


# In[50]:


predictions=log_reg.predict([[1,0,3,1,0,2,2,2,2,2,1,3,1,7,2,2]])
predictions


# In[ ]:




