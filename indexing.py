#-------------------------------------------------------------------------
# AUTHOR: Isabel Ganda
# FILENAME: indexing.py
# SPECIFICATION: Question 8 of Assignment 1: calculate tf, idf, and tf-idf
# FOR: CS 4250-01 Assignment #1
# TIME SPENT: 3 hours
#-----------------------------------------------------------*/

#Importing some Python libraries
import csv
import math

documents = []

#Reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
         if i > 0:  # skipping the header
            documents.append(row[0].lower()) #Make document case insensitve

#Conducting stopword removal for pronouns/conjunctions. Hint: use a set to define your stopwords.
#--> add your Python code here
stopWords = {"i", "she", "they", "and", "her", "their"}

#Function that removes stopwords in a given document based on the stopWords set variable
def removeStopwords(document):
  words = document.split()
  return ' '.join([word for word in words if word not in stopWords])


#Conducting stemming. Hint: use a dictionary to map word variations to their stem.
#--> add your Python code here
steeming = {"loves": "love",
            "love": "love",
            "cats": "cat",
            "cat": "cat",
            "dogs": "dog",
            "dog": "dog"
            }

#Function that conducts stemming to a given document by using the steeming dictionary variable
def stemming(document):
  words = document.split()
  return ' '.join([steeming.get(word, word) for word in words])


#Remove stopwords and apply stemming before identifying index terms and place them into newDoc
updatedDoc = []
for i in documents:
  editedDoc = removeStopwords(i)
  stemDoc = stemming(editedDoc)
  updatedDoc.append(stemDoc)


#Identifying the index terms.
#--> add your Python code here
terms = []

for i in updatedDoc:
  for word in i.split():
      if word not in terms:
          terms.append(word)



#Building the document-term matrix by using the tf-idf weights.
#--> add your Python code here

#Function that caluclates tf
def tf(term, doc):
  words = doc.split()
  return words.count(term) / len(words)

#Function that caluclates idf
def idf(term, docs):
  countDoc = len(docs)
  countDocWithWord = sum(1 for doc in docs if term in doc.split())
  return math.log10(countDoc / countDocWithWord)

#Function that caluclates tf-idf
def tf_idf(tfValue, idfValue):
  return tfValue * idfValue


docTermMatrix = []

for doc in updatedDoc:
  tfidfRow = []
  for term in terms:
     tfValue = tf(term, doc)
     idfValue = idf(term, updatedDoc)
     tfidfValue = tf_idf(tfValue, idfValue)
     tfidfRow.append(tfidfValue)
  docTermMatrix.append(tfidfRow)


#Printing the document-term matrix.
#--> add your Python code here

#Format answer to make it more readable
print()
print("+++++++Document-Term Matrix (TF-IDF)+++++++")
print("Terms:", terms)
for i, row in enumerate(docTermMatrix):
    print(f"   d{i + 1}: {row}")

print("+++++++++++++++++++++++++++++++++++++++++++")
print()