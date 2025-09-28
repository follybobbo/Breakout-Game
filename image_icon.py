import pygame

class Image:


    def __init__(self, image_url):
        self.img = None
        self.hover_img = None
        self.url = image_url



    def create_image(self, size_1, size_2):
        img = pygame.image.load(self.url).convert_alpha()
        img = pygame.transform.scale(img, (size_1, size_2))
        self.img = img

        img_hover = pygame.image.load(self.url).convert_alpha()
        img_hover = pygame.transform.scale(img_hover, (size_1 + 10, size_2 + 10))
        self.hover_img = img_hover

        list_of_img = [img, img_hover]

        #return both normal and loaded image
        return list_of_img

    def create_rect(self, x, y):
        img_rect = self.img.get_rect(center=(x, y))
        hover_img_rect = self.hover_img.get_rect(center=(x, y))

        list_of_rect = [img_rect, hover_img_rect]
        return list_of_rect

