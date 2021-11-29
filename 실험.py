import tkinter as tk
from tkinter import messagebox
import pygame
import random
from pygame.rect import *
# pygame 초기화
pygame.init()
pygame.display.set_caption("MHD")
background = pygame.image.load("background.png")

pygame.init()
pygame.display.set_caption("mohamD")
pygame.mixer.music.load("white.mp3")
pygame.mixer.music.play(-1)
class lastnightstory(tk.Frame):
# pygame 초기화
    pygame.init()
    pygame.display.set_caption("MHD")
    background = pygame.image.load("background.png")

    pygame.init()
    pygame.display.set_caption("mohamD")
    pygame.mixer.music.load("lastNightStory.mp3")
    pygame.mixer.music.play(-1)


# ======== 함수 ===============================
# 키 이벤트 처리하기
def resultProcess(direction):
    global isColl, score, DrawResult, result_ticks

    if isColl and CollDirection.direction == direction:
        score += 10
        CollDirection.y = -1
        DrawResult = 1
    else:
        DrawResult = 2
    result_ticks = pygame.time.get_ticks()


def eventProcess():
    global isActive, score, health
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isActive = False
            if health > 0:
                if event.key == pygame.K_UP:  # 0
                    resultProcess(0)
                if event.key == pygame.K_LEFT:  # 1
                    resultProcess(1)
                if event.key == pygame.K_DOWN:  # 2
                    resultProcess(2)
                if event.key == pygame.K_RIGHT:  # 3
                    resultProcess(3)
            else:
                if event.key == pygame.K_SPACE:
                    score = 0
                    health = health_MAX
                    for direc in Directions:
                        direc.y = -1


###################################################################################
# 방향 아이콘 클래스
class Direction(object):
    def __init__(self):
        self.pos = None
        self.direction = 0
        self.image = pygame.image.load(f"up.png")
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rotated_image = pygame.transform.rotate(self.image, 0)
        self.y = -1
        self.x = int(SCREEN_WIDTH / 2) - (self.image.get_width() /2)

    def rotate(self, direction=0):
        self.direction = direction
        self.rotated_image = pygame.transform.rotate(
            self.image, 90 * self.direction)

    def draw(self):
        if self.y >= SCREEN_HEIGHT:
            self.y = 5
            return True
        elif self.y == -1:
            return False
        else:
            self.y += 1
            self.pos = screen.blit(self.rotated_image, (self.x, self.y))
            return False


###################################################################################
# 방향 아이콘 생성과 그리기
def drawIcon():
    global start_ticks, health

    if health <= 0:
        return

    elapsed_time = (pygame.time.get_ticks() - start_ticks)
    if elapsed_time > 700:
        start_ticks = pygame.time.get_ticks()
        for direc in Directions:
            if direc.y == -1:
                direc.y = 100
                direc.rotate(direction=random.randint(0, 3))
                break

    for direc in Directions:
        if direc.draw():
            health -= 1


###################################################################################
# 타겟 영역 그리기와 충돌 확인하기
def draw_targetArea():
    global isColl, CollDirection
    isColl = False
    for direc in Directions:
        if direc.y == -1:
            continue
        if direc.pos.colliderect(targetArea):
            isColl = True
            CollDirection = direc
            pygame.draw.rect(screen, (255, 255, 255, 0.3), targetArea)
            break
    pygame.draw.rect(screen, (0, 0, 0), targetArea, 3)


###################################################################################
# 문자 넣기
def setText():
    global score, health
    mFont = pygame.font.SysFont("굴림", 40)

    mtext = mFont.render(f'score : {score}', True, 'red')
    screen.blit(mtext, (138, 10, 0, 0))

    mtext = mFont.render(f'health : {health}', True, 'red')
    screen.blit(mtext, (125, 42, 0, 0))

    if health <= 0:
        mFont = pygame.font.SysFont("굴림", 90)
        mtext = mFont.render(f'Game over!!', True, 'blue')
        tRec = mtext.get_rect()
        tRec.centerx = SCREEN_WIDTH / 2
        tRec.centery = SCREEN_HEIGHT / 2 - 40
        pygame.mixer.music.pause()
        screen.blit(mtext, tRec)


