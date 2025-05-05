import streamlit as st

st.title("📖 Моё учебное приложение")  # Заголовок
st.header("Это раздел")  # Подзаголовок
st.subheader("А это подраздел")  # Подподзаголовок
st.text('Обычный текст без форматирования')

# Markdown-форматирование
st.markdown("**Жирный текст** и *курсив*")
st.markdown("[Ссылка на Google](https://google.com)")

# Разделитель
st.divider()

# Пример с многострочным текстом
st.write("""  
Это многострочный текст.  
Streamlit автоматически учитывает переносы строк.  
""")

st.markdown("<span style='color:red'>Красный текст</span>", unsafe_allow_html=True)