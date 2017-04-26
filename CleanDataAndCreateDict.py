from collections import OrderedDict

Headers = [
    "ID",
    "Post",
    "OriginalPost",
    "Months",
    "Hours",
    "anger",
    "anticipation",
    "disgust",
    "fear",
    "joy",
    "negative",
    "positive",
    "sadness",
    "surprise",
    "trust",
    "sEXT",
    "sNEU",
    "sAGR",
    "sCON",
    "sOPN",
    "cEXT",
    "cNEU",
    "cAGR",
    "cCON",
    "cOPN",
    "NETWORKSIZE"
]
All = OrderedDict({
    "ID":[],
    "Post":[],
    "OriginalPost":[],
    "Months":[],
    "Hours":[],
    "anger":[],
    "anticipation":[],
    "disgust":[],
    "fear":[],
    "joy":[],
    "negative":[],
    "positive":[],
    "sadness":[],
    "surprise":[],
    "trust":[],
    "sEXT":[],
    "sNEU":[],
    "sAGR":[],
    "sCON":[],
    "sOPN":[],
    "cEXT":[],
    "cNEU":[],
    "cAGR":[],
    "cCON":[],
    "cOPN":[],
    "NETWORKSIZE":[]
})
File = open("mypersonality_CLEANED1.csv","r")
Headers_row = True
for row in File:
    row = row.rstrip().split(",")
    if(Headers_row):
        Headers_row = False
        continue

    All["ID"].append(row[0])
    All["Post"].append(row[1])
    All["OriginalPost"].append(row[15])
    All["Months"].append(row[2])
    All["Hours"].append(row[3])
    All["anger"].append(0)
    All["anticipation"].append(0)
    All["disgust"].append(0)
    All["fear"].append(0)
    All["joy"].append(0)
    All["negative"].append(0)
    All["positive"].append(0)
    All["sadness"].append(0)
    All["surprise"].append(0)
    All["trust"].append(0)
    All["sEXT"].append(row[4])
    All["sNEU"].append(row[5])
    All["sAGR"].append(row[6])
    All["sCON"].append(row[7])
    All["sOPN"].append(row[8])
    All["cEXT"].append(row[9])
    All["cNEU"].append(row[10])
    All["cAGR"].append(row[11])
    All["cCON"].append(row[12])
    All["cOPN"].append(row[13])
    All["NETWORKSIZE"].append(row[14])

