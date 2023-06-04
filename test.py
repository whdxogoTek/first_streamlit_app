
# import streamlit
# import snowflake.connector


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



