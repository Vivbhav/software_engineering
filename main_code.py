from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def main_code(string):
    word_list = word_tokenize(string)
    stop_words = set(stopwords.words('english'))
    
    #if "reminder" in word_list
