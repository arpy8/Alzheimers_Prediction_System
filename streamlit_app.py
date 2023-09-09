import time
import joblib
import pandas as pd
import streamlit as st
from team_members import team_members

APOE_CATEGORIES = ['APOE Genotype_2,2', 'APOE Genotype_2,3', 'APOE Genotype_2,4', 'APOE Genotype_3,3',
                   'APOE Genotype_3,4', 'APOE Genotype_4,4']
PTHETHCAT_CATEGORIES = ['PTETHCAT_Hisp/Latino', 'PTETHCAT_Not Hisp/Latino', 'PTETHCAT_Unknown']
IMPUTED_CATEGORIES = ['imputed_genotype_True', 'imputed_genotype_False']
PTRACCAT_CATEGORIES = ['PTRACCAT_Asian', 'PTRACCAT_Black', 'PTRACCAT_White']
PTGENDER_CATEGORIES = ['PTGENDER_Female', 'PTGENDER_Male']
APOE4_CATEGORIES = ['APOE4_0', 'APOE4_1', 'APOE4_2']


st.set_page_config(
    page_title="Alzheimer's Prediction System",
    page_icon=":brain:",
)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.sidebar.image("assets/side_banner.png")

st.sidebar.title("Navigation")
app_mode = st.sidebar.selectbox(
    "Choose a page",
    ["Home", "Prediction", "Team Members"],
)

st.sidebar.write("""
# Disclaimer
The predictions provided by this system are for informational purposes only. Consult a healthcare professional for accurate diagnosis and advice.

# About Me
This application is developed by [arpy8](https://github.com/arpy8).

# Contact
For inquiries, please contact me at [arpitsengar99@gmail.com](mailto:arpitsengar99@gmail.com).
""")

