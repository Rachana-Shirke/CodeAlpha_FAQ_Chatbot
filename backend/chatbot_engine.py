import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class FAQChatbot:
    def __init__(self, csv_path: str):
        self.df = pd.read_csv(csv_path)
        self._prepare_data()
        self._build_vectorizer()

    def _clean_text(self, text: str) -> str:
        text = text.lower()
        text = re.sub(r'\n', ' ', text)
        text = re.sub(r'[^a-z0-9\s]', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    def _prepare_data(self):
        self.df = self.df[['question', 'answer']].dropna()
        self.df['question'] = self.df['question'].apply(self._clean_text)
        self.df['answer'] = self.df['answer'].apply(self._clean_text)
        self.df.reset_index(drop=True, inplace=True)

    def _build_vectorizer(self):
        self.vectorizer = TfidfVectorizer()
        self.question_vectors = self.vectorizer.fit_transform(
            self.df['question']
        )

    def get_answer(self, user_question: str) -> str:
        user_question = self._clean_text(user_question)
        user_vector = self.vectorizer.transform([user_question])
        similarity = cosine_similarity(user_vector, self.question_vectors)
        best_index = similarity.argmax()
        return self.df.iloc[best_index]['answer']
