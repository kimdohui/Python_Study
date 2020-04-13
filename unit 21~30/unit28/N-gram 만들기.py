# N-gram이란 문자열에서 N개의 연속된 요소를 추출하는 방법
# 예를 들어 hello를 2-gram으로 추출하면 He \n  el \n ll\n lo\n로 2개씩 끊어서 출력된다


text = 'hello'

for i in range(len(text)-1) : # 2-gram이므로 문자열 끝에서 한글자 앞까지만 반복(끝은 i+1로 표현하면 되므로)
    print(text[i], text[i+1], sep='')


# 반복문으로 N-gram 출력(위는 2-gram이다)

print('----------\n')


text = 'this is python'
words = text.split()  # 공백을 기준으로 문자열을 분리한 뒤 리스트를 만듦

for i in range(len(words)-1):   
    print(words[i], words[i+1])

    
# 리스트에 공백 별로 쪼개면 0 : this  1 : is  2 : python 이므로
# i가 0일때 this와 is  , i가 1일때 is와 python이 출력됨


print('----------\n')

text = 'hello'
 
two_gram = zip(text, text[1:]) #문자열 text와 text[1:]의 각 요소를 묶어서 튜플로 만듦
for i in two_gram:
    print(i[0], i[1], sep='')


#zip 으로 N-gram 만들기
    
# two_gram에 [('h', 'e'), ('e', 'l'), ('l', 'l'), ('l', 'o')] 과 같이 저장됨
# 이를 출력 하여 He\n el\n ll\n lo가 출력됨


print('----------\n')


