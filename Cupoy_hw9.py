
# coding: utf-8

# 作業目標:<br>
# 1.讀取各種檔案格式<br>
# 2.輸出各種檔案格式<br>

# 作業重點:<br>
# 1.不同檔案讀取方式皆不同，須了解檔案格式中的邏輯，例如:csv是以逗號分隔<br>
# 2.讀取、輸出檔案的程式碼不同，須注意使用方式

# 題目: <br>
# 讀取資料夾中boston.csv讀取其欄位CHAS、NOX、RM，輸出成.xlsx檔案

# In[2]:


import pandas as pd


# In[ ]:


#讀取資料夾中boston.csv讀取其欄位CHAS、NOX、RM，輸出成.xlsx檔案


# In[3]:


doggy = pd.read_csv('boston.csv', usecols=['CHAS', 'NOX', 'RM'])

doggy


# In[6]:


doggy.to_excel('thisdoggo.xlsx',sheet_name='shortdoggy')


# In[7]:


pd.read_excel('thisdoggo.xlsx')

