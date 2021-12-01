# 음악 패키지 설치 및 임포트

from playsound import playsound


# 음악파일 경로설정

m1=('assignmentSong.mp3')

m2=('lastNightStory.mp3')

m3=('white.mp3')

m4=('sakuranbo.mp3')
m5=('sketerboy.mp3')

# 음악 재생 안내문 출력하기

print("--------------------------")

print("- 나의 뮤직 플레이어 -")

print("- 1. 과제곡  -")

print("- 2. 어젯밤이야기          -")

print("- 3. 화이트      -")

print("- 4. 사쿠란보       -")

print("-5.스케이터보이      -")
print("-------------------------")



# 음악 재생 희망곡 입력받기

var1=int( ) # var1의 값을 정수형으로 입력

var1=input("어떤 음악을 재생할까요?") # var1의 값을 입력



# 음악재생하기

if '1' in var1: # var1의 값이 1인 경우

    print('당신의 선택:', var1) # 출력

    print('1번 노래를 재생합니다.') # 출력

    playsound(m1) # m1 경로의 음악 재생

elif '2' in var1: # var1의 값이 2인 경우

    print('당신의 선택:', var1) # 출력

    print('2번 노래를 재생합니다.') # 출력

    playsound(m2) # m2 경로의 음악 재생

elif '3' in var1: # var1의 값이 3인 경우

    print('당신의 선택:', var1) # 출력

    print('3번 노래를 재생합니다.') # 출력

    playsound(m3) # m3 경로의 음악 재생

elif '4' in var1: # var1의 값이 4인 경우

    print('당신의 선택:', var1) # 출력

    print('4번 노래를 재생합니다.') # 출력

    playsound(m4) # m4 경로의 음악 재생
elif '5' in var1: # var1의 값이 4인 경우

    print('당신의 선택:', var1) # 출력

    print('5번 노래를 재생합니다.') # 출력

    playsound(m5) # m4 경로의 음악 재생

else:

    print('당신의 선택:', var1) # 출력

    print('1~4번 중에 선택하여 주세요.') # 출력
