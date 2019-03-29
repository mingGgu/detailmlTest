from sklearn import  svm,metrics
import random, re

data = [
    [20,100,'합격'],
    [18,3,'불합격'],
    [15,10,'불합격'],
    [18,80,'합격'],
    [20,100,'합격'],
    [18,0,'불합격'],
    [20,90,'합격'],
    [17,50,'불합격'],
    [19,90,'합격'],
    [14,50,'불합격']
]
# 70%만 학습에 참여시키고 30%를 갖고 예측하여 정답률을 계산하여 출력

total_len = len(data)
train_len = int(total_len * 7/10)
# 7 (data의 70%인 7개만 뽑아오기 위해 설정해준다.)

# train_data = data[:7]
# test data = data[7:] 
# 이렇게 추출가능

train_data =[]
train_label = []
test_data = []
test_label = []

# 훈련데이터로부터 문제와 답을 각각 분리하기
for i in range(train_len):
    p = data[i][0]
    q = data[i][1]
    r = data[i][2]
    train_data.append([p,q])
    train_label.append(r)

# 학습시키기
clf = svm.SVC()
clf.fit(train_data,train_label)


for n in range(train_len,len(data)):
    ppre = data[n][0]
    qpre = data[n][1]
    rpre = data[n][2]
    test_data.append([ppre,qpre])
    test_label.append(rpre)

pre = clf.predict(test_data)
print(pre)

ok = 0; total = 0
for idx, answer in enumerate(test_label):
    # 결과를 알고있어야지 계산식이 가능하다.
    p = pre[idx]
    if p == answer: ok +=1
    total += 1
print(ok/total)

acc = metrics.accuracy_score(test_label,pre)
# 반환 건수와 답의수가 같아야한다
print(acc)


