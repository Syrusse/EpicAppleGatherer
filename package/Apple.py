from package.Menu import Menu


import os, sys, pygame, random
from os import path
dossier_img = path.join(path.dirname(__file__), 'img')


class Apple(pygame.sprite.Sprite):
    def __init__(self, force_applique_lorsque_la_pomme_tombe_de_larbre, image_objets):
        pygame.sprite.Sprite.__init__(self)
        self.x = random.randint(14, 1150)
        self.y = random.randint(-70, 100)
        self.image = pygame.image.load(image_objets)
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
        self.vely = force_applique_lorsque_la_pomme_tombe_de_larbre

    def update_pomme(self, gravity_pomme):

        self.vely += gravity_pomme
        self.rect.move_ip(0, self.vely)
        if self.rect.y > 660 :
            pygame.sprite.Sprite.kill(self)
