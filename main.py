import pandas as pd
from io import BytesIO
import requests

import streamlit as st
from streamlit_option_menu import option_menu

from pages_list import *
from pages_list.advanced import advanced_page
from pages_list.baseline import baseline_page
from pages_list.missuse import missuse_page
from pages_list.recommend import recommend_page


r = requests.get(DATA_PATH)
df_search = pd.read_csv(BytesIO(r.content), index_col=0)


st.set_page_config(page_title="Лаборатория цифровых компетенций", page_icon="👾", layout="wide")

with st.sidebar:
    redirect_url = "http://83.143.66.61:27369/"
    logo_image = 'https://raw.githubusercontent.com/Chetoff1228/images/main/logo.png'
    #st.markdown(f'<a href="{redirect_url}"><img src="{logo_image}" alt="Foo" width="100" height="100"/></a>', unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center; color:grey;'><a href='{redirect_url}'><img src='{logo_image}' alt='Foo' width='100' height='100'/></a></p>", unsafe_allow_html=True)

with st.sidebar:
    selected = option_menu('', ["1. Промпт-инжиниринг🚀", "2. Рекомендации по созданию промптов🤔", "3. Базовые техники 🤓", "4. Вредоносное применение 🤖", "5. Проверка знаний 🎓", "6. Практика 📜", "7. Итоги 🧐"])

if selected == "1. Промпт-инжиниринг🚀":
    intro_page()
elif selected == "2. Рекомендации по созданию промптов🤔":
    recommend_page()
elif selected == "3. Базовые техники 🤓":
    baseline_page()
elif selected == "4. Вредоносное применение 🤖":
    missuse_page()
elif selected == "5. Проверка знаний 🎓":
    check_page()
elif selected == "6. Практика 📜":
    practice_page()
else:
    result_page(df_search)