#문자열의 연산 - 문자열의 부분은 변경할 수 없다
str1 = "FirstString"
str2 = "SecondString"

print(str1 + str2)
print(str1*3)
print(str1[2])  #0부터 1, 2, 3, ...
print(str1[-1])  #뒤에서부터 셀때는 -1로 시작
print(str2[2:5])    #[2]부터 [5]앞까지!!!([5]는 포함안됨)
print(str1[1:9:2])  #[1]부터 [9]앞까지 2칸씩 증가
print(str1[:9])     #처음부터 [9]앞까지
print(str1[2:])     #[2]부터 끝까지
print(str1[:])      #처음부터 끝까지
print(str1[-6:-2])  #[-6]부터 [-2]앞까지

print(str1[::-1])   #[-1]부터 역순!!!
print(len(str2))    #문자열 길이


name = "토마스"
name2 = name[::-1]
print(name)
print(name2)

#문자열 객체와 정수형 객체는 + 연산을 할 수 없다.
name = "길동"
age = 40
#print( name + age )
print( name + str(age) )


