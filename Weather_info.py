
# coding: utf-8

# In[7]:


import requests
from bs4 import BeautifulSoup
response = requests.get('https://pythondojang.bitbucket.io/weather/observation/currentweather.html')

soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table', {'class' : 'table_develop3'})#<table class = "table_develop3">

data = []

for tr in table.find_all('tr'): # 모든 <tr>태그를 찾아서 반복
    tds = list(tr.find_all('td')) # <td>태그를 찾아 리스트로 만듦
    for td in tds:
        if(td.find('a')): #<a>태그가 있으면 , 지점인지 확인
            point = td.find('a').text #지점 가져옴
            temperature = tds[5].text
            humidity = tds[9].text
            data.append([point, temperature, humidity])
print(data)

# In[8]:


with open('weather.csv', 'w') as file:
    file.write('point, temperature, humidity \n')
    for i in data:
        file.write('{0}, {1}, {2} \n'.format(i[0],i[1],i[2]))

# 크롤링, CSV파일 저장


# In[9]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd #데이터 저장 처리 패키지
import matplotlib as mpl # 그래프 그리기 패키지
import matplotlib.pyplot as plt # 그래프 그리기 패키지

df = pd.read_csv('weather.csv', index_col = 'point', encoding = 'euc-kr')
df


# In[11]:


city_df = df.loc[['서울', '인천', '대전', '대구', '광주', '부산', '울산']]
city_df


# In[12]:


df.loc['서울']


# In[13]:


# Windows 한글 폰트 설정
font_name = mpl.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

# 차트 종류, 제목, 차트 크기, 범례, 폰트 크기 설정
ax = city_df.plot(kind='bar', title='날씨', figsize=(12, 4), legend=True, fontsize=12)
ax.set_xlabel('도시', fontsize=12)          # x축 정보 표시
ax.set_ylabel('기온/습도', fontsize=12)     # y축 정보 표시
ax.legend(['기온', '습도'], fontsize=12)    # 범례 지정


# In[30]:


city_df

