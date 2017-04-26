#!/usr/bin/python
# -*- coding: iso-8859-15 -*-


from openpyxl import load_workbook
from nltk.tokenize import word_tokenize
import codecs
# Import regex
import re
import operator
# Import string
import string
from nltk.corpus import stopwords
from collections import OrderedDict


replacement_patterns = [
(r'won\'t', 'will not'),
(r'can\'t', 'cannot'),
(r'i\'m', 'i am'),
(r'ain\'t', 'is not'),
(r'(\w+)\'ll', '\g<1> will'),
(r'(\w+)n\'t', '\g<1> not'),
(r'(\w+)\'ve', '\g<1> have'),
(r'(\w+)\'s', '\g<1> is'),
(r'(\w+)\'re', '\g<1> are'),
(r'(\w+)\'d', '\g<1> would')
 ]
class RegexpReplacer(object):

   def __init__(self, patterns=replacement_patterns):

      # Fixed this line - "patterns", not "pattern"
      self.patterns = [(re.compile(regex), repl) for (regex, repl) in patterns]

   def replace(self, text):
      s = text
      for (pattern, repl) in self.patterns:
          (s, count) = re.subn(pattern, repl, s)

      # Fixed indentation here
      return s




def CleanUp(Text):
    SwordsIndex = list(stopwords.words('english')).index('not')
    Swords = list(stopwords.words('english'))
    Swords.pop(SwordsIndex)
    Swords = set(Swords)
    try:
        Text = str(Text).lower().replace("propname","")
    except:
        return " "
    if(Text.isdigit() or Text.rsplit() == ""):
        return " "
    rep=RegexpReplacer()
    Text = rep.replace(Text)

    # Apply word_tokenize to each element of the list called incoming_reports
    tokenized_reports = word_tokenize(Text)

    regex = re.compile('[%s]' % re.escape(string.punctuation)) #see documentation here: http://docs.python.org/2/library/string.html

    tokenized_reports_no_punctuation = []

    new_review = []
    for token in tokenized_reports:
        new_token = regex.sub(u'', token)
        if not new_token == u'':
            tokenized_reports_no_punctuation.append(new_token)


    tokenized_reports_no_stopwords = []
    for word in tokenized_reports_no_punctuation:
        if not word in Swords:
            tokenized_reports_no_stopwords.append(word)

    return tokenized_reports_no_stopwords

wb = load_workbook(filename='mypersonality_final.xlsx', read_only=True)
ws = wb["mypersonality_final"]
File = open("mypersonality_CLEANED1.csv","w")
File.write("ID,Status,TimeMonth,TimeHour,sEXT,sNEU,sAGR,sCON,sOPN,cEXT,cNEU,cAGR,cCON,cOPN,NETWORKSIZE,OriginalStatus\n")


Hours = {}
Headers = True
for row in ws.rows:
    if(Headers):
        Headers = False
        continue
    ID = row[0].value
    OriginalStatus = row[1].value
    try:
        TimeMonth = str(row[12].value).split(" ")[0].split("-")[1]
        TimeHour = str(row[12].value).split(" ")[1][:2]
    except:
        continue

    Status = " ".join(CleanUp(OriginalStatus))
    try:
        OriginalStatus = str(OriginalStatus).replace(","," ")
        File.write(ID+","+Status+","+TimeMonth+","+TimeHour+","+str(row[2].value)+","+str(row[3].value)+","+str(row[4].value)+","+str(row[5].value)+","+str(row[6].value)+","+str(row[7].value)+","+str(row[8].value)+","+str(row[9].value)+","+str(row[10].value)+","+str(row[11].value)+","+str(row[13].value)+","+OriginalStatus+"\n")
    except:
        File.write(ID+","+Status+","+TimeMonth+","+TimeHour+","+str(row[2].value)+","+str(row[3].value)+","+str(row[4].value)+","+str(row[5].value)+","+str(row[6].value)+","+str(row[7].value)+","+str(row[8].value)+","+str(row[9].value)+","+str(row[10].value)+","+str(row[11].value)+","+str(row[13].value)+",NOT AVAILABLE\n")
File.close()
