from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Catch-up')
background = transform.scale(image.load('background.png'), (700, 500))

x1 = 650
y1 = 0
x2 = 10
y2 = 450

sprite1 = transform.scale(image.load('sprite1.png'), (50, 50))
sprite2 = transform.scale(image.load('sprite2.png'), (50, 50))


def checks(x1, x2, y1, y2):
    if y2 <= y1 <= y2 + 50 and x2 <= x1 <= x2 + 50:
        return True
    if y2 <= y1 <= y2 + 50 and x1 <= x2 + 50 <= x1 + 50:
        return True
    if y2 <= y1 + 50 <= y2 + 50 and x1 <= x2 <= x1 + 50:
        return True
    if y2 <= y1 + 50 <= y2 + 50 and x1 <= x2 + 50 <= x1 + 50:
        return True
    return False


game = True
state = True
clock = time.Clock()
FPS = 60
timer = 0

while game:
    window.blit(background, (0, 0))
    if state:
        window.blit(sprite1, (x1, y1))
        window.blit(sprite2, (x2, y2))
        keys_pressed = key.get_pressed()

        if checks(x1, x2, y1, y2):
            state = False

        if keys_pressed[K_LEFT] and x1 > 0:
            x1 -= 10
        if keys_pressed[K_a] and x2 > 0:
            x2 -= 10
        if keys_pressed[K_RIGHT] and x1 < 650:
            x1 += 10
        if keys_pressed[K_d] and x2 < 650:
            x2 += 10
        if keys_pressed[K_UP] and y1 > 0:
            y1 -= 10
        if keys_pressed[K_w] and y2 > 0:
            y2 -= 10
        if keys_pressed[K_DOWN] and y1 < 450:
            y1 += 10
        if keys_pressed[K_s] and y2 < 450:
            y2 += 10
    else:
        if timer == 60:
            state = True
            x1 = 650
            y1 = 0
            x2 = 10
            y2 = 450
            timer = 0
        timer += 1

    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(FPS)

    display.update()