a = 'spartacodingclub@gmail.com'


# 채워야하는 함수
def check_mail(s):
    print(s.find("@"))
    return ("true")


print(check_mail(a))

a = 'spartacodingclub@gmail.com'


# 채워야하는 함수
def get_mail(s):
    ## 여기에 코딩을 해주세요

    return s.split('@')[1].split('.')[0]


# 결과값
print(get_mail(a))


#입력값
a = ['사과','감','감','배','포도','포도','딸기','포도','감','수박','딸기']

#채워야하는 함수
def count_list(a_list):
    result = {} result라는 딕셔너리를 만들고
    for el in a_list: a_list에 있는 각 값들을 el 에 넣는것
        if el in result: 만약 result 에 el이 있으면
            result[el] += 1 el 값에 +1
        else:
            result[el] = 1 없으면 1로 선언
    return result 최종적으로 result로 출력

#결과값
print(count_list(a))

#아래와 같이 출력됩니다
{'사과': 1, '감': 3, '배': 1, '포도': 3, '딸기': 2, '수박': 1}