#주석은 ####
#변수명

friend = 1
a = 10
my_name = '홍길동'
myName = '홍길동'
_yourName = '유재석'
member1 = '박명수'

print(friend)
print(a)
print(myName)
print(my_name)
print(_yourName)
print(member1)

#변수명 오류들
#     friend% = 1
#     a! = 10
#     @myName = '홍길동'
#     1abc = 10       ->숫자
#     def = 10        ->예약어


#예약어 알아보기
import keyword
print(keyword.kwlist)   #예약어 리스트
print(len(keyword.kwlist))  #예약어 리스트의 갯수 확인