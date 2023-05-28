

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



# ------------------------------ old code ---------------------------
# streamlit.header("Fruityvice Fruit Advice!")

# fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
# streamlit.write('The user entered ', fruit_choice)

# import requests 
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice) 
# streamlit.text(fruityvice_response.json())

# write your own comment -what does the next line do? 
# fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
# streamlit.dataframe(fruityvice_normalized)

# ------------------ New Code ---------------------------------------------------------
# New Section 
# streamlit.header("Fruityvice Fruit Advice!")
# try:  
#    fruit_choice = streamlit.text_input('What fruit would you like information about?')
#    if not fruit_choice:
#        streamlit.error("Please select a fruit to get information.")
#    else:
#            fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice) 
#            fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#            streamlit.dataframe(fruityvice_normalized)
#    except URLError as e:
#    streamlit.error()
# -----------------------------------------------------------------------------------------

# ------------------------------------------New Code_chatgpt-------------------------------
# import streamlit
# import requests
# import pandas
# from urllib.error import URLError

# streamlit.header("Fruityvice Fruit Advice!")

# try:  
#     fruit_choice = streamlit.text_input('What fruit would you like information about?')
#     if not fruit_choice:
#         streamlit.error("Please select a fruit to get information.")
#     else:
#         fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice) 
#         fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#         streamlit.dataframe(fruityvice_normalized)
# except URLError as e:
#     streamlit.error("An error occurred while retrieving the fruit information.")

# ------------------------------------new code_2------------------------------------------------
# Create the called a function 
def get_fruityvice_data(this_fruit_choice):
      fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice) 
      fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      return fruityvice_normalized

# New Section 
streamlit.header("Fruityvice Fruit Advice!")
try:  
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
        streamlit.error("Please select a fruit to get information.")
    else:   
            back_from_function = get_fruityvice_data(fruit_choice)
            streamlit.dataframe(back_from_function) 
except URLError as e:
    streamlit.error("An error occurred while retrieving the fruit information.")
    
    
# ----------------------------------code_2 (button) -------------------------------------------------------
streamlit.header("The fruit load list contains:")
# Snowflake-related funtions
def get_fruit_load_list():
   with my_cnx.cursor() as my_cur: 
        my_cur.execute("select * from fruit_load_list")
        return my_cur.fetchall() 

# Add a button to load the fruit 
if streamlit.button("Get Fruit Load List"): 
      my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
      my_data_rows = get_fruit_load_list()
      streamlit.dataframe(my_data_rows)

streamlit.stop()


# ----------------------------------- code_2 (insert) -------------------------------------------------------
# # Allow the end user add a fruit to the list 
# def insert_row_snowflake(new_fruit):
#      with my_cnx.cursor() as my_cur:
#            my_cur.execute("insert into fruit_load_list values ('from streamlit')")
#            return "Thanks for adding" + new_fruit

# add_my_fruit = streamlit.text_input('What fruit would you like to add?') 
# if streamlit.button('Add a Fruit to the List'):
#     my_cnx = snowflake.connector.conn(**streamlit.secrets['snowflake'])
#     back_from_function = insert_row_snowflake(add_my_fruit)
#     streamlit.text(back_from_function) 





# # -----------------------------------------code_1-----------------------------------------------------------------
# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_data_row = my_cur.fetchone()
# streamlit.text("Hello from Snowflake:")
# streamlit.text(my_data_row)

# # --- basic 
# # my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
# # my_data_row = my.cur.fetchone()
# # streamlit.text("The fruit load list contains:")
# # streamlit.text(my_data_row)

# # --- make it nicer 
# # my_data_row = my_cur.fetchone()
# # streamlit.header("The fruit load list contains:")
# # streamlit.dataframe(my_data_row)


# # --- Get All the Rows 
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows) 

 # --- Challenge_1 
add_my_fruit = streamlit.text_input('What fruit would you like add?','jackfruit')
streamlit.write('Theanks for adding jackfruit', add_my_fruit)

#---------------------------------------------------------------------------------------------------------


