import streamlit as st
import pandas as pd


st.set_page_config(layout='wide')
col1,col2 = st.columns(2)

with col1:
    st.image("images/photo.png",width=300)

with col2:
    st.title("Saurabh Sharma")
    content="""
    Hi I am Saurabh.I am a python coder with a software developer working in a large MNC Bank.
    Got good expertise on Big Data,Spark,Cloud(AWS/Azure),Databricks,ETL/ELT,Databases(SQL 
    and NoSql),Machine Learning,Gen AI,Devops,Iac(Infra as code).
    I graduated in 2007 from Pune University and from thereon Have worked with various companies.
    Started my career from IBM on unix,sql and java.Moved onto Big data in 2014 when I was working
    with Reliance Jio and thereafter worked on Big data and cloud from 2018.Worked majorly on AWS.
    Have got good idea on Machine Learning,Deep Learning and Gen AI as well.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I built in python.Feel Free to contact me!.
"""
st.info(content2)

"""empty col adds more space between the col3 and col4"""
col3,empty_col,col4=st.columns([1.5 , 0.5 , 1.5])

df=pd.read_csv("data.csv",sep=";")

with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")




