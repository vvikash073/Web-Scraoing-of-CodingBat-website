#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup


# In[2]:


user_agent = UserAgent()


# In[3]:


url='https://codingbat.com/java'
page = requests.get(url,headers={'user-agent':user_agent.chrome})
soup = BeautifulSoup(page.content,'lxml')
base_url ='https://codingbat.com'


# # p1

# In[9]:


all_divs=soup.find_all('div',class_='summ')
print(all_divs)


# In[8]:


all_links=[base_url + div.a['href'] for div in all_divs]
print(all_links)


# # p2

# In[24]:


for link in all_links:
    second = requests.get(link,headers={'user_agent':user_agent.chrome})
    second_soup = BeautifulSoup(second.content,'lxml')
    div= second_soup.find('div',class_='tabc')
    question_links = [base_url + td.a['href'] for td in div.table.find_all('td')]

    
    #p2.1
    
    for question_link in question_links:
        final_page = requests.get(question_link)
        final_soup= BeautifulSoup(final_page.content,'lxml')
        indent_div= final_soup.find('div',class_='indent')
        problem_statement = indent_div.table.div.string
    
        sibling_statement = indent_div.table.div.next_siblings
        
        examples=[sibling for sibling in sibling_statement if sibling.string is not None]
        print(problem_statement)
        for example in examples:
              print(example)

        print('\n')

