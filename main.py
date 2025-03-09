import streamlit as st

st.set_page_config(page_title="Home", page_icon=":house:")

st.title("Welcome To My Project!!! :wave:")
col1, col2, col3 = st.columns(3)
with col1:
    st.image("data/pic/pic2.png", width=200)

with col2:
    st.image("data/pic/pic.png", width=200)

with col3:
    st.image("data/pic/pic3.png", width=200)

st.write(" ")

st.markdown(
    """**This project consists of two parts.**
    
**The first part is:** PDF Reader, where you can upload your chosen PDF document and ask questions related to its content.

**The second part is a movie recommendation system.** Here, you can also upload a document containing a list of movies and specify the theme or genre you are interested in. 
The system will then provide you with the three most relevant recommendations.

__I look forward to your suggestions and feedback on how this project could be further improved.__ 
"""
)

st.markdown(":point_left: **On the left side, you can select a project.**")
