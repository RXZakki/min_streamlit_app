import streamlit as st


expressbiljett = 1.2
returbiljett = 0.8
enkelbiljett = 1
totalprice = 0
saldo = 0

st.title('Tågbiljetts kalkylator baserad på ålder')
updsaldo =st.number_input('Välj belopp här')
saldo = saldo + updsaldo
st.write(f'Uppdaterat saldo till {saldo}kr')


st.header('vilken typ av biljett vill du ha?: enkel, retur, express')
biljettyp = st.selectbox('Vilken biljettyp vill du ha?',("enkel", "retur", "express"),
 )
st.subheader('vänligen ange din ålder nedan')
age = st.slider("Ange här", min_value=None, max_value=120, value=None, step=1)


if age < 18 and biljettyp == 'enkel':
    saldo=saldo- 130 * enkelbiljett
    st.write(f'Du angav åldern: {age}. Ditt nya saldo är {saldo}kr')
    st.subheader('Ha en trevlig resa!')
elif age < 18 and biljettyp == 'retur':
    saldo=saldo - 130 * 2 * returbiljett
    st.write(f'Du angav åldern: {age}. Ditt nya saldo är {saldo}kr')
    st.subheader('Ha en trevlig resa!')
elif age < 18 and biljettyp == 'express':
    saldo=saldo - 130 * expressbiljett
    st.write(f'Du angav åldern: {age}. Ditt nya saldo är {saldo}kr')
    st.subheader('Ha en trevlig resa!')
elif 18 <= age <= 64 and biljettyp == 'enkel':
    saldo=saldo - 230 * enkelbiljett
    st.write(f'Du angav åldern: {age}. Ditt nya saldo är {saldo}kr')
    st.subheader('Ha en trevlig resa!')
elif 18 <= age <= 64 and biljettyp == 'retur':
    saldo=saldo - 230 * 2 * returbiljett
    st.write(f'Du angav åldern: {age}. Ditt nya saldo är {saldo}kr')
    st.subheader('Ha en trevlig resa!')
elif 18 <= age <= 64 and biljettyp == 'express':
    saldo=saldo - 230 * expressbiljett
    st.write(f'Du angav åldern: {age}. Ditt nya saldo är {saldo}kr')
    st.subheader('Ha en trevlig resa!')
elif 64 < age <= 120 and biljettyp == 'enkel':
    saldo=saldo - 100 * enkelbiljett
    st.write(f'Du angav åldern: {age}. Ditt nya saldo är {saldo}kr')
    st.subheader('Ha en trevlig resa!')
elif 64 < age <= 120 and biljettyp == 'retur':
    saldo=saldo - 100 * 2 * returbiljett
    st.write(f'Du angav åldern: {age}. Ditt nya saldo är {saldo}kr')
    st.subheader('Ha en trevlig resa!')
elif 64 < age <= 120 and biljettyp == 'express':
    saldo=saldo - 100 * expressbiljett
    st.write(f'Du angav åldern: {age}. Ditt nya saldo är {saldo}kr')
    st.subheader('Ha en trevlig resa!')
else:
    st.subheader('ogiltigt svar')
    breakpoint()
