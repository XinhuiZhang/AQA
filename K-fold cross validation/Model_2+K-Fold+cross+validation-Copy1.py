
# coding: utf-8

# In[47]:


import pandas as pd


# In[48]:


from sklearn import datasets,linear_model


# In[49]:


from sklearn.model_selection import train_test_split 


# In[50]:


from matplotlib import pyplot as plt


# In[51]:


import csv


# In[52]:


from sklearn.cross_validation import cross_val_score,cross_val_predict


# In[53]:


from sklearn import metrics


# In[54]:


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
            complaint_categories.append(row[19])
    
    return score, test_Pass_Rate,test_Mean_Deviation,complaint_Responsiveness,document_Compliance,complaint_categories
            


# In[55]:


score,test_Pass_Rate,test_Mean_Deviation,complaint_Responsiveness,document_Compliance,complaint_categories=readMyFile('R_all matrices.csv')


# In[56]:


df=pd.DataFrame({
            #'test_Pass_Rate':test_Pass_Rate,
            #'test_Mean_Deviation':test_Mean_Deviation,
            'complaint_Responsiveness':complaint_Responsiveness,
            'document_Compliance':document_Compliance,
            'complaint_categories':complaint_categories},
            index=range(0,15)
)


# In[57]:


df=df.drop(0)


# In[58]:


score=score[1:15]


# In[59]:


import numpy as np


# In[60]:


score=np.asarray(score,dtype="float64")


# In[61]:


lm=linear_model.LinearRegression()


# In[62]:


model=lm.fit(df,score)


# In[63]:


accuracyscore=cross_val_score(model,df,score,cv=6)


# In[64]:


accuracyscore


# In[65]:


predictions=cross_val_predict(model,df,score,cv=6)


# In[66]:


plt.scatter(score,predictions)
plt.xlabel("True Value")
plt.ylabel("Predictions")
plt.show()


# In[67]:


R_square=metrics.r2_score(score,predictions)


# In[68]:


R_square

