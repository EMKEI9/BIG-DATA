#!/usr/bin/env python
# coding: utf-8

# In[1]:


import urllib.request


# In[2]:


client_id = "SD0DKeX9rskF9DIy4heT"
client_secret = "JrIO2TLrA5"


# In[4]:


encType = urllib.parse.quote("여행")


# In[5]:


url = "https://openapi.naver.com/v1/search/blog?query="+encType


# In[8]:


request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

print(rescode)


# In[9]:


if(rescode == 200):
    response_body = response.read()
    print(response_body.decode("utf-8"))
else:
    print("Error Code" + rescode)


# In[ ]:




