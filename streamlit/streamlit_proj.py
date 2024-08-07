import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Заголовок страницы
st.title("Загрузка собственного датасета")
df = pd.read_csv('train.csv')
# Компонент для загрузки файла
uploaded_file = st.file_uploader("Выберите файл")

if uploaded_file is not None:
    try:
        # Предположим, что это файл CSV
        df = pd.read_csv(uploaded_file)

        # Показать данные
        st.write("Вот ваши данные:")
        st.write(df)
    except Exception as e:
        st.error(f"Произошла ошибка при загрузке файла: {e}")

else:
    st.write("Пожалуйста, загрузите файл чтобы увидеть данные")

if (st.button('Посмотреть готовые данные')):
    st.write("Готовые данные:")
    st.write(df)

def sidebar_input_features():
    str_columns = df.select_dtypes(include=['object']).columns.tolist()
    column = st.sidebar.selectbox("Распределение данных в столбце", tuple(str_columns))
    st.sidebar.title("Выберите ячейку для просмотра:")
    col = st.sidebar.selectbox("Столбец", tuple(df.columns))
    s = st.sidebar.slider("Номер строки", min_value=0, max_value=df.shape[0], value=0,
                            step=1)
    if st.sidebar.button("Вывод данных"):
        fig = plt.figure(figsize=(10, 6))
        st.write(column)
        plt.hist(df[column], bins=5, edgecolor='black')
        plt.title('Распределение данных в столбце "values"')
        plt.xlabel('Значения')
        plt.ylabel('Частота')
        plt.xticks(rotation=45)
        plt.grid(True)
        st.pyplot(fig)

        st.write("## Выбранная ячейка")
        st.write(df.loc[s, col])

sidebar_input_features()