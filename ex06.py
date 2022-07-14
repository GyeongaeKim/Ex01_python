#복소수 - complex
"""
복소수 타입의 객체는 실수부+허수부로 나뉘며
허수부에는 j 또는 J를 숫자 뒤에 붙인다
"""

a=4+5j
print(a, type(a))

a=4+5j
b=7-2j
print(a+b)  #실수부는 실수부끼리, 허수부는 허수부끼리

print(b.real)
print(b.imag)


c=4
d=5.4
print(complex(c))   #복소수형으로 변경-형이 아예 바뀐건 아님
print(complex(d))

print(c)    #-형이 아예 바뀐건 아님