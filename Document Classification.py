from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
file=open('trainingdata.txt', 'r')
file.seek(0)
all_text=file.read()
labels=[]
texts=[]
content=[]
content=all_text.split("\n")
content.remove(content[0])

#print(content)
for stat in content:
    ar=stat.split(" ")
    
    labels.append(ar[0])
    ar=ar[1:]

    
    s=' '.join(ar)
#    print(s)
    texts.append(s)

vectorizer = TfidfVectorizer(sublinear_tf=True, stop_words='english')
X_train = vectorizer.fit_transform(texts)
Y_train = np.array(labels)


    
predict_data=[]
n=int(input().strip())
for i in range(n):
    predict_data.append(input().strip())
X_test  = vectorizer.transform(predict_data) 


clf = PassiveAggressiveClassifier(n_iter=50)
clf.fit(X_train, Y_train)
results=clf.predict(X_test)

for i in results:
    print(i)
