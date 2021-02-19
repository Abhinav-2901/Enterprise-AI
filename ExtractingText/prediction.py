from textblob import TextBlob
from gensim.summarization import keywords
from gensim.summarization import summarize
import pickle
import ExtractingText.preprocessing as pre


# loading  the trained  model from our app directory using pikel
rt_ml = pickle.load(open('RatingModel/rating_model.pkl', 'rb'))
rt_cv=pickle.load(open('RatingModel/rating_vectorizer.pkl','rb'))

em_ml = pickle.load(open('EmotionModel/emotion_model.pkl', 'rb'))
em_cv=pickle.load(open('EmotionModel/emotion_vectorizer.pkl','rb'))


def rating(message):
    if(len(message)>2):
        data = pre.text_Preprocessing(message)
        text = [data]
        vect = rt_cv.transform(text)
        my_prediction = rt_ml.predict(vect)
    else:
        prediction = 'Invalid Input'

    if my_prediction == 1:
        prediction = 'Poor'
    elif my_prediction == 2:
        prediction = 'Fair'
    elif my_prediction == 3:
        prediction = 'Average'
    elif my_prediction == 4:
        prediction = 'Good'
    else:
        prediction = 'Excellent'

    return prediction



def emotion(message):
    if(len(message)>2):
        data = pre.text_Preprocessing(message)
        text = [data]
        vect = em_cv.transform(text)
        my_prediction = em_ml.predict(vect)
    else:
        prediction = 'Invalid Input'

    if my_prediction == 0:
        prediction = 'anger'
    elif my_prediction == 1:
        prediction = 'fear'
    elif my_prediction == 2:
        prediction = 'joy'
    elif my_prediction == 3:
        prediction = 'neutral'
    else:
        prediction = 'sad'

    return prediction



def analyze(message):
    keyword = ''
    summary = ''
    alert = ''
    Polarity = ''
    Subjectivity = ''
    if len(message)<2:
        alert='enter text more than 2 character'
        print(alert)
    elif len(message)>2 and len(message)<100:
        overview = TextBlob(message)
        Polarity = round(overview.sentiment.polarity,2)
        Polarity = str(Polarity)
        Subjectivity = round(overview.sentiment.subjectivity,2)
        Subjectivity = str(Subjectivity)
    elif len(message)>100 and len(message)<250:
        Keywords = keywords(message)
        Keywords = str(Keywords)
        new = Keywords.split('\n')
        for word in new:
            keyword = keyword + word + ', '
        overview = TextBlob(message)
        Polarity = round(overview.sentiment.polarity,2)
        Polarity = str(Polarity)
        Subjectivity = round(overview.sentiment.subjectivity,2)
        Subjectivity = str(Subjectivity)
    elif len(message)>250:
        Keywords = keywords(message)
        Keywords = str(Keywords)
        new = Keywords.split('\n')
        for word in new:
            keyword = keyword + word + ', '
        summary = summarize(message)
        overview = TextBlob(message)
        Polarity = round(overview.sentiment.polarity,2)
        Polarity = str(Polarity)
        Subjectivity = round(overview.sentiment.subjectivity,2)
        Subjectivity = str(Subjectivity)

    lst = []
    lst.extend([Polarity, Subjectivity, summary, keyword])

    return(lst)