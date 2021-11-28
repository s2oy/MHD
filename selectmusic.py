from playsound import playsound

m1 =('D:\MHD\mp3\assignmentSong.mp3')
m2 = ('D:\MHD\mp3\lastNightStory.mp3')

# 음악 재생 희망곡 입력받기

var1=int( ) # var1의 값을 정수형으로 입력

var1=input("어떤 음악을 재생할까요?") # var1의 값을 입력



# 음악 재생 안내문 출력하기

print("--------------------------")

print("- 나의 뮤직 플레이어 -")

print("- 1. 과제곡  -")

print("- 2. 어젯밤 이야기          -")

print("-------------------------")

if '1' in var1: # var1의 값이 1인 경우

    print('당신의 선택:', var1) # 출력

    print('1번 노래를 재생합니다.') # 출력

    playsound(m1) # m1 경로의 음악 재생

elif '2' in var1: # var1의 값이 2인 경우

    print('당신의 선택:', var1) # 출력

    print('2번 노래를 재생합니다.') # 출력

    playsound(m2) # m2 경로의 음악 재생

# 음악 재생 희망곡 입력받기

var1=int( ) # var1의 값을 정수형으로 입력

var1=input("어떤 음악을 재생할까요?") # var1의 값을 입력