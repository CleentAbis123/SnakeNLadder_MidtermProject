import pygame
from random import randint
import time

clock = pygame.time.Clock()

pygame.init()
w = 1366
h = 768

icon = pygame.image.load("img/icon.jpg")
GD = pygame.display.set_mode((w, h))
pygame.display.set_caption("Snakes N Ladders")
pygame.display.set_icon(icon)
pygame.display.update()

black = (10, 10, 10)
white = (250, 250, 250)
red = (200, 0, 0)
b_red = (240, 0, 0)
green = (0, 200, 0)
b_green = (0, 230, 0)
blue = (0, 0, 200)
grey = (50, 50, 50)
yellow = (150, 150, 0)
purple = (43, 3, 132)
b_purple = (60, 0, 190)

board = pygame.image.load("img/Snakes-and-Ladders-Bigger.jpg")
dice1 = pygame.image.load("img/dice1.png")
dice2 = pygame.image.load("img/dice2.png")
dice3 = pygame.image.load("img/dice3.png")
dice4 = pygame.image.load("img/dice4.png")
dice5 = pygame.image.load("img/dice5.png")
dice6 = pygame.image.load("img/dice6.png")

redgoti = pygame.image.load("img/redgoti.png")
yellowgoti = pygame.image.load("img/yellowgoti.png")
greengoti = pygame.image.load("img/greengoti.png")
bluegoti = pygame.image.load("img/bluegoti.png")
menubg = pygame.image.load("img/menu.jpg")
p = pygame.image.load("img/playbg.jpg")
intbg = pygame.image.load("img/intropic.png")
intbg2 = pygame.image.load("img/intropic2.jpg")
intbg3 = pygame.image.load("img/intropic3.jpg")
intbg4 = pygame.image.load("img/intropic4.jpg")
intbg5 = pygame.image.load("img/intropic5.jpg")

pygame.mixer.music.load("sounds/music.wav")
snakesound = pygame.mixer.Sound("sounds/snake.wav")
win = pygame.mixer.Sound("sounds/win.wav")
lose = pygame.mixer.Sound("sounds/lose.wav")
ladder = pygame.mixer.Sound("sounds/ladder.wav")

# mouse pos
mouse = pygame.mouse.get_pos()
click = pygame.mouse.get_pressed()

custom_font = pygame.font.Font(None, 30)


# Message displaying for buttons
def message_display(text, x, y, fs):
    largeText = pygame.font.Font('freesansbold.ttf', fs)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x, y)
    GD.blit(TextSurf, TextRect)


def message_display1(text, x, y, fs, c):
    text_surface = custom_font.render(text, True, c)
    text_rect = text_surface.get_rect(center=(x, y))
    GD.blit(text_surface, text_rect)


def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


# Message displaying for field
def message_display1(text, x, y, fs, c):
    largeText = pygame.font.Font('freesansbold.ttf', fs)
    TextSurf, TextRect = text_objects1(text, largeText)
    TextRect.center = (x, y)
    GD.blit(TextSurf, TextRect)


def text_objects1(text, font, c):
    textSurface = font.render(text, True, c)
    return textSurface, textSurface.get_rect()


def goti(a):
    l1 = [[406, 606], [456, 606], [506, 606], [556, 606], [606, 606], [656, 606], [706, 606], [756, 606], [806, 606],
          [856, 606], [906, 606], [906, 560], [856, 560], [806, 560], [756, 560], [706, 560], [656, 560], [606, 560],
          [556, 560], [506, 560], [456, 560], [456, 506], [506, 506], [556, 506], [606, 506], [656, 506], [706, 506],
          [756, 506], [806, 506], [856, 506], [906, 506], [906, 460], [856, 460], [806, 460], [756, 460], [706, 460],
          [656, 460], [606, 460], [556, 460], [506, 460], [456, 460], [456, 406], [506, 406], [556, 406], [606, 406],
          [656, 406], [706, 406], [756, 406], [806, 406], [856, 406], [906, 406], [906, 360], [856, 360], [806, 360],
          [756, 360], [706, 360], [656, 360], [606, 360], [556, 360], [506, 360], [456, 360], [456, 306], [506, 306],
          [556, 306], [606, 306], [656, 306], [706, 306], [756, 306], [806, 306], [856, 306], [906, 306], [906, 260],
          [856, 260], [806, 260], [756, 260], [706, 260], [656, 260], [606, 260], [556, 260], [506, 260], [456, 260],
          [456, 206], [506, 206], [556, 206], [606, 206], [656, 206], [706, 206], [756, 206], [806, 206], [856, 206],
          [906, 206], [906, 160], [856, 160], [806, 160], [756, 160], [706, 160], [656, 160], [606, 160], [556, 160],
          [506, 160], [456, 160]]
    l2 = l1[a]
    x = l2[0] - 25
    y = l2[1] - 25
    return x, y


