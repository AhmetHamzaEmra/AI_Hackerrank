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

from sklearn import linear_model
clf= linear_model.LinearRegression()
clf.fit(x,y)
for i in range(t):
    print ((clf.predict(p[i]))[0])
