import streamlit as st
st.title("Formatting values to be inserted into an MySql tabel")
st.subheader("please note that this will only work if every column uses a varchar datatype")

txtic= st.empty()
txt= st.text_area(label="Enter values",height=300,max_chars=1000,placeholder="values go here")






lines=txt.split("\n")
for line in lines:
    a=line.split()
    st.write(str(a)[1:-1])

