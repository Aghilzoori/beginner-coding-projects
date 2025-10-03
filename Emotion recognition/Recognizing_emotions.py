from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
class SentimentAnalysis:
    def __init__(self):
        pass

    def train_sentiment_model(self):
        vectorizer = CountVectorizer() # تبدیل به اعداد
        X = vectorizer.fit_transform(texts)
        model = MultinomialNB()
        model.fit(X, labelss)
        return model, vectorizer

    def predict_sentiment(self, text):
        model, vectorizer = self.train_sentiment_model()
        text_vec = vectorizer.transform([text])
        prediction = model.predict(text_vec)
        probability = model.predict_proba(text_vec)
        if prediction[0] == 1:
            return 1 #مثبت
        elif prediction[0] == 0:
            return 0 #منفی
        elif prediction[0] == 2:
            return 2 #سوالی
        else:
            return 3 #خنثی