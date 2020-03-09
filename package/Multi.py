import os, sys, pygame, time, random, decimal
from package.Player import Player
from package.Apple import Apple
from os import path

time.sleep(1) #Pour que la fenêtre se lance

#Histoire de ne pas réécrire l'emplacement de l'image a chaque fois
#N'y prête pas attention ^^
dossier_img = path.join(path.dirname(__file__), 'image')
dossier_police = path.join(path.dirname(__file__), "police")
dossier_son_musique = path.join(path.dirname(__file__), "son et musique")
dossier_fond = path.join(path.dirname(__file__), "Fond")
dossier_fond_final = path.join(path.dirname(__file__), "Fond Final")
#Taille de la fenêtre en pixel/Nom du jeu
screen = pygame.display.set_mode((1221,660))
pygame.display.set_caption('                                                                                                                                                                          Epic Apple Gatherer')

#Temps de jeu en seconde
temps_de_jeu = 60
#Position de spawns des joueurs en pixels
joueur1_spawn_x = 407
joueur1_spawn_y = 200
joueur2_spawn_x = 814
joueur2_spawn_y = 200

#Les images, les polices, et du son
police_a_utiliser_pour_les_scores = (path.join(dossier_police, 'Minecraft.ttf'))
police_a_utiliser_pour_le_temps_restant = (path.join(dossier_police, 'hachicro.TTF'))
police_a_utiliser_pour_laffichage_final = (path.join(dossier_police, 'stocky.ttf'))
image_a_utiliser_pour_j1 =  (path.join(dossier_img, 'perso_immobile.png'))
image_a_utiliser_pour_j2 =  (path.join(dossier_img, 'perso_immobilej2.png'))
image_pomme =  (path.join(dossier_img, 'pomme.png'))
image_poisson1 = (path.join(dossier_img, 'clownfish.png'))
image_poisson2 = (path.join(dossier_img, 'raw_fish.png'))
image_pomme_enchantee = (path.join(dossier_img, 'pomme_enchantée.png'))
image_pomme_doree = (path.join(dossier_img, 'pomme_dorée.png'))
image_pomme_de_terre = (path.join(dossier_img, 'potato.png'))
image_pomme_de_terre_empoisonnee = (path.join(dossier_img, 'poisonous_potato.png'))
image_carotte_doree = (path.join(dossier_img, 'golden_carrot.png'))
son_du_saut = (path.join(dossier_son_musique, 'saut.wav'))

#Temps d'intervalle pour spawn chaque pomme en seconde
spawn_pomme_rouge = 10
spawn_poisson = 5
#En pixel par frame
vitesse_des_joueurs = 6
#Change la valeur et tu comprendras (valeur en pixels)
force_applique_lorsque_la_pomme_tombe_de_larbre = 0.5
force_applique_lorsque_le_poisson_tombe_de_larbre = 0.5
force_applique_lorsque_les_bonus_tombent_de_larbre = 0
#Si tu mets ca à 0 les pommes, les poissons et les joueurs tombent à vitesse constante
gravity_pomme = 0.1
gravity_poisson = 0.1
gravity_bonus = 0.05
gravite_des_joueurs = 0.2
#Intensité du saut
intensite_du_saut = 8
#Les probabilités que telle chose spawn, plus c'est grand, plus il y a de chance
proba_spawn_pomme_enchantee = 3
proba_spawn_pomme_doree = 10
proba_spawn_carotte_doree = 7
proba_spawn_pomme_de_terre = 15
proba_spawn_pomme_de_terre_empoisonnee = 30

#Rien d'interéssant ici, juste des scores qu'il faut définir:
score_joueur1 = 0
score_joueur2 = 0
couleur_du_texte_des_scores = (255, 255, 255)
couleur_du_texte_du_temps_restant = (255, 255, 255)
taille_du_texte = 30
taille_du_texte2 = 20
#Position des affichages de scores en pixels
emplacement_du_score_joueur1 = (10,10)
emplacement_du_score_joueur2 = (941, 10)
emplacement_du_temps_restant = (450,10)

#Score obtenu selon les objets récoltés :
score_pomme_rouge = 1
score_pomme_de_terre = 2
score_pomme_enchantee = 10
score_pomme_doree = 5
score_carotte_doree = 7
score_pomme_de_terre_empoisonnee = -5
score_poisson_clown = -3
score_poisson_cru = -4


#Definit l'image de base pour lancer le gif
image_de_fond = '1.gif'
temps_daffichage_image_gif = 0.05
variable_poubelle_pour_le_temps = time.time() + 1
numero_image = 1

#Variable qu'il faut définir u_u:
direction = 0
compteur_gauche = 0
compteur_droite = 0
directionj2 = 0
compteur_gauchej2 = 0
compteur_drotiej2 = 0

#-------------------------------------------------------------------------FIN DES REGLAGES---------------------------------------------------------------------------
#On définit les deux joueurs selon la classe (dans le fichier Player)
#et on donne les attributs
p1 = Player(joueur1_spawn_x , joueur1_spawn_y, image_a_utiliser_pour_j1)
p2 = Player(joueur2_spawn_x , joueur2_spawn_y, image_a_utiliser_pour_j2)

