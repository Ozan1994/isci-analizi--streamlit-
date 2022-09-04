import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("filled_employees.csv")

st.title("İşçiler")

st.sidebar.header("Kullanıcı Seçenekleri")
upt_df = df.fillna(method="bfill")

not_null_team = sorted(df.Team.dropna().unique())
not_null_team.append("All Team")
not_null_team = sorted(not_null_team)

selected_team = st.sidebar.selectbox("Team",not_null_team)


upt_df[upt_df.Team == selected_team].Salary.mean()




if selected_team == "All Team":
    slt_mean = upt_df.Salary.mean()

elif selected_team:
    upt_df = upt_df[upt_df.Team == selected_team]
    slt_mean = upt_df[upt_df.Team == selected_team].Salary.mean()



gender_all = upt_df.Gender.value_counts(normalize=True)*100
writing_all = selected_team + " takımında " + str( gender_all.keys()[0] ) + " %" + str( round(gender_all.values[0],2) ) + " ve " + str(gender_all.keys()[1]) + " %" + str(round(gender_all.values[1],2)) + " bulunmaktadır"

#Tablo verileri
st.dataframe(upt_df)

#Tablo hakkında bilgi
st.subheader("Tablo hakkında bilgiler")
st.write(str(selected_team)+" takımının ortalama maaşları: " + str(slt_mean) )

# Tablodaki kişilerin oranı
if selected_team == "All Team":
    st.write(writing_all)
elif selected_team:
    gender = upt_df[upt_df.Team == str(selected_team)].Gender.value_counts(normalize=True) * 100
    writing = selected_team + " takımında " + str(gender.keys()[0]) + " %" + str(
        round(gender.values[0], 2)) + " ve " + str(gender.keys()[1]) + " %" + str(
        round(gender.values[1], 2)) + " bulunmaktadır"
    st.write(writing)



st.subheader("**{}** takımının maaş ve bonus noktaları".format(selected_team))
# Grafik çizimi
f, ax = plt.subplots(figsize=(9,7))
ax.scatter(upt_df.Salary,upt_df["Bonus %"])

ax = plt.xlabel("Salary")
ax = plt.ylabel("Bonus %")

st.pyplot(f)






