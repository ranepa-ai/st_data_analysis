import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt    
from scipy.stats import ttest_ind

# Главы
chapters = {
    " Блок 1: Описательная   статистика данных": ["Показать описательную статистику данных", "Добавить еще задание"],
    " Блок 2: Визуализация данных": ["Показать гистограмму зарплат", "Показать график опыта и зарплаты"],
    " Блок 3: Статистический анализ": ["Провести t-тест", "Добавить еще задание"]
}

# Заголовок приложения
st.title("""Тренажер: Статистика""")

with st.sidebar:
#   st.image(r"streamlit_hh\android-chrome-192x192.png", width=100)
  redirect_url = "http://83.143.66.61:27369/"

  logo_html = f'<a href="{redirect_url}" target="_blank"><img src="data:image/png;base64,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" style="width:80px;"></a>'
  st.sidebar.markdown(logo_html, unsafe_allow_html=True) 
  
# Левая колонка с главами
chapter = st.sidebar.radio("Выберите главу", list(chapters.keys()))
chapter_info = {
    " Блок 1: Описательная статистика данных": {"icon": "📊", "description": """ # Изучение общих характеристик данных
    \n # В данном блоке мы погрузимся в мир базовых методов описательной статистики, предназначенных для анализа данных. """},
    " Блок 2: Визуализация данных": {"icon": "📈", "description": """# Построение графиков и диаграмм \n # В данном блоке мы изучим основные виды визуализации в статистике."""},
    " Блок 3: Статистический анализ": {"icon": "📊", "description": """# Проведение статистических тестов и анализ результатов \n # В данном блоке мы изучим основные статистические тесты, а так же применим их на наших данных о вакансиях."""}
}

# Вывод иконки и заголовка главы с описанием
chapter_icon = chapter_info[chapter]["icon"]
chapter_description = chapter_info[chapter]["description"]
st.sidebar.markdown(f"## {chapter_icon} {chapter}\n{chapter_description}")

# Глава "Описательная статистика данных"
if chapter == " Блок 1: Описательная статистика данных":
    df_hh = pd.read_csv(r'data\data.csv', index_col=0)
    st.header("Блок 1: Описательная статистика данных")
    st.write("""В мире данных, где информация может быть ошеломляющей в своей многообразности, описательная статистика выступает важным инструментом для обобщения, упорядочивания и представления существенных характеристик набора данных. Она не только облегчает восприятие информации, но и является ключом к глубокому пониманию структуры и особенностей данных.

Ключевые параметры описательной статистики, такие как среднее значение, медиана, мода, дисперсия и стандартное отклонение, становятся опорой в процессе анализа данных. С помощью этих метрик мы можем выявить центральные тенденции, оценить степень изменчивости и выделить наиболее часто встречающиеся значения.

Описательная статистика не только служит средством конденсации информации, но и создает базу для сравнения различных наборов данных, выявления выбросов и выделения особенностей распределения. Эта методология позволяет исследователям, аналитикам и принимающим решениям сфокусироваться на ключевых аспектах данных, сэкономив время и ресурсы.

Таким образом, важность описательной статистики и ключевых параметров в анализе данных заключается не только в их способности предоставлять краткую характеристику, но и в том, что они служат основой для дальнейшего исследования и принятия обоснованных решений на основе числовых фактов.""")




    st.write("В данной части нашего курса мы будем работать с данными, которые содержат информацию о более чем 135.000 вакансий, и были получены с помощью парсинга с сайта HH.ru.")
    st.write("В них есть данные о вакансиях практически со всех сфер трудового рынка, а так же есть дополнительная информации о самой вакансии, как например, необходимый трудовой стаж, а так же ключевые навыки, которые нужны для выполнения рабочих задач.")
    st.write("Эти данные будут очень полезны нам для получения реальной статистики о трудовом рынке за 2022-2023 год.")


    is_button_clicked = False

    # Создание кнопки
    button_label = "Открыть теоретическую информацию" if not is_button_clicked else "Закрыть"
    if st.button(button_label):
        # Изменение состояния при клике
        is_button_clicked = not is_button_clicked

    # Дополнительные элементы, которые появляются при открытой кнопке
    if is_button_clicked:


        st.write("""#### Основное понятие теории вероятности - это **вероятность**. 
                \n **Вероятность** в статистике представляет собой отношение числа благоприятных случаев (т.е., событий, которые нас интересуют) к общему числу возможных случаев. Вероятность обычно выражается от 0 до 1, где 0 означает невозможность события, а 1 – его достоверность. 
                 Вероятность также может быть выражена в процентах, умножив значение на 100.""")

        st.write("""### Теоретическая информация о описательной статистике:

#### 1. **Средние показатели:**
   - *Среднее арифметическое:* Сумма всех значений, делённая на количество наблюдений.
   - *Медиана:* Значение, разделяющее упорядоченный набор данных на две равные половины.
   - *Мода:* Самое часто встречающееся значение в наборе данных.

#### 2. **Разброс данных:**
   - *Дисперсия:* Среднеквадратическое отклонение от среднего значения.
   - *Стандартное отклонение:* Квадратный корень из дисперсии; измеряет степень изменчивости данных.

#### 3. **Меры положения:**
   - *Квартили:* Значения, разделяющие упорядоченный ряд на четыре равные части.
   - *Децили и процентили:* Значения, разделяющие ряд на десяти и произвольные процентные части соответственно.

#### 4. **Визуализация данных:**
   - *Гистограммы:* Графическое представление распределения данных.
   - *Ящик с усами (box plot):* Иллюстрация основных статистических характеристик, таких как медиана и квартили.

#### 5. **Корреляция и регрессия:**
   - *Корреляция:* Измеряет степень взаимосвязи между двумя переменными.
   - *Регрессия:* Позволяет предсказывать значения одной переменной на основе значений другой.
 """)

    if is_button_clicked and st.button("Закрыть"):
        # Изменение состояния при клике на кнопку "Закрыть"
        is_button_clicked = not is_button_clicked

    st.write("#### Посмотрим на первые пять строк датасета.")
    if st.button("Посмотреть на содержание набора данных"):
        st.write(df_hh.head())

    st.write("#### Теперь нужно понять, какие типы данных мы имеем в наших колонках")
    if st.button("Посмотреть на типы данных"):
        st.write(df_hh.dtypes)

        st.write("В нашем датасете есть различные типы данных, как категориальные (название вакансии), так и численные (зарплата)")

    st.write("#### Узнав типы данных, мы можем смело выдвигать различные гипотезы для анализа данных, например, найти численные характеристики в колонке зарплаты")

    if st.button("Показать данные о зарплате"):

        st.write(f"Минимальная зарплата: {df_hh['salary'].min():.2f} ₽")
                 
        st.write(f"Средняя зарплата: {df_hh['salary'].mean():.2f} ₽")

        st.write(f"Максимальная зарплата: {df_hh['salary'].max():.2f} ₽")

        mode_result = df_hh['salary'].mode()
        st.write(f"Мода зарплаты: {', '.join(map(str, mode_result))} ₽")

        st.write(f"Медианная зарплата: {df_hh['salary'].median():.2f} ₽")
        

    st.write("#### Теперь можно попробовать использовать инструмент для визуального анализа зарплаты")
    if st.button("Показать распределение зарплаты по всем вакансиям", type='primary'):
        # Ваш код для построения гистограммы
        fig, ax = plt.subplots()
        sns.histplot(df_hh['salary'], kde=True, ax=ax)
        ax.set_title('Распределение зарплат')
        ax.set_xlabel('Зарплата')
        ax.set_ylabel('Частота')
        st.pyplot(fig)


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
    st.title("Вопросы по теории")

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


