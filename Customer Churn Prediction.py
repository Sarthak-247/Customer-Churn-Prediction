#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[7]:


dataset= pd.read_csv(r"C:\Users\Prathmesh\OneDrive\Desktop\LinkedIn\Datasets\customer_churn_large_extended.csv")
print(dataset.head())


# In[14]:


yes_count= dataset['Churn'].value_counts().get('Yes',0)
No_count= dataset['Churn'].value_counts().get('No',0)

print("Total number of customers:")
print(yes_count+No_count)
print("Number of the Churned Customers:")
print(yes_count)
print("Number of the Non-Churned Customers:")
print(No_count)


# In[22]:


sns.countplot(x=dataset['Churn'])
plt.xlabel('Chrun Status',c="red")
plt.ylabel('Count',c="red")


# In[24]:


churn_rate=(yes_count/(yes_count+No_count))*100
print("The Churn rate for the data is:")
print(churn_rate)


# In[46]:


Churn_and_contract_relation=dataset.groupby("Contract")["Churn"].value_counts(normalize=True).unstack()*100
print(Churn_and_contract_relation)

Churn_and_contract_relation['Yes'].plot(kind='bar',color=['red','blue','green'])
plt.xlabel("Contract type")
plt.ylabel("Churn in %")


# In[45]:


sns.boxplot(x=dataset['Churn'],y=dataset["MonthlyCharges"])


# In[57]:


Not_churned=dataset[dataset["Churn"]=="Yes"]

payment=Not_churned["PaymentMethod"].value_counts()
print(payment)

payment.plot(kind="bar",color=['blue', 'green', 'orange', 'purple'])
plt.xlabel("PaymentMethod",c="red")
plt.ylabel("Count",c="red")


# In[ ]:




