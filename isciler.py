import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

upt_df = pd.read_csv("filled_employees.csv")

st.title("İşçiler")

st.sidebar.header("Kullanıcı Seçenekleri")

not_null_team = sorted(upt_df.Team.dropna().unique())
not_null_team.append("All Team")
not_null_team = sorted(not_null_team)

#Takımların kutusu
selected_team = st.sidebar.selectbox("Team",not_null_team)
# Cinsiyet kutusu
selected_gender = np.append(["All"],upt_df.Gender.unique())
selected_gender = st.sidebar.selectbox("Gender",selected_gender)





if selected_gender == "All":
    if selected_team == "All Team":
        slt_mean = round(upt_df.Salary.mean(),2)


    elif selected_team:
        upt_df = upt_df[upt_df.Team == selected_team]
        slt_mean = upt_df.Salary.mean()
        slt_mean = round(slt_mean,2)

elif selected_gender == "Male":
    upt_df = upt_df[upt_df.Gender == "Male"]
    if selected_team == "All Team":
        slt_mean = round(upt_df.Salary.mean(),2)

    elif selected_team:
        upt_df = upt_df[upt_df.Team == selected_team]
        slt_mean = upt_df.Salary.mean()
        slt_mean = round(slt_mean,2)

elif selected_gender == "Female":
    upt_df = upt_df[upt_df.Gender == "Female"]
    if selected_team == "All Team":
        slt_mean = round(upt_df.Salary.mean(),2)

    elif selected_team:
        upt_df = upt_df[upt_df.Team == selected_team]
        slt_mean = upt_df.Salary.mean()
        slt_mean = round(slt_mean,2)



#Tablo verileri
st.dataframe(upt_df)


st.write("***")

#Tablo hakkında bilgi
st.subheader("Tablo hakkında bilgiler")

# Tablodaki maaş ortalamaları
st.write(str(selected_team)+" takımının ortalama maaşları: " + str(slt_mean) )

# Tablodaki kişilerin oranı
if selected_gender == "All":
    gender_all = upt_df.Gender.value_counts(normalize=True) * 100
    writing_all = selected_team + " takımında " + str(gender_all.keys()[0]) + " %" + str(
        round(gender_all.values[0], 2)) + " ve " + str(gender_all.keys()[1]) + " %" + str(
        round(gender_all.values[1], 2)) + " bulunmaktadır"

    if selected_team == "All Team":
        st.write(writing_all)

    elif selected_team:
        gender = upt_df[upt_df.Team == str(selected_team)].Gender.value_counts(normalize=True) * 100
        writing = selected_team + " takımında " + str(gender.keys()[0]) + " %" + str(
            round(gender.values[0], 2)) + " ve " + str(gender.keys()[1]) + " %" + str(
            round(gender.values[1], 2)) + " bulunmaktadır"
        st.write(writing)

else:
    pass





st.write("***")


st.subheader("Tüm takımların cinsiyete göre ortalama maaş grafiği ")
# Grafik çizimi

upt_df = pd.read_csv("filled_employees.csv")

fig = plt.figure(figsize=(12,10))
sns.set(font_scale= 1.5)
plt.grid(which = "both",color="y",axis = "y")
sns.barplot(x = 'Team',
            y = 'Salary',
            hue= 'Gender',
            data = upt_df,
            palette=["mediumblue","orangered"],
            estimator = np.mean,
            capsize=0.15,
            ci=0)

plt.xticks(rotation=35)
plt.tight_layout()

st.pyplot(fig)





