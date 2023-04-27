print('Hello World')

#1
num = int(input('숫자를 넣어용>>>'))

for i in range(1, num+1):
    print('*'*i)

for i in range(1, num+1):
    print('*'*(num+1 - i))

for i in range(1, num+1):
    print(' '*(num-i), '*'*i)

for i in range(1, num+1):
    print(' '*(num-i), '*'*(2*i-1))


#2, 3
id = input('주민번호를 입력해주세요')
print('year :', id[0:2])
print('month :', id[2:4])
print('day :', id[4:6])

if int(id[7])%2 == 1 :
    print('남자입니다')
else:
    print('여자입니다')


#4
x, y, w, h = map(int, input('x, y, w, h를 입력해주세요>>>').split())
min = min(abs(w-x), abs(x), abs(h-y), abs(y))
print(min)

#5
temp = {}

temp = {
    '메로나' : 1000,
    '폴라포' : 1200,
    '빵빠레' : 1800
}

temp['죠스바'] = 1200
temp['원드콘'] = 1500

print('메로나 가격:', temp['메로나'])

temp['메로나'] = 1300

del temp['메로나']