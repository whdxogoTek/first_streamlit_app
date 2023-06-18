
import streamlit 
import pandas
import requests
import snowflake.connector 
from urllib.error import URLError 
import seaborn
import numpy
import random

streamlit.title("식사를 합시다. 😎")
streamlit.markdown('#### 점심식당 정하기!')    
streamlit.text('🥗 더 이상 어디갈지 고민은 그만!')
streamlit.text('🎯 즐겁고 빠르게 점심식당을 정해봐요!')     

streamlit.markdown('#### 점심식당 추가하기:')      
streamlit.text('📝 식당을 추가해봅시다.')  

# ------------------------------------------------------------
def get_test_RESTAURANT():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT * FROM FACT_RESTAURANT")
        return my_cur.fetchall()
    
def insert_row_snowflake(new_RESTAURANT):
    if not new_RESTAURANT:
        return "식당을 입력하세요!"
    
    with my_cnx.cursor() as my_cur:
        my_cur.execute("INSERT INTO test_food VALUES ('" +new_RESTAURANT+ "' )")
    
    return "식당을 추가했습니다~🤗" 

# -----------------------------------------------------------------
Data_Restaurant_ID = streamlit.text_input('식당을 추가하세요')
Data_Restaurant_Type = streamlit.text_input('식당 종류를 작성해주세요')
Data_Restaurant_Add_Name = streamlit.text_input('식당을 추가한 당신의 성함을 작성해주세요')

if streamlit.button('식당 데이터 확인 ✅'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    streamlit.write(insert_row_snowflake(Data_Restaurant_ID))
    streamlit.write(insert_row_snowflake(Data_Restaurant_Type))
    streamlit.write(insert_row_snowflake(Data_Restaurant_Add_Name))
    my_data_rows = get_test_RESTAURANT()
    my_cnx.close()
    streamlit.dataframe(my_data_rows)
