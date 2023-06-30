
import streamlit as st
import pandas as pd
import requests
import snowflake.connector 
from urllib.error import URLError 
import seaborn
import numpy
import random
from datetime import date

# 랜덤 복원추출 필요
# 그냥 눌렀을 때 뜨는거 if문 필요 


st.title("식사를 합시다. 😎")
st.markdown('#### 점심식당 정하기!')    
st.text('🥗 더 이상 어디갈지 고민은 그만!')
st.text('🎯 즐겁고 빠르게 점심식당을 정해봐요!')     

st.markdown('#### 점심식당 추가하기:')      
st.text('📝 식당을 추가해봅시다.')  
# -------------------------------------------------------------------------
import streamlit as st
import snowflake.connector
import pandas as pd

# Establish Snowflake connection
my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
cursor = my_cnx.cursor()

# Create Streamlit input fields
restaurant_name = st.text_input('Enter the name of the restaurant')
restaurant_type = st.text_input('Write down the restaurant type')
added_by = st.text_input('Write down your name')

# Insert data into Snowflake table upon button press
# if st.button('Add Restaurant'):
#     insert_query = f"INSERT INTO FACT_RESTAURANT (Restaurant_ID, Restaurant_Type, Restaurant_Add_Name) VALUES ('{restaurant_name}', '{restaurant_type}', '{added_by}')"
#     cursor.execute(insert_query)
#     my_cnx.commit()
#     st.success('Restaurant added successfully!')

# Insert data into Snowflake table upon button press
if st.button('Add Restaurant'):
    # Get the current date
    current_date = date.today().isoformat()

    insert_query = f"INSERT INTO FACT_RESTAURANT (Restaurant_ID, data_added_ID, Restaurant_Add_Name, Restaurant_Type) VALUES ('{restaurant_name}', '{current_date}', '{added_by}', '{restaurant_type}')"
    cursor.execute(insert_query)
    my_cnx.commit()
    st.success('Restaurant added successfully!')


# Display accumulated data upon button press
if st.button('Get Food List'):
    select_query = "SELECT * FROM FACT_RESTAURANT"
    cursor.execute(select_query)
    results = cursor.fetchall()
    df = pd.DataFrame(results, columns=['Restaurant_ID', 'data_added_ID','Restaurant_Add_Name','Restaurant_Type'])
    st.write(df)

st.markdown('#### 오늘의 점심식당 Pick!:')     
st.text('이제 점심식당을 골라볼까요? 😋')    

# if st.button('Pick a Random Restaurant'):
#     select_query = "SELECT Restaurant_ID FROM FACT_RESTAURANT"
#     cursor.execute(select_query)
#     results = cursor.fetchall()
#     random_restaurant = random.choice(results)[0]
#     st.write("Randomly picked restaurant:", random_restaurant)
      

#     current_date_1 = date.today().isoformat()
#     insert_query_1 = f"INSERT INTO dimension_visit_table (Visit_Date, Restaurant_ID) VALUES ('{current_date_1}', '{random_restaurant}')"
#     cursor.execute(insert_query_1)

# -------------------------------------------------------------------------------


import random
import datetime

# Generate random restaurant ID
select_query = "SELECT Restaurant_ID FROM FACT_RESTAURANT"
cursor.execute(select_query)
results = cursor.fetchall()
random_restaurant = random.choice(results)[0]

# ...
import random
import datetime

# Generate random restaurant ID
select_query = "SELECT Restaurant_ID FROM FACT_RESTAURANT"
cursor.execute(select_query)
results = cursor.fetchall()
random_restaurant = random.choice(results)[0]

# ...

# if st.button('Pick a Random Restaurant'):
#     # Generate current date
#     current_date = datetime.date.today().isoformat()

#     # Check if a record with the same restaurant ID and current date already exists
#     select_query = f"SELECT COUNT(*) FROM dimension_visit_table WHERE Visit_Date = '{current_date}' AND Restaurant_ID = '{random_restaurant}'"
#     cursor.execute(select_query)
#     count = cursor.fetchone()[0]

#     if count == 0:
#         # Insert a new record if it doesn't already exist
#         insert_query = f"INSERT INTO dimension_visit_table (Visit_Date, Restaurant_ID) VALUES ('{current_date}', '{random_restaurant}')"
#         cursor.execute(insert_query)
#         st.write("Randomly picked restaurant:", random_restaurant)
#     else:
#         st.write("Restaurant already picked for today:", random_restaurant)


# --------------------------------------------------------------------------------------------------------------------------
import random
import datetime

# Initialize the randomly selected restaurant for the day
random_restaurant = None

