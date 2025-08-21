# **Projet de Prototypage d'Applications GenAI avec Streamlit**

Ce dépôt contient le code de deux applications de prototypage développées avec la librairie Streamlit en python, dans le cadre du cours Fast Prototyping of GenAI Apps with Streamlit.
Les deux versions utilisent des modèles d'intelligence artificielle pour effectuer des tâches d'analyse de texte, mais avec des approches différentes.

## Version 1 (V1 App) : Analyse de Sentiment de Texte et Génération de Texte
Cette première application est une démo interactive qui permet à un utilisateur de saisir une phrase et d'obtenir une analyse de sentiment ainsi qu'une réponse générée par un modèle de langage.  

**Fonctionnalités :**  
- Analyse de sentiment : Utilise la bibliothèque TextBlob pour déterminer si une phrase est positive, négative ou neutre. Fonctionne en anglais uniquement.  
- Génération de texte : Répond à la phrase de l'utilisateur en utilisant le modèle de langage GPT-2 de Hugging Face. (Pas aussi performant que les LLMs actuels mais gratuit)  
- Interface simple : Une interface conviviale avec une zone de texte et un bouton pour lancer l'analyse et la génération.

## Version 2 : Analyse de Sentiment sur Fichier CSV/Excel
Cette application est conçue pour l'analyse de données. Elle permet de charger un fichier de données (CSV ou Excel) et d'effectuer une analyse de sentiment par lot sur une colonne de texte spécifique.  

**Fonctionnalités :**  
- Chargement de données : Prend en charge les fichiers .csv et .xlsx.  
- Nettoyage de texte : Inclut une fonction pour nettoyer automatiquement les données (ponctuation, majuscules, espaces).  
- Filtrage et visualisation : Permet de filtrer les données par produit et d'afficher un graphique à barres pour visualiser la répartition des sentiments.  
- A venir : Analyse de sentiment par lot : Applique l'analyse de sentiment de TextBlob à l'ensemble d'une colonne. Pour le moment, le fichier utilisé a déjà une colonne contenant les résultats d’une analyse de sentiments. 


## Comment lancer les applications
Prérequis : Assurez-vous d'avoir Python 3.8+ (et d'avoir installé VS Code).
Clonez ce dépôt  
cd NomDuProjet

Créez et activez un environnement virtuel :
python -m venv venv
**Pour Windows (Powershell) :**
.\venv\Scripts\activate.ps1
**Pour macOS/Linux :**
source venv/bin/activate

Installez les dépendances :
pip install streamlit pandas textblob transformers

Lancez l'application V1 :
streamlit run app_v1.py

Lancez l'application V2 :
streamlit run app_v2.py


