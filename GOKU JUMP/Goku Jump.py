import  pygame
import time
from random import*

pygame.mixer.init()
pygame.mixer.music.load('generique.ogg')
pygame.mixer.music.play(loops=50)
pygame.mixer.music.set_volume(0.65)
son = pygame.mixer.Sound("fail.wav")
bruit = pygame.mixer.Sound("pop.wav")


blue = (0,128,255)
black = (0,0,0)

pygame.init()

surfaceW = 1000
surfaceH = 800
gokuW = 184
gokuH = 156
nuageW = 360
nuageH = 190


surface = pygame.display.set_mode((surfaceW,surfaceH),pygame.RESIZABLE)
pygame.display.set_caption("Goku Jump")
clock = pygame.time.Clock()


img = pygame.image.load('Goku.png')
img_nuage01 = pygame.image.load('NuageHaut.png')
img_nuage02 = pygame.image.load('NuageBas.png')

def score(compte) :
    police = pygame.font.Font('Police.ttf', 16)
    texte = police.render("score : " + str(compte), True, black)
    surface.blit(texte, [10,0])

def nuages(x_nuage, y_nuage, espace):
    surface.blit(img_nuage01, (x_nuage, y_nuage))
    surface.blit(img_nuage02,(x_nuage,y_nuage+ nuageH +espace))


def rejoueOuQuitte():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT :
            pygame.quit()
            quit()
        elif event.type ==pygame.KEYUP:
            continue
        return event.key

    return  None

def creaTexteObjs (texte, font):
    texteSurface = font.render(texte,True,black)
    return texteSurface, texteSurface.get_rect()


def msgSurface (texte):
    GOTexte = pygame.font.Font('Police.ttf', 35)
    petitTexte = pygame.font.Font('Police.ttf',19)

    titreTexteSurf, titreTexteRect = creaTexteObjs(texte, GOTexte)
    titreTexteRect.center = surfaceW/2,((surfaceH/2)-50)
    surface.blit(titreTexteSurf, titreTexteRect)

    petitTexteSurf, petitTexteRect = creaTexteObjs\
        ("Donne de la force a Goku en appuyant sur un bouton !", petitTexte )
    petitTexteRect.center = surfaceW/2, ((surfaceH/2) +50)
    surface.blit(petitTexteSurf, petitTexteRect)

    pygame.display.update()
    time.sleep(2)

    while rejoueOuQuitte() == None :
        clock.tick()

    main()

def gameOver():
    msgSurface("Vous avez perdu votre force !")
    bruit.play()

def goku(x,y, image):
    surface.blit(image, (x,y))

def main():
    x=150
    y=200
    y_move=0

    x_nuage = surfaceW
    y_nuage = randint(-100,50)
    espace = gokuH*5
    nuage_vitesse = 4

    score_actuel = 0

    game_over = False


    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over= True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -3
            if event.type ==pygame.KEYUP :
                y_move = 3

            if event.type == pygame.KEYUP :
                bruit.play()

        y += y_move

        surface.fill(blue)
        goku(x,y,img)

        nuages(x_nuage,y_nuage, espace)

        score(score_actuel)

        x_nuage -=nuage_vitesse


        if y>surfaceH -4 or y <-1:
            gameOver()

        if x_nuage < (-1*nuageW):
            x_nuage = surfaceW
            y_nuage = randint(-100,50)

            if 3 <= score_actuel < 5:
                nuage_vitesse = 7
                espace = gokuH*2.8
            if 5 <= score_actuel < 7 :
                nuage_vitesse = 8
                espace = gokuH*2.7
            if 7 <= score_actuel < 10 :
                nuage_vitesse = 9
                espace = gokuH*2.5
            if 10 <= score_actuel <22:
                nuage_vitesse = 10
                espace = gokuH*2.2
            if 22 <= score_actuel:
                nuage_vitesse = 11
                espace = gokuH*5



        if x +gokuW > x_nuage + 40 :
            if y < y_nuage + nuageH  -50:
                if x - gokuW < x_nuage +nuageW -30 :
                    #print("touche haut!!!")
                    gameOver()

        if x +gokuW >x_nuage + 40 :
            if y +gokuH > y_nuage + nuageH + espace +50 :
                if x -gokuW < x_nuage+ nuageW - 30:
                    #print("touche bas!!!")
                    gameOver()

        if x_nuage < (x-nuageW) <x_nuage+nuage_vitesse :
            score_actuel +=1


        pygame.display.update()



main()
pygame.quit()
quit()