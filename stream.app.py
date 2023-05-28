import streamlit
import pandas 

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



streamlit.header("Fruityvice Fruit Advice!")

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests 
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice) 
# streamlit.text(fruityvice_response.json())

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)


import streamlit
import pandas as pd
import snowflake.connector


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

# --- basic 
# my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
# my_data_row = my.cur.fetchone()
# streamlit.text("The fruit load list contains:")
# streamlit.text(my_data_row)

# --- make it nicer 
# my_data_row = my_cur.fetchone()
# streamlit.header("The fruit load list contains:")
# streamlit.dataframe(my_data_row)


# --- Get All the Rows 
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows) 

# --- Chagggenge 
add_my_fruit = streamlit.text_input('What fruit would you like information about?','jackfruit')
streamlit.write('Theanks for adding jackfruit', add_my_fruit)




