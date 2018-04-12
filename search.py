import os

try:
    from googlesearch import search
except ImportError: 
    print("No module named 'google' found")

def search(string): 
	# Generates links and info as well
	#query = input("Enter your query- ")
    query = string
    cmd = "googler -C "+query+" | tee out.txt"

	#following Code Only Generates Links, Not Info 
	#for j in search(query, tld="co.in", num=1, stop=1, pause=2):
	#    print(j)
    os.system(cmd)

    with open('out.txt', 'r') as myfile:
		data = myfile.read()
		return data

#data = search("cricket")
#print (data)
