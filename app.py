import streamlit as st

st.title('power calculator')
st.write('enter the number to calculate its square, cube and fifth power.')

#Get user input
n=st.number_input('Enter an integer', value=1, step=1)

square=n**2
cube=n**3
fifth_power=n**5

#display result
st.write(f'The sqaure of a {n} is {square} .')
st.write(f'The cube of a {n} is {cube} .')
st.write(f'The fifth power of a {n} is {fifth_power} .')