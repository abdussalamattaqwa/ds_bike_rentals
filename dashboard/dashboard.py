import pandas as pd
import seaborn as sns
import streamlit as st 

st.title('Dashboard Submission')
st.header('Belajar Analisis Data dengan Python')


day_bs_df = pd.read_csv("./data/day.csv")

# mengubah value numerik pada kolom season menjadi string sesuai dengan definisinya
day_bs_df['season'] = day_bs_df['season'].map({
    1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'
})

day_bs_df['yr'] = day_bs_df['yr'].map({
    0: '2011', 1: '2012'
})

# Mengubah nama kolom yr menjadi year
day_bs_df.rename(columns={
    'yr': 'year',
}, inplace=True)


st.write('Tabel data penyewaan sepeda selama tahun 2011 dan 2012')
st.write(day_bs_df)


st.markdown(
    """

    ## Grafik tren penyewaan sepeda setiap musim


    """
)



st.bar_chart(day_bs_df, x="season", y="cnt")

st.markdown(
    """

    ## Grafik tren penyewaan sepeda setiap musim selama dua tahun berturut-turut


    """
)


plot = sns.barplot(data=day_bs_df, x="season", y="cnt", hue="year")
st.pyplot(plot.get_figure())