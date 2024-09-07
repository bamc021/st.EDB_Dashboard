import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title = 'MLB Player Stats',layout='wide')

hittingmajors = pd.read_csv("https://raw.githubusercontent.com/bamc021/st.EDB_Dashboard/main/CSV%20Files/EDBrosteredhitters.csv")
hittingmajors = hittingmajors.drop(columns=['ID','Pos','Status','Opponent','FANTRAXID','IDFANGRAPHS','MLBID','Swings','Z-Pitches','Z-Swings','O-Pitches','O-Swings'])
hittingmajors = hittingmajors.rename(columns={'Eligible': 'Pos'})
team_col = hittingmajors.pop('team_name')
hittingmajors.insert(3,'team_name',team_col)

pitchingmajors = pd.read_csv("https://raw.githubusercontent.com/bamc021/st.EDB_Dashboard/main/CSV%20Files/EDBrosteredpitchers.csv")
pitchingmajors = pitchingmajors.drop(columns=['ID','Pos','Status','Opponent','FANTRAXID','IDFANGRAPHS','MLBID'])
team_col = pitchingmajors.pop('team_name')
pitchingmajors.insert(3,'team_name',team_col)

hittingmajors_vars = hittingmajors.columns.tolist()
pitchingmajors_vars = pitchingmajors.columns.tolist()


hitplotvars = [e for e in hittingmajors_vars if e not in ('ID','Pos','Player','Team','Eligible','Status','Opponent','FANTRAXID','IDFANGRAPHS','MLBID','team_name')]
pitchplotvars = [g for g in pitchingmajors_vars if g not in ('ID','Pos','Player','Team','Eligible','Status','Opponent','FANTRAXID','IDFANGRAPHS','MLBID','team_name')]

st.header('Major League Hitting')
col1, col2 = st.columns(2)
with col1:
    majorhit_xaxis = st.selectbox('X Axis',hitplotvars,index=4)
with col2:
    majorhit_yaxis = st.selectbox('Y Axis',hitplotvars,index=8)

majorhitfig = px.scatter(hittingmajors,x=majorhit_xaxis,y=majorhit_yaxis,color='team_name',hover_name='Player')
st.plotly_chart(majorhitfig)
st.dataframe(hittingmajors,hide_index=True)

st.header('Major League Pitching')
col3,col4 = st.columns(2)
with col3:
    majorpitch_xaxis = st.selectbox('X Axis',pitchplotvars,index=4)
with col4:
    majorpitch_yaxis = st.selectbox('Y Axis',pitchplotvars,index=5)

majorpitchfig = px.scatter(pitchingmajors,x=majorpitch_xaxis,y=majorpitch_yaxis,color='team_name',hover_name='Player')
st.plotly_chart(majorpitchfig)
st.dataframe(pitchingmajors,hide_index=True)
