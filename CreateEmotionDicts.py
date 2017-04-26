from collections import OrderedDict
import json

F = open("Corpus/NRC-Emotion-Lexicon-Senselevel-v0.92.txt","r")

Words = OrderedDict({})

for row in F:
    row = row.rstrip()
    Word = row.split("--")[0]
    RemainingDate = row.split("--")[1].split(", ")
    synonyms = RemainingDate[:len(RemainingDate)-1]
    LastSynonym = RemainingDate[len(RemainingDate)-1].split("\t")[0]
    synonyms.append(LastSynonym)
    
    EmotionCategory = RemainingDate[len(RemainingDate)-1].split("\t")[1]
    if(EmotionCategory == "anticip"):
        EmotionCategory = "anticipation"
    EmotionValue = RemainingDate[len(RemainingDate)-1].split("\t")[2]

    if not Word in Words.keys():
        Words[Word] = {"synonyms":[],"general":{"fear":0,"anger":0,"anticipation":0,"trust":0,"surprise":0,"positive":0,"negative":0,"sadness":0,"disgust":0,"joy":0}}
        Words[Word]["synonyms"].append({"words":synonyms,"emotions":{"fear":0,"anger":0,"anticipation":0,"trust":0,"surprise":0,"positive":0,"negative":0,"sadness":0,"disgust":0,"joy":0}})
    else:
        if (synonyms != Words[Word]["synonyms"][len(Words[Word]["synonyms"])-1]["words"]):
            Words[Word]["synonyms"].append({"words":synonyms,"emotions":{"fear":0,"anger":0,"anticipation":0,"trust":0,"surprise":0,"positive":0,"negative":0,"sadness":0,"disgust":0,"joy":0}})

    Words[Word]["synonyms"][len(Words[Word]["synonyms"])-1]["emotions"][EmotionCategory] = int(EmotionValue)

with open('Synonyms.json', 'w') as f:
    json.dump(Words, f)

with open('Synonyms.json') as f:
    Words = json.load(f)


F = open("Corpus/NRC-Emotion-Lexicon-Wordlevel-v0.92.txt","r")

for row in F:
    row = row.rstrip()
    Word = row.split("\t")[0]

    EmotionCategory = row.split("\t")[1]
    EmotionValue = row.split("\t")[2]

    if not Word in Words.keys():
        Words[Word] = {"synonyms":[],"general":{"fear":0,"anger":0,"anticipation":0,"trust":0,"surprise":0,"positive":0,"negative":0,"sadness":0,"disgust":0,"joy":0}}
    Words[Word]["general"][EmotionCategory] = int(EmotionValue)

with open('General.json', 'w') as f:
    json.dump(Words, f)


with open('General.json') as f:
    Words = json.load(f)


F = open("Corpus/NRC-Hashtag-Emotion-Lexicon-v0.2.txt","r")

for row in F:
    row = row.rstrip()
    Word = row.split("\t")[1].replace("#","")

    EmotionCategory = row.split("\t")[0]
    EmotionValue = row.split("\t")[2]

    if not Word in Words.keys():
        Words[Word] = {"synonyms":[],"general":{"fear":0,"anger":0,"anticipation":0,"trust":0,"surprise":0,"positive":0,"negative":0,"sadness":0,"disgust":0,"joy":0}}
    Words[Word]["general"][EmotionCategory] = float(EmotionValue)


with open('Adjusted.json', 'w') as f:
    json.dump(Words, f)
