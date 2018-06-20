
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


from sklearn import datasets,linear_model


# In[5]:


from sklearn.model_selection import train_test_split 


# In[6]:


from matplotlib import pyplot as plt


# In[7]:


import csv


# In[9]:


from sklearn.cross_validation import cross_val_score,cross_val_predict


# In[10]:


from sklearn import metrics


# In[11]:


def readMyFile(filename):
    score=[]
    test_Pass_Rate=[]
    test_Mean_Deviation=[]
    complaint_Responsiveness=[]
    document_Compliance=[]
    complaint_categories=[]
    with open(filename) as csvDataFile:
        csvReader=csv.reader(csvDataFile)
        for row in csvReader:
            score.append(row[13])
            test_Pass_Rate.append(row[14])
            test_Mean_Deviation.append(row[15])
            complaint_Responsiveness.append(row[16])
            document_Compliance.append(row[17])
            complaint_categories.append(row[18])
    
    return score, test_Pass_Rate,test_Mean_Deviation,complaint_Responsiveness,document_Compliance,complaint_categories
            


# In[14]:


score,test_Pass_Rate,test_Mean_Deviation,complaint_Responsiveness,document_Compliance,complaint_categories=readMyFile('R_all matrices.csv')


# In[15]:


df=pd.DataFrame({'test_Pass_Rate':test_Pass_Rate,
            'test_Mean_Deviation':test_Mean_Deviation,
            'complaint_Responsiveness':complaint_Responsiveness,
            'document_Compliance':document_Compliance,
            'complaint_categories':complaint_categories},
            index=range(0,15)
)


# In[16]:


df=df.drop(0)


# In[17]:


score=score[1:15]


# In[18]:


import numpy as np


# In[23]:


score=np.asarray(score,dtype="float64")


# In[24]:


lm=linear_model.LinearRegression()


# In[25]:


model=lm.fit(df,score)


# In[39]:


accuracyscore=cross_val_score(model,df,score,cv=6)


# In[40]:


accuracyscore


# In[31]:


predictions=cross_val_predict(model,df,score,cv=6)


# In[36]:


plt.scatter(score,predictions)
plt.xlabel("True Value")
plt.ylabel("Predictions")
plt.show()


# In[33]:


R_square=metrics.r2_score(score,predictions)


# In[34]:


R_square

