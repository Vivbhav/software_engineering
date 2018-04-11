from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def main_code(string):
    word_list = word_tokenize(string)
    stop_words = set(stopwords.words('english'))
    
    if "event" in word_list:
        if "create" in word_list:
		    name = word_list[2]

		    start_time = 

		    end_time = raw_input("Enter end time of event\n")
		    dt_2 = parser.parse(end_time)

		    cursor.execute(("insert into events_list(event_name,start_time,end_time) values('{}', '{}', '{}');".format(name, dt, dt_2)))
		    cursor.execute(("commit;"))

            
