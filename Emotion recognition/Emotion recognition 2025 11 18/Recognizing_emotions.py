from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os
from Samples import prepare_data_en, prepare_data_fa

class SentimentAnalysis:
    def __init__(self):
        self.model = None
        self.vectorizer = None
        self.model_file = "sentiment_model.pkl"
        self.vectorizer_file = "vectorizer.pkl"
    
    def train_sentiment_model(self):
        """آموزش مدل و ذخیره آن"""
        texts, labels = prepare_data_en # or prepare_data_fa
        
        # ایجاد و آموزش vectorizer
        self.vectorizer = CountVectorizer(ngram_range=(1, 2))
        X = self.vectorizer.fit_transform(texts)
        
        # آموزش مدل
        self.model = MultinomialNB()
        self.model.fit(X, labels)
        
        # ذخیره مدل
        joblib.dump(self.model, self.model_file)
        joblib.dump(self.vectorizer, self.vectorizer_file)
        
        print(f"✅ مدل با {len(texts)} نمونه آموزش داده شد")
        return self.model, self.vectorizer
    
    def load_model(self):
        """بارگذاری مدل ذخیره شده"""
        if os.path.exists(self.model_file) and os.path.exists(self.vectorizer_file):
            self.model = joblib.load(self.model_file)
            self.vectorizer = joblib.load(self.vectorizer_file)
            return True
        return False
    
    def predict_sentiment(self, text):
        """پیش‌بینی احساس متن"""
        if self.model is None:
            if not self.load_model():
                self.train_sentiment_model()
        
        # تبدیل متن به بردار
        text_vec = self.vectorizer.transform([text])
        
        # پیش‌بینی
        prediction = self.model.predict(text_vec)[0]
        probability = self.model.predict_proba(text_vec)[0]
        
        sentiment_map = {
            0: 0,       #منفی
            1: 1,       #مثبت
            2: 2,       #سوالی
            3: 3          #خنثی
        }
        
        confidence = max(probability) * 100
        
        result = {
            "sentiment": sentiment_map[prediction],
            "confidence": f"{confidence:.1f}%",
            "raw_prediction": prediction,
            "probabilities": {
                "منفی": f"{probability[0]*100:.1f}%",
                "مثبت": f"{probability[1]*100:.1f}%", 
                "سوالی": f"{probability[2]*100:.1f}%",
                "خنثی": f"{probability[3]*100:.1f}%"
            }
        }
        
        return result