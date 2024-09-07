import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title = 'MiLB Player Stats',layout='wide')

hittingminors = pd.read_csv("https://raw.githubusercontent.com/bamc021/st.EDB_Dashboard/main/CSV%20Files/Minors%20Stats%20for%20Fantasy%20-%20Batters.csv")
hittingminors = hittingminors[hittingminors['EDB Team'].notna()]
hittingminors = hittingminors.drop(columns=['TWTC Team','BL Team','PlayerId'])
hittingminors = hittingminors.drop(hittingminors.columns[0],axis=1)
team_col = hittingminors.pop('EDB Team')
hittingminors.insert(3,'EDB Team',team_col)

pitchingminors = pd.read_csv("https://raw.githubusercontent.com/bamc021/st.EDB_Dashboard/main/CSV%20Files/Minors%20Stats%20for%20Fantasy%20-%20Pitchers.csv")
pitchingminors = pitchingminors[pitchingminors['EDB Team'].notna()]
pitchingminors = pitchingminors.drop(columns=['TWTC Team','BL Team','PlayerId'])
pitchingminors = pitchingminors.drop(hittingminors.columns[0],axis=1)
team_col = pitchingminors.pop('EDB Team')
pitchingminors.insert(3,'EDB Team',team_col)

hittingminors_vars = hittingminors.columns.tolist()
pitchingminors_vars = pitchingminors.columns.tolist()

minhitplotvars = [e for e in hittingminors_vars if e not in ('Name','Team','Level','PlayerId','EDB Team','TWTC Team','BL Team')]
minpitchplotvars = [g for g in pitchingminors_vars if g not in ('Name','Team','Level','PlayerId','EDB Team','TWTC Team','BL Team')]

st.header('Minor League Hitting')
col1,col2 = st.columns(2)
with col1:
    minorhit_xaxis = st.selectbox('X Axis',minhitplotvars,index=18)
with col2:
    minorhit_yaxis = st.selectbox('Y Axis',minhitplotvars,index=21)

minorhitfig = px.scatter(hittingminors,x=minorhit_xaxis,y=minorhit_yaxis,color='EDB Team',hover_name='Name')
st.plotly_chart(minorhitfig)
st.dataframe(hittingminors,hide_index=True)

st.header('Minor League Pitching')
col3,col4 = st.columns(2)
with col3:
    minorpitch_xaxis = st.selectbox('X Axis',minpitchplotvars,index=1)
with col4:
    minorpitch_yaxis = st.selectbox('Y Axis',minpitchplotvars,index=10)

minorpitchfig = px.scatter(pitchingminors,x=minorpitch_xaxis,y=minorpitch_yaxis,color='EDB Team',hover_name='Name')
st.plotly_chart(minorpitchfig)
st.dataframe(pitchingminors,hide_index=True)
