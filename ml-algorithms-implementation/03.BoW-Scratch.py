from typing import List
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

class BowFromScratch(object):
    def __init__(self):
        self.vocab = set()

    def create_vocab(self,data):
        for sentence in data:
            self.vocab.update(sentence.split(' '))

    def create_bow(self,data):
        bow = []
        for sentence in data:
            sentence_bow = [0] * len(self.vocab)
            for word in sentence.split(' '):
                if word in self.vocab:
                    sentence_bow[list(self.vocab).index(word)] += 1
            bow.append(sentence_bow)
        return bow

class BowScikit(object):
    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.bow = None

    def create_bow(self,data : List[str]):
        self.bow = self.vectorizer.fit(data)

    def get_bow(self,data : List[str]) -> pd.DataFrame:
        raw_bow = self.vectorizer.transform(data)
        return pd.DataFrame(raw_bow.toarray(),columns=self.bow.get_feature_names())

if __name__ == '__main__':
    doc1 = 'Game of Thrones is an amazing tv series!'
    doc2 = 'Game of Thrones is the best tv series!'
    doc3 = 'Game of Thrones is so great'

    documents = [doc1, doc2, doc3]
    df = pd.DataFrame(documents, columns=['text'])

    # Remove punctuation from df column text and lower case 
    df["text"] = df["text"].str.replace('[^\w\s]','').str.lower()

    # remove extra spaces
    df["text"] = df["text"].str.replace('\s+', ' ')

    bow = BowFromScratch()
    bow.create_vocab(df.text.values)
    print('Vocabulary: ',bow.vocab)

    bow_df = pd.DataFrame(bow.create_bow(df.text.values),columns=bow.vocab)
    # merge df and bow_df
    bow_df = pd.concat([df, bow_df], axis=1)

    print("Bow from Scratch")
    print("=================")
    print(bow_df)

    bow_scikit = BowScikit()
    bow_scikit.create_bow(df.text.values)
    bow_df = bow_scikit.get_bow(df.text.values)
    bow_df = pd.concat([df, bow_df], axis=1)
    print("Bow Scikit")
    print("=================")
    print(bow_df)