if __name__ == "__main__":

    if app_mode == "Home":
        st.title("Welcome to the Alzheimer's Prediction System")

        st.image("assets/banner.png")

        st.write("""
            ## About Alzheimer's Disease
            Alzheimer's disease (AD) is a progressive neurodegenerative disease. Though best known for its role in declining memory function, symptoms also include: difficulty thinking and reasoning, making judgements and decisions, and planning and performing familiar tasks. It may also cause alterations in personality and behavior. The cause of AD is not well understood. There is thought to be a significant hereditary component. For example, a variation of the APOE gene, APOE e4, increases risk of Alzheimer's disease.

            ## Purpose of the project
            The purpose of this project proposal is to develop a machine learning model for the early prediction of Alzheimer's disease. Alzheimer's disease is a devastating neurodegenerative disorder that affects millions of individuals worldwide. Early detection is crucial for better patient care and the development of potential interventions. This project aims to leverage machine learning techniques to create a predictive model that can identify individuals at risk of Alzheimer's disease based on relevant data.
            """)

    if app_mode == "Prediction":
        def convert_to_one_hot(selected_category, all_categories):
            one_hot = [True if category == selected_category else False for category in all_categories]
            for value in one_hot:
                user_input.append(value)

        def predict_alzheimer(input_data):
            loaded_model = joblib.load('model/alzheimer_model.pkl')
            predictions = loaded_model.predict(input_data)
            return predictions

        st.title("Patient Information")

        age = st.number_input("Age", min_value=0, max_value=122, step=1, value=65)
        gender = st.selectbox("Gender", ("Male", "Female"))
        education = st.number_input("Years of Education", min_value=0, value=12)

        st.write("<br>", unsafe_allow_html=True)

        st.header("Demographics")
        ethnicity = st.radio("Ethnicity", ("Hisp/Latino", "Not Hisp/Latino", "Unknown"))
        race_cat = st.radio("Race Category", ("White", "Black", "Asian"))

        st.write("<br>", unsafe_allow_html=True)

        st.header("Genetic Information")
        apoe_allele_type = st.selectbox("APOE Allele Type", ["APOE4_0", "APOE4_1", "APOE4_2"])
        apoe_genotype = st.selectbox("APOE4 Genotype", ("2,2", "2,3", "2,4", "3,3", "3,4", "4,4"))
        imputed_genotype = st.radio("Imputed Genotype", ("True", "False"))

        st.header("Cognitive Assessment")
        mmse = st.number_input("MMSE Score", min_value=0, max_value=30, step=1)

        predict_button = st.button("Predict")
        st.write("")

        if age and education and mmse and apoe_genotype and race_cat and gender and apoe_allele_type and imputed_genotype and ethnicity and predict_button:
            st.write("Thank you for entering the patient's information.")
            progress_text = "Please wait, we're predicting your clinical condition..."
            my_bar = st.progress(0, text=progress_text)

            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1, text=progress_text)

            user_input = [age, education, mmse]

            convert_to_one_hot("PTRACCAT_" + race_cat, PTRACCAT_CATEGORIES)
            convert_to_one_hot("APOE Genotype_" + apoe_genotype, APOE_CATEGORIES)
            convert_to_one_hot("PTETHCAT_" + ethnicity, PTHETHCAT_CATEGORIES)
            convert_to_one_hot(apoe_allele_type, APOE4_CATEGORIES)
            convert_to_one_hot("PTGENDER_" + gender, PTGENDER_CATEGORIES)
            convert_to_one_hot("imputed_genotype_" + imputed_genotype, IMPUTED_CATEGORIES)

            data = pd.DataFrame([user_input])
            predicted_condition = predict_alzheimer(data)
            abbreviation = {
                "AD": "Alzheimer's Disease ",
                "LMCI": "Late Mild Cognitive Impairment ",
                "CN": "Cognitively Normal"
            }
            condition_description = {
                "AD": "This indicates that the individual's data aligns with characteristics commonly associated with "
                    "Alzheimer's disease. Alzheimer's disease is a progressive neurodegenerative disorder that affects "
                    "memory and cognitive functions.",
                "LMCI": "This suggests that the individual is in a stage of mild cognitive impairment that is progressing "
                        "towards Alzheimer's disease. Mild Cognitive Impairment is a transitional state between normal "
                        "cognitive changes of aging and more significant cognitive decline.",
                "CN": "This suggests that the individual has normal cognitive functioning without significant impairments. "
                    "This group serves as a control for comparison in Alzheimer's research."
            }

            st.write("")
            st.write("")
            st.subheader("Predicted Clinical Condition:")
            st.write(f"**{predicted_condition[0]}** ({abbreviation[predicted_condition[0]]})")
            st.subheader("Condition Description:")
            st.write(condition_description[predicted_condition[0]])

    if app_mode == "Team Members":
        team_members()
        st.write("<h1 style='text-align:center;'>Our Team</h1><br><br>", unsafe_allow_html=True)

        padding_1, main, padding_2 = st.columns((1,2,1))

        with padding_1:
            st.empty()

        with main:
            left, right = st.columns(2)
            
            with left:
                st.image("assets/arpy8.png", width=100)
            with right:
                st.write(f"""
                <h4 style="text-align:center;">Arpit Sengar</h4>
                            
                <table>
                    <tr>
                        <th><a href="https://github.com/arpy8">Github</a></th>
                        <th><a href="https://www.linkedin.com/in/arpitsengar">Linkedin</a></th> 
                    </tr> 
                </table>
                            
                """, unsafe_allow_html=True)

            st.write("<br><br>", unsafe_allow_html=True)

        with padding_2:
            st.empty()

        # -----

        outer_left, padding, outer_right = st.columns((5,1,5))

        with outer_left:
            left_1, right_1 = st.columns(2)
            
            with left_1:
                st.image("assets/arpy8.png", width=100)
            with right_1:
                st.write(f"""
                <h4 style="text-align:center;">Arpit Sengar</h4>
                <table>
                    <tr>
                        <th><a href="https://github.com/arpy8">Github</a></th>
                        <th><a href="https://www.linkedin.com/in/arpitsengar">Linkedin</a></th> 
                    </tr> 
                </table>
                            
                """, unsafe_allow_html=True)

            st.write("<br><br>", unsafe_allow_html=True)

            left_2, right_2 = st.columns(2)
            with left_2:
                st.image("assets/arpy8.png", width=100)
            with right_2:
                st.write(f"""
                <h4 style="text-align:center;">Arpit Sengar</h4>
                            
                <table>
                    <tr>
                        <th><a href="https://github.com/arpy8">Github</a></th>
                        <th><a href="https://www.linkedin.com/in/arpitsengar">Linkedin</a></th> 
                    </tr> 
                </table>
                            
                """, unsafe_allow_html=True)

        with padding:
            st.empty()


        with outer_right:
            left_3, right_3 = st.columns(2)
            
            with left_3:
                st.image("assets/arpy8.png", width=100)
            with right_3:
                st.write(f"""
                <h4 style="text-align:center;">Arpit Sengar</h4>
                        
                <table>
                    <tr>
                        <th><a href="https://github.com/arpy8">Github</a></th>
                        <th><a href="https://www.linkedin.com/in/arpitsengar">Linkedin</a></th> 
                    </tr> 
                </table>
                            
                """, unsafe_allow_html=True)

            st.write("<br><br>", unsafe_allow_html=True)

            left_4, right_4 = st.columns(2)
            with left_4:
                st.image("assets/arpy8.png", width=100)
            with right_4:
                st.write(f"""
                <h4 style="text-align:center;">Arpit Sengar</h4>
                            
                <table>
                    <tr>
                        <th><a href="https://github.com/arpy8">Github</a></th>
                        <th><a href="https://www.linkedin.com/in/arpitsengar">Linkedin</a></th> 
                    </tr> 
                </table>
                            
                """, unsafe_allow_html=True)