# Глава "Визуализация данных"
elif chapter == " Блок 2: Визуализация данных":
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

    df_visual = pd.read_csv(r'data\data.csv', index_col=0)
    # Кнопка для отображения графика опыта и зарплаты
    if st.button("Показать график опыта и зарплаты"):
        # Ваш код для построения графика опыта и зарплаты
        fig, ax = plt.subplots()
        sns.boxplot(x='experience', y='salary', data=df_visual, ax=ax)
        ax.set_title('График опыта и зарплаты')
        ax.set_xlabel('Опыт')
        ax.set_ylabel('Зарплата')
        st.pyplot(fig)

    if st.button("Показать график типа расписания и зарплаты"):
        # Ваш код для построения графика опыта и зарплаты
        fig, ax = plt.subplots(figsize=(12, 12))
        sns.boxplot(x='schedule', y='salary', data=df_visual, ax=ax)
        ax.set_title('График типа расписания и зарплаты')
        ax.set_xlabel('Тип расписания')
        ax.set_ylabel('Зарплата')
        st.pyplot(fig)

    if st.button("Показать график типа занятости и зарплаты"):
        # Ваш код для построения графика опыта и зарплаты
        fig, ax = plt.subplots(figsize=(12, 12))
        sns.boxplot(x='employment', y='salary', data=df_visual, ax=ax)
        ax.set_title('График типа занятости и зарплаты')
        ax.set_xlabel('Тип занятости')
        ax.set_ylabel('Зарплата')
        st.pyplot(fig)

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
    st.title("Вопросы по теории")

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

