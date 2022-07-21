import streamlit as st

import numpy as np
import pandas as pd

st.title("This is a title")
st.header("My first Streamlit App")


st.write("""
# This is a first-level heading
## This is a second-level heading
""")

st.write(pd.DataFrame({
    'Intplan': ['yes', 'yes', 'yes', 'no'],
    'Churn Status': [0, 0, 0, 1]
}))

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