# ...

if st.button('Pick a Random Restaurant'):
    # Generate current date
    current_date = datetime.date.today().isoformat()

    if random_restaurant is None:
        # Select a new random restaurant if it hasn't been selected yet for the day
        select_query = "SELECT Restaurant_ID FROM FACT_RESTAURANT"
        cursor.execute(select_query)
        results = cursor.fetchall()
        random_restaurant = random.choice(results)[0]

        # Insert the initial record for the day
        insert_query = f"INSERT INTO dimension_visit_table (Visit_Date, Restaurant_ID) VALUES ('{current_date}', '{random_restaurant}')"
        cursor.execute(insert_query)
    else:
        # Check if a record with the same restaurant ID and current date already exists
        select_query = f"SELECT COUNT(*) FROM dimension_visit_table WHERE Visit_Date = '{current_date}' AND Restaurant_ID = '{random_restaurant}'"
        cursor.execute(select_query)
        count = cursor.fetchone()[0]

        if count == 0:
            # Insert a new record if it doesn't already exist
            insert_query = f"INSERT INTO dimension_visit_table (Visit_Date, Restaurant_ID) VALUES ('{current_date}', '{random_restaurant}')"
            cursor.execute(insert_query)

    st.write("Randomly picked restaurant:", random_restaurant)
































# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# cursor = my_cnx.cursor()
# query = "SELECT * FROM FACT_RESTAURANT"
# cursor.execute(query)

# results = cursor.fetchall()
# for row in results:
#     print(row)



# ------------------------------------------------------------
# def get_test_food():
#     with my_cnx.cursor() as my_cur:
#         my_cur.execute("SELECT * FROM FACT_RESTAURANT")
#         return my_cur.fetchall()
       
# def insert_row_snowflake(new_fruit):
#     if not new_fruit:
#         return "Enter fruits"
    
#     with my_cnx.cursor() as my_cur:
#         my_cur.execute("INSERT INTO Fact_Restaurant(Restaurant_ID) VALUES ('" + new_fruit + "' )")
#        # my_cur.execute("INSERT INTO Fact_Restaurant(Restaurant_Type) VALUES ('" + new_fruit + "' )")
#        # my_cur.execute("INSERT INTO Fact_Restaurant(Restaurant_Add_Name) VALUES ('" + new_fruit + "' )")
    
#     return "Thanks for adding " + new_fruit
# # add_my_fruit = streamlit.text_input('What food would you like to add?')
# Data_Restaurant_ID = streamlit.text_input('식당을 추가하세요')
# # Data_Restaurant_Type = streamlit.text_input('식당 종류를 작성해주세요')
# # Data_Restaurant_Add_Name = streamlit.text_input('식당을 추가한 당신의 성함을 작성해주세요')

# if streamlit.button('Get food List'):
#     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#     streamlit.write(insert_row_snowflake(Data_Restaurant_ID))
#     # streamlit.write(insert_row_snowflake(Data_Restaurant_Type))
#     # streamlit.write(insert_row_snowflake(Data_Restaurant_Add_Name))
#     my_data_rows = get_test_food()
#     my_cnx.close()
#     streamlit.dataframe(my_data_rows)









# def get_test_RESTAURANT():
#     with my_cnx.cursor() as my_cur:
#         my_cur.execute("SELECT * FROM FACT_RESTAURANT")
#         return my_cur.fetchall()
    
# def insert_row_snowflake(new_RESTAURANT):
#     #if not new_RESTAURANT:
#     #    return "식당을 입력하세요!"
    
#     with my_cnx.cursor() as my_cur:
#         my_cur.execute("INSERT INTO Fact_Restaurant(Restaurant_ID) VALUES ('" + new_RESTAURANT + "' )")
    
#     return "Thanks for adding " + new_RESTAURANT

# # -----------------------------------------------------------------
# Data_Restaurant_ID = streamlit.text_input('식당을 추가하세요')
# Data_Restaurant_Type = streamlit.text_input('식당 종류를 작성해주세요')
# Data_Restaurant_Add_Name = streamlit.text_input('식당을 추가한 당신의 성함을 작성해주세요')

# if streamlit.button('식당 데이터 확인 ✅'):
#     my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#     streamlit.write(insert_row_snowflake(Data_Restaurant_ID))
#     # streamlit.write(insert_row_snowflake(Data_Restaurant_Type))
#     # streamlit.write(insert_row_snowflake(Data_Restaurant_Add_Name))
#     my_data_rows = get_test_RESTAURANT()
#     my_cnx.close()
#     streamlit.dataframe(my_data_rows)
