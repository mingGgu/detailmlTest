from sklearn import svm,metrics
import random, re

# 붓꽃의 csv 데이터 읽어 들이기
csv = []
with open('iris.csv','r',encoding='utf-8') as fp:
    # 한줄씩 읽어들이기
    for line in fp:
        line = line.strip() #줄바꿈 제거
        cols = line.split(',') #쉼표로 자르기
        # 문자열 데이터를 숫자로 변환하기
        fn = lambda n : float(n) if re.match(r'^[0-9\.]+$',n) else n
        # 람다식 : 함수가 간단한 경우 사용한다.
        # 매개변수 n을 받아서 if 컨디션이 참이면 float(n)[실수만들어주기]을 실행
        # if컨디션의 뜻은 숫자의 데이터 이면 float(n)을 실행하고 그렇지않으면
        # n 그상태를 반환해라 라는뜻
        cols = list(map(fn, cols)) #리스트 함수로 만들어주세요
        csv.append(cols)
        #데이터를 2차원배열안에 넣음
print(csv)
# --결과--
# [['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Name'], [5.1, 3.5, 1.4, 0.2, 'Iris-setosa'], [4.9, 3.0, 1.4, 0.2, 'Iris-setosa'], [4.7, 3.2, 1.3, 0.2, 'Iris-setosa'], [4.6, 3.1, 1.5, 0.2, 'Iris-setosa'], [5.0, 3.6, 1.4, 0.2, 'Iris-setosa'], [5.4, 3.9, 1.7, 0.4, 'Iris-setosa'], [4.6, 3.4, 1.4, 0.3, 'Iris-setosa'], [5.0, 3.4, 1.5, 0.2, 'Iris-setosa'], [4.4, 2.9, 1.4, 0.2, 'Iris-setosa'], [4.9, 3.1, 1.5, 0.1, 'Iris-setosa'], [5.4, 3.7, 1.5, 0.2, 'Iris-setosa'], [4.8, 3.4, 1.6, 0.2, 'Iris-setosa'], [4.8, 3.0, 1.4, 0.1, 'Iris-setosa'], [4.3, 3.0, 1.1, 0.1, 'Iris-setosa'], [5.8, 4.0, 1.2, 0.2, 'Iris-setosa'], [5.7, 4.4, 1.5, 0.4, 'Iris-setosa'], [5.4, 3.9, 1.3, 0.4, 'Iris-setosa'], [5.1, 3.5, 1.4, 0.3, 'Iris-setosa'], [5.7, 3.8, 1.7, 0.3, 'Iris-setosa'], [5.1, 3.8, 1.5, 0.3, 'Iris-setosa'], [5.4, 3.4, 1.7, 0.2, 'Iris-setosa'], [5.1, 3.7, 1.5, 0.4, 'Iris-setosa'], [4.6, 3.6, 1.0, 0.2, 'Iris-setosa'], [5.1, 3.3, 1.7, 0.5, 'Iris-setosa'], [4.8, 3.4, 1.9, 0.2, 'Iris-setosa'], [5.0, 3.0, 1.6, 0.2, 'Iris-setosa'], [5.0, 3.4, 1.6, 0.4, 'Iris-setosa'], [5.2, 3.5, 1.5, 0.2, 'Iris-setosa'], [5.2, 3.4, 1.4, 0.2, 'Iris-setosa'], [4.7, 3.2, 1.6, 0.2, 'Iris-setosa'], [4.8, 3.1, 1.6, 0.2, 'Iris-setosa'], [5.4, 3.4, 1.5, 0.4, 'Iris-setosa'], [5.2, 4.1, 1.5, 0.1, 'Iris-setosa'], [5.5, 4.2, 1.4, 0.2, 'Iris-setosa'], [4.9, 3.1, 1.5, 0.1, 'Iris-setosa'], [5.0, 3.2, 1.2, 0.2, 'Iris-setosa'], [5.5, 3.5, 1.3, 0.2, 'Iris-setosa'], [4.9, 3.1, 1.5, 0.1, 'Iris-setosa'], [4.4, 3.0, 1.3, 0.2, 'Iris-setosa'], [5.1, 3.4, 1.5, 0.2, 'Iris-setosa'], [5.0, 3.5, 1.3, 0.3, 'Iris-setosa'], [4.5, 2.3, 1.3, 0.3, 'Iris-setosa'], [4.4, 3.2, 1.3, 0.2, 'Iris-setosa'], [5.0, 3.5, 1.6, 0.6, 'Iris-setosa'], [5.1, 3.8, 1.9, 0.4, 'Iris-setosa'], [4.8, 3.0, 1.4, 0.3, 'Iris-setosa'], [5.1, 3.8, 1.6, 0.2, 'Iris-setosa'], [4.6, 3.2, 1.4, 0.2, 'Iris-setosa'], [5.3, 3.7, 1.5, 0.2, 'Iris-setosa'], [5.0, 3.3, 1.4, 0.2, 'Iris-setosa'], [7.0, 3.2, 4.7, 1.4, 'Iris-versicolor'], [6.4, 3.2, 4.5, 1.5, 'Iris-versicolor'], [6.9, 3.1, 4.9, 1.5, 'Iris-versicolor'], [5.5, 2.3, 4.0, 1.3, 'Iris-versicolor'], [6.5, 2.8, 4.6, 1.5, 'Iris-versicolor'], [5.7, 2.8, 4.5, 1.3, 'Iris-versicolor'], [6.3, 3.3, 4.7, 1.6, 'Iris-versicolor'], [4.9, 2.4, 3.3, 1.0, 'Iris-versicolor'], [6.6, 2.9, 4.6, 1.3, 'Iris-versicolor'], [5.2, 2.7, 3.9, 1.4, 'Iris-versicolor'], [5.0, 2.0, 3.5, 1.0, 'Iris-versicolor'], [5.9, 3.0, 4.2, 1.5, 'Iris-versicolor'], [6.0, 2.2, 4.0, 1.0, 'Iris-versicolor'], [6.1, 2.9, 4.7, 1.4, 'Iris-versicolor'], [5.6, 2.9, 3.6, 1.3, 'Iris-versicolor'], [6.7, 3.1, 4.4, 1.4, 'Iris-versicolor'], [5.6, 3.0, 4.5, 1.5, 'Iris-versicolor'], [5.8, 2.7, 4.1, 1.0, 'Iris-versicolor'], [6.2, 2.2, 4.5, 1.5, 'Iris-versicolor'], [5.6, 2.5, 3.9, 1.1, 'Iris-versicolor'], [5.9, 3.2, 4.8, 1.8, 'Iris-versicolor'], [6.1, 2.8, 4.0, 1.3, 'Iris-versicolor'], [6.3, 2.5, 4.9, 1.5, 'Iris-versicolor'], [6.1, 2.8, 4.7, 1.2, 'Iris-versicolor'], [6.4, 2.9, 4.3, 1.3, 'Iris-versicolor'], [6.6, 3.0, 4.4, 1.4, 'Iris-versicolor'], [6.8, 2.8, 4.8, 1.4, 'Iris-versicolor'], [6.7, 3.0, 5.0, 1.7, 'Iris-versicolor'], [6.0, 2.9, 4.5, 1.5, 'Iris-versicolor'], [5.7, 2.6, 3.5, 1.0, 'Iris-versicolor'], [5.5, 2.4, 3.8, 1.1, 'Iris-versicolor'], [5.5, 2.4, 3.7, 1.0, 'Iris-versicolor'], [5.8, 2.7, 3.9, 1.2, 'Iris-versicolor'], [6.0, 2.7, 5.1, 1.6, 'Iris-versicolor'], [5.4, 3.0, 4.5, 1.5, 'Iris-versicolor'], [6.0, 3.4, 4.5, 1.6, 'Iris-versicolor'], [6.7, 3.1, 4.7, 1.5, 'Iris-versicolor'], [6.3, 2.3, 4.4, 1.3, 'Iris-versicolor'], [5.6, 3.0, 4.1, 1.3, 'Iris-versicolor'], [5.5, 2.5, 4.0, 1.3, 'Iris-versicolor'], [5.5, 2.6, 4.4, 1.2, 'Iris-versicolor'], [6.1, 3.0, 4.6, 1.4, 'Iris-versicolor'], [5.8, 2.6, 4.0, 1.2, 'Iris-versicolor'], [5.0, 2.3, 3.3, 1.0, 'Iris-versicolor'], [5.6, 2.7, 4.2, 1.3, 'Iris-versicolor'], [5.7, 3.0, 4.2, 1.2, 'Iris-versicolor'], [5.7, 2.9, 4.2, 1.3, 'Iris-versicolor'], [6.2, 2.9, 4.3, 1.3, 'Iris-versicolor'], [5.1, 2.5, 3.0, 1.1, 'Iris-versicolor'], [5.7, 2.8, 4.1, 1.3, 'Iris-versicolor'], [6.3, 3.3, 6.0, 2.5, 'Iris-virginica'], [5.8, 2.7, 5.1, 1.9, 'Iris-virginica'], [7.1, 3.0, 5.9, 2.1, 'Iris-virginica'], [6.3, 2.9, 5.6, 1.8, 'Iris-virginica'], [6.5, 3.0, 5.8, 2.2, 'Iris-virginica'], [7.6, 3.0, 6.6, 2.1, 'Iris-virginica'], [4.9, 2.5, 4.5, 1.7, 'Iris-virginica'], [7.3, 2.9, 6.3, 1.8, 'Iris-virginica'], [6.7, 2.5, 5.8, 1.8, 'Iris-virginica'], [7.2, 3.6, 6.1, 2.5, 'Iris-virginica'], [6.5, 3.2, 5.1, 2.0, 'Iris-virginica'], [6.4, 2.7, 5.3, 1.9, 'Iris-virginica'], [6.8, 3.0, 5.5, 2.1, 'Iris-virginica'], [5.7, 2.5, 5.0, 2.0, 'Iris-virginica'], [5.8, 2.8, 5.1, 2.4, 'Iris-virginica'], [6.4, 3.2, 5.3, 2.3, 'Iris-virginica'], [6.5, 3.0, 5.5, 1.8, 'Iris-virginica'], [7.7, 3.8, 6.7, 2.2, 'Iris-virginica'], [7.7, 2.6, 6.9, 2.3, 'Iris-virginica'], [6.0, 2.2, 5.0, 1.5, 'Iris-virginica'], [6.9, 3.2, 5.7, 2.3, 'Iris-virginica'], [5.6, 2.8, 4.9, 2.0, 'Iris-virginica'], [7.7, 2.8, 6.7, 2.0, 'Iris-virginica'], [6.3, 2.7, 4.9, 1.8, 'Iris-virginica'], [6.7, 3.3, 5.7, 2.1, 'Iris-virginica'], [7.2, 3.2, 6.0, 1.8, 'Iris-virginica'], [6.2, 2.8, 4.8, 1.8, 'Iris-virginica'], [6.1, 3.0, 4.9, 1.8, 'Iris-virginica'], [6.4, 2.8, 5.6, 2.1, 'Iris-virginica'], [7.2, 3.0, 5.8, 1.6, 'Iris-virginica'], [7.4, 2.8, 6.1, 1.9, 'Iris-virginica'], [7.9, 3.8, 6.4, 2.0, 'Iris-virginica'], [6.4, 2.8, 5.6, 2.2, 'Iris-virginica'], [6.3, 2.8, 5.1, 1.5, 'Iris-virginica'], [6.1, 2.6, 5.6, 1.4, 'Iris-virginica'], [7.7, 3.0, 6.1, 2.3, 'Iris-virginica'], [6.3, 3.4, 5.6, 2.4, 'Iris-virginica'], [6.4, 3.1, 5.5, 1.8, 'Iris-virginica'], [6.0, 3.0, 4.8, 1.8, 'Iris-virginica'], [6.9, 3.1, 5.4, 2.1, 'Iris-virginica'], [6.7, 3.1, 5.6, 2.4, 'Iris-virginica'], [6.9, 3.1, 5.1, 2.3, 'Iris-virginica'], [5.8, 2.7, 5.1, 1.9, 'Iris-virginica'], [6.8, 3.2, 5.9, 2.3, 'Iris-virginica'], [6.7, 3.3, 5.7, 2.5, 'Iris-virginica'], [6.7, 3.0, 5.2, 2.3, 'Iris-virginica'], [6.3, 2.5, 5.0, 1.9, 'Iris-virginica'], [6.5, 3.0, 5.2, 2.0, 'Iris-virginica'], [6.2, 3.4, 5.4, 2.3, 'Iris-virginica'], [5.9, 3.0, 5.1, 1.8, 'Iris-virginica']]


# 가장 앞 줄의 헤더 제거
del csv[0]

# 데이터 셔플하기(섞기)
random.shuffle(csv)

# 학습 전용 데이터와 테스트전용 데이터 분할하기
tot_len = len(csv)
train_len = int(tot_len * 2/3)
train_data = []
train_label = []
test_data = []
test_label = []

for i in range(tot_len):
    data = csv[i][0:4]
    label = csv[i][4]
    if i < train_len:
        train_data.append(data)
        train_label.append(label)
    else:
        test_data.append(data)
        test_label.append(label)
# 데이터를 학습시키고 예측하기
clf = svm.SVC()
clf.fit(train_data,train_label)
pre = clf.predict(test_data)

# 정답률 구하기
ac_score = metrics.accuracy_score(test_label,pre)
print("정답률: ",ac_score)

















