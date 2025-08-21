import streamlit as st
import pandas as pd
#import openai
#import seaborn as sns
import matplotlib.pyplot as plt
from textblob import TextBlob
from transformers import pipeline
import string
#openai.api_key = st.secrets["OPENAI_API_KEY"]  # ou directement via os.environ
print ("packages ok")

# Nettoyer le texte
def clean_text(text):
    # 1. Convertir le texte en minuscule
    # Cela permet de traiter "Bonjour" et "bonjour" de la même manière.
    text = str(text).lower()
    # 2. Supprimer la ponctuation
    # On crée une chaîne de caractères de tous les signes de ponctuation.
    # On utilise la méthode translate() pour les supprimer.
    text = text.translate(str.maketrans('', '', string.punctuation))
    # 3. Retirer les espaces au début et à la fin de la chaîne
    # et remplacer les espaces multiples par un seul espace.
    text = ' '.join(text.split())
    return text

# Charger le modèle de génération de texte une seule fois
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="gpt2")

# Se souvenir des analyses sentiments déjà faites pour ne pas recommencer les calculs
@st.cache_data
def analyze_sentiment(text):
    blob = TextBlob(str(text))
    polarity = blob.sentiment.polarity  # -1 = négatif, 0 = neutre, +1 = positif
    if polarity > 0.1:
        st.write(f"Sentiment : Positive")
    elif polarity < -0.1:
        st.write(f"Sentiment : Negative")
    else:
        st.write(f"Sentiment : Neutral")

# Utiliser le modèle de génération de texte pour produire une réponse
def get_response(user_input):
    with st.spinner("Analyzing sentiment and generating text..."):
        result = generator(user_input, max_length=50, num_return_sequences=1)
        st.write(result[0]["generated_text"])

#MAIN
st.title("Hello people")
st.write("This is my first streamlit app. It's a sentiment analysis app and text generator + analyse datas on csv or excel . Might take some time when launched. Works in english only")
#user_input = st.text_area("Enter prompt (in english only):")
generator = load_model()

uploaded_file = st.file_uploader(label = "Enter datas", accept_multiple_files = False, type=["csv", "xlsx"])
col1, col2 = st.columns(2)
with col1:
    if st.button("DATA analyse"):
        try :
            if uploaded_file:
                st.write(uploaded_file.type)
                if uploaded_file.type == "text/csv":
                    st.session_state["df"] = pd.read_csv(uploaded_file)
                elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
                    st.session_state["df"] = pd.read_excel(uploaded_file)
                else:
                    st.error("Unsupported file type.")
            else :
                st.error("No file uploaded.")
        except Exception as e:
            st.error(f"Error loading document: {e}")

with col2:
    if st.button("Clear text"):
        if "df" in st.session_state:
            st.session_state["df"]["Cleaned SUMMARY"] = st.session_state["df"]["SUMMARY"].apply(clean_text)

if "df" in st.session_state:
    # Do something with the dataframe
    st.subheader("Filter by product")
    product = st.selectbox("Select a product", ["All products"] + st.session_state["df"]["PRODUCT"].unique().tolist())
    if product != "All products":
        filtered_df = st.session_state["df"][st.session_state["df"]["PRODUCT"] == product]
    else:
        filtered_df = st.session_state["df"]
    st.dataframe(filtered_df)

    # Show a bar plot of the sentiment distribution by product
    st.subheader("Sentiment Analysis")
    grouped = st.session_state["df"].groupby(["PRODUCT"])["SENTIMENT_SCORE"].mean()
    st.bar_chart_chart(grouped)
    # fig = plt.figure()
    # sns.barplot(x=grouped.index, y=grouped.values)
    # plt.title("Sentiment Analysis by Product")
    # plt.xlabel("Product")
    # plt.ylabel("Average Sentiment Score")

    # st.pyplot(fig)
