# ✈️ Aviation FAQ Chatbot

An AI-powered FAQ Chatbot designed to answer aviation-related queries such as airport rules, flight services, and passenger guidelines using Natural Language Processing (NLP).

This project was developed as part of the ** Artificial Intelligence Internship**.

---

## 📌 Project Overview

The Aviation FAQ Chatbot allows users to ask questions related to:
- Airports
- Flights
- Passenger services
- Aviation rules and guidelines

The chatbot uses **TF-IDF vectorization** and **Cosine Similarity** to match user queries with the most relevant answers from an aviation FAQ dataset.

---

## 🧠 Technologies Used

- Python  
- Pandas  
- Scikit-learn  
- Natural Language Processing (NLP)  
- TF-IDF Vectorizer  
- Cosine Similarity  
- Streamlit  

---

## 📂 Project Structure

---

## ⚙️ How It Works

1. The dataset is cleaned and preprocessed.
2. Questions are converted into numerical vectors using **TF-IDF**.
3. User input is vectorized using the same TF-IDF model.
4. **Cosine similarity** is calculated between the user query and stored questions.
5. The most relevant answer is returned.

---

## ▶️ How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/Rachana-Shirke/CodeAlpha_FAQ_Chatbot.git
cd CodeAlpha_FAQ_Chatbot

## 📸 Screenshots

Below is a screenshot of the working chatbot UI:

![Aviation FAQ Chatbot UI](screenshots/chatbot_ui.png)
