import pickle
 
name = 'hana'
age = 18
address = '서울시'
scores = {'korean': 90, 'english': 95}

with open('hanaInfo.p', 'wb') as file: # pickle.dump로 객체 저장 시 파일모드를 wb로 해야 함
     pickle.dump(name,file)
     pickle.dump(age,file)
     pickle.dump(address,file)
     pickle.dump(scores,file)


print('----------------\n')
with open('hanaInfo.p', 'rb') as file:    # james.p 파일을 바이너리 읽기 모드(rb)로 열기
    name = pickle.load(file)
    age = pickle.load(file)
    address = pickle.load(file)
    scores = pickle.load(file)
    print(name)
    print(age)
    print(address)
    print(scores)
