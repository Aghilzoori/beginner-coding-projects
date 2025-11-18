def prepare_data_en():
    positive_words = [
    "happy", "joyful", "successful", "beautiful", "great", "good",
    "energetic", "kind", "pretty", "calm", "hopeful", "winner",
    "success", "awesome", "fantastic", "amazing", "excellent",
    "admirable", "wonderful", "positive", "smart", "strong",
    "motivated", "creative", "lucky", "brilliant", "sweet",
    "lovely", "peaceful", "friendly", "inspiring", "powerful",
    "confident", "helpful", "supportive", "charming", "elegant",
    "honest", "respectful", "optimistic"
    ]

    
    negative_words = [
    "sad", "upset", "failure", "terrible", "awful", "bored",
    "tired", "hopeless", "hard", "pain", "angry", "bad", "ugly",
    "worthless", "horrible", "discouraged", "weak", "stupid",
    "lazy", "annoying", "depressed", "fear", "scared", "hurt",
    "sick", "stress", "disappointed", "negative", "broken",
    "rude", "toxic", "frustrated", "miserable", "lonely",
    "jealous", "ashamed", "guilty"
    ]

    
    question_words = [
        "what", "who", "where", "why", "how", "when", "which",
        "whose", "whom", "how many", "how much", "how long",
        "how far", "how often", "how old", "what time",
        "what is", "who is", "where is", "why is",
        "can", "do", "does", "did", "is", "are",
        "should", "could", "would", "might"
    ]

    
    neutral_words = [
    "day", "time", "today", "tomorrow", "yesterday",
    "this", "that", "these", "those", "maybe", "probably",
    "possibly", "usually", "sometimes", "often", "rarely",
    "always", "never", "here", "there", "now", "then",
    "people", "someone", "something", "anyone", "anything",
    "place", "thing", "idea", "moment", "situation",
    "event", "person", "world", "life", "work",
    "activity", "story", "fact", "reason", "example"
    ]

    
    texts = (positive_words + negative_words + 
            question_words + neutral_words)
    
    labels = ([1] * len(positive_words) + 
                [0] * len(negative_words) + 
                [2] * len(question_words) + 
                [3] * len(neutral_words))
    
    return texts, labels

def prepare_data_fa():
    positive_words = [
        "خوشحال", "شاد", "موفق", "زیبا", "عالی", "خوب", "پرانرژی", 
        "مهربان", "قشنگ", "آرامش", "امیدوار", "برنده", "موفقیت",
        "عالیه", "فوقالعاده", "محشر", "بینظیر", "تحسین‌برانگیز"
    ]
    
    negative_words = [
        "ناراحت", "غمگین", "شکست", "مزخرف", "افتضاح", "بدمزه",
        "بی‌حوصله", "خسته", "ناامید", "سخت", "درد", "عصبانی",
        "بد", "زشت", "بی‌ارزش", "وحشتناک", "مأیوس"
    ]
    
    question_words = [
        "چی", "کی", "کجا", "چرا", "چطور", "چگونه", "کیه", 
        "آیا", "کدوم", "چیست", "مگه", "چه چیزی", "چه وقت",
        "چه کسی", "چند", "چطوری", "کِی", "چیه", "چرا اینطوریه"
    ]
    
    neutral_words = [
        "باشد", "می‌شود", "کرد", "گفت", "روز", "وقت", "حال",
        "امروز", "فردا", "دیروز", "این", "آن", "همین", "همان",
        "شاید", "احتمالا", "ممکن", "بعضا", "معمولا"
    ]
    
    texts = (positive_words + negative_words + 
            question_words + neutral_words)
    
    labels = ([1] * len(positive_words) + 
                [0] * len(negative_words) + 
                [2] * len(question_words) + 
                [3] * len(neutral_words))
    
    return texts, labels