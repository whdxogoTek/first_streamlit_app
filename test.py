
# import streamlit
# import snowflake.connector
#
import streamlit 
import pandas
import requests
import snowflake.connector 
from urllib.error import URLError 
import seaborn
import numpy
import random



# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_data_row = my_cur.fetchone()
# streamlit.text("Hello from Snowflake:")
# streamlit.text(my_data_row)

# #-----------------------------------------------------------------------------------

# streamlit.header("The Fruity List Contains:")
# def get_test_food():
#   with my_cnx.cursor() as my_cur:
#       my_cur.execute("select * from test_food ")
#       return my_cur.fetchall()
    
# def insert_row_snowflake(new_fruit):
#   with my_cnx.cursor() as my_cur:
#       my_cur.execute("insert into test_food values ('" + new_fruit + "' )")
#       return "Thanks for adding " + new_fruit
     
# add_my_fruit = streamlit.text_input('What food would you like to add?')

# if streamlit.button('Get food List'):
#   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#   streamlit.write(insert_row_snowflake(add_my_fruit))
#   my_data_rows = get_test_food()
#   my_cnx.close()
#   streamlit.dataframe(my_data_rows)
  
  
  
#   # ----------------------------------------------------


# def select_variable(variables):
#     selected_variable = random.choice(variables)
#     variables.remove(selected_variable)
#     return selected_variable

  
# get_test_food(my_data_rows)

import random
import streamlit as streamlit

streamlit.title("식사를 합시다. 😎")

## streamlit.header('점심 매뉴도 똑똑하게! 우리는 Proven Bees!')
streamlit.markdown('#### 점심 매뉴도 똑똑하게! 우리는 Proven Bees!')    
streamlit.text('🥗 더 이상 고민하는 점심매뉴 그만!')
streamlit.text('🎯 즐겁고 빠르게 점심식사 매뉴를 정해봐요!')     

streamlit.markdown('#### 점심식사 매뉴 추가하기:')              

def get_test_food():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT * FROM test_food")
        return my_cur.fetchall()

def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("INSERT INTO test_food VALUES ('" + new_fruit + "' )")
    return "Thanks for adding " + new_fruit

add_my_fruit = streamlit.text_input('What food would you like to add?')

if streamlit.button('Get food List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    streamlit.write(insert_row_snowflake(add_my_fruit))
    my_data_rows = get_test_food()
    my_cnx.close()
    streamlit.dataframe(my_data_rows)

if streamlit.button('Pick a Random Fruit'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_test_food()
    my_cnx.close()
    
    fruits = [row[0] for row in my_data_rows]
    random_fruit = random.choice(fruits)
    streamlit.write("Randomly picked fruit:", random_fruit)
    
       
streamlit.markdown('#### 점심식사 Dataframe:')         
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_data_rows = get_test_food()
my_cnx.close()
my_food_list = streamlit.dataframe(my_data_rows)
my_food_list = my_food_list.set_index('FOOD_LIST')
my_food_list_selected = streamlit.multiselect("Pick 식당:", list(my_food_list.index), ['기소야', '동경규동'])
my_food_list_show = my_food_list.loc[my_food_list_selected]
streamlit.dataframe(my_food_list_show)






