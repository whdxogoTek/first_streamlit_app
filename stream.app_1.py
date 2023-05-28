# ▶▶▶▶▶▶▶▶▶▶ Lesson 12-1 
# ----------------- 🥋 Create a Fruit Load List Table ------------------------------------------

# use role pc_rivery_role;
# use warehouse pc_rivery_wh;

# create or replace TABLE PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST (
# 	FRUIT_NAME VARCHAR(25)
# );


# ----------------- 🥋 Add Rows to the Fruit Load List Table -----------------------------------

# insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST
# values ('banana')
# , ('cherry')
# , ('strawberry')
# , ('pineapple')
# , ('apple')
# , ('mango')
# , ('coconut')
# , ('plum')
# , ('avocado')
# , ('starfruit');

# ▶▶▶▶▶▶▶▶▶▶ Lesson 12-[]
# ----------------- 🥋 Same common ------------------------------------------------------
import streamlit 
import pandas
import requests
import snowflake.connector 
from urllib.error import URLError 

streamlit.title("My Mom's New Healthy Diner")

streamlit.header('Breakfast Menu')
streamlit.text('🥗Omega 3 & Blueberry Oatmeal')
streamlit.text('🐔Kale, Spinach & Rocket Smoothie')
streamlit.text('🥑🍞Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected] ## loc[:,'fruits_selected'] 
streamlit.dataframe(fruits_to_show)

# ▶▶▶▶▶▶▶▶▶▶ Lesson 7-[]
# ----------------- 🥋 Same common ------------------------------------------------------

streamlit.header('Fruityvice Fruit Advice')
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = request.get('https://fruityvice.com/api/fruit/' + fruit_choice)

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

