import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt    
from configuration import TTEST_DATA_PATH


ttest_data = pd.read_csv(TTEST_DATA_PATH, index_col=0)


def page_visual(df):
    st.header("Глава: Визуализация данных")

    st.write("""
Визуализация в статистике играет ключевую роль, предоставляя мощный инструмент для анализа данных и понимания сложных явлений. Статистика, будучи наукой о сборе, анализе, интерпретации, представлении и организации данных, часто сталкивается с объемными и сложными информационными массивами. В этом контексте визуализация становится неотъемлемой частью процесса, помогая перевести абстрактные цифры в наглядные и понятные формы.

Визуализация данных позволяет выделить основные тренды, зависимости и аномалии, делая статистическую информацию более доступной и доступной для широкой аудитории. Графики, диаграммы, гистограммы и другие визуальные элементы способны эффективно передавать сложные концепции, делая процесс интерпретации данных более интуитивным.

Помимо этого, визуализация помогает выявлять взаимосвязи между переменными, выявлять паттерны и обнаруживать тенденции, что является ключевым элементом в принятии информированных решений. Важность визуализации в статистике не только заключается в предоставлении инструментов для анализа данных, но и в способности делиться результатами идеями, подчеркивая их важность в понятной и эффективной форме.""")
    
    is_button_clicked = False

    # Создание кнопки
    button_label = "Открыть теоретическую информацию" if not is_button_clicked else "Закрыть"
    if st.button(button_label):
        # Изменение состояния при клике
        is_button_clicked = not is_button_clicked

    # Дополнительные элементы, которые появляются при открытой кнопке
    if is_button_clicked:
        st.write("""## Теоретическая информация о визуализации данных:  \n Визуализация данных представляет собой мощный инструмент в области анализа и интерпретации информации. Этот блок фокусируется на методах и техниках визуализации, которые позволяют превратить сырые числовые данные в наглядные графические представления. Основная цель визуализации данных - упростить восприятие сложных структур и паттернов, что существенно облегчает процесс принятия решений.

## 1. Графики и Диаграммы:

   - **Линейные графики:** Используются для отслеживания изменения переменной во времени. Они позволяют выявлять тренды, циклы и сезонные изменения.
   
   - **Столбчатые и круговые диаграммы:** Эффективны при сравнении частей целого. Идеальны для иллюстрации распределения категорий.

## 2. Двумерные и Трехмерные Графики:

   - **Диаграммы рассеяния:** Позволяют оценить взаимосвязь между двумя переменными, выявлять корреляции и выбросы.
   
   - **Трехмерные графики:** Используются для визуализации трех переменных, что может быть полезно при анализе сложных взаимосвязей.

## 3. Графики временных рядов:

   - **Свечные графики:** Широко применяются в финансовой аналитике для визуального отображения изменений цен.
   
   - **Гистограммы временных рядов:** Используются для анализа распределения значений в определенный период времени.

## 4. Интерактивная визуализация:

   - **Интерактивные дашборды:** Обеспечивают возможность пользователю взаимодействовать с данными, изменять параметры и получать мгновенные результаты.

## 5. Эффективное использование цвета и формы:

   - **Цветовая схема:** Выбор правильной цветовой гаммы помогает выделить важные элементы и создает четкую структуру.
   
   - **Использование форм:** Различные формы и маркеры могут помочь выделить ключевые точки данных на графиках.

## 6. Визуализация больших данных:

   - **Тепловые карты:** Используются для визуализации плотности и распределения значений в больших наборах данных.
   
   - **Дендрограммы:** Применяются для иерархической кластеризации и визуализации сложных структур.
                                     """)

    if is_button_clicked and st.button("Закрыть"):
        # Изменение состояния при клике на кнопку "Закрыть"
        is_button_clicked = not is_button_clicked

    # Кнопка для отображения графика опыта и зарплаты
    if st.button("Показать график опыта и зарплаты"):
        # Ваш код для построения графика опыта и зарплаты
        fig, ax = plt.subplots()
        sns.boxplot(x='experience', y='salary', data=df, ax=ax)
        ax.set_title('График опыта и зарплаты')
        ax.set_xlabel('Опыт')
        ax.set_ylabel('Зарплата')
        st.pyplot(fig)

    if st.button("Показать график типа расписания и зарплаты"):
        # Ваш код для построения графика опыта и зарплаты
        fig, ax = plt.subplots(figsize=(12, 12))
        sns.boxplot(x='schedule', y='salary', data=df, ax=ax)
        ax.set_title('График типа расписания и зарплаты')
        ax.set_xlabel('Тип расписания')
        ax.set_ylabel('Зарплата')
        st.pyplot(fig)

    if st.button("Показать график типа занятости и зарплаты"):
        # Ваш код для построения графика опыта и зарплаты
        fig, ax = plt.subplots(figsize=(12, 12))
        sns.boxplot(x='employment', y='salary', data=df, ax=ax)
        ax.set_title('График типа занятости и зарплаты')
        ax.set_xlabel('Тип занятости')
        ax.set_ylabel('Зарплата')
        st.pyplot(fig)