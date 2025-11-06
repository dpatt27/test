import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

st.write("hello")
st.title("My first app")

df = pd.DataFrame(np.random.randn(10,2), columns= ["Product A", "Product B"])
st.line_chart(df)
st.bar_chart(df)

df2 = pd.DataFrame(np.random.randn(500,2)/[50, 50] + [30.5, -97.6], columns=["lat", "lon"])
st.map(df2)


st.video("https://www.youtube.com/watch?v=3pJNTJfDh90")

st.checkbox("this is a checkbox")
st.button("Select")
st.radio("Choose one", ["option 1", "option 2", "option 3"])
st.multiselect("multiselect", ["option 1", "option 2", "option 3"])
st.slider("slider", 0, 100, 50)

st.header("Header")
st.latex(r"E=mc^2")


data = np.random.normal(loc=1, scale=2, size=5000)

fig, ax = plt.subplots()
ax.hist(data, bins=15)
ax.set_xlabel("Value")
ax.set_ylabel("Frequency")

st.pyplot(fig)