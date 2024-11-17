import streamlit as st

st.set_page_config(layout='wide')
col1,col2 = st.columns(2)

with col1:
    st.image("images/photo.png",width=300)

with col2:
    st.title("Saurabh Sharma")
    content="""
    Hi I am Saurabh.I am a python coder with a software developer working in a large MNC Bank.
    I graduated in 2007 from Pune University and from thereon Have worked with various companies.
    Started my career from IBM on unix,sql and java.Moved onto Big data in 2014 when I was working
    with Reliance Jio and thereafter worked on Big data and cloud from 2018.Worked majorly on AWS.
    Have got good idea on Machine Learning,Deep Learning and Gen AI as well.
    """
    st.info(content)