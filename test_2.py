
import streamlit 
import pandas
import requests
import snowflake.connector 
from urllib.error import URLError 
import seaborn
import numpy
import random

streamlit.markdown('#### 점심식당 정하기!')    
streamlit.text('🥗 더 이상 어디갈지 고민은 그만!')
streamlit.text('🎯 즐겁고 빠르게 점심식당을 정해봐요!')     

streamlit.markdown('#### 점심식당 추가하기:')      
streamlit.text('📝 식당을 추가해봅시다.')  
