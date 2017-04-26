import CleanDataAndCreateDict
import json
from stemming.porter2 import stem
from collections import OrderedDict
import xlwt

book = xlwt.Workbook()
sh = book.add_sheet("1")


sh.write(0, 0, "ID")
sh.write(0, 1, "Post")
sh.write(0, 2, "Months")
sh.write(0, 3, "Hours")
sh.write(0, 4, "anger")
sh.write(0, 5, "anticipation")
sh.write(0, 6, "disgust")
sh.write(0, 7, "fear")
sh.write(0, 8, "joy")
sh.write(0, 9, "negative")
sh.write(0, 10, "positive")
sh.write(0, 11, "sadness")
sh.write(0, 12, "surprise")
sh.write(0, 13, "trust")
sh.write(0, 14, "sEXT")
sh.write(0, 15, "sNEU")
sh.write(0, 16, "sAGR")
sh.write(0, 17, "sCON")
sh.write(0, 18, "sOPN")
sh.write(0, 19, "cEXT")
sh.write(0, 20, "cNEU")
sh.write(0, 21, "cAGR")
sh.write(0, 22, "cCON")
sh.write(0, 23, "cOPN")
sh.write(0, 24, "NETWORKSIZE")


Index = {
    "ID":0,
    "Post":1,
    "Months":2,
    "Hours":3,
    "anger":4,
    "anticipation":5,
    "disgust":6,
    "fear":7,
    "joy":8,
    "negative":9,
    "positive":10,
    "sadness":11,
    "surprise":12,
    "trust":13,
    "sEXT":14,
    "sNEU":15,
    "sAGR":16,
    "sCON":17,
    "sOPN":18,
    "cEXT":19,
    "cNEU":20,
    "cAGR":21,
    "cCON":22,
    "cOPN":23,
    "NETWORKSIZE":24

}


Source = CleanDataAndCreateDict



with open('ALL.json') as f:
    All = json.load(f)

Count = 1
for Record in range(len(All["Post"])):
    for Header in Source.Headers:
        if (Header in ["ID","Post","Months","Hours","anger","anticipation","disgust","fear","joy","negative","positive","sadness","surprise","trust","sEXT","sNEU","sAGR","sCON","sOPN","cEXT","cNEU","cAGR","cCON","cOPN","NETWORKSIZE"]):
            if (Header in ["anger","anticipation","disgust","fear","joy","negative","positive","sadness","surprise","trust"]):
                Output = float(round(All[Header][Record],2))

                sh.write(Count, Index[Header], Output)
            else:
                Output = str(All[Header][Record])
                if (Header == "Months"):
                    if(Output in ["12","01","02"]):
                        Output = 1
                    elif(Output in ["03","04","05"]):
                        Output = 2
                    if(Output in ["06","07","08"]):
                        Output = 3
                    if(Output in ["09","10","11"]):
                        Output = 4
                sh.write(Count, Index[Header], Output)
    Count += 1
print Count
book.save("seasons_twitter_MyPersonality5.xls")
