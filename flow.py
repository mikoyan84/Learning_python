# if 문
x = int(input("Please enter an interger: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')



# Strategy: Create a new collection
active_users = {}
for user,  status in users.items():
    if status == 'active':
        active_users[user] = status

# for문

# Measure some strings:
words = ['cat', 'window', 'defensestrate']
for w in words:
    print(w, len(w))

# Create a sample collection
    user = {'Hans': 'active', 'Elenore': 'inactive', 'Seoul': 'active'}

# Strategy: iterate over copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# range() 함수
for i in range(5):
    print(i)


print(list(range(5, 10)))
# 5, 6, 7, 8, 9
print(list(range(0, 10, 3)))
# 0, 3, 6, 9
print(list(range(-10, -100, -30)))
# -10, -40, -70

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a))
    print(i, a[i])