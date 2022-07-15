s = "I like Python"

print(s.upper())
print(s.lower())
print(s.swapcase())     #소문자는 대문자로, 대문자는 소문자로
print(s.capitalize())   #제일 첫글자만 대문자로
print(s.title())        #단어 첫글자마다 대문자로

print(5*3)
print(5+5)
print("="*50)



#검색관련
s = 'I Like Python. I Like Java Also'

print(s.find("Like"))
print(s.find("Like", 5))    #5번째부터 찾아봐
print(s.find("Like", 5, 40))
print(s.find("Java"))
print(s.rfind("Like"))  #마지막 인덱스를 찾아줌

print(s.index('Java'))
print(s.rindex('Like'))

print(s.startswith('I Like'))   #해당값으로 시작하는지?
print(s.startswith('I Like', 2))    
print(s.endswith('Also'))
print(s.endswith('Java', 0, 26))
print("="*50)



#편집과 치환
s = '   spam and ham    '
print(s.strip())        #양쪽 공백 자르기
print(s.rstrip())        #오른쪽 공백 자르기
print(s.lstrip())        #왼쪽 공백 자르기


s = '<><abc><><defg><><>'
print(s.strip("<>"))

s = 'Hello Java Java java'
print(s.replace( 'Java', 'Python'))

print("="*50)



#정렬
s = 'king and queen'

print(s.center(60))
print(s.center(60, '-'))
print(s.ljust(60, '-'))
print(s.rjust(60, '-'))

print("="*50)



#판별
print('1234'.isdigit())
print('abcd'.isalpha())
print('1234abcd'.isalpha())     #글자로만 이루어져야 한다..

print('abcd'.islower())     #소문자인지 판별
print('ABCD'.isupper())     #대문자인지 판별

print('\n\n'.isspace())     #공백이 포함되어 있으면 True
print('    '.isspace())
print(''.isspace())         #공백이 포함되어 있지않으면 False

print("="*50)



# 0 으로 채우기
print('20'.zfill(10))
print('1234'.zfill(10))
