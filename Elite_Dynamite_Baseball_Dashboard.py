import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title = 'Team Stats',layout='wide')

teamhitting = pd.read_csv("https://raw.githubusercontent.com/bamc021/st.EDB_Dashboard/main/CSV%20Files/EDBteamhitting.csv")
teampitching = pd.read_csv("https://raw.githubusercontent.com/bamc021/st.EDB_Dashboard/main/CSV%20Files/EDBteampitching.csv")

teamhitting_vars = teamhitting.columns.tolist()
teampitching_vars = teampitching.columns.tolist()

hitplotvars = [e for e in teamhitting_vars if e not in ('ID','Pos','Player','Team','Eligible','Status','Opponent','FANTRAXID','IDFANGRAPHS','MLBID','team_name')]
pitchplotvars = [g for g in teampitching_vars if g not in ('ID','Pos','Player','Team','Eligible','Status','Opponent','FANTRAXID','IDFANGRAPHS','MLBID','team_name')]

col1,col2=st.columns(2)

with col1:
    col1_1,col1_2=st.columns(2)
    with col1_1:
        teamhit_xaxis = st.selectbox('X Axis',hitplotvars,index=5)
    with col1_2:
        teamhit_yaxis = st.selectbox('Y Axis',hitplotvars,index=6)
    teamhitfig = px.scatter(teamhitting,x=teamhit_xaxis,y=teamhit_yaxis,color='Team')
    st.plotly_chart(teamhitfig)

with col2:
    st.header("Team Hitting Statistics")
    st.dataframe(teamhitting,hide_index=True)


col3,col4=st.columns(2)

with col3:
    col3_1,col3_2=st.columns(2)
    with col3_1:
        teampitch_xaxis = st.selectbox('X Axis',pitchplotvars,index=1)
    with col3_2:
        teampitch_yaxis = st.selectbox('Y Axis',pitchplotvars,index=4)
    teampitchfig = px.scatter(teampitching,x=teampitch_xaxis,y=teampitch_yaxis,color='Team')
    st.plotly_chart(teampitchfig)
   
with col4:
    st.header("Team Pitching Statistics")
    st.dataframe(teampitching,hide_index=True)
