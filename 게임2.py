import pygame

pygame.init()

black=(000,000,51)
size=[1600,900]
screen=pygame.display.set_mode(size)

done=False
clock=pygame.time.Clock()

car=pygame.image.load('images/그냥 네모.jpg')
car=pygame.transform.scale(car,(200,200))

def rungame():
    global done, car
    x=100
    y=100




    while not done:
        clock.tick(10)
        screen.fill(black)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True


        screen.blit(car,(x,y))

            if event.type==pygame






        pygame.display.update()

rungame()


pygame.quit()
