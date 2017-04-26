import CleanDataAndCreateDict
import json
from stemming.porter2 import stem
from collections import OrderedDict
Source = CleanDataAndCreateDict

File = open("Months_MyPersonality.txt","w")



with open('General.json') as f:
    Words = json.load(f)
with open('Adjusted.json') as f:
    AdjustedWords = json.load(f)
All = OrderedDict(Source.All)

Count = 0
Reverse = False
for Record in range(len(All["Post"])):
    Post = All["Post"][Record].split(" ")
    for OriginalWord in Post:
        if OriginalWord == "not":
            Reverse = True
            continue
        if not OriginalWord in Words.keys():
            Word = stem(OriginalWord)
        else:
            Word = OriginalWord
        if Word in Words.keys():
            for Emotion in Words[Word]["general"].keys():
                if(Words[Word]["general"][Emotion] > 0):
                    Score = Words[Word]["general"][Emotion]
                    if Reverse:
                        Score = Score * -1
                    All[Emotion][Record] += Score
            Reverse = False
with open('ALL.json', 'w') as f:
    json.dump(All, f)
