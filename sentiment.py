from pycorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP('http://localhost:9000')
res = nlp.annotate("I am bored by this project. Want to finish this off. Cannot do the GUI. Hope to get a grade and wrap this up.",
                   properties={
                       'annotators': 'sentiment',
                       'outputFormat': 'json',
                       'timeout': 1000,
                   })
count = 0
for s in res["sentences"]:
    sum_sen = s["sentimentValue"]
    count = count + 1
sum_sen = sum_sen / count
print sum
#    print("%d: '%s': %s %s" % (
#        s["index"],
#        " ".join([t["word"] for t in s["tokens"]]),
#        s["sentimentValue"], s["sentiment"]))
