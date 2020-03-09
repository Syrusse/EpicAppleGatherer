import pygame, os, sys, time
from os import path
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

screen_menu = pygame.display.set_mode((1024,576))
temps_daffichage_image_gif = 0.1
dossier_son_musique = path.join(path.dirname(__file__), "son et musique")
dossier_police = path.join(path.dirname(__file__), "police")
police_a_utiliser_pour_le_menu = (path.join(dossier_police, 'Pixel.ttf'))
pygame.mixer.music.load(path.join(dossier_son_musique, 'lol.mp3'))
pygame.mixer.music.play()
police_decriture_menu = pygame.font.Font(police_a_utiliser_pour_le_menu, 40)
police_decriture_menu2 = pygame.font.Font(police_a_utiliser_pour_le_menu, 28)

#Ces rectangles la sont invisible, ils servent d'hitbox
rectangle_solo =  pygame.draw.rect(screen_menu, (0, 0, 0, 0),(250, 40, 600, 70)) #Couleur, position X, position Y, largeur, hauteur
rectangle_multi = pygame.draw.rect(screen_menu, (0, 0, 0, 0),(450, 190, 600, 70))
rectangle_instruction = pygame.draw.rect(screen_menu, (0, 0, 0, 0),(50, 490, 400, 70))
pygame.display.update()


#Variable poubelle qu'il faut définir une fois
numero_image_menu = 1
image_de_fond_menu = '1.gif'
dossier_fond_menu = path.join(path.dirname(__file__), "Fond Menu")
fond_menu = pygame.image.load(path.join(dossier_fond_menu, image_de_fond_menu)).convert()
variable_poubelle_pour_le_temps = time.time()
fond_rect_menu = fond_menu.get_rect()
valeur_poubelle = 0
anti_spam = 0

#Variable qu'on doit définir avant la boucle :
texte_1 = "Jouer tout seul ? :("
texte_2 = " Jouer à deux ? :^)"
texte_3 = "Instruction !"
texte_instruction1 = ''
texte_instruction1bis = ''
texte_instruction2 = ''
texte_instruction2bis = ''
regle1 = ''
regle2 = ''
regle3 = ''

while True:
    position_souris = pygame.mouse.get_pos()

    if valeur_poubelle == 2:
        valeur_poubelle = 0
        texte_1 = "Jouer tout seul ? :("
        texte_2 = " Jouer à deux ? :^)"
        texte_3 = " Instruction !"
        rectangle_solo =  pygame.draw.rect(screen_menu, (0, 0, 0, 0),(250, 40, 600, 70))
        rectangle_multi = pygame.draw.rect(screen_menu, (0, 0, 0, 0),(450, 190, 600, 70))
        texte_instruction1 = ''
        texte_instruction1bis = ''
        texte_instruction2 = ''
        texte_instruction2bis = ''
        regle1 = ''
        regle2 = ''
        regle3 = ''
           
    
    if numero_image_menu == 128:
        numero_image_menu = 1
        image_de_fond_menu = '1.gif'
        
    if (image_de_fond_menu) == (str(numero_image_menu) + '.gif'):
        if variable_poubelle_pour_le_temps < time.time():
            image_de_fond_menu = (str(numero_image_menu+1) + '.gif')
            numero_image_menu += 1
            variable_poubelle_pour_le_temps = time.time() + temps_daffichage_image_gif            
    fond_menu = pygame.image.load(path.join(dossier_fond_menu, image_de_fond_menu)).convert()
    screen_menu.blit(fond_menu, fond_rect_menu)

    texte_menu = police_decriture_menu.render(texte_1, True, (50,50,50))
    texte_menu2 = police_decriture_menu.render(texte_2, True, (128,128,255))
    texte_menu3 = police_decriture_menu.render(texte_3, True, (255,128,255))
#Au vu de comment vous vous battez les couilles de ce projet, j'en ai ras le cul de rendre le code lisible en me cassant le cul à écrire des variables
#Démerdez-vous
    f = police_decriture_menu2.render(texte_instruction1, True, (49, 140, 231))
    v = police_decriture_menu2.render(texte_instruction1bis, True, (49, 140, 231))
    c = police_decriture_menu2.render(texte_instruction2, True, (108, 2, 119))
    k = police_decriture_menu2.render(texte_instruction2bis, True, (108, 2, 119))
    y = police_decriture_menu2.render(regle1, True, (223, 109, 20))
    o = police_decriture_menu2.render(regle2, True, (223, 109, 20))
    u = police_decriture_menu2.render(regle3, True, (223, 109, 20))
    
    screen_menu.blit(f, (10,10))
    screen_menu.blit(v, (470,60))
    screen_menu.blit(c, (10,160))
    screen_menu.blit(k, (400,210))
    screen_menu.blit(y, (10,330))
    screen_menu.blit(o, (10,380))
    screen_menu.blit(u, (10,430)) 
    screen_menu.blit(texte_menu, (250,50))
    screen_menu.blit(texte_menu2, (450,200))
    screen_menu.blit(texte_menu3, (50,500))


#Traduction : Si le rectangle invisible se situant la ou il y'a ecrit jouer en solo entre en collision avec la position de la sours ET QUE la sourisclic sur le clic GAUCHE (GAUCHE UNIQUEMENT SI JE VOULAIS METTRE LA MOLETTE ET LE CLIC DROIT IL AURAIT FALLU TRANSFORMER LES 0 EN 1) alors fait ca: 
    if rectangle_solo.collidepoint(position_souris) and pygame.mouse.get_pressed() == (1,0,0):
        pygame.quit()
        from package.Solo import Solo
    
    if rectangle_multi.collidepoint(position_souris) and pygame.mouse.get_pressed() == (1,0,0):
        pygame.quit()
        from package.Multi import Multi
        
    if rectangle_instruction.collidepoint(position_souris) and pygame.mouse.get_pressed() == (1,0,0):
        if time.time() > anti_spam:
            texte_3 = "Retour ?"
            valeur_poubelle += 1
            anti_spam = time.time() + 0.5
            texte_1 = ''
            texte_2 = ''
            rectangle_solo = pygame.draw.rect(screen_menu, (0, 0, 0, 0),(250, 40, 0, 0))
            rectangle_multi = pygame.draw.rect(screen_menu, (0, 0, 0, 0),(250, 40, 0, 0))
            texte_instruction1 = "Joueur 1 : Utilisez les touches Q, D et Z"
            texte_instruction1bis = "pour vous déplacer :3" #\n ne fonctionne pas avec cette police, je suis pas débile merci
            texte_instruction2 = "Joueur 2 : Utilisez les flèches directionelles "
            texte_instruction2bis = "pour vous déplacer =)"
            regle1 = "Règles : Amassez simplement le plus de"
            regle2 = "comestibles provenant de la ferme et évitez" 
            regle3 = "la nourriture provenant d'ailleurs ou avariée :p"
            
        
    pygame.display.update()
    pygame.time.Clock().tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
