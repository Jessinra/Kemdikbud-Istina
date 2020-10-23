#!/usr/bin/env python
# coding: utf-8

# # Download all images

# In[ ]:


import json
import re


# In[ ]:


with open("images.json") as f:
    data = json.load(f)


# In[ ]:


images_list = [v["guid"] for _, v in data.items()]


# In[ ]:


with open("attachments.json") as f:
    data = json.load(f)


# In[ ]:


attachments_list = [v["guid"] for _, v in data.items()]


# In[ ]:


def migrate_domain(url):
    return re.sub("dikdas.kemdikbud.go.id", "dikdasmen.kemdikbud.go.id", url)


# In[ ]:


images_list = [migrate_domain(x) for x in images_list]
attachments_list = [migrate_domain(x) for x in attachments_list]


# ## Download and save

# In[ ]:


import urllib.request
from tqdm import tqdm
import os


# In[ ]:


def mkdir(path):
    try:
        os.makedirs(path)
    except Exception as e:
        pass


# In[ ]:


download_dir = os.getcwd() + "/wp-content/uploads"


# In[ ]:


for url in tqdm(images_list):
    split = url.split("http://dikdasmen.kemdikbud.go.id/wp-content/uploads")
    folder_filename = split[-1]
    
    split = folder_filename.split("/")
    folder = "/".join(split[:-1])

    mkdir(download_dir + folder)
    
    urllib.request.urlretrieve(url, download_dir + folder_filename)


# In[ ]:


for url in tqdm(attachments_list):
    split = url.split("http://dikdasmen.kemdikbud.go.id/wp-content/uploads")
    folder_filename = split[-1]
    
    split = folder_filename.split("/")
    folder = "/".join(split[:-1])

    mkdir(download_dir + folder)
    
    urllib.request.urlretrieve(url, download_dir + folder_filename)


# In[ ]:



