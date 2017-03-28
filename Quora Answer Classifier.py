n,m=map(int, input().strip().split(" "))
name=[]
label=[]
data=[]
for i in range(n):
    line=[a for a in input().strip().split()]
    name.append(line[0])
    label.append(line[1])
    datas=line[2:]
    arr=[]
    for i in range(len(datas)):
        if i+1<10:
            a=list(datas[i])
            b=''.join(a[2:])
            arr.append(float(b))
        else:
            a=list(datas[i])
            b=''.join(a[3:])
            arr.append(float(b))
    data.append(arr)
from sklearn import ensemble
clf = ensemble.GradientBoostingClassifier()
clf=clf.fit(data,label)
tname=[]
tdata=[]
p=int(input().strip())
for i in range(p):
    line=[a for a in input().strip().split(" ")]
    tname.append(line[0])
    datas=line[1:]
    arr=[]
    for i in range(len(datas)):
        if i+1<10:
            a=list(datas[i])
            b=''.join(a[2:])
            arr.append(float(b))
        else:
            a=list(datas[i])
            b=''.join(a[3:])
            arr.append(float(b))
    tdata.append(arr)
pred=clf.predict(tdata)
for i in range(len(tname)):
    if int(pred[i])==1:
        print(tname[i], "+1")
    else:
        print(tname[i], int(pred[i]))
