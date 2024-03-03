import streamlit as st
import pandas as pd
from scipy.stats import ttest_ind
from configuration import DATA_PATH


def page_tests():
    st.header("Глава: Проверка знаний")

    st.write("""Вам предстоит ответить на 10 вопросов по прошлым блокам.""")
    
    def create_question_block(question, correct_answer, wrong_answers):
        st.subheader(question)
        
        # Создание радиокнопок для ответов
        options = [correct_answer] + wrong_answers
        user_answer = st.radio("Выберите правильный ответ:", options, index=None)
        
        # Проверка ответа и вывод результата
        if user_answer is not None:
            if user_answer == correct_answer:
                st.success("Верно!")
            else:
                st.error("Неверно. Правильный ответ: {}".format(correct_answer))

     # Главный блок приложения
    st.title("Вопросы по теории блока описательной статистики")

    # Первый вопрос
    question1 = "Что такое среднее арифметическое?"
    correct_answer1 = "Сумма всех значений делённая на их количество"
    wrong_answers1 = ["Медиана", "Мода", "Дисперсия"]
    create_question_block(question1, correct_answer1, wrong_answers1)

    # Второй вопрос
    question2 = "Как вычислить стандартное отклонение?"
    correct_answer2 = "Корень из дисперсии"
    wrong_answers2 = ["Медиана", "Мода", "Среднее арифметическое"]
    create_question_block(question2, correct_answer2, wrong_answers2)

    # Третий вопрос
    question3 = "Что такое вероятность в статистике?"
    correct_answer3 = "Отношение числа благоприятных случаев к общему числу случаев"
    wrong_answers3 = ["Среднее арифметическое", "Стандартное отклонение", "Дисперсия"]
    create_question_block(question3, correct_answer3, wrong_answers3)


        # Главный блок приложения
    st.title("Вопросы по теории блока визуализации данных")

    question4 = "Что из нижеперечисленного не является типом графика визуализации данных?"
    correct_answer4 = "Контурная карта"
    wrong_answers4 = ["Скрипичная диаграмма", "График рассеяния", "Тепловая карта"]
    create_question_block(question4, correct_answer4, wrong_answers4)

    # Пятый вопрос
    question5 = "Какой тип графика лучше всего подходит для отображения тренда во времени?"
    correct_answer5 = "Линейный график"
    wrong_answers5 = ["Гистограмма", "Круговая диаграмма", "Ящик с усами (Box plot)"]
    create_question_block(question5, correct_answer5, wrong_answers5)

    # Шестой вопрос
    question6 = "Что из перечисленного используется для выявления выбросов в данных?"
    correct_answer6 = "Ящик с усами (Box plot)"
    wrong_answers6 = ["Круговая диаграмма", "Гистограмма", "Линейный график"]
    create_question_block(question6, correct_answer6, wrong_answers6)


        # Главный блок приложения
    st.title("Вопросы по теории блока статистического анализа")

    question7 = "Какую гипотезу проверяет t-тест?"
    correct_answer7 = "Нулевая гипотеза о равенстве средних значений в двух выборках"
    wrong_answers7 = ["Гипотеза о наличии корреляции", "Гипотеза о равенстве дисперсий", "Гипотеза о наличии различий в распределении"]
    create_question_block(question7, correct_answer7, wrong_answers7)


    question8 = "Какой тип ANOVA применяется, если у нас есть более двух групп для сравнения?"
    correct_answer8 = "Многофакторная ANOVA"
    wrong_answers8 = ["Однофакторная ANOVA", "ANOVA с повторными измерениями", "Корреляционный анализ"]
    create_question_block(question8, correct_answer8, wrong_answers8)


    question9 = "Какой критерий используется в Хи-квадрат тесте для оценки различий между ожидаемым и фактическим распределением частот?"
    correct_answer9 = "Пирсоновский критерий"
    wrong_answers9 = ["t-критерий", "Z-критерий", "Спирменовский критерий"]
    create_question_block(question9, correct_answer9, wrong_answers9)

    question10 = "Что показывает коэффициент корреляции в корреляционном анализе?"
    correct_answer10 = "Степень линейной взаимосвязи между двумя переменными"
    wrong_answers10 = ["Среднее значение переменной", "Стандартное отклонение переменной", "Медиана переменной"]
    create_question_block(question10, correct_answer10, wrong_answers10)