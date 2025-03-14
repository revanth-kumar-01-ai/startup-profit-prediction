import streamlit as st

from StreamlitUI import config

st.set_page_config(page_title = config.PROJECT_NAME, layout = 'wide')

home = st.Page(
    page = "StreamlitUI/ViewPage/Home.py", 
    title = "Home", 
    icon = '🏠' 
)

dataExploration = st.Page(
    page = "StreamlitUI/ViewPage/Data_Exploration.py", 
    title = "Data Exploration", 
    icon = '📊' 
)

modelTraining = st.Page(
    page = "StreamlitUI/ViewPage/Model_Training.py", 
    title = "Model Training", 
    icon = '🤖' 
)

prediction = st.Page(
    page = "StreamlitUI/ViewPage/Prediction.py", 
    title = "Prediction", 
    icon = '🎯' 
)

conclusion = st.Page(
    page = "StreamlitUI/ViewPage/Conclusion.py", 
    title = "Conclusion", 
    icon = '🔍' 
)

st.logo('StreamlitUI/assets/logo.png', size = 'large')

pg = st.navigation({
    config.PROJECT_NAME:[home, dataExploration, modelTraining, prediction, conclusion]
})

pg.run()