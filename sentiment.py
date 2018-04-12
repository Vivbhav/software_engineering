from pycorenlp import StanfordCoreNLP

def sentiment_analysis(string):
    nlp = StanfordCoreNLP('http://localhost:9000')
    res = nlp.annotate(string, 
                   properties={
                       'annotators': 'sentiment',
                       'outputFormat': 'json',
                       'timeout': 1000,
                   })
    count = 0
    tot = 0
    for s in res["sentences"]:
        #print (s["sentimentValue"])
        tot = tot + int(s["sentimentValue"])
        count = count + 1
    tot = tot / count
    return tot
#    print("%d: '%s': %s %s" % (
#        s["index"],
#        " ".join([t["word"] for t in s["tokens"]]),
#        s["sentimentValue"], s["sentiment"]))
#sentiment_analysis("i am bored. i hate you.")
