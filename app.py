import pandas as pd
import numpy as np
import streamlit as st
import joblib
from joblib import load

import plotly.graph_objects as go

# carregamento do modelo treinado

model = load('models/model.joblib')

# Título da aplicação

st.title("Classificador de desempenho acadêmico")

# divisão da entrada em colunas

col1, col2, col3, col4 = st.columns(4)

# inputs

gender = col1.selectbox( 
    label='Gênero',
    help='Como você se identifica quanto ao gênero?',
    options=['Male', 'Female']
)

NationalITy = col2.selectbox(
    'Nacionalidade do estudante',
    ["Kuwait", "Lebanon", "Egypt", 
     "SaudiArabia", "USA", "Jordan", 
     "Venezuela"," Iran","Tunis",
     "Morocco","Syria","Palestine",
     "Iraq","Lybia"]
)

PlaceofBirth = col3.selectbox(
    'Local de nascimento do estudante',
    ["Kuwait", "Lebanon", "Egypt", 
     "SaudiArabia", "USA", "Jordan", 
     "Venezuela"," Iran","Tunis",
     "Morocco","Syria","Palestine",
     "Iraq","Lybia"]
)


StageID = col4.selectbox(
    'Nível escolar do estudante',
    ["lowerlevel", "MiddleSchool", "HighSchool"]
)


GradeID = col1.selectbox(
    'Turma a qual o aluno pertence',
    ["G-01", "G-02", "G-03", "G-04", 
     "G-05", "G-06", "G-07", "G-08", 
     "G-09", "G-10", "G-11", "G-12"]
)


SectionID = col2.selectbox(
    'Sala de aula a qual o aluno pertence',
    ["A", "B", "C"]
)


Topic = col3.selectbox(
    'Topico do curso',
    ["English", "Spanish", "French", 
     "Arabic", "IT", "Math", 
     "Chemistry", "Biology", "Science", 
     "History", "Quran", "Geology"]
)


Semester = col4.selectbox(
    'Semestre letivo',
    ["F", "S"]
)


Relation = col1.selectbox(
    'Parente responsavel pelo estudante',
    ["Mom", "Father"]
)


raisedhands = col2.number_input(
    "Quantas vezes o estudante levanta sua mão na sala de aula?", 
                min_value=0, 
                max_value=100, 
                value=0)


VisITedResources = col3.number_input(
    "Quantas vezes o estudante pesquisa o conteudo do curso?", 
                min_value=0, 
                max_value=100, 
                value=0)


AnnouncementsView = col4.number_input(
    "Quantas vezes o estudante verifica as novidades do curso?", 
                min_value=0, 
                max_value=100, 
                value=0)

Discussion = col1.number_input(
    "Quantas vezes o estudante participa de grupo de discurssão?", 
                min_value=0, 
                max_value=100, 
                value=0)


ParentAnsweringSurvey = col2.selectbox(
    'O responsavel respondeu as pesquisas fornecidas?',
    ["Yes", "No"]
)


ParentschoolSatisfaction = col3.selectbox(
    'Qual o grau de satisfação com as escolas?',
    ["Good", "Bad"]
)


StudentAbsenceDays = col4.selectbox(
    'O número total de faltas do aluno é?',
    ["above - 7", "Under - 7"]
)

# armazenamento dos inputs

inputs = {'gender':[gender], 'NationalITy':[NationalITy],
         'PlaceofBirth':[PlaceofBirth], 'StageID':[StageID], 
         'GradeID':[GradeID], 'SectionID':[SectionID], 
         'Topic':[Topic], 'Semester':[Semester], 
         'Relation':[Relation], 'raisedhands':[raisedhands], 
         'VisITedResources':[VisITedResources], 'AnnouncementsView':[AnnouncementsView],
         'Discussion':[Discussion],'ParentschoolSatisfaction':[ParentschoolSatisfaction],
         'ParentAnsweringSurvey':[ParentAnsweringSurvey],
         'StudentAbsenceDays':[StudentAbsenceDays]
        }

# conversão em data frame

df = pd.DataFrame (inputs)

foo = [2, 0, 1]

# Predição

if st.button('Análise da(o) aluna(o)'):
    result = model.predict_proba(df)
    final_result = foo[result.argmax()]*(1/3)+result.max()/3
    result_ = model.predict(df)
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = final_result,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Nível"},
        gauge = {
            'axis': {'range':[0,1]},
            'steps': [
                {'range':[0,0.3333],
                 'color': "lightgray"},
                {'range':[0.3333, 0.6666],
                 'color': "gray"}
            ] 
        }
    ))
    st.plotly_chart(fig)
    
    if result_ == 'L':
        st.error("A maior probabilidade é que o aluno pertença ao Lower Level")
    elif result_ == 'M':
        st.info("A maior probabilidade é que o aluno pertença ao Middle Level")
    else:
        st.success("A maior probabilidade é que o aluno pertença ao High Level")
    
        