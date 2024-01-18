import csv 
import requests
import time

with open('input.csv', newline='') as csvfile:

    spamreader = csv.reader(csvfile, delimiter=',')

    resultListONS = []
    resultListNLP = []
    i = 1
    for row in spamreader:
        urlONS = 'http://localhost:23900/search?q=' + row[0]
        urlNLP = 'http://localhost:23900/search?q=' + row[0] + '&c=1'

        print("This is the url for ONS" + urlONS)
        rONS = requests.get(urlONS)
        print("This is the url for NLP" + urlNLP)
        rNLP = requests.get(urlNLP)

        if rONS.status_code:
            if rONS.json()["items"]:
                resultListONS.append([row[0], rONS.json()["items"][0]["title"]])
                print("For query:" + row[0] + " the response is " + rONS.json()["items"][0]["title"])
            else:
                print("Potentially there's something wrong with the query")

        if rNLP.status_code:
            if rNLP.json()["items"]:
                resultListNLP.append(rNLP.json()["items"][0]["title"])
                print("For query:" + row[0] + " the NLP response is " + rNLP.json()["items"][0]["title"])
            else:
                print("Potentially there's something wrong with the query")
        i = i + 1
            
    with open('output.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerow(["Initial query", "ONS Response title", "NLP response title", "Score"])

        for i in range(len(resultListNLP)):
            if resultListONS[i][1] == resultListNLP[i]:
                spamwriter.writerow([resultListONS[i][0], resultListONS[i][1], resultListNLP[i], "0"])
            else:
                spamwriter.writerow([resultListONS[i][0], resultListONS[i][1], resultListNLP[i], "change"])