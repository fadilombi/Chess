from email.mime import image
import pygame
pygame.init()

WIDTH, HEIGHT = 800,800
Win = pygame.display.set_mode((WIDTH, HEIGHT))

Font = pygame.font.SysFont("Arial", 80)

piece_w = 100
piece_h = 100

wp = pygame.transform.scale(pygame.image.load("Images\wp.png"), (piece_w, piece_h))
wr = pygame.transform.scale(pygame.image.load("Images\wr.png"), (piece_w, piece_h))
wn = pygame.transform.scale(pygame.image.load("Images\wn.png"), (piece_w, piece_h))
wk = pygame.transform.scale(pygame.image.load("Images\wk.png"), (piece_w, piece_h))
wq = pygame.transform.scale(pygame.image.load("Images\wq.png"), (piece_w, piece_h))
wb = pygame.transform.scale(pygame.image.load("Images\wb.png"), (piece_w, piece_h))

bp = pygame.transform.scale(pygame.image.load(r"Images\bp.png"), (piece_w, piece_h))
br = pygame.transform.scale(pygame.image.load(r"Images\br.png"), (piece_w, piece_h))
bn = pygame.transform.scale(pygame.image.load(r"Images\bn.png"), (piece_w, piece_h))
bk = pygame.transform.scale(pygame.image.load(r"Images\bk.png"), (piece_w, piece_h))
bq = pygame.transform.scale(pygame.image.load(r"Images\bq.png"), (piece_w, piece_h))
bb = pygame.transform.scale(pygame.image.load(r"Images\bb.png"), (piece_w, piece_h))

class GridBoxes:
    def __init__(self, x, y, color, piece):
        self.x=x
        self.y=y
        self.color=color
        self.piece=piece

        self.image_rect = 0

        self.rect = pygame.Rect(self.x, self.y, 100, 100)
        

    def draw(self):
        pygame.draw.rect(Win, self.color, self.rect)

        self.image = self.piece
        if self.image:
            self.image_rect = self.image.get_rect(x=self.x, y=self.y)
        if self.image_rect:
            Win.blit(self.image, self.image_rect)

def create_box(x,y,color,Boxes):
    Box = GridBoxes(x,y,color,None)
    Boxes.append(Box)

def create_grid(Boxes, colors):
    for i in range(0, 8, 1):
        for j in range(0, 7, 2):
            create_box(j*100, i*100, colors[1], Boxes)
            create_box(j*100+100, i*100, colors[0], Boxes)
        temp = colors[0]
        colors[0] = colors[1]
        colors[1] = temp

b_order = [
    br,bn,bb,bq,bk,bb,bn,br,
    bp,bp,bp,bp,bp,bp,bp,bp
]

w_order = [
    wp,wp,wp,wp,wp,wp,wp,wp,
    wr,wn,wb,wq,wk,wb,wn,wr
]

Boxes = []

colors = [(92, 115, 130), (255, 255, 255)]

create_grid(Boxes, colors)

current_turn = 'White'
chosen_piece = 0


            
run = True
while run:
    pygame.display.update()

    mouse_coordinates = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and not chosen_piece:
            for i in Boxes:
                if mouse_coordinates[0] > i.rect.x and mouse_coordinates[0] < i.rect.x+100 and i.piece:
                    if mouse_coordinates[1] > i.rect.y and mouse_coordinates[1] < i.rect.y+100:
                        if chosen_piece:
                            chosen_piece.color = colors[Boxes.index(chosen_piece)%2-1]
                        i.color = "Blue"
                        chosen_piece = i
        elif event.type == pygame.MOUSEBUTTONDOWN and chosen_piece:
            for i in Boxes:
                if mouse_coordinates[0] > i.rect.x and mouse_coordinates[0] < i.rect.x+100:
                    if mouse_coordinates[1] > i.rect.y and mouse_coordinates[1] < i.rect.y+100:
                        i.piece = chosen_piece.piece
                        chosen_piece.color = colors[Boxes.index(chosen_piece)%2-1]
                        chosen_piece.piece = 0
                        chosen_piece = 0
                        break




    for x in range(0, len(b_order)):
        Boxes[x].piece = b_order[x]
        Boxes[x+48].piece = w_order[x]



    for one in Boxes:
        one.draw()

    print(chosen_piece)
