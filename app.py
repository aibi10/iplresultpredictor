import streamlit as st
import pickle
import pandas as pd

teams = ['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals']



pipe = pickle.load(open('pipe.pkl','rb'))
st.markdown("<h1 style='text-align: center; color: maroon;'>IPL Result Predictor</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select the batting team',sorted(teams), index = 5)
with col2:
    bowling_team = st.selectbox('Select the bowling team',sorted(teams), index = 6)


target = st.number_input('Target', min_value = 0)

col3,col4,col5 = st.columns(3)

with col3:
    score = st.number_input('Score', min_value = 0)
with col4:
    overs = st.number_input('Overs completed', value = 0.1, format="%.1f")
with col5:
    wickets = st.number_input('Wickets out', min_value = 0)





if st.button('Click Here For Results'):
    runs_left = target - score
    ov = str(overs)
    index = ov.index('.')
    o = ov[0 : index]
    b = ov[index : ]
    if float(o) != 0.0:
        z = int(float(o) * 6 + float(b))
    else:
        z = float(float(o) * 6 + float(b))
    balls_left = 120 - z
    wickets = 10 - wickets
    crr = score / z
    rrr = (runs_left*6)/balls_left

    input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'runs_left':[runs_left],'balls_left':[balls_left],'wickets':[wickets],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})

    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.header(batting_team + "- " + str(round(win*100)) + "%")
    st.header(bowling_team + "- " + str(round(loss*100)) + "%")
    
st.caption('To my three cute nephews: Aadarsh, Devansh and Atharva')
    