def text_objects1(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def ladders(x):
    if x == 1:
        return 38
    elif x == 4:
        return 14
    elif x == 9:
        return 31
    elif x == 28:
        return 84
    elif x == 21:
        return 42
    elif x == 51:
        return 67
    elif x == 80:
        return 99
    elif x == 72:
        return 91
    else:
        return x


def snakes(x):
    if x == 17:
        return 7
    elif x == 54:
        return 34
    elif x == 62:
        return 19
    elif x == 64:
        return 60
    elif x == 87:
        return 36
    elif x == 93:
        return 73
    elif x == 95:
        return 75
    elif x == 98:
        return 79
    else:
        return x


def dice_roll_animation():
    frames = [dice1, dice2, dice3, dice4, dice5, dice6]
    time_start = pygame.time.get_ticks()

    while pygame.time.get_ticks() - time_start < 1000:
        frame_index = int((pygame.time.get_ticks() - time_start) / 200) % 6
        current_frame = frames[frame_index]
        GD.blit(current_frame, (300, 500))
        pygame.display.update()

        pygame.time.delay(100)

    return frame_index + 1


def dice(a):
    if a == 1:
        a = dice1
    elif a == 2:
        a = dice2
    elif a == 3:
        a = dice3
    elif a == 4:
        a = dice4
    elif a == 5:
        a = dice5
    elif a == 6:
        a = dice6

    time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - time < 1000:
        GD.blit(a, (300, 500))
        pygame.display.update()


def button2(text, xmouse, ymouse, x, y, w, h, i, a, fs):
    # mouse pos
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > xmouse > x and y + h > ymouse > y:
        pygame.draw.rect(GD, a, [x - 2.5, y - 2.5, w + 5, h + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
            return True

    else:
        pygame.draw.rect(GD, i, [x, y, w, h])
    message_display(text, (x + w + x) / 2, (y + h + y) / 2, fs)


def button1(text, xmouse, ymouse, x, y, w, h, i, a, fs):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > xmouse > x and y + h > ymouse > y:
        pygame.draw.rect(GD, a, [x - 2.5, y - 2.5, w + 5, h + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
            return True

    else:
        pygame.draw.rect(GD, i, [x, y, w, h])
    message_display(text, (x + w + x) / 2, (y + h + y) / 2, fs)


# Turn
def turn(score, l, s):
    a = randint(1, 6)
    dice_roll_animation()

    if a == 6:
        six = True
    else:
        six = False
    p = dice(a)
    score += a
    if score <= 100:
        lad = ladders(score)
        if lad != score:
            l = True
            pygame.mixer.Sound.play(ladder)
            time = pygame.time.get_ticks()
            score = lad
        snk = snakes(score)
        if snk != score:
            s = True
            pygame.mixer.Sound.play(snakesound)
            score = snk

    else:
        score -= a
        time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time < 1500:
            message_display1("Can't move!", 650, 50, 35, black)
            pygame.display.update()
    return score, l, s, six


def Quit():
    pygame.quit()
    quit()


def button(text, xmouse, ymouse, x, y, w, h, i, a, fs, b):
    if x + w > xmouse > x and y + h > ymouse > y:
        pygame.draw.rect(GD, a, [x - 2.5, y - 2.5, w + 5, h + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if b == 1:
                options()
            elif b == 5:
                return 5
            elif b == 0:
                Quit()
            elif b == "s" or b == 2 or b == 3 or b == 4:
                return b
            elif b == 7:
                options()
            else:
                return True


    else:
        pygame.draw.rect(GD, i, [x, y, w, h])
    message_display(text, (x + w + x) / 2, (y + h + y) / 2, fs)


def intro():
    intro_music = pygame.mixer.Sound("sounds/intro_music.wav")

    intro_music_played = False

    time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - time < 2500:
        if not intro_music_played:
            intro_music.play(-1)
            intro_music_played = True

        GD.blit(intbg, (0, 0))
        pygame.display.update()

    while True:
        time = pygame.time.get_ticks()
        intro_music.stop()
        while pygame.time.get_ticks() - time < 500:
            GD.blit(intbg2, (0, 0))
            pygame.display.update()
        time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time < 500:
            GD.blit(intbg3, (0, 0))
            pygame.display.update()
        time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time < 500:
            GD.blit(intbg4, (0, 0))
            pygame.display.update()
        time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time < 500:
            GD.blit(intbg5, (0, 0))
            pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return
        pygame.display.update()


def button_image(image_path, xmouse, ymouse, x, y, w, h, action=None):
    button_img = pygame.image.load(image_path)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > xmouse > x and y + h > ymouse > y:
        GD.blit(button_img, (x, y))
        if click[0] == 1 and action is not None:
            return action
    else:
        GD.blit(button_img, (x, y))


def main():
    pygame.mixer.music.play(-1)

    menu = True
    play_music_clicked = True
    mute_clicked = False

    while menu:
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse = pygame.mouse.get_pos()
                    if (w / 2 - 100) <= mouse[0] <= (w / 2 + 100) and (h / 2) <= mouse[1] <= (h / 2 + 100):
                        play(2)
                    elif (w / 2 - 100) <= mouse[0] <= (w / 2 + 100) and (h / 2 + 200) <= mouse[1] <= (h / 2 + 300):
                        Quit()
                    elif 1166 <= mouse[0] <= 1366 and 75 <= mouse[1] <= 125:
                        pygame.mixer.music.pause()
                        mute_clicked = not mute_clicked
                        play_music_clicked = False
                    elif 1166 <= mouse[0] <= 1366 and 0 <= mouse[1] <= 50:
                        pygame.mixer.music.unpause()
                        play_music_clicked = True
                        mute_clicked = False

        GD.blit(menubg, (0, 0))
        button_image("img/play.png", mouse[0], mouse[1], (w / 2 - 100), h / 2, 200, 100)
        button_image("img/quit.png", mouse[0], mouse[1], (w / 2 - 100), (h / 2) + 200, 200, 100)

        if mute_clicked:
            button_image("img/mute.png", mouse[0], mouse[1], 1166, 0, 200, 50)
        else:
            button_image("img/mute1.png", mouse[0], mouse[1], 1166, 0, 200, 50)

        if play_music_clicked:
            button_image("img/play_music.png", mouse[0], mouse[1], 1166, 75, 200, 50)
        else:
            button_image("img/play_music1.png", mouse[0], mouse[1], 1166, 75, 200, 50)

        pygame.display.update()


# Options Menu:
def options():
    flag = True
    while flag == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()

        # mouse pos
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        b1 = b2 = b3 = b4 = b5 = -1
        GD.blit(menubg, (0, 0))

        b2 = button("2 Players", mouse[0], mouse[1], (w / 2) - 150, 350, 300, 50, green, b_green, 30, 2)
        # 3 player
        b3 = button("3 Players", mouse[0], mouse[1], (w / 2) - 150, 450, 300, 50, green, b_green, 30, 3)
        # 4 player
        b4 = button("4 Players", mouse[0], mouse[1], (w / 2) - 150, 550, 300, 50, green, b_green, 30, 4)
        # Back button
        b5 = button("Back", mouse[0], mouse[1], 0, 650, 200, 50, red, b_red, 30, 5)
        if b5 == 5:
            main()
        if b2 == 2:
            play(2)
        if b3 == 3:
            play(3)
        if b4 == 4:
            play(4)

        pygame.display.update()


def play(b):
    current_player = 1

    p1score = p2score = p3score = p4score = 0
    xcr = xcy = xcg = xcb = 406 - 25
    ycr = ycy = ycg = ycb = 606 - 25

    while True:
        l = False
        s = False
        time = 3000
        GD.blit(p, (0, 0))
        GD.blit(board, (w / 2 - 250, h / 2 - 250))
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()

        message_display1(f"Player {current_player}'s Turn", 650, 20, 30, white)
        if current_player == 1:
            if button1("Player 1", mouse[0], mouse[1], 100, 700, 200, 50, red, grey, 30):
                p1score, l, s, six = turn(p1score, l, s)
                xcr, ycr = goti(p1score)
                if not six:
                    current_player = 2 if b > 1 else 1
                if p1score == 100:
                    break

        elif current_player == 2:
            if button1("Player 2", mouse[0], mouse[1], 400, 700, 200, 50, yellow, grey, 30):
                p2score, l, s, six = turn(p2score, l, s)
                xcy, ycy = goti(p2score)
                if not six:
                    current_player = 3 if b > 2 else 1
                if p2score == 100:
                    break

        elif current_player == 3:
            if button1("Player 3", mouse[0], mouse[1], 700, 700, 200, 50, green, grey, 30):
                p3score, l, s, six = turn(p3score, l, s)
                xcg, ycg = goti(p3score)
                if not six:
                    current_player = 4 if b > 3 else 1
                if p3score == 100:
                    break

        elif current_player == 4:
            if button1("Player 4", mouse[0], mouse[1], 1000, 700, 200, 50, blue, grey, 30):
                p4score, l, s, six = turn(p4score, l, s)
                xcb, ycb = goti(p4score)
                if not six:
                    current_player = 1
                if p4score == 100:
                    break

        b6 = button("Back", mouse[0], mouse[1], 0, 0, 200, 50, red, b_red, 30, 7)
        GD.blit(redgoti, (xcr, ycr))
        if 5 > b > 1 or b == 21:
            GD.blit(yellowgoti, (xcy + 2, ycy))
        if 5 > b > 2:
            GD.blit(greengoti, (xcg + 4, ycg))
        if 5 > b > 3:
            GD.blit(bluegoti, (xcb + 6, ycb))

        if l:
            time = pygame.time.get_ticks()
            while pygame.time.get_ticks() - time < 2000:
                message_display1("There's a Ladder!", 650, 50, 35, white)
                pygame.display.update()
        if s:
            time = pygame.time.get_ticks()
            while pygame.time.get_ticks() - time < 2000:
                message_display1("There's a Snake!", 650, 50, 35, white)
                pygame.display.update()

        clock.tick(7)
        pygame.display.update()


intro()
main()
