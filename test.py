
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



my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

#-----------------------------------------------------------------------------------

streamlit.header("The Fruity List Contains:")
def get_test_food():
  with my_cnx.cursor() as my_cur:
      my_cur.execute("select * from test_food ")
      return my_cur.fetchall()
    
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
      my_cur.execute("insert into test_food values ('" + new_fruit + "' )")
      return "Thanks for adding " + new_fruit
     
add_my_fruit = streamlit.text_input('What food would you like to add?')

if streamlit.button('Get food List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  streamlit.write(insert_row_snowflake(add_my_fruit))
  my_data_rows = get_test_food()
  my_cnx.close()
  streamlit.dataframe(my_data_rows)
  
  
  
  # ----------------------------------------------------


def select_variable(variables):
    selected_variable = random.choice(variables)
    variables.remove(selected_variable)
    return selected_variable

  
get_test_food(my_data_rows)





