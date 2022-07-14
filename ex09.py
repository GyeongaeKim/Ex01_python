#문자 자료형
s = ''
str1 = 'hello world'
str2 = "안녕 세상"

print(s, str1, str2)
print(type(s))
print(type(str1))
print(type(str2))
print(isinstance(str2, str))

print(2, 4, 6, sep=" ")

print("="*50)



s01 = "aaa"
s02 = "aaa"
print(id(s01))
print(id(s02))

s02 = "aaaa"
print(id(s01))
print(id(s02))

print("="*50)


str = "abcdef\nghijklmn"
print(str)
str = """abcdef
ghijklmn"""     # \n없이 줄바꿈 가능
print(str)

print("="*50)


#이스케이프 문자표
print('Hello\nWorld\nI\'d Say "hello World"')
print("Hello\nWorld\nI'd Say \"hello World\"")
print("Hello\rWorld")
print("Hello\bWorld")
print("Hello\tWorld")
