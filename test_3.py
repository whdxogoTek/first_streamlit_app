import streamlit as st
import pandas as pd
import requests
import snowflake.connector 
from urllib.error import URLError 
import seaborn
import numpy
import random
from datetime import date

st.title("식사를 합시다. 😎")
st.markdown('#### 점심식당 정하기!')    
st.text('🥗 더 이상 어디갈지 고민은 그만!')
st.text('🎯 즐겁고 빠르게 점심식당을 정해봐요!')     

st.markdown('#### 점심식당 추가하기:')      
st.text('📝 식당을 추가해봅시다.')  

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
cursor = my_cnx.cursor()

# Create Streamlit input fields
restaurant_name = st.text_input('식당이름을 입력하세요')
restaurant_type = st.text_input('식당의 종류를 작성해주세요 ex) 한식, 일식')
added_by = st.text_input('식당을 추가한 당신의 이름을 작성해주세요')

if st.button('식당 추가'):
    # Get the current date
    current_date = date.today().isoformat()

    insert_query = f"INSERT INTO Insert_Restaurant (I_Restaurant_ID, I_data_added_ID, I_Restaurant_Add_Name, I_Restaurant_Type) VALUES ('{restaurant_name}', '{current_date}', '{added_by}', '{restaurant_type}')"
    cursor.execute(insert_query)
    my_cnx.commit()
    st.success('식당 추가 완료!')

if st.button('식당 데이터 보기'):
    select_query = "SELECT * FROM Insert_Restaurant"
    cursor.execute(select_query)
    results = cursor.fetchall()
    df = pd.DataFrame(results, columns=['I_Restaurant_ID', 'I_data_added_ID','I_Restaurant_Add_Name','I_Restaurant_Type'])
    st.write(df)

st.markdown('#### 오늘의 점심식당 Pick!:')     
st.text('이제 점심식당을 골라볼까요? 😋')    

select_query = "SELECT I_Restaurant_ID FROM Insert_Restaurant"
cursor.execute(select_query)
results = cursor.fetchall()
random_restaurant = random.choice(results)[0]

if st.button('오늘의 점심 선택하기'):
    # Generate current date
    current_date = date.today().isoformat()

    # Check if a record with the same restaurant ID and current date already exists
    select_query = f"SELECT COUNT(*) FROM Visit_Restaurant WHERE V_Visit_Date = '{current_date}' AND V_Restaurant_ID = '{random_restaurant}'"
    cursor.execute(select_query)
    count = cursor.fetchone()[0]

    if count == 0:
        # Insert a new record if it doesn't already exist
        insert_query = f"INSERT INTO dimension_visit_table (V_Visit_Date, V_Restaurant_ID) VALUES ('{current_date}', '{random_restaurant}')"
        cursor.execute(insert_query)
        st.write("오늘의 랜덤 식당!:", random_restaurant)
    else:
        st.write(random_restaurant)



