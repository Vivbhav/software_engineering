import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import sys

reload(sys)  
sys.setdefaultencoding('utf8')
  
hotel_rev = input()
  
sid = SentimentIntensityAnalyzer()
for sentence in hotel_rev:
     print(sentence)
     ss = sid.polarity_scores(sentence)
     for k in ss:
         print(‘{0}: {1}, ‘.format(k, ss[k]), end=’’)
     print()

