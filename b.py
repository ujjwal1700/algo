import pygame
import time
import random
pygame.font.init()


win=pygame.display.set_mode((1300,600))
fps=10
clock=pygame.time.Clock()

def draw_win(arr):

    i=100
    b=[]
    win.fill((255,255,255))
    for a in arr:
            i+=15
            pygame.draw.rect(win,(0,0,0),(i,10,10,20*a))
    pygame.display.update()

def main():


    txt="Press A for small set"
    txt1="Press B for medium set"
    txt2="Press L for large set"

    font=pygame.font.SysFont(None,25)
    screen_text=font.render(txt,True,(0,0,0))
    font=pygame.font.SysFont(None,25)
    screen_text1=font.render(txt1,True,(0,0,0))
    font=pygame.font.SysFont(None,25)
    screen_text2=font.render(txt2,True,(0,0,0))


    arr=[0]
    global l
    l=len(arr)

    m=0
    run = True
    f=100
    while run:

        clock.tick(fps)
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                run=False
                pygame.quit()
            if event.type== pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    arr=[0]
                    for i in range(20):
                        arr.append(random.randint(1,25))
                    l=len(arr)
                if event.key==pygame.K_b:
                    arr=[0]
                    for i in range(40):
                        arr.append(random.randint(1,25))
                    l=len(arr)
                if event.key==pygame.K_l:
                    arr=[0]
                    for i in range(65):
                        arr.append(random.randint(1,25))
                    l=len(arr)



        for j in range(l-1-m):
            f=100
            for i in range(l-1):
                draw_win(arr)
                time.sleep(0.01)
                if arr[i]>arr[i+1]:
                    win.fill((255,255,255))
                    draw_win(arr)
                    pygame.draw.rect(win,(255,0,0),(f+15,10,10,20*arr[i]))
                    pygame.display.update()
                    time.sleep(0.01)
                    d=arr[i]
                    c=arr[i+1]
                    arr[i+1]=arr[i]
                    arr[i]=c
                    win.fill((255,255,255))
                    draw_win(arr)
                    pygame.draw.rect(win,(255,0,0),(f+30,10,10,20*d))
                    pygame.display.update()
                    time.sleep(0.01)
                f+=15
            m+=1

        win.fill((255,255,255))
        win.blit(screen_text,[500,40])
        win.blit(screen_text1,[500,80])
        win.blit(screen_text2,[500,120])
        pygame.display.update()



if __name__ == '__main__':
    main()
