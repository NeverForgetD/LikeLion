import datetime

def handleID(id):
    retry = True
    pt1 = ord('가')
    pt2 = ord('힣')
    for i in id:
        if pt1 <= ord(i) <= pt2 and 2 <= len(id) <= 4:
            retry = False
        return retry

def handlePassword(password):
    retry = True
    flag = 0
    pt1 = ord('!')
    pt2 = ord('@')
    pt3 = ord('#')
    pt4 = ord('$')
    if ord('A') <= ord(password[0]) <= ord('Z'):
        flag+=1
    if len(password) >= 8:
        flag+=1
    for i in password:
        index = ord(i)
        if index == pt1 or index == pt2 or index == pt3 or index == pt4:
            flag+=1
    if flag >= 3:
        retry = False
    
def handlePasswordTwice(password1, password2):
    retry = True
    if password1 == password2:
        retry = False
    return retry

def handleEmail(email):
    retry = False
    flag = 0
    pt1 = ord('0')
    pt2 = ord('9')
    pt3 = ord('a')
    pt4 = ord('z')
    pt5 = ord('A')
    pt6 = ord('Z')
    pt7 = ord('.')
    for i in email:
        index = ord(i)
        if not (pt1 <= index <= pt2 or pt3 <= index <= pt4 or pt5 <= index <= pt6 or index == pt7):
            if index == ord('@'):
                flag+=1
            else:
                retry = True
                break
    if not email[-4:] == '.com':
        retry = True
    if not flag ==  1:
        retry = True

    return retry


def getInput():
    id = input("이름을 입력해주세요>>>")
    password1 = input('비밀번호를 입력해주세요>>>')
    password2 = input('확인을 위해 다시 한 번 입력해주세요>>>')
    email = input("이메일 주소를 입력해주세요>>>")

    return [id, password1, password2, email]

def handleInput(info):
    retry = False
    if handleID(info[0]):
        print('아이디 제대로x')
        retry = True
    if not info[1] == info[2]:
        print('패스워드가 다르다')
        etry = True
    else:
        if handlePassword(info[1]):
            print('패스워드 제대로x')
            etry = True
    if handleEmail(info[3]):
        print('email 제대로 x')
        etry = True
    if not len(info) == 4:
        print('정보가 부족해요...')
        retry = True
    
    if not retry:
        return [info[0], info[1], info[3]]
    else:
        return retry




def create_membership():
		# 아래 코드는 python에 내장되어 있는 datetime 모듈을 활용하여 오늘 날짜를 입력하는 코드입니다. 
		# stnr_date 코드는 제가 작성했으니, 건드리지 않으셔도 되옵니다 :)
    now = datetime.datetime.now()
    stnr_date = now.strftime('%Y%m%d')
    
    users = []
    user = {}
	# user 딕셔너리에 username, password, email을 아래 주어진 제한 조건에 알맞게 입력받는 코드를 작성하세요.
	# user 딕셔너리 값에는 username, password, email, stnr_date 총 4가지 값이 저장되어야 합니다.

    info = getInput()
    data = handleInput(info)
    if data:
        #retry
        print('다시 시도해주세요')
        print(data)
    else:
        user['username'] = data[0]
        user['password'] = data[1]
        user['email'] = data[2]
        user['stnr_date'] = stnr_date

    users.append(user)

    return users

#고칠 부분
# 에러 메시지가 하나 입력할 때마다 다시 들어가게
# 전체 에러 / 좋은 입력이 오류로 반응

"""
id 제한 조건
- 한글만 입력 받아야 함
- 총 글자 수는 2-4글자

password 제한 조건
- 첫 문자는 영문 대문자
- 총 글자 수는 8글자 이상
- 특수문자 (!, @, #, $) 중 1가지 반드시 포함

email 제한 조건
- @를 제외한 특수문자는 입력될 수 없음 (입력 가능한 문자는 숫자와 영문)
- 통상적인 email 포맷을 따름
  * @을 포함하고, '.com'으로 이메일 주소가 끝나야 함
  

/데이터 예시/
{홍산하, asdf1234!, sannah@naver.com, 20230427}
{김한준, q1w2e3r4!, zhivagokim@naver.com, 20230427}
{천승범, zxcv4860!, vision6@naver.com, 20230427}

반복문과 조건문을 잘 활용하여, 사용자가 입력을 중단할 때까지 입력 받을 수 있도록 코드를 작성할 것
"""


def load_to_txt(user_list):
    f = open('memberdb.txt', 'w', encoding='UTF-8')
    # user_list에 있는 user 3명의 딕셔너리 값을 txt에 작성하세요.
	  # 올바르게 생성된 텍스트 파일의 예시는 상단에 이미지로 첨부되어 있습니다.
    f.close()
    
def run():
		# 위에서 정의한 create_membership 함수가 실행되어 반환된 결과값을 user_list 객체에 저장합니다.
    user_list = create_membership()
    # 위에 생성된 user_list 객체를 load_to_txt 함수의 입력변수로 활용하여 txt 파일을 생성합니다.
    load_to_txt(user_list)
    
run()