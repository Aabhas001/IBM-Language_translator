
# coding: utf-8

# In[1]:


get_ipython().system('pip install ibm_watson wget')


# In[2]:


from ibm_watson import LanguageTranslatorV3


# In[3]:


import json 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


# In[4]:


url_lt = 'https://api.kr-seo.language-translator.watson.cloud.ibm.com/instances/526e71aa-1909-4295-bf5d-977984689e80'


# In[5]:


apikey_lt = 't64o_yZHnLgVU6pG0IAq7uVNH0GlD6aB9komVXj4Qlkv'


# In[6]:


version_lt = '2020-07-20'


# In[7]:


authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)
language_translator


# In[8]:


from pandas.io.json import json_normalize

json_normalize(language_translator.list_identifiable_languages().get_result(),"languages")


# In[32]:


recognized_text = input("Enter text you want to translate")
model_id = input("Enter Language codes from above to convert in format of ab-cd - ")
translation_response = language_translator.translate(text=recognized_text, model_id= model_id)
translation_response


# In[33]:


translation = translation_response.get_result()
translation


# In[34]:


spanish_transaltion = translation['translations'][0]['translation']
spanish_transaltion


# In[22]:


model_id_1 = input("Enter Language codes from above to convert in format of ab-cd -")
translation_new = language_translator.translate(text = spanish_transaltion, model_id = model_id_1).get_result()


# In[23]:


transalation_eng = translation_new['translations'][0]['translation']
transalation_eng


# In[24]:


french_transaltion = language_translator.translate(text=transalation_eng, model_id='en-fr').get_result()


# In[25]:


french_transaltion['translations'][0]['translation']

