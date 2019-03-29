from sklearn import svm

xor_data = [
    [0,0,0],
    [0,1,1],
    [1,0,1],
    [1,1,0]
]
# 1차원배열의 마지막 숫자가 답이다.
data = []
# 변수들은 data안에 넣고
label = []
# 답은 label에 넣는다.

for row in xor_data:
    p = row[0]
    q = row[1]
    r = row[2]
    data.append([p,q])
    # 배열의 형태
    label.append(r)

print(data)
print(label)

# -- 결과 --
# 문제 => [[0, 0], [0, 1], [1, 0], [1, 1]]
# 답 =>  [0, 1, 1, 0]

clf = svm.SVC()
clf.fit(data,label)

pre = clf.predict(data)
print("예측결과: ",pre)
# -- 결과 --
# 예측결과:  [0 1 1 0]
# 답을 위에서 그냥 주었기때문에 답 대로 나온다.


# 얼마나 맞혔는지 계산하는 코딩
ok = 0; total = 0
for idx, answer in enumerate(label):
# 다중
    p = pre[idx]
    # pre에 있는 idx에 있는 것을 가져와 p에 담는다.
    if p == answer: ok += 1
    # p(실제정답) 하고 answer(예측값) 과 똑같냐
    total += 1
print("정답률: ", ok, "/" , total,"=", ok/total)

ok = 0
total = len(label)
for i in range(len(label)):
    answer = label[i]
    p = pre[i]
    if answer == p:
        ok = ok+1
print("정답률: ", ok, "/" , total,"=", ok/total)