#Je sais, je sais, c'est moche mais j'ai pas trouvé d'autres moyens efficaces
pomme_rouge = Apple(force_applique_lorsque_la_pomme_tombe_de_larbre, image_pomme)
pomme_rouge1 = Apple(force_applique_lorsque_la_pomme_tombe_de_larbre, image_pomme)
pomme_rouge2 = Apple(force_applique_lorsque_la_pomme_tombe_de_larbre, image_pomme)
pomme_rouge3 = Apple(force_applique_lorsque_la_pomme_tombe_de_larbre, image_pomme)
pomme_rouge4 = Apple(force_applique_lorsque_la_pomme_tombe_de_larbre, image_pomme)
pomme_rouge5 = Apple(force_applique_lorsque_la_pomme_tombe_de_larbre, image_pomme)
pomme_rouge6 = Apple(force_applique_lorsque_la_pomme_tombe_de_larbre, image_pomme)
pomme_rouge7 = Apple(force_applique_lorsque_la_pomme_tombe_de_larbre, image_pomme)
pomme_rouge8 = Apple(force_applique_lorsque_la_pomme_tombe_de_larbre, image_pomme)
pomme_rouge9 = Apple(force_applique_lorsque_la_pomme_tombe_de_larbre, image_pomme)
pomme_rouge10 = Apple(force_applique_lorsque_la_pomme_tombe_de_larbre, image_pomme)
#Les poissons, avec la même méthode
poisson_clown1 = Apple(force_applique_lorsque_le_poisson_tombe_de_larbre, image_poisson1)
poisson_clown2 = Apple(force_applique_lorsque_le_poisson_tombe_de_larbre, image_poisson1)
poisson_cru1 = Apple(force_applique_lorsque_le_poisson_tombe_de_larbre, image_poisson2)
poisson_cru2 = Apple(force_applique_lorsque_le_poisson_tombe_de_larbre, image_poisson2)

#En fait à partir de la, les objets tombent selon une probabilité
#Donc on peut très bien se retrouver avec 0 bonus :p

