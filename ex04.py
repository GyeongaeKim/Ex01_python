#정수형
a = 101
print(a, type(a))
print(isinstance(a, int))

#2진수, 8진수, 16진수 표현 가능   --> 10진수로 표현
b = 0b101   #2진수
c = 0o101   #8진수
d = 0x101   #16진수
print(b, type(b))
print(c, type(c))
print(d, type(d))



#10진수 --> 2진수, 8진수, 16진수
print(bin(5))
print(oct(65))
print(hex(257))

#파이썬 3.x 에서는 long형이 없어지고 int 타입으로 처리
e = 2**1024 #2의 1024승
print(e)
print(type(e))