# Глава "Статистический анализ"
elif chapter == " Блок 3: Статистический анализ":
    st.header("Глава: Статистический анализ")

    st.write("""Статистические тесты – это ключевое звено в статистике, которое помогает проверять гипотезы, выявить закономерности и принять обоснованные решения на основе полученных результатов.

Но что же такое статистические тесты и почему они имеют такую важность для области статистики? Статистические тесты – это инструменты, предназначенные для проверки статистических гипотез и выявления значимых различий в данных. Они позволяют нам понять, насколько результаты эксперимента или исследования являются статистически значимыми, а не случайными.

Здесь мы рассмотрим различные виды статистических тестов, их применение в различных областях, а также объясним, почему умение правильно использовать эти инструменты является неотъемлемой частью работы в области статистики.""")
    
    
    is_button_clicked = False

    # Создание кнопки
    button_label = "Открыть теоретическую информацию" if not is_button_clicked else "Закрыть"
    if st.button(button_label):
        # Изменение состояния при клике
        is_button_clicked = not is_button_clicked

    # Дополнительные элементы, которые появляются при открытой кнопке
    if is_button_clicked:
        st.write("""### Теоретическая информация:  Введение в Основные Статистические Тесты

## 1. t-тест

T-тест является одним из наиболее распространенных статистических тестов. Он используется для сравнения средних значений двух групп и выявления статистической значимости различий между ними. Независимый t-тест применяется, когда данные в группах независимы, а зависимый t-тест – когда данные в группах зависимы друг от друга.

## 2. Анализ дисперсии (ANOVA)

ANOVA применяется для сравнения средних значений более чем двух групп. Этот тест позволяет определить, есть ли статистически значимые различия хотя бы между двумя из групп. Он имеет различные варианты, такие как однофакторный ANOVA и многофакторный ANOVA, в зависимости от числа факторов, рассматриваемых в исследовании.

## 3. Хи-квадрат тест (χ²)

Хи-квадрат тест применяется для анализа связи между категориальными переменными. Он используется для определения того, ожидаемо ли наблюдаемое распределение частот в таблице сопряженности, или есть статистически значимая разница.

## 4. Корреляционный анализ

Корреляционный анализ используется для измерения степени взаимосвязи между двумя непрерывными переменными. Коэффициент корреляции Пирсона применяется, если данные имеют нормальное распределение, в то время как коэффициент корреляции Спирмена подходит для ранговых данных.

## 5. Регрессионный анализ

Регрессионный анализ используется для изучения отношений между зависимой переменной и одной или несколькими независимыми переменными. Этот анализ может быть простым линейным (с одной независимой переменной) или множественным (с несколькими независимыми переменными).

## Заключение

Выбор правильного статистического теста зависит от природы данных и целей исследования. Понимание основных статистических тестов позволяет исследователям принимать обоснованные решения при анализе данных и выводе статистической значимости результатов.""")

    if is_button_clicked and st.button("Закрыть"):
        # Изменение состояния при клике на кнопку "Закрыть"
        is_button_clicked = not is_button_clicked
    
    ttest_data = pd.read_csv(r'data\ttest_data.csv')

    # Функция для выполнения t-теста и вывода результатов
    def perform_t_test(dataframe, group1, group2):
        t_statistic, p_value = ttest_ind(dataframe[group1], dataframe[group2])
        return t_statistic, p_value

    # Основной блок приложения
    st.title("Анализ данных с использованием t-теста")

    # Кнопка для проведения t-теста
    if st.button("1. Проведите t-тест о средних в двух выборках"):
        st.write("""Для проведения данного теста нам нужны данные внутри отдельных групп, давайте возьмём данные зарплаты для двух разных групп, первая группа - это вакансии с требуемым опытом работы от 1 до 3-х лет, а вторая группа - вакансии без требуемого опыта работы.""")
        
        st.write("""Но для последующего тестирования, нам нужно ввести некоторые понятия: 
                 \n **Уровень значимости** - это порог для оценки результата как статистически значимого. Если показатель значимости ниже уровня значимости, результат считается статистически значимым. Уровень значимости также называют альфа-уровнем (в нашем тесте он будет равен 0.05)
                 \n **Статистически значимым** (и позволяющим отвергнуть нулевую гипотезу)при этом считается результат, р-значение которого равно уровню значимости или меньше его. Это, как правило, обозначается следующим образом: p ≤ 0,05.
                 \n Мы проведем двухвыборочный t-тест со следующими гипотезами:
                 \n  **H 0 : µ 1 = µ 2** (средние значения двух популяций равны)
                 \n  **H 1 : μ 1 ≠ μ 2** (средние значения двух популяций не равны)
                 """)
                 
        t_statistic, p_value = perform_t_test(ttest_data, 'salary_1-3_years', 'salary_0_years')


        st.write("#### Результат t-теста:")
        st.write(f"**t-статистика**: {round(t_statistic, 4)}")
        st.write(f"**p-значение**: {round(p_value, 4)}")

        st.write(f"**Среднее в группе вакансий с требуемым опытом от 1 до 3-х лет**: {round(ttest_data['salary_1-3_years'].mean(), 4)}")
        st.write(f"**Среднее в группе вакансий без требуемого опыта**: {round(ttest_data['salary_0_years'].mean(), 4)}")

        st.divider()
        st.write("""#### Задание: 
                 \n #### Попробуйте самостоятельно объяснить результаты теста""")

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
    st.title("Вопросы по теории")

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

