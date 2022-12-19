# ezen04-3
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형

# 딕셔너리 자료형(순서X, 중복X, 수정o, 삭제o)
'''
    1. 사전(dictionary) 자료형
      1) 데이터를 키(key)와 값(value) 쌍의 형태로 저장할 때 사용할 수 있음

      사전 데이터[키] = 값
'''
# 선언
a = {'name':'ezen', 'phone':'01023439874', 'birth':'990124'}
b = { 0 : 'Hello Ezen!'}
c = {'arr' : [1, 2, 3, 4]}

print('a : ', type(a), a)
print('b : ', type(b), b)
print('c : ', type(c), c)

# 출력
print('a : ', a['name'])    # 존재 X => 에러 발생
print('a : ', a.get('phone'))   # 존재 X => None 처리
print('b : ', b[0])
print('b : ', b.get(0))
print('b : ', c['arr'])
print('b : ', c['arr'][3])
print('b : ', c.get('arr'))

# 딕셔너리 추가
a['address'] = 'seoul'
print('a : ', a)
# rank      [1, 2, 3]
a['rank'] = [1, 2, 3]
print('a : ',a)

arr1 = ["컴퓨터", "키보드", "모니터"]
arr2 = ["computer", "keyboard", "monitor"]

data = {arr1[0]:arr2[0], arr1[1]:arr2[1], arr1[2]:arr2[2]}
print(data)

data1 = {}
for i in range(3):
  data1[arr1[i]] = arr2[i]

print(data1)

# 모든 키(key)를 하나씩 확인할때는 keys()메서드 사용함
data = {}
data['apple'] = "사과"
data['banana']  = "바나나"
data['carrot'] = "당근"

for key in data.keys():
  print("key : ", key, ", value : ", data[key])

# keys()
print('a : ', a.keys())
print('b : ', b.keys())
print('c : ', c.keys())

print('a : ', list(a.keys()))
print('b : ', list(b.keys()))
print('c : ', list(c.keys()))

# values()
print('a : ', a.values())
print('b : ', b.values())
print('c : ', c.values())

print('a : ', list(a.values()))
print('b : ', list(b.values()))
print('c : ', list(c.values()))

# items()
print('a : ', a.items())
print('b : ', b.items())
print('c : ', c.items())

print('a : ', list(a.items()))
print('b : ', list(b.items()))
print('c : ', list(c.items()))

# 특정한 데이터의 등장 횟수를 세기
data = [1, 3, 3, 5, 4, 3, 1, 4]
counter = {}

for x in data:
  if x not in counter:
    counter[x] = 1
  else:
    counter[x] += 1

print(counter)

# 집합(Set) 자료형 : 순서X, 중복 X
'''
    - 데이터의 중복을 허용하지 않고, 순서가 상관 없을 때 사용하는 자료형
    - 특정한 데이터가 등장한 적이 있는지 체크할 때 효과적으로 사용됨
    - 데이터를 삽입할 때 add() 메서드를 사용함
'''

# 선언
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Powerful', 'Health', 'Features'])

print('a : ', type(a), a)
print('b : ', type(b), b)
print('c : ', type(c), c)
print('d : ', type(d), d)

print()
# 튜플 변환
t = tuple(b)
print('t : ', type(t), t)

# 리스트 변환
l = list(c)
print('t : ', type(l), l)

data = [1, 3, 3, 5, 4, 3, 1, 4]
visited = set()

for x in data:
  if x not in visited:
    visited.add(x)
  else:
    print("중복 원소 발견함 : ", x)
print("고유한 원소들 : ", visited)

# 집합 자료형 (set) 원소 제거 : remove()
data = {5, 6, 7, 8, 9}
print(data)

data.remove(7)
print(data)

# 합집합 연산자 : |     교집합 연산자 : &       차집합 연산자 : -
data1 = {3, 4, 5, 6, 7}
data2 = {6, 7, 8, 9, 10}

data = data1 | data2  # 합집합
print(data)

data = data1 & data2  # 교집합
print(data)

data = data1 - data2  # 차집합
print(data)