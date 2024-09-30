import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

#streamlit wide layout
st.set_page_config(layout="wide")

day_df = pd.read_csv("data/day.csv")
hour_df = pd.read_csv("data/hour.csv")

#konversi tipe data kolum dteday dari string menjadi datetime
day_df.dteday = pd.to_datetime(day_df["dteday"])

#input awal start_date dan end_date untuk sidebar
min_date = day_df["dteday"].min()
max_date = day_df["dteday"].max()

#Inisiasi default value untuk dates
start_date, end_date = str(min_date)[0:10], str(max_date)[0:10]

#Mengecek jika tanggal awal dan akhir terpilih
def min_max_date():
    return (str(min_date)[0:10] == str(start_date)) and (str(max_date)[0:10] == str(end_date))
    

#Sidebar
with st.sidebar:
        
    timespan_date_input = st.date_input(
        label='Time Span',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date],
        key="test"
    )       

    if st.button("confirm"):
        start_date, end_date = timespan_date_input



#dataframe yang telah terfilter dengan min dan max value dari sidebar
main_df = day_df[(day_df["dteday"] >= str(start_date)) & (day_df["dteday"] <= str(end_date))]

if(min_max_date()):
    st.header("Total Rent Statistics")
else:
    st.header('Rent Statistic Within ' + str(start_date) + " - " + str(end_date))

#Kolum
col1, col2, col3, col4 = st.columns(4)

with col1:
    total_rent = main_df.cnt.sum()
    st.metric("Total Rent", value=total_rent)

with col2:
    mean = main_df.cnt.mean()
    st.metric("Mean", value=np.round(mean, decimals=2))

with col3:
    min = main_df.cnt.min()
    st.metric("Min", value=min)

with col4:
    max = main_df.cnt.max()
    st.metric("Max", value=max)


#grafik
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    main_df.dteday,
    main_df.cnt, 
)

plt.xlabel("Time Span", fontsize=20)
plt.ylabel("Rent", fontsize=20)


plt.grid(True)
st.pyplot(fig)

if (min_max_date()):
    col1, col2 = st.columns(2)

    with col1:
        fig, ax = plt.subplots(figsize=(20, 10))

        sns.scatterplot(
        x="hr",
        y="cnt", 
        data=hour_df,
        ax=ax,
        s=500
        )

        ax.set_title("Rental Demand by Hour", loc="center", fontsize=50)
        ax.set_xlabel("Hours (24:00)", fontsize=40)
        ax.set_ylabel("Rented", fontsize=40)
        ax.tick_params(axis='x', labelsize=35)
        ax.tick_params(axis='y', labelsize=30)
        plt.grid(True)
        st.pyplot(fig)

    with col2:
        fig, ax = plt.subplots(figsize=(20, 10))
        
        sns.scatterplot(
        x="temp",
        y="cnt", 
        data=hour_df,
        ax=ax,
        s=500
        )

        ax.set_title("Rental Demand by Temperature in Celsius", loc="center", fontsize=50)
        ax.set_xlabel("Temperature (values x 41)", fontsize=40)
        ax.set_ylabel("Rented", fontsize=40)
        ax.tick_params(axis='x', labelsize=35)
        ax.tick_params(axis='y', labelsize=30)
        plt.grid(True)
        st.pyplot(fig)

    col1, col2 = st.columns(2)

    with col1:
        fig, ax = plt.subplots(figsize=(20, 10))
        
        sns.scatterplot(
        x="atemp",
        y="cnt", 
        data=hour_df,
        ax=ax,
        s=500
        )

        ax.set_title("Rental Demand by Feeling Temperature in Celsius", loc="center", fontsize=45)
        ax.set_xlabel("Feeling Temperature (values x 50)", fontsize=30)
        ax.set_ylabel("Rented", fontsize=40)
        ax.tick_params(axis='x', labelsize=35)
        ax.tick_params(axis='y', labelsize=30)
        plt.grid(True)
        st.pyplot(fig)

    with col2:
        fig, ax = plt.subplots(figsize=(20, 10))
        
        sns.scatterplot(
        x="hum",
        y="cnt", 
        data=hour_df,
        ax=ax,
        s=500
        )

        ax.set_title("Rental Demand by Humidty", loc="center", fontsize=50)
        ax.set_xlabel("Humidty (values x 100)", fontsize=30)
        ax.set_ylabel("Rented", fontsize=40)
        ax.tick_params(axis='x', labelsize=35)
        ax.tick_params(axis='y', labelsize=30)
        plt.grid(True)
        st.pyplot(fig)
        sns.scatterplot(data = hour_df, x = "hum", y = "cnt")
        plt.show()
