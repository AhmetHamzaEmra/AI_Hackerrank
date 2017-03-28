## Some terms :

X_Train = Training Data


Y_Train = Training Labels


X_Test = Testing Data


Y_Test = Testing Labels


clf= classifier


# Regression

### linear regression 
```(python)
from sklearn.linear_model import LinearRegression

clf=LinearRegression()
clf.fit(X_train, Y_train)
clf.predict(X_test)
```

### Polynomial Regression
```(python)
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

poly=PoliynomialFeatures(degree=2) ## if only 2 column!
clf=LinearRegression()
X_train=poly.fit_transform(X_train)
clf.fit(X_train, Y_train)
X_test=poly.fit_transform(X_test)
clf.predict(X_test)
```

### DecisionTreeRegressor
```(python)
from sklearn import tree
clf=tree.DecisionTreeRegressor()
clf.fit(X_train, Y_train)
clf.predict(X_test)
```

# Text

### CountVectorizer & MultinomialNB & Pipeline
```(python)
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB

pipeline=Pipeline([('vectorixer', CountVectorizer(stop_words="english")), ("classifier", MultinomialNB())])
pipeline.fit(X_train, Y_train)
pipeline.predict(X_test)
```

### PasiveAggressiveClassifier & TdidfVectorizer
```(python)
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer=TfidfVectorizer(sublinear_tf=True, stop_words='english')
X_train=vectorizer.fit_transform(X_train)
X_test = vectorizer.fit_transform(X_test)
clf=PassiveAggressiveClassifier(n_iter=50)
clf.fit(X_train, Y_train)
clf.predict(X_test)
```
### SGDClassifier & TdidfVectorizer
```(python)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier

vectorizer = TfidfVectorizer(sublinear_tf=True,analyzer = 'word', max_df = 0.1, ngram_range=(1,2),stop_words="english")
X_train=vectorizer.fit_transform(X_train)
X_test = vectorizer.fit_transform(X_test)
clf = SGDClassifier(alpha=.00002, n_iter=50, penalty="l2")
clf.fit(X_train, Y_train)
clf.predict(X_test)
```
### BernoulliNB & MultinomialNB & CountVectorizer & TfidfTransformer
```(python)
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

count_vect = CountVectorizer(lowercase = False, max_df = .6)
tfidf_transformer = TfidfTransformer()
X_train_counts = count_vect.fit_transform(X_train)
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
X_test_counts = count_vect.transform(X_test)
X_test_tfidf = tfidf_transformer.transform(X_test_counts)
clf = BernoulliNB(alpha = .3)
clf.fit(X_train_tfidf, Y_train)
clf.predict(X_test_tfidf)
```

# reading data!

## Json
```(python)
import json

f=open("training.json", "r")
for line in f:
	j=json.loads(line)
	object = j['sectionName']
```

## text with comma delimiter
```(python)
from numpy import genfromtxt
data = genfromtxt('trainingdata.txt', delimiter=',')
```