###################################################################################
# 결과 이모티콘 그리기
def drawResult():
    global DrawResult, result_ticks
    if result_ticks > 0:
        elapsed_time = (pygame.time.get_ticks() - result_ticks)
        if elapsed_time > 400:
            result_ticks = 0
            DrawResult = 0
    screen.blit(resultImg[DrawResult], resultImgRec)


###################################################################################
# ========= 변수 =================================
isActive = True
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
health_MAX = 30
score = 0
health = health_MAX
isColl = False
CollDirection = 0
DrawResult, result_ticks = 0, 0
start_ticks = pygame.time.get_ticks()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 방향 아이콘
Directions = [Direction() for i in range(0, 10)]
# 타겟 박스
targetArea = Rect(SCREEN_WIDTH/3, 500, SCREEN_WIDTH /3, 50)
# 결과 이모티콘
resultFileNames = ["good.png", "perfect.png", "bad.png"]
resultImg = []
for i, name in enumerate(resultFileNames):
    resultImg.append(pygame.image.load(name))
    resultImg[i] = pygame.transform.scale(resultImg[i], (150, 75))

resultImgRec = resultImg[0].get_rect()
resultImgRec.centerx = SCREEN_WIDTH / 2.15 - resultImgRec.width / 2 - 40 #아이콘과 박스 width 정렬
resultImgRec.centery = targetArea.centery

# ========= 반복문 ===============================
while (isActive):
    screen.blit(background,(0, 0))
    eventProcess()
    # Directions[0].y = 100
    # Directions[0].rotate(1)
    # Directions[0].draw()
    draw_targetArea()
    drawIcon()
    setText()
    drawResult()
    pygame.display.update()
    clock.tick(400)
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(selectpage)
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame().destory()
        self._frame = new_frame
        self._frame.pack()
# 노래고르기
class selectpage(tk.Frame):
    def __init__(self,master):
        music = {'어젯밤 이야기': 0, '과제곡': 0, '화이트': 0, '사쿠란보': 0, '스케이터보이': 0}
        order = []
        sum = 0

        def select(item):
            global sum

            if item not in music:
                print("선택 안함")
            this_music = music.get(item)
            sum += this_music
            order.append(item)
            textarea.insert(tk.INSERT, item + " ")
            label1['text'] = "선택한곡:" + str(sum)

        def btn_exit():
            msgbox = tk.messagebox.askquestion('확인', '플레이를 하시겠습니까?')
            if msgbox == 'yes':
                exit()

        window = tk.Tk()
        window.title('노래 고르기')
        window.geometry("600x600")
        frame1 = tk.Frame(window)
        frame1.pack()

        tk.Button(frame1, text="어젯밤 이야기", command=lambda: master.switch_frame(lastnightstory), width=10, height=2).grid(row=0, column=1)
        tk.Button(frame1, text="과제곡", command=lambda: select('과제곡'), width=10, height=2).grid(row=0, column=2)
        tk.Button(frame1, text="화이트", command=lambda: select('화이트'), width=10, height=2).grid(row=0, column=3)
        tk.Button(frame1, text="사쿠란보", command=lambda: select('사쿠란보'), width=10, height=2).grid(row=0, column=4)
        tk.Button(frame1, text="스케이터보이", command=lambda: select('스케이터보이'), width=10, height=2).grid(row=0, column=5)
        tk.Button(frame1, text="exit", command=btn_exit, width=10, height=2).grid(row=0, column=6)

        label1 = tk.Label(window, text="선택한곡:", width=100, height=2, fg="blue")
        label1.pack()

        textarea = tk.Text(window)
        textarea.pack()




if __name__ == "__main__":
    game = SampleApp()
    game.mainloop()