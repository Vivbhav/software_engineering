import os

try:
    from googlesearch import search
except ImportError: 
    print("No module named 'google' found")
 
# Generates links and info as well
query = input("Enter your query- ")
cmd = "googler "+query

#following Code Only Generates Links, Not Info 
#for j in search(query, tld="co.in", num=1, stop=1, pause=2):
#    print(j)

os.system(cmd)
