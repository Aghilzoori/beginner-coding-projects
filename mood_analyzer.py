from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
class Filtering:
    
    def __init__(self, data, mood):
        self.data = data
        self.mood = mood
        self.labels = []
        self.result = 0
    
    def initialize_labels(self):
        for i in range(len(self.data)):
            self.labels.append(0)
    
    def get_mood_index(self):
        index_mood = self.data.index(self.mood)
        return index_mood
    
    def mark_mood_occurrences(self):
        index_mood = self.get_mood_index()
        if not self.labels:
            self.initialize_labels()
        self.labels[index_mood] = 1
        for i, text in enumerate(self.data):
            if self.mood in text and i != index_mood:
                self.labels[i] = 1
    
    def count_mood_occurrences(self):
        if not self.labels:
            self.mark_mood_occurrences()
        vectorizer = CountVectorizer()
        X = vectorizer.fit_transform(self.data)
        model = MultinomialNB()
        model.fit(X, self.labels)
        test_trees = self.data
        X_test = vectorizer.transform(test_trees)
        predictions = model.predict(X_test)
        for tree, pred in zip(test_trees, predictions):
            if pred == 1:
                self.result += 1
            else:
                pass
        return self.result

        

data = [
    "happy", "sad", "angry", "excited", "joyful", "content", "anxious", "calm",
    "happy mood", "sad feeling", "angry emotion", "excited state", "joyful moment", 
    "content mind", "anxious thought", "calm spirit", "very happy", "extremely sad",
    "quite angry", "very excited", "so joyful", "very content", "highly anxious",
    "perfectly calm", "happy person", "sad day", "angry face", "excited child",
    "joyful occasion", "content life", "anxious mind", "calm ocean", "happy time",
    "sad story", "angry voice", "excited crowd", "joyful noise", "content smile",
    "anxious heart", "calm breeze", "happy place", "sad memory", "angry reaction",
    "excited anticipation", "joyful celebration", "content satisfaction", 
    "anxious uncertainty", "calm meditation", "happy dance", "sad song",
    "angry outburst", "exited energy", "joyful laughter", "content peace",
    "anxious worry", "calm silence", "happy family", "sad ending", "angry words",
    "excited news", "joyful reunion", "content rest", "anxious wait", "calm water",
    "happy hour", "sad news", "angry look", "excited talk", "joyful play",
    "content sleep", "anxious dream", "calm night", "happy meal", "sad movie",
    "angry response", "exited shout", "joyful dance", "content work", "anxious test",
    "calm morning", "happy journey", "sad goodbye", "angry protest", "exited jump",
    "joyful song", "content reading", "anxious interview", "calm yoga", "happy pet",
    "sad poem", "angry storm", "exited run", "joyful walk", "content cooking",
    "anxious flight", "calm garden", "happy vacation", "sad loss", "angry debate",
    "exited competition", "joyful game", "content painting", "anxious decision",
    "calm music", "happy birthday", "sad memory", "angry argument", "exited party",
    "joyful holiday", "content writing", "anxious meeting", "calm reading",
    "happy wedding", "sad funeral", "angry customer", "exited travel", "joyful event",
    "content hobby", "anxious presentation", "calm exercise", "happy anniversary",
    "sad breakup", "angry driver", "exited adventure", "joyful surprise",
    "content relaxation", "anxious appointment", "calm shower", "happy home",
    "sad illness", "angry neighbor", "exited discovery", "joyful achievement",
    "content meditation", "anxious exam", "calm walk", "happy friend", "sad accident",
    "angry boss", "exited opportunity", "joyful success", "content nap",
    "anxious surgery", "calm drive", "happy smile", "sad tear", "angry letter",
    "exited news", "joyful gift", "content meal", "anxious result", "calm tea",
    "happy sun", "sad rain", "angry wind", "exited sun", "joyful rainbow",
    "content book", "anxious call", "calm moon", "happy star", "sad cloud",
    "angry thunder", "exited lightning", "joyful flower", "content tree",
    "anxious dark", "calm light", "happy river", "sad mountain", "angry fire",
    "exited wave", "joyful bird", "content fish", "anxious storm", "calm snow",
    "happy beach", "sad desert", "angry volcano", "exited island", "joyful forest",
    "content valley", "anxious cliff", "calm meadow", "happy city", "sad village",
    "angry traffic", "exited building", "joyful park", "content street",
    "anxious crowd", "calm home", "happy school", "sad hospital", "angry office",
    "exited store", "joyful restaurant", "content cafe", "anxious bank", "calm library"
]
mood_value = "happy"
filter_obj = Filtering(data, mood_value)
result = filter_obj.count_mood_occurrences()
print(result)