import pygame;import random

pygame.init()

black=(000,000,51)
size=[800,900]
screen=pygame.display.set_mode(size)

done=False
clock=pygame.time.Clock()

car=pygame.image.load('images/자동차.png')
car=pygame.transform.scale(car,(200,200))
xcar=pygame.image.load('images/역주행 자동차.png')
xcar=pygame.transform.scale(xcar,(200,200))
xcars=[]

def rungame():
    global done, car
    x=100
    y=700


for xcar in xcars:
    xcar['rect'].top += xcar['dy']
    if xcar['rect'].top > size[1]:
        xcars.remove(xcar)
        rect = pygame.Rect(xcar.get_rect())
        rect.left = random.randint(0, size[0])
        rect.top = -100
        dy = random.randint(3, 9)
        xcars.append({'rect': rect, 'dy': dy})


for xcar in xcars:
    if xcar['rect'].colliderect(car):
        done = True
    screen.blit(xcar, xcar['rect'])

    while not done:
        clock.tick(10)
        screen.fill(black)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x-=70
            elif event.key==pygame.K_RIGHT:
                x+=70





        screen.blit(car,(x,y))

           





        pygame.display.update()

rungame()


pygame.quit()
