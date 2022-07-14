#확장 연산자
# += 수을 더한 후 다시 대입
x=2
x+=5    #x=x+5
print(x)

# -= 수을 뺀 후 다시 대입
x=2
x-=5    #x=x-5
print(x)

# *= 수을 곱한 후 다시 대입
x=2
x*=5    #x=x*5
print(x)

# /= 수을 나눈 후 다시 대입
x=2
x/=5    #x=x/5
print(x)

print("="*50)



#관계연산자
print(1>3)
print(2<4)
print(4<=5)
print(4>=5)
print(6==9)
print(6!=9)

print("="*50)


a=6
print(0<a and a<10)
print(0<a<10)

print("="*50)



# == 는 객체의 값을 비교
# 같은 객체(동일성)을 비교할 때는 is 연산자
a=10
b=20
c=a
d=10

print(id(a))    #주소값 - 계속 변함
print(id(b))    
print(id(c))    # c=a이기 때문에, 둘의 주소값은 같다
print(id(d))    # 같은값(10)이 이미 있기 때문에 기존값 참조 -> 주소값도 같다

print(a==b)
print(a==c)
print(a is b)
print(a is c)
print(a is d)


print("="*50)





#논리 연산자
print(True and True)
print(False and True)

print(True or True)
print(False or True)

print(not True)
print(not False)

print("="*50)


#내장 수치 함수
print(abs(-3))           # 절대값으로
print(int(3.1415))      # 정수형으로
print(float(3))           # 실수형으로
print(complex(3))      # 복소수형으로
print(pow(2, 10))       # 승수 계산
