import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier

f = open("training.json", "r")
N=int(f.readline())
i=0
train_label=[]
train=[]
for line in f:
    j=json.loads(line)
    train_label.append(j['category'])
    train.append((j['section']+" "+j['heading']))

test=[]
N=int(input())
for i in range(N):
    j = json.loads(input())
    test.append(j['section']+" "+j['heading'])

v = TfidfVectorizer(sublinear_tf=True,analyzer = 'word', max_df = 0.6, ngram_range=(1,2),stop_words="english")
X = v.fit_transform(train)
Y = train_label
X_test = v.transform(test)

clf = SGDClassifier(alpha=.00002, n_iter=75, penalty="l2")
clf.fit(X, Y)

predictions = clf.predict(X_test)
for i in predictions:
    print (i)
