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

# ▶▶▶▶▶▶▶▶▶▶ Lesson 9-[]
# ----------------- 🥋 Same common ------------------------------------------------------

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi") -- 제거
# streamlit.text(fruityvice_response) -- 제거 

# write your own comment what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

# ▶▶▶▶▶▶▶▶▶▶ Lesson 12-4
#--------------------- 🥋 Let's Query Our Trial Account Metadata ------------------------------------
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

# ▶▶▶▶▶▶▶▶▶▶ Lesson 12-5
# --------------------- 🥋 Oops! Let's Get All the Rows, Not Just One ----------------------------------
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall() # 한 번에 모든 로우를 읽기 위해서는 fetchall 메서드
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

# ▶▶▶▶▶▶▶▶▶▶ Lesson 12-[]
# --------------------- 🎯 Can You Add A Second Text Entry Box?  ----------------------------------
add_my_fruit = streamlit.text_input('What fruit would you like add?','jackfruit')
streamlit.write('Theanks for adding jackfruit', add_my_fruit)

# ▶▶▶▶▶▶▶▶▶▶ Lesson 12-[] 🥋 Time to Tidy Up? 
# -----------------------🥋 Write Code to Add Rows to Our Fruit List in Snowflake-------------------------
# --- insert into fruit_load_list values ('test') ; 
# --- select * 
# --- from fruit_load_list ; 

streamlit.write('Thanks for adding', add_my_fruit)
# This will not work correctly, but just go with it for now 
my_cur.execute("insert into fruit_load_list values('from streamlit')")

# -------------------------🥋 Add a STOP Command to Focus Our Attention---------------------------------------
streamlit.stop()
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

# -------------------------- 🥋 재구성된 버전을 실행하고 여전히 작동하는지 확인 -----------------------------------
# streamlit 가서 확인중... 

# ▶▶▶▶▶▶▶▶▶▶ Lesson 12-[] 
# ------------------------------ 🥋 Fruityvice 코드를 Try-Except로 이동(중첩된 If-Else 포함) ---------------------



