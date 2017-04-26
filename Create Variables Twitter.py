import CleanDataAndCreateDict
import json
from stemming.porter2 import stem
from collections import OrderedDict
Source = CleanDataAndCreateDict




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
        if not OriginalWord in AdjustedWords.keys():
            Word = stem(OriginalWord)
        else:
            Word = OriginalWord
        if Word in AdjustedWords.keys():
            for Emotion in AdjustedWords[Word]["general"].keys():
                if(AdjustedWords[Word]["general"][Emotion] > 0):
                    Score = AdjustedWords[Word]["general"][Emotion]
                    if Reverse:
                        Score = Score * -1
                    All[Emotion][Record] += Score
        Reverse = False
with open('ALL.json', 'w') as f:
    json.dump(All, f)
