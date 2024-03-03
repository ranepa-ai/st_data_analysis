import streamlit as st

this_name = 'Основы промпт-инжиниринг💬🚀'

def page_redirect(df):
    # Section: Course Summary and Feedback
    st.header("Глава: Итоги 🏁", divider='rainbow')

    # CSI and NPS questions
    csi_rating = st.radio("Насколько вам понравился этот курс?", options=["1 (Совсем не понравился)", "2", "3", "4", "5 (Понравился очень)"], index=None)
    nps_rating = st.radio("Насколько вероятно, что вы порекомендуете этот курс своим знакомым?", options=["1 (Совсем не вероятно)", "2", "3", "4", "5 (Очень вероятно)"], index=None)

    # Display feedback based on ratings
    if csi_rating == "5 (Понравился очень)" and nps_rating == "5 (Очень вероятно)":
        st.success("Спасибо за высокие оценки! Мы очень рады, что вам понравился курс.")
    elif csi_rating in ["1 (Совсем не понравился)", "2", "3"] or nps_rating in ["1 (Совсем не вероятно)", "2", "3"]:
        st.error("Мы сожалеем, что курс не полностью соответствовал вашим ожиданиям. Мы постараемся улучшить его в будущем.")
    elif csi_rating in ["4"] or nps_rating in ["4"]:
        st.info("Спасибо за ваш отзыв! Ваши комментарии помогут нам сделать курс еще лучше.")

    df_sample = df.iloc[df[df['Name'] == this_name].index[0]:]
    this_track = df_sample.Track.iloc[0]
    
    N_cards_per_row = 3
    n_place = 0

    st.header("Продолжайте практику!")

    if len(df_sample[df_sample['Name'] == this_track]) > 1:
        df_sample_new = df_sample[df_sample.Track==this_track].iloc[1:].reset_index(drop=True)
    else:
         this_track = df_sample.Track.iloc[1]
         df_sample_new = df_sample[df_sample.Track==this_track].reset_index(drop=True)
    cols = st.columns(N_cards_per_row, gap="large")
    print(df_sample_new)
    for n_row, row in df_sample_new.iterrows():
        
        # URL изображения
        image_cot = f'https://github.com/Chetoff1228/images/blob/main/{row["Picture"]}.png?raw=true'

        with cols[n_place % N_cards_per_row]:
            st.markdown(f"**{row['Name']}**")
            st.markdown(f'<a href="{row["Source"]}"><img src="{image_cot}" alt="Foo" width="275" height="250"/></a>', unsafe_allow_html=True)
            st.caption(f"**{row['Caption'].strip()}**")
        n_place += 1
        
    st.write("---")