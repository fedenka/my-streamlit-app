import streamlit as st
from streamlit_option_menu import option_menu


# Настройки страницы
st.set_page_config(page_title="Красивое меню", layout="wide")

# Горизонтальное меню
selected = option_menu(
    menu_title=None,  # Без заголовка
    options=["Главная", "Проекты", "Контакты", "Настройки"],
    icons=["house", "folder", "envelope", "gear"],  # Иконки из Bootstrap (https://icons.getbootstrap.com/)
    menu_icon="cast",  # Иконка меню
    default_index=0,  # Активный пункт по умолчанию
    orientation="horizontal",  # Горизонтальное меню
    styles={
        "container": {"padding": "0!important", "background-color": "#f8f9fa"},
        "icon": {"color": "orange", "font-size": "14px"},
        "nav-link": {
            "font-size": "14px",
            "text-align": "center",
            "margin": "0px",
            "--hover-color": "#eee",
        },
        "nav-link-selected": {"background-color": "#ff4b4b"},
    }
)

from teta import set_video_background
set_video_background("background.mp4")
