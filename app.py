import pandas as pd
import numpy as np
import streamlit as st
from joblib import load
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
# carregamento do modelo treinado

model = load('models/model.joblib')


country_mapping = {
    "Kuwait": "Kuwait",
    "Lebanon": "Líbano",
    "Egypt": "Egito",
    "SaudiArabia": "Arábia Saudita",
    "USA": "Estados Unidos",
    "Jordan": "Jordânia",
    "Venezuela": "Venezuela",
    " Iran": "Irã",
    "Tunis": "Tunísia",
    "Morocco": "Marrocos",
    "Syria": "Síria",
    "Palestine": "Palestina",
    "Iraq": "Iraque",
    "Lybia": "Libia"
}

level_mapping = {
    "lowerlevel": "Pré escolar",
    "MiddleSchool": "Ensino fundamental",
    "HighSchool": "Ensino médio"
}

topic_mapping = {
    "English": "Inglês",
    "Spanish": "Espanhol",
    "French": "Frances",
    "Arabic": "Árabe",
    "IT": "Informática",
    "Math": "Matemática",
    "Chemistry": "Química",
    "Biology": "Biologia",
    "Science": "Ciências",
    "History": "História",
    "Quran": "Religião",
    "Geology": "Geologia",
}


def main():

    with st.sidebar:
        selected = option_menu("Menu", ["Aplicação", 'Sobre nós'], 
            icons=['house', 'emoji-smile'], menu_icon="cast", default_index=0)

    if selected == 'Aplicação':
    # Título da aplicação
        st.markdown("<h1 style='text-align: center; font-size: 36px;'>Classificador de desempenho acadêmico</h1>", unsafe_allow_html=True)
        # divisão da entrada em colunas

        col1, col2, col3, col4 = st.columns(4)

        # inputs

        gender = col1.selectbox( 
            label='Gênero',
            help='Como você se identifica quanto ao gênero?',
            format_func=lambda x: 'Masculino' if x == 'Male' else 'Feminino',
            options=['Male', 'Female']
        )

        NationalITy = col2.selectbox(
            label='Nacionalidade',
            help='Nacionalidade do estudante',
            format_func=lambda x: country_mapping.get(x),
            options=["Kuwait", "Lebanon", "Egypt", 
             "SaudiArabia", "USA", "Jordan", 
             "Venezuela"," Iran","Tunis",
             "Morocco","Syria","Palestine",
             "Iraq","Lybia"]
        )

        PlaceofBirth = col3.selectbox(
            label='Naturalidade',
            help='Local de nascimento do estudante',
            format_func=lambda x: country_mapping.get(x),
            options=["Kuwait", "Lebanon", "Egypt", 
             "SaudiArabia", "USA", "Jordan", 
             "Venezuela"," Iran","Tunis",
             "Morocco","Syria","Palestine",
             "Iraq","Lybia"]
        )


        StageID = col4.selectbox(
            label='Grau escolar',
            help='Nível escolar do estudante',
            format_func=lambda x: level_mapping.get(x),
            options=["lowerlevel", "MiddleSchool", "HighSchool"]
        )


        GradeID = col1.selectbox(
            label='Turma',
            help='Turma a qual o aluno pertence',
            options=["G-01", "G-02", "G-03", "G-04", 
             "G-05", "G-06", "G-07", "G-08", 
             "G-09", "G-10", "G-11", "G-12"]
        )


        SectionID = col2.selectbox(
            label='Nome da sala',
            help='Sala de aula a qual o aluno pertence',
            options=["A", "B", "C"]
        )


        Topic = col3.selectbox(
            label='Disciplina',
            help='Topico do curso',
            format_func=lambda x: topic_mapping.get(x),
            options=["English", "Spanish", "French", 
             "Arabic", "IT", "Math", 
             "Chemistry", "Biology", "Science", 
             "History", "Quran", "Geology"]
        )


        Semester = col4.selectbox(
            label='Semestre',
            help='Semestre letivo',
            format_func=lambda x: "Primeiro" if x == "F" else "Segundo",
            options=["F", "S"]
        )


        Relation = col1.selectbox(
            label='Tutor',
            help='Parente responsável pelo estudante',
            format_func=lambda x: "Mãe" if x == "Mom" else "Pai",
            options=["Mom", "Father"]
        )


        raisedhands = col2.number_input(
            label='Interação do aluno',
            help="Quantas vezes o estudante levanta sua mão na sala de aula?", 
            min_value=0, 
            max_value=100, 
            value=0
        )


        VisITedResources = col3.number_input(
            label='Quantidade de pesquisa',
            help="Quantas vezes o estudante pesquisa o conteudo do curso?", 
            min_value=0, 
            max_value=100, 
            value=0
        )


        AnnouncementsView = col4.number_input(
            label='Novidades de conteudo',
            help="Quantas vezes o estudante verifica as novidades do curso?", 
            min_value=0, 
            max_value=100, 
            value=0
        )

        Discussion = col1.number_input(
            label='Participação de debates',
            help="Quantas vezes o estudante participa de grupo de discurssão?", 
            min_value=0, 
            max_value=100, 
            value=0
        )


        ParentAnsweringSurvey = col2.selectbox(
            label='Participação do tutor',
            help='O responsavel respondeu as pesquisas fornecidas?',
            format_func=lambda x: "Sim" if x == "Yes" else "Não",
            options=["Yes", "No"]
        )


        ParentschoolSatisfaction = col3.selectbox(
            label='Nível de satisfação',
            help='Qual o grau de satisfação com as escolas?',
            format_func=lambda x: "Bom" if x == "Good" else "Ruim",
            options=["Good", "Bad"]
        )


        StudentAbsenceDays = col4.selectbox(
            label='Faltas do aluno',
            help='O número total de faltas do aluno é?',
            format_func=lambda x: "Acima de 7" if x == "above - 7" else "Abaixo de 7",
            options=["above - 7", "Under - 7"]
        )

        # armazenamento dos inputs

        inputs = {
            'gender':[gender], 'NationalITy':[NationalITy],
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

        df = pd.DataFrame(inputs)

        foo = [2, 0, 1]

        # Predição
        substantivo = 'o aluno' if gender == 'Male' else 'a aluna'
        if st.button(f'Analisar'):
            st.write(df)
            result = model.predict_proba(df)
            st.write(result)
            final_result = foo[result.argmax()]*(1/3)+result.max()/3
            result_ = model.predict(df)
            fig = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = final_result,
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': "Nível"},
                gauge = {
                    'axis': {'range':[0,1]},
                    'bar': {'color': "cornflowerblue"},
                    'steps': [
                        {'range':[0,0.3333],
                         'color': "red"},
                        {'range':[0.3333, 0.6666],
                         'color': "yellow"},
                        {'range':[0.6666, 1],
                         'color': "green"}
                    ] 
                }
            ))
            st.plotly_chart(fig)
            
            

            if result_ == 'L':
                st.error(f"A maior probabilidade é de que {substantivo} tenha um desempenho baixo.")
            elif result_ == 'M':
                st.info(f"A maior probabilidade é de que {substantivo} tenha um desempenho mediano.")
            else:
                st.success(f"A maior probabilidade é que {substantivo} tenha um desempenho alto.")

    else:
        st.title('Sobre nós')
        st.markdown("Fazemos parte do terceiro ciclo do Programa de Capacitação Tecnológica criado pelo Instituto Atlântico para formar profissionais em tecnologias estratégicas para o mercado de Tecnologia da Informação e Comunicação – TIC. O Bootcamp, nada mais é, do que um treinamento intensivo para que nós estudantes absorvamos o conhecimento teórico de maneira conjunta com a prática. Essa iniciativa é voltada para o fomento de uma cultura de resolução de problemas práticos e auto aprendizado constante por meio de metodologias modernas de ensino, ferramentas e tecnologias inovadoras.")
        st.markdown('### Equipe Data Warriors:')
        st.markdown("[Adilio Freitas](https://github.com/adiliojf)")   
        st.markdown("[Aline Moreira](https://github.com/AlineDamas)")
        st.markdown("[Carlos Estelita](https://github.com/CarlosEstellita)")
        st.markdown("[Haendel Moreira](https://github.com/HaendelMoreira)")
        st.markdown("[Joshuel Nobre](https://github.com/JoshuelNobre)")
        st.markdown("[Stefane Adna](https://github.com/stefaneadna)")
        st.markdown("[Valdemi Junior](https://github.com/vjuniorr)")

if __name__== '__main__':
    main()