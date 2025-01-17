# An Informal Introduction to Python

# 주석사용법을 적어 놓은 것으로 보인다.

spam = 1 # and this is the second comment
         # ... and now a third!
text = "# This is not a comment because it's inside quotes."

print(2 + 2)
# 4
print(50 - 5*6)
# 20
print((50 - 5*6) / 4)
# 5.0
print(8 / 5) # 나누기는 언제나 float형으로 반환한다
# 1.6


print(17 / 3) # classic division returns a float 
# 5.666666666666667
print(17 // 3) # floor division discards the fractional part
# 5 
print(17 % 3) # operator returns the remainder of the division
# 2
print(5 * 3 + 2) #floored quotient * divisor + remainder
# 17


print(5 ** 2) # 5 squared, 5의 제곱을 표현
# 25
print(2 ** 7) # 2 to the power of 7
# 128


width = 20
height = 5 * 9
print(width * height)
# 900

n
#Traceback (most recent call last):#  File "/Users/dream/PythonWorkspace/tempCodeRunnerFile.py", line 1, in <module>
#    n
#NameError: name 'n' is not defined

print(4 * 3.75 - 1)
# 14.0

tax = 12.5 / 100
price = 100.50
print(price * tax)
# 12.5625

print(price + (price * tax))
# 113.0625
# >>> price + _
print(round((price + price * tax), 2))
# 113.06
# >>> round(_ , 2)
# >>> 인터렉티브 모드에서 실행방법


print('spam eggs')
print("Paris rabbit got your back :)! Yay!")
print('1975')

print('doesn\'t')
print("doens't")
print('"Yes," they said.')
print("\"Yes,\" they said.")
print('"Isn\'t," they said.')



s = 'First line.\nSecond line.'
s # without print(), special chracters are included in the string
print(s) #with print(), special characters are interpreted, so \n produces new

print('C:\some\name') # here \n means newline!
print(r'C:\some\name') # note the r before the quote

print("""\
    Usage: thingy [OPTIONS]
            -h                  Display this usage message
            -H                  Hostname to connect to
     """)

# 3times 'un' , fllowed by 'ium'
print(3 * 'un' + 'uim')
print('Py' 'thon')



# 변수끼리 혹은 변수와 문자열 리터럴(literal)을 붙이려면 + 를 사용해야 함
# 변수와 문자열을 이어붙임

prefix = 'Py'
print(prefix + 'thon')


# 인덱스 사용방법 
word = 'Python'
print(word[0]) # 변수 처음 문자인 P를 출력
print(word[5]) # 변수 마지막 문자인 n을 출력

# 인덱스는 음수가 될 수도 있다
word = 'Python'
print(word[-1]) # 변수 맨 마지막 n
print(word[-2]) # 변수 맨 마지막 앞 o
print(word[-6]) # 변수 맨 처음 P

word = 'Python'
print(word[:2] + word [2:]) # index 2까지 출력 index 2뒷부분 출력
print(word[:4] + word [4:]) # index 2까지 출력 index 2뒷부분 출력

#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1

word = 'Python'
# print(word[4:42])
print(word[42:])
# 너무 큰 값을 인덱스로 사용하면 애러가 발생
print(word[42])


# 파이썬 문자열은 변경이 불가능하므로 다른 변수를 대입하려고 하면 에러를 발생시킨다.
print(word[0] = 'J')

word = 'Python'
print( 'J' + word[1:])
print(word[:2] + 'py')

s = 'supercalifragilisticexpialidocious'
print(len(s)) # len()는 문자열의 길이를 돌려준다


# 리스트 정리
squares = [1, 4, 9, 16, 25]
print(squares)
print(squares[0])
print(squares[-1])
print(squares[-3:])

# 이어 붙이기 가능
squares = [1, 4, 9, 16, 25]
print((squares) + [36, 49, 64, 81, 100])

# 불변인 문자열과는 다르게, 리스트는 가변이므로 내용변경이 가능하다.
cubes = [1, 8, 27, 65, 125]
#print(4 ** 3) # 4의 3제곱
cubes[3] = 64 # 리스트는 중간에 끼워넣기가 가능하다
cubes.append(216)
cubes.append(7 ** 3)
print(cubes)

# 111111
rgb = ["Red", "Green", "Blue"]
rgba = rgb
id(rgb) == id(rgba)  # they reference the same object
rgba.append("Alph")
# print(rgb)
correct_rgba = rgba[:]
correct_rgba[-1] = "Alpha"
print(correct_rgba)
print(rgba)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
print(letters[2:5])

letters[2:5] = []
print(letters)

letters[:] = []
print(letters)


letters = ['a', 'b', 'c', 'd']
print(len(letters))

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)

print(x[0])
print(x[0][1])





# 피보나치 수열
# the sum of two elements defines the next
a, b = 0, 1
while a < 10 : # 루프 조건
    print(a)    
    a, b = b, a+b