#Les pommes et carottes spéciales (putain c'est super chiant)
pomme_enchantee = Apple(force_applique_lorsque_les_bonus_tombent_de_larbre, image_pomme_enchantee)
pomme_doree = Apple(force_applique_lorsque_les_bonus_tomimport os, sys, pygame, time, random, decimal
from package.Player import Player
from package.Apple import Apple
from os import path

time.sleep(1) #Pour que la fenêtre se lance

#Histoire de ne pas réécrire l'emplacement de l'image a chaque fois
#N'y prête pas attention ^^
dossier_img = path.join(path.dirname(__file__), 'image')
dossier_police = path.join(path.dirname(__file__), "police")
dossier_son_musique = path.join(path.dirname(__file__), "son et musique")
dossier_fond = path.join(path.dirname(__file__), "Fond")
dossier_fond_final = path.join(path.dirname(__file__), "Fond Final")
#Taille de la fenêtre en pixel/Nom du jeu
screen = pygame.display.set_mode((1221,660))
pygame.display.set_caption('                                                                                                                                                                          Epic Apple Gatherer')

#Temps de jeu en seconde
temps_de_jeu = 60
#Position de spawns des joueurs en pixels
joueur1_spawn_x = 407
joueur1_spawn_y = 200
joueur2_spawn_x = 814
joueur2_spawn_y = 200

#Les images, les polices, et du son
police_a_utiliser_pour_les_scores = (path.join(dossier_police, 'Minecraft.ttf'))
police_a_utiliser_pour_le_temps_restant = (path.join(dossier_police, 'hachicro.TTF'))
police_a_utiliser_pour_laffichage_final = (path.join(dossier_police, 'stocky.ttf'))
image_a_utiliser_pour_j1 =  (path.join(dossier_img, 'perso_immobile.png'))
image_a_utiliser_pour_j2 =  (path.join(dossier_img, 'perso_immobilej2.png'))
image_pomme =  (path.join(dossier_img, 'pomme.png'))
image_poisson1 = (path.join(dossier_img, 'clownfish.png'))
image_poisson2 = (path.join(dossier_img, 'raw_fish.png'))
image_pomme_enchantee = (path.join(dossier_img, 'pomme_enchantée.png'))
image_pomme_doree = (path.join(dossier_img, 'pomme_dorée.png'))
image_pomme_de_terre = (path.join(dossier_img, 'potato.png'))
image_pomme_de_terre_empoisonnee = (path.join(dossier_img, 'poisonous_potato.png'))
image_carotte_doree = (path.join(dossier_img, 'golden_carrot.png'))
son_du_saut = (path.join(dossier_son_musique, 'saut.wav'))

#Temps d'intervalle pour spawn chaque pomme en seconde
spawn_pomme_rouge = 10
spawn_poisson = 5
#En pixel par frame
vitesse_des_joueurs = 6
#Change la valeur et tu comprendras (valeur en pixels)
force_applique_lorsque_la_pomme_tombe_de_larbre = 0.5
force_applique_lorsque_le_poisson_tombe_de_larbre = 0.5
force_applique_lorsque_les_bonus_tombent_de_larbre = 0
#Si tu mets ca à 0 les pommes, les poissons et les joueurs tombent à vitesse constante
gravity_pomme = 0.1
gravity_poisson = 0.1
gravity_bonus = 0.05
gravite_des_joueurs = 0.2
#Intensité du saut
intensite_du_saut = 8
#Les probabilités que telle chose spawn, plus c'est grand, plus il y a de chance
proba_spawn_pomme_enchantee = 3
proba_spawn_pomme_doree = 10
proba_spawn_carotte_doree = 7
proba_spawn_pomme_de_terre = 15
proba_spawn_pomme_de_terre_empoisonnee = 30

#Rien d'interéssant ici, juste des scores qu'il faut définir:
score_joueur1 = 0
score_joueur2 = 0
couleur_du_texte_des_scores = (255, 255, 255)
couleur_du_texte_du_temps_restant = (255, 255, 255)
taille_du_texte = 30
taille_du_texte2 = 20
#Position des affichages de scores en pixels
emplacement_du_score_joueur1 = (10,10)
emplacement_du_score_joueur2 = (941, 10)
emplacement_du_temps_restant = (450,10)

#Score obtenu selon les objets récoltés :
score_pomme_rouge = 1
score_pomme_de_terre = 2
score_pomme_enchantee = 10
score_pomme_doree = 5
score_carotte_doree = 7
score_pomme_de_terre_empoisonnee = -5
score_poisson_clown = -3
score_poisson_cru = -4


#Definit l'image de base pour lancer le gif
image_de_fond = '1.gif'
temps_daffichage_image_gif = 0.05
variable_poubelle_pour_le_temps = time.time() + 1
numero_image = 1

#Variable qu'il faut définir u_u:
direction = 0
compteur_gauche = 0
compteur_droite = 0
directionj2 = 0
compteur_gauchej2 = 0
compteur_drotiej2 = 0

#-------------------------------------------------------------------------FIN DES REGLAGES---------------------------------------------------------------------------
#On définit les deux joueurs selon la classe (dans le fichier Player)
#et on donne les attributs
p1 = Player(joueur1_spawn_x , joueur1_spawn_y, image_a_utiliser_pour_j1)
p2 = Player(joueur2_spawn_x , joueur2_spawn_y, image_a_utiliser_pour_j2)

#Je sais, je sais, c'est moche mais j'ai pas trouvé d'autres moyens efficaces
pomme_rouge = Apple(force_applique_lorsque_la_pomme_tombe_de_larbre, image_pomme)
pomme_rouge1 = Apple(force_applique_lorsque_la_pomme_tombe_de_larbre, image_pomme)
pomme_rouge2 = Apple(force_applique_lorsque_la_pomme_tombe_de_larbre, image_pomme)
pomme_rouge3 = Apple(force_applique_lorsque_la_pomme_tombe_de_larbre, image_pomme)
pomme_rouge4 = Apple(force_applique_lorsque_la_pomme_tombe_de_larbre, image_pomme)
pomme_rouge5 = Apple(force_applique_lorsque_la_pomme_tombe_de_larbre, image_pomme)
pomme_rouge6 = Apple(force_applique_lorsque_la_pomme_tombe_de_larbre, image_pomme)
pomme_rouge7 = Apple(force_applique_lorsque_la_pomme_tombe_de_larbre, image_pomme)
pomme_rouge8 = Apple(force_applique_lorsque_la_pomme_tombe_de_larbre, image_pomme)
pomme_rouge9 = Apple(force_applique_lorsque_la_pomme_tombe_de_larbre, image_pomme)
pomme_rouge10 = Apple(force_applique_lorsque_la_pomme_tombe_de_larbre, image_pomme)
#Les poissons, avec la même méthode
poisson_clown1 = Apple(force_applique_lorsque_le_poisson_tombe_de_larbre, image_poisson1)
poisson_clown2 = Apple(force_applique_lorsque_le_poisson_tombe_de_larbre, image_poisson1)
poisson_cru1 = Apple(force_applique_lorsque_le_poisson_tombe_de_larbre, image_poisson2)
poisson_cru2 = Apple(force_applique_lorsque_le_poisson_tombe_de_larbre, image_poisson2)

#En fait à partir de la, les objets tombent selon une probabilité
#Donc on peut très bien se retrouver avec 0 bonus :p

#Les pommes et carottes spéciales (putain c'est super chiant)
pomme_enchantee = Apple(force_applique_lorsque_les_bonus_tombent_de_larbre, image_pomme_enchantee)
pomme_doree = Apple(force_applique_lorsque_les_bonus_tombent_de_larbre, image_pomme_doree)
carotte_doree = Apple(force_applique_lorsque_les_bonus_tombent_de_larbre, image_carotte_doree)
#D'autres malus pour diversifier lol
pomme_de_terre = Apple(force_applique_lorsque_la_pomme_tombe_de_larbre, image_pomme_de_terre)
pomme_de_terre_empoisonnee = Apple(force_applique_lorsque_la_pomme_tombe_de_larbre, image_pomme_de_terre_empoisonnee)

#On crée des groupes ou on va foutre les sprites pour
#gérer les collisions correctement
sprites_joueurs = pygame.sprite.Group()
sprites_pommes = pygame.sprite.Group()
sprites_poisson_clown = pygame.sprite.Group()
sprites_poisson_cru = pygame.sprite.Group()
sprite_pomme_enchantee = pygame.sprite.Group()
sprite_pomme_doree = pygame.sprite.Group()
sprite_carotte_doree = pygame.sprite.Group()
sprite_pomme_de_terre = pygame.sprite.Group()
sprite_pomme_de_terre_empoisonnee = pygame.sprite.Group()
sprite_joueur1 = pygame.sprite.Group()
sprite_joueur2 = pygame.sprite.Group()
#On rajoute les joueurs dans le groupe tout bêtement
sprites_joueurs.add(p1)
sprites_joueurs.add(p2)
sprite_joueur1.add(p1)
sprite_joueur2.add(p2)


#Le convert permet de bouffer beaucoup moins de performances sur l'ordi, pas primordial
#mais si on veut avoir 60 fps c'est plutot utile

clock = pygame.time.Clock()
#Le chrono se lance ici et ne se reset que quand c'est demandé, j'aime vraiment
#pas la méthode que j'utilise mais j'ai rien trouvé d'autre
t0 = time.time() + (spawn_pomme_rouge*(1/10)) -spawn_pomme_rouge
t1 = time.time() + (spawn_pomme_rouge*(2/10)) -spawn_pomme_rouge
t2 = time.time() + (spawn_pomme_rouge*(3/10)) -spawn_pomme_rouge
t3 = time.time() + (spawn_pomme_rouge*(4/10)) -spawn_pomme_rouge
t4 = time.time() + (spawn_pomme_rouge*(5/10)) -spawn_pomme_rouge
t5 = time.time() + (spawn_pomme_rouge*(6/10)) -spawn_pomme_rouge
t6 = time.time() + (spawn_pomme_rouge*(7/10)) -spawn_pomme_rouge
t7 = time.time() + (spawn_pomme_rouge*(8/10)) -spawn_pomme_rouge
t8 = time.time() + (spawn_pomme_rouge*(9/10)) -spawn_pomme_rouge
t9 = time.time() + (spawn_pomme_rouge)

poisson0 = time.time() + (spawn_poisson*(1/4))
poisson1 = time.time() + (spawn_poisson*(2/4))
poisson2 = time.time() + (spawn_poisson*(3/4))
poisson3 = time.time() + (spawn_poisson)

#------------------------------------------------------------------------FIN DE L'INITIALISATION --------------------------------------------------------------------
#On lance pygame quand même lol
pygame.init()


#Juste pour ne pas les mettres dans la boucle while, tout comme la musique
#Faut aboslument les mettres ici
police_decriture = pygame.font.Font(police_a_utiliser_pour_les_scores, taille_du_texte)
police_decriture2 = pygame.font.Font(police_a_utiliser_pour_le_temps_restant, taille_du_texte2)

#Les musiques oui c'est obligé de les mettres la, sinon ca marche pas :p

variable_musique = random.randint(1, 3)

if variable_musique == 1:
    pygame.mixer.Sound(path.join(dossier_son_musique, 'a.ogg')).play()
if variable_musique == 2:
    pygame.mixer.Sound(path.join(dossier_son_musique, 'b.ogg')).play()
if variable_musique == 3:
    pygame.mixer.Sound(path.join(dossier_son_musique, 'c.ogg')).play()


#--------------------------------------------------------------------------FIN DE LA PARTIE MUSIQUE------------------------------------------------------------------

#Un chrono qui se lance au début du jeu et qui arrête le jeu :)
temps_depart = time.time()
fin_du_jeu = temps_depart + temps_de_jeu
while time.time() < fin_du_jeu:

#Il faut comprendre que temps_de_jeu n'est pas égal à temps_de_jeu_sur_60s
#je t'invite à utiliser la fonction print pour comprendre :)
    temps_de_jeu_sur_60s = fin_du_jeu - time.time()

    if 15 > temps_de_jeu_sur_60s > 14:
        pygame.mixer.Sound(path.join(dossier_son_musique, '15s.wav')).play()


#Il faut comprendre ici que ce chrono prends un temps de référence, ici c'est le
#01/01/1970 (epoch) en gros le chrono calcule le temps passé depuis cette date
#et chaque frame il est rafraîchi, tandis que t0 qui n'est pas dans une boucle
#ne va pas être rafraîchi (logique) jusqu'à ce qu'il y ai la valeur de
#spawn_pomme_rouge soit écoulé

    temps1 = time.time()
    dt = temps1-t0
    if dt >= (spawn_pomme_rouge):
        pomme_rouge = Apple(force_applique_lorsque_la_pomme_tombe_de_larbre, image_pomme)
        sprites_pommes.add(pomme_rouge)
        t0 = temps1

    temps2 = time.time()
    dt = temps2-t1
    if dt >= (spawn_pomme_rouge):
        pomme_rouge1 = Apple(force_applique_lorsque_la_pomme_tombe_de_larbre, image_pomme)
        sprites_pommes.add(pomme_rouge1)
        t1 = temps2

    temps3 = time.time()
    dt = temps3-t2
    if dt >= (spawn_pomme_rouge):
        pomme_rouge2 = Apple(force_applique_lorsque_la_pomme_tombe_de_larbre, image_pomme)
        sprites_pommes.add(pomme_rouge2)
        t2 = temps3

    temps4 = time.time()
    dt = temps4-t3
    if dt >= (spawn_pomme_rouge):
        pomme_rouge3 = Apple(force_applique_lorsque_la_pomme_tombe_de_larbre, image_pomme)
        sprites_pommes.add(pomme_rouge3)
        t3 = temps4

    temps5 = time.time()
    dt = temps5-t4
    if dt >= (spawn_pomme_rouge):
        pomme_rouge4 = Apple(force_applique_lorsque_la_pomme_tombe_de_larbre, image_pomme)
        sprites_pommes.add(pomme_rouge4)
        t4 = temps5

    temps6 = time.time()
    dt = temps6-t5
    if dt >= (spawn_pomme_rouge):
        pomme_rouge5 = Apple(force_applique_lorsque_la_pomme_tombe_de_larbre, image_pomme)
        sprites_pommes.add(pomme_rouge5)
        t5 = temps6

    temps7 = time.time()
    dt = temps7-t6
    if dt >= (spawn_pomme_rouge):
        pomme_rouge6 = Apple(force_applique_lorsque_la_pomme_tombe_de_larbre, image_pomme)
        sprites_pommes.add(pomme_rouge6)
        t6 = temps7

    temps8 = time.time()
    dt = temps8-t7
    if dt >= (spawn_pomme_rouge):
        pomme_rouge7 = Apple(force_applique_lorsque_la_pomme_tombe_de_larbre, image_pomme)
        sprites_pommes.add(pomme_rouge7)
        t7 = temps8

    temps9 = time.time()
    dt = temps9-t8
    if dt >= (spawn_pomme_rouge):
        pomme_rouge8 = Apple(force_applique_lorsque_la_pomme_tombe_de_larbre, image_pomme)
        sprites_pommes.add(pomme_rouge8)
        t8 = temps9

    temps10 = time.time()
    dt = temps10-t9
    if dt >= (spawn_pomme_rouge):
        pomme_rouge9 = Apple(force_applique_lorsque_la_pomme_tombe_de_larbre, image_pomme)
        sprites_pommes.add(pomme_rouge9)
        t9 = temps10


#Pareil mais avec les poissons la :

    tempspoisson1 = time.time()
    dt = tempspoisson1-poisson0
    if dt >= (spawn_poisson):
        poisson_clown1 = Apple(force_applique_lorsque_le_poisson_tombe_de_larbre, image_poisson1)
        sprites_poisson_clown.add(poisson_clown1)
        poisson0 = tempspoisson1

    tempspoisson2 = time.time()
    dt = tempspoisson2-poisson1
    if dt >= (spawn_poisson):
        poisson_clown2 = Apple(force_applique_lorsque_le_poisson_tombe_de_larbre, image_poisson1)
        sprites_poisson_clown.add(poisson_clown1)
        poisson1 = tempspoisson2

    tempspoisson3 = time.time()
    dt = tempspoisson3-poisson2
    if dt >= (spawn_poisson):
        poisson_cru1 = Apple(force_applique_lorsque_le_poisson_tombe_de_larbre, image_poisson2)
        sprites_poisson_cru.add(poisson_cru1)
        poisson2 = tempspoisson3

    tempspoisson4 = time.time()
    dt = tempspoisson4-poisson3
    if dt >= (spawn_poisson):
        poisson_cru2 = Apple(force_applique_lorsque_le_poisson_tombe_de_larbre, image_poisson2)
        sprites_poisson_cru.add(poisson_cru2)
        poisson3 = tempspoisson4

#--------------------------------------------------------------------------------FIN DES SPAWNS OBLIGATOIRES----------------------------------------------------------
#Simplement une probabilité qui se répète 60* par seconde
#Une autre méthode quoi, en gros c'est pas sur de tomber
#je pense que y'a pas besoin d'explication

    chance_pomme_enchantee = random.randint(0,60000)
    if chance_pomme_enchantee < proba_spawn_pomme_enchantee:
#Sans ca y'a un bug qui fait que la pomme reste figé
#Donc la ca va chercher si il y a déjà une pomme qui est en jeu
#Si oui, alors ca va rien faire, autrement ca en spawn une
#Beau jeu ou pas ? :D
        if pygame.sprite.Sprite.alive(pomme_enchantee) == True:
            pass
        else:
             pomme_enchantee = Apple(force_applique_lorsque_les_bonus_tombent_de_larbre, image_pomme_enchantee)
             sprite_pomme_enchantee.add(pomme_enchantee)

    chance_pomme_doree = random.randint(0,6000)
    if chance_pomme_doree < proba_spawn_pomme_doree:
        if pygame.sprite.Sprite.alive(pomme_doree) == True:
            pass
        else:
            pomme_doree = Apple(force_applique_lorsque_les_bonus_tombent_de_larbre, image_pomme_doree)
            sprite_pomme_doree.add(pomme_doree)

    chance_carotte_doree = random.randint(0,6000)
    if chance_carotte_doree < proba_spawn_carotte_doree:
        if pygame.sprite.Sprite.alive(carotte_doree) == True:
            pass
        else:
            carotte_doree = Apple(force_applique_lorsque_les_bonus_tombent_de_larbre, image_carotte_doree)
            sprite_carotte_doree.add(carotte_doree)

    chance_pomme_de_terre = random.randint(0,6000)
    if chance_pomme_de_terre < proba_spawn_pomme_de_terre:
        if pygame.sprite.Sprite.alive(pomme_de_terre) == True:
            pass
        else:
            pomme_de_terre = Apple(force_applique_lorsque_la_pomme_tombe_de_larbre, image_pomme_de_terre)
            sprite_pomme_de_terre.add(pomme_de_terre)

    chance_pomme_de_terre_empoisonnee = random.randint(0,6000)
    if chance_pomme_de_terre_empoisonnee < proba_spawn_pomme_de_terre_empoisonnee:
        if pygame.sprite.Sprite.alive(pomme_de_terre_empoisonnee) == True:
            pass
        else:
            pomme_de_terre_empoisonnee = Apple(force_applique_lorsque_la_pomme_tombe_de_larbre, image_pomme_de_terre_empoisonnee)
            sprite_pomme_de_terre_empoisonnee.add(pomme_de_terre_empoisonnee)

#-------------------------------------------------------------------FIN DES SPAWNS ALEATOIRES--------------------------------------------------------------------------
#Mouvement avec les touches du clavier
    key = pygame.key.get_pressed()
    touche_appuye = 0
    touche_appuyej2 = 0


    if key[pygame.K_a]:
#Je fais bouger le rectangle p1 appartenant à la classe Player qui est
#représenté par l'image du bonhomme de la valeur de la vitesse_des_joueurs dans
#l'axe des X et de 0 par celui des Y (c'est logique on veut pas que le perso
#monte ou descende en appuyant sur la touche gauche/droite lol
        p1.rect.move_ip(-vitesse_des_joueurs , 0)
#Et voila, c'est ce qu'il fallait ajouter avant que le jeu soit parfait
#Je vais pas me casser le cul à commenter, il est une heure de la nuit et puis vous allez pas lire
#Si par miracle vous avez des questions demandait moi directement
        compteur_gauche += 1
        compteur_droite = 0
        direction = -1
        touche_appuye = 1
        if 15 > compteur_gauche > 0:
            p1.image = pygame.image.load(path.join(dossier_img, 'gauche1.png'))
        if 30 > compteur_gauche > 15:
            p1.image = pygame.image.load(path.join(dossier_img, 'gauche2.png'))
        if compteur_gauche > 30:
            compteur_gauche = 0
    if touche_appuye == 0 and direction == -1:
        p1.image = pygame.image.load(path.join(dossier_img, 'gauche0.png'))
        
    if key[pygame.K_d]:
        p1.rect.move_ip(vitesse_des_joueurs , 0)
        compteur_droite += 1
        compteur_gauche = 0
        direction = 1
        touche_appuye = 1
        if 15 > compteur_droite > 0:
            p1.image = pygame.image.load(path.join(dossier_img, 'droite1.png'))
        if 30 > compteur_droite > 15:
            p1.image = pygame.image.load(path.join(dossier_img, 'droite2.png'))
        if compteur_droite > 30:
            compteur_droite = 0
    if touche_appuye == 0 and direction == 1:
        p1.image = pygame.image.load(path.join(dossier_img, 'droite0.png'))

        
    if key[pygame.K_w]:
        p1.jump(intensite_du_saut, son_du_saut)

    if key[pygame.K_LEFT]:
        p2.rect.move_ip(-vitesse_des_joueurs , 0)
        compteur_gauchej2 += 1
        compteur_droitej2 = 0
        directionj2 = -1
        touche_appuyej2 = 1
        if 15 > compteur_gauchej2 > 0:
            p2.image = pygame.image.load(path.join(dossier_img, 'gauche1j2.png'))
        if 30 > compteur_gauchej2 > 15:
            p2.image = pygame.image.load(path.join(dossier_img, 'gauche2j2.png'))
        if compteur_gauchej2 > 30:
            compteur_gauchej2 = 0
    if touche_appuyej2 == 0 and directionj2 == -1:
        p2.image = pygame.image.load(path.join(dossier_img, 'gauche0j2.png'))
        
    if key[pygame.K_RIGHT]:
        p2.rect.move_ip(vitesse_des_joueurs , 0)
        compteur_droitej2 += 1
        compteur_gauchej2 = 0
        directionj2 = 1
        touche_appuyej2 = 1
        if 15 > compteur_droitej2 > 0:
            p2.image = pygame.image.load(path.join(dossier_img, 'droite1j2.png'))
        if 30 > compteur_droitej2 > 15:
            p2.image = pygame.image.load(path.join(dossier_img, 'droite2j2.png'))
        if compteur_droitej2 > 30:
            compteur_droitej2 = 0
    if touche_appuyej2 == 0 and directionj2 == 1:
        p2.image = pygame.image.load(path.join(dossier_img, 'droite0j2.png'))

    if key[pygame.K_UP]:
        p2.jump(intensite_du_saut, son_du_saut)

#On met à jour le groupe des sprites et leurs attributs
    sprites_joueurs.update
    sprites_pommes.update
    sprites_poisson_clown.update
    sprites_poisson_cru.update

#On utilise la fonction update() définit dans la classe Player, on la met ici
#pour s'en servir chaque frame, elle est donc appelé 60 fois chaque seconde
#De même pour les pommes jpp
    p1.update(gravite_des_joueurs)
    p2.update(gravite_des_joueurs)
    pomme_rouge.update_pomme(gravity_pomme)
    pomme_rouge1.update_pomme(gravity_pomme)
    pomme_rouge2.update_pomme(gravity_pomme)
    pomme_rouge3.update_pomme(gravity_pomme)
    pomme_rouge4.update_pomme(gravity_pomme)
    pomme_rouge5.update_pomme(gravity_pomme)
    pomme_rouge6.update_pomme(gravity_pomme)
    pomme_rouge7.update_pomme(gravity_pomme)
    pomme_rouge8.update_pomme(gravity_pomme)
    pomme_rouge9.update_pomme(gravity_pomme)
    poisson_clown1.update_pomme(gravity_poisson)
    poisson_clown2.update_pomme(gravity_poisson)
    poisson_cru1.update_pomme(gravity_poisson)
    poisson_cru2.update_pomme(gravity_poisson)
    pomme_enchantee.update_pomme(gravity_bonus)
    pomme_doree.update_pomme(gravity_bonus)
    carotte_doree.update_pomme(gravity_bonus)
    pomme_de_terre.update_pomme(gravity_pomme)
    pomme_de_terre_empoisonnee.update_pomme(gravity_pomme)
#----------------------------------------------------------------------FIN DES MISES A JOURS DES INTERACTIONS----------------------------------------------------------
#Bon c'est la ou je voulais en venir dès le début, cette ligne gère les collisions
#RIEN D'AUTRES, et par ailleurs elle supprime les sprites touché, c'est plus
#pratique Vincent, non ? xd
#Pour info, ici les joueurs ne sont plus dans le même groupe de sprites, pourquoi ?
#Parce que sinon je ne pourrais pas donner 1 point à un joueur sans en donner
#à l'autre :p
#Bref si tu piges pas demande moi xd
    if pygame.sprite.groupcollide(sprite_joueur1, sprites_pommes, False, True):
        score_joueur1 += score_pomme_rouge
        pygame.mixer.Sound(path.join(dossier_son_musique, '1.wav')).play()
    if pygame.sprite.groupcollide(sprite_joueur1, sprites_poisson_clown, False, True):
        score_joueur1 += score_poisson_clown
        pygame.mixer.Sound(path.join(dossier_son_musique, '0.wav')).play()
    if pygame.sprite.groupcollide(sprite_joueur1, sprites_poisson_cru, False, True):
        score_joueur1 += score_poisson_cru
        pygame.mixer.Sound(path.join(dossier_son_musique, '0.wav')).play()
    if pygame.sprite.groupcollide(sprite_joueur1, sprite_pomme_enchantee, False, True):
        score_joueur1 += score_pomme_enchantee
        pygame.mixer.Sound(path.join(dossier_son_musique, '5.ogg')).play()
    if pygame.sprite.groupcollide(sprite_joueur1, sprite_pomme_doree, False, True):
        score_joueur1 += score_pomme_doree
        pygame.mixer.Sound(path.join(dossier_son_musique, '3.ogg')).play()
    if pygame.sprite.groupcollide(sprite_joueur1, sprite_carotte_doree, False, True):
        score_joueur1 += score_carotte_doree
        pygame.mixer.Sound(path.join(dossier_son_musique, '4.wav')).play()
    if pygame.sprite.groupcollide(sprite_joueur1, sprite_pomme_de_terre, False, True):
        score_joueur1 += score_pomme_de_terre
        pygame.mixer.Sound(path.join(dossier_son_musique, '2.ogg')).play()
    if pygame.sprite.groupcollide(sprite_joueur1, sprite_pomme_de_terre_empoisonnee, False, True):
        score_joueur1 += score_pomme_de_terre_empoisonnee
        pygame.mixer.Sound(path.join(dossier_son_musique, '0.wav')).play()

    if pygame.sprite.groupcollide(sprite_joueur2, sprites_pommes, False, True):
        score_joueur2 += score_pomme_rouge
        pygame.mixer.Sound(path.join(dossier_son_musique, '1.wav')).play()
    if pygame.sprite.groupcollide(sprite_joueur2, sprites_poisson_clown, False, True):
        score_joueur2 += score_poisson_clown
        pygame.mixer.Sound(path.join(dossier_son_musique, '0.wav')).play()
    if pygame.sprite.groupcollide(sprite_joueur2, sprites_poisson_cru, False, True):
        score_joueur2 += score_poisson_cru
        pygame.mixer.Sound(path.join(dossier_son_musique, '0.wav')).play()
    if pygame.sprite.groupcollide(sprite_joueur2, sprite_pomme_enchantee, False, True):
        score_joueur2 += score_pomme_enchantee
        pygame.mixer.Sound(path.join(dossier_son_musique, '5.ogg')).play()
    if pygame.sprite.groupcollide(sprite_joueur2, sprite_pomme_doree, False, True):
        score_joueur2 += score_pomme_doree
        pygame.mixer.Sound(path.join(dossier_son_musique, '3.ogg')).play()
    if pygame.sprite.groupcollide(sprite_joueur2, sprite_carotte_doree, False, True):
        score_joueur2 += score_carotte_doree
        pygame.mixer.Sound(path.join(dossier_son_musique, '4.wav')).play()
    if pygame.sprite.groupcollide(sprite_joueur2, sprite_pomme_de_terre, False, True):
        score_joueur2 += score_pomme_de_terre
        pygame.mixer.Sound(path.join(dossier_son_musique, '2.ogg')).play()
    if pygame.sprite.groupcollide(sprite_joueur2, sprite_pomme_de_terre_empoisonnee, False, True):
        score_joueur2 += score_pomme_de_terre_empoisonnee
        pygame.mixer.Sound(path.join(dossier_son_musique, '0.wav')).play()
#--------------------------------------------------------------------FIN DES DETECTIONS DES COLLISION------------------------------------------------------------------

#Méthode originale pour faire fonctionner les gifs
#Vous avez pas idée à quel point j'en suis fier
    fond = pygame.image.load((path.join(dossier_fond, image_de_fond))).convert()
    fond_rect = fond.get_rect()

    if numero_image == 271:
        numero_image = 1
        image_de_fond = '1.gif'
    if(image_de_fond) == (str(numero_image) + '.gif'):
        if variable_poubelle_pour_le_temps < time.time():
            image_de_fond = (str(numero_image+1) + '.gif')
            variable_poubelle_pour_le_temps = time.time() + temps_daffichage_image_gif
            numero_image += 1

    screen.blit(fond, fond_rect)


#On dessine le groupe des sprites
    sprites_joueurs.draw(screen)
    sprites_pommes.draw(screen)
    sprites_poisson_clown.draw(screen)
    sprites_poisson_cru.draw(screen)
    sprite_pomme_enchantee.draw(screen)
    sprite_pomme_doree.draw(screen)
    sprite_carotte_doree.draw(screen)
    sprite_pomme_de_terre.draw(screen)
    sprite_pomme_de_terre_empoisonnee.draw(screen)

#Affichage des scores, je pense que c'est assez explicite comme ca

    score_a_afficher_du_joueur1 = police_decriture.render("Score joueur 1: " + str(score_joueur1) , True, couleur_du_texte_des_scores)
    screen.blit(score_a_afficher_du_joueur1, emplacement_du_score_joueur1)

    score_a_afficher_du_joueur2 = police_decriture.render("Score joueur 2: " + str(score_joueur2) , True, couleur_du_texte_des_scores)
    screen.blit(score_a_afficher_du_joueur2, emplacement_du_score_joueur2)



#Fait pas attention, c'est juste pour arrondir le temps restant

    variable_osef = decimal.Decimal(temps_de_jeu_sur_60s)
    temps_du_jeu_sur_60s_arrondi_au_centième = round(variable_osef,2)

#Affichage du temps restant
   
    temps_restant = police_decriture2.render("Temps restant: " + str(temps_du_jeu_sur_60s_arrondi_au_centième) ,True, couleur_du_texte_du_temps_restant)
    screen.blit(temps_restant, emplacement_du_temps_restant)


#En gros y'a un bug qui fait que IDLE va crash si pygame ne quitte pas avant
#la fenêtre et en gros ce code permet de forcer la fermeture de Pygame
#avant celle de la fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

#Mise à jour de l'écran, rien de particulier lol
    pygame.display.update()
    clock.tick(60)

#------------------------------------------------------------------AFFICHAGE DES SCORES-------------------------------------------------------------------------------
pygame.display.quit()

pygame.init()
screen_final = pygame.display.set_mode((768,384))
numero_image_final = 1
image_de_fond_final = '1.gif'
fond_final = pygame.image.load(path.join(dossier_fond_final, image_de_fond_final)).convert()
fond_rect_final = fond_final.get_rect()
police_decriture3 = pygame.font.Font(police_a_utiliser_pour_laffichage_final, 100)
variable_poubelle_pour_le_temps = 0 #En gros faut la définir au début, et ensuite on la définit grâce à la boucle magique, en gros plus c'est gros plus la première fois que le gif se lancera sera long, ensuite vu qu'elle est changé bah on osef de la première fois, donc même je la laisse à 0 pour lancer le gif directement
temps_daffichage_image_gif = 0.1

while True:
    if numero_image_final == 27:
        numero_image_final = 1
        image_de_fond_final = '1.gif'
    if (image_de_fond_final) == (str(numero_image_final) + '.gif'):
        if variable_poubelle_pour_le_temps < time.time():
            image_de_fond_final = (str(numero_image_final+1) + '.gif')
            variable_poubelle_pour_le_temps = time.time() + temps_daffichage_image_gif
            numero_image_final = numero_image_final + 1
    fond_final = pygame.image.load(path.join(dossier_fond_final, image_de_fond_final)).convert()
    screen_final.blit(fond_final, fond_rect_final)
    
    if score_joueur1 > score_joueur2:
        fin = police_decriture3.render("Le joueur 1 a gagné avec " + str(score_joueur1) + " points" , True, couleur_du_texte_des_scores)
        fin2 = police_decriture3.render("contre " + str(score_joueur2) + " points pour le joueur 2 " , True, couleur_du_texte_des_scores)
        fin3 = police_decriture3.render("Merci d'avoir joué" , True, couleur_du_texte_des_scores)
        screen_final.blit(fin, (50, 10))
        screen_final.blit(fin2, (80, 100))
        screen_final.blit(fin3, (220,200))
    if score_joueur1 < score_joueur2:
        fin = police_decriture3.render("Le joueur 2 a gagné avec " + str(score_joueur2) + " points" , True, couleur_du_texte_des_scores)
        fin2 = police_decriture3.render("contre " + str(score_joueur1) + " points pour le joueur 1 " , True, couleur_du_texte_des_scores)
        fin3 = police_decriture3.render("Merci d'avoir joué" , True, couleur_du_texte_des_scores)
        screen_final.blit(fin, (50,10))
        screen_final.blit(fin2, (80, 100))
        screen_final.blit(fin3, (220,200))
    if score_joueur1 == score_joueur2 :
        fin = police_decriture3.render("Egalité !", True, couleur_du_texte_des_scores)
        fin3 = police_decriture3.render("Merci d'avoir joué " , True, couleur_du_texte_des_scores)
        screen_final.blit(fin, (300,10))
        screen_final.blit(fin3, (220,100))
    
    if pygame.mixer.get_busy() == False:
        pygame.quit()


    pygame.display.update()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    

