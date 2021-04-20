import streamlit as st
import sklearn
import joblib
model =joblib.load('Email_Class')

add_selectbox = st.sidebar.radio("Our page",['Home',"Rate us"])
if(add_selectbox == 'Home'):
  st.title("Myntra collections")
  st.image('https://akm-img-a-in.tosshub.com/sites/btmt/images/stories/myntra_logo_660_300121011207.jpg')

  ip = st.text_input('Enter your valuabe review')
  p = model.predict([ip])
  if st.button('Predict'):
    st.header(p[0])
    if(p[0]=='Good'):
      st.markdown(""":smile:""")
    else:
      st.markdown(""":angry:""")
else:
  st.title("Please Rate US")
  st.slider("Rate us",0,5)
  if st.button("Press Submit"):
    st.header("Thanks for your rating..")
  