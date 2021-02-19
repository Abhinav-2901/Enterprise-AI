#import nltk
#nltk.download('punkt')
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import re
#nltk.download('stopwords')

stop_words = set()
for word in set(stopwords.words('english')):
    if word != 'not':
        stop_words.add(word)

def text_Preprocessing(review):
    review= BeautifulSoup(review,'lxml').getText()    #remove html tags
    review=re.sub('\\S*\\d\\S*','',review).strip()
    review=re.sub('[^A-Za-z]+',' ',review)        #remove special chars\n",
    review=re.sub("n't","not",review)
    review=word_tokenize(str(review.lower())) #tokenize the reviews into word tokens
    review=' '.join(PorterStemmer().stem(word) for word in review if word not in stop_words)
    return review