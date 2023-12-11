# Submission Dicoding Kelas "Belajar Analisis Data dengan Python"
Projek ini merupakan projek submission untuk kelas "Belajar Analisis Data dengan Python". Dataset yang digunakan adalah dataset penyewaan sepeda. Analisis dilakukan dengan cara melihat pola penyewaan sepeda berdasarkan season selama dua tahun terakhir.

# Tahapan Analisis
- Data Wrangling
- Exploratory Data Analysis (EDA)
- Visualization & Explanatory Analysis
- Conclusion

# Cara Menjalankan Program
## Cloning Program
Cloning repositori ini kedalam penyimpanan lokal komputer
```
git clone https://github.com/abdussalamattaqwa/ds_bike_rentals.git
```
Buka direktori proyek
```
cd ds_bike_rentals
```

## Setup environment
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install - r requirements.txt
```

## Run steamlit app
```
streamlit run dashboard/dashboard.py
```