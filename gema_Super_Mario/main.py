import pygame

pygame.init()

# رنگ ها 
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# کارکتر 
image = pygame.image.load('12345.png')

width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("    game Super Mario    ")  

running = True

# موقعیت کارکتر و فیزیک پرش (مقادیر سوپر ماریو)
K_X = 400
K_Y = 500
velocity_y = 0  # سرعت عمودی
gravity = 0.2  
jump_strength = -8  
is_jumping = False
ground_level = 291  # سطح زمین

clock = pygame.time.Clock()  

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()

    # حرکت افقی
    if keys[pygame.K_RIGHT]:
        K_X += 3  
    elif keys[pygame.K_LEFT]:
        K_X -= 3  
    
    # پرش با کلید بالا
    if keys[pygame.K_UP] and not is_jumping:
        velocity_y = jump_strength  
        is_jumping = True
        print("پرش!")
    
    # اعمال گرانش و حرکت عمودی
    K_Y += velocity_y
    velocity_y += gravity
    
    # بررسی برخورد با زمین
    if K_Y >= ground_level:
        K_Y = ground_level
        velocity_y = 0
        is_jumping = False
    
    # محدودیت حرکت افقی
    K_X = max(0, min(K_X, 550))
    
    # موقعیت فعلی
    positions = (K_X, int(K_Y))
    
    # رسم
    screen.fill((250, 250, 250))
    pygame.draw.rect(screen, GREEN, (0, 390, 640, 150))  # زمین
    screen.blit(image, positions)
    
    pygame.display.flip()
    clock.tick(60)  

pygame.quit()