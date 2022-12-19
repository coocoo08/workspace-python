# ezen06-4
'''
    5) 딕셔너리(Dictionary) 자료형
      - {Key1:Vakue1, Key2:Vakue2, Key3:Vakue3, ....}
      - {'name' : 'Jessica', 'age' : 19}
      - stu = {'name' : ['Susan', 'Jessica', 'John', 'Michael'], 'age':[19, 15, 16, 17]}
'''

stu = {'name' : ['Susan', 'Jessica', 'John', 'Michael'], 'age':[19, 15, 16, 17]}
print(stu)

print(type(stu))

stu['math'] = [50, 100, 70, 80]
print(stu)

del stu['math']
print(stu)

for key, value in stu.items():
  print(key, value)

  