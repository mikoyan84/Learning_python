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



# plus로 해줘야

prefix = 'Py'
print(prefix + 'thon')
