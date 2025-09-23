#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[5]:

#data imputer module
import pandas as pd
data = {
    "Name": ["Arun", "Meena", "Raj", "Priya"],
    "Age": [25, 30, 22, 28],
    "Department": ["HR", "IT", "Finance", "Marketing"],
    "Salary": [40000, 50000, 35000, 45000]}
df = pd.DataFrame(data)
print(df)
df.to_csv("C:\\Users\\akila\\OneDrive\\Desktop\\sea.csv", index=False)

print("Data saved to sea")


# In[ ]:





# In[ ]:




