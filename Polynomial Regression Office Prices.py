n, k = map(int, input().strip().split(" "))
x=[]
y=[]
for i in range(k):
    a=[float(b) for b in input().strip().split(" ")]
    x.append(a[:n])
    y.append(a[n])
t=int(input().strip())
p=[]
for i in range(t):
    p.append([float(q) for q in input().strip().split(" ")])
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=2)
x=poly.fit_transform(x)
clf=LinearRegression()
clf.fit(x,y)
p=poly.fit_transform(p)
pred=(clf.predict(p))
for i in range(t):
    print(pred[i])
