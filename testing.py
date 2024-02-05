import pandas as pd

import streamlit as st
from streamlit_option_menu import option_menu

from configuration import (DATA_PATH, TTEST_DATA_PATH, REDIRECT_URL, LOGO_URL)
from pages_list.page_data import page_data
from pages_list.page_visual import page_visual
from pages_list.page_stats import page_stats


df = pd.read_csv(DATA_PATH, index_col=0)
ttest_data = pd.read_csv(TTEST_DATA_PATH, index_col=0)


st.set_page_config(page_title="Лаборатория цифровых компетенций", page_icon="👾", layout="wide")

with st.sidebar:
    st.markdown(f"<p style='text-align:center; color:grey;'><a href='{REDIRECT_URL}'><img src='{LOGO_URL}' alt='Foo' width='100' height='100'/></a></p>", unsafe_allow_html=True)

with st.sidebar:
    selected = option_menu('', ["1. Описательная статистика", "2. Визуализация данных", "3. Статистический анализ"])

if selected == "1. Описательная статистика":
    page_data(df)
elif selected == "2. Визуализация данных":
    page_visual(df)
elif selected == "3. Статистический анализ":
    page_stats(ttest_data)
