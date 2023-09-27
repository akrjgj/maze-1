from data import *
from maze_funcion import *

window = pygame.display.set_mode((setting_win["WIDTH"], setting_win["HEIGHT"]))
pygame.display.set_caption("MAZE")

def run():
    game = True
    menu = False
    key_check = True
    level = 1

    hero = Hero(10,10, 30, 50, image= hero_list)
    bot1 = Bot(230, 10, 50, 50, image= bot1_list)
    bot2 = Bot(900, 550, 80, 100, image= bot2_list, vertical= True)
    clock = pygame.time.Clock()
    button_start = pygame.Rect(setting_win["WIDTH"] // 2 - 270, setting_win["HEIGHT"] // 2, 250, 60)
    button_end = pygame.Rect(setting_win["WIDTH"] // 2 + 20, setting_win["HEIGHT"] // 2, 250, 60)
    font_start_end = pygame.font.Font(None, 50)

    while game:
        events = pygame.event.get()
        window.fill((164, 193, 222))

        x = 920
        for i in range(hero.HP):
            window.blit(hp_image, (x, 10))
            x += 25
        if hero.HP == 0:
            menu = True
            hero.SPEED = 0


        for wall in wall_list:
            pygame.draw.rect(window, (255,255,255), wall)

        hero.move(window)

        bot1.shoot(window, hero)

        bot2.move(window, hero)


        if key_check:
            window.blit(key_image, (520, 30))

            if hero.colliderect(key_image.get_rect(topleft= (520, 30))):
                key_check = False

        else:
            window.blit(door_image, (880, 350))

            if hero.colliderect(door_image.get_rect(topleft= (80, 350))):
                level +=1
        if level == 2:
            hero.SPEED = 0
            bot1.SPEED = 0
            bot2.SPEED = 0
            render = font_start_end.render("!ТИ ПРОЙШОВ ГРУ!",True, (0,0,0))
            window.blit(render, (setting_win["WIDTH"] // 2 - 100, setting_win["HEIGHT"] // 2))
            key_check = True

        for event in events:
                if event.type == pygame.QUIT:
                    game = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        hero.MOVE["UP"] = True
                    if event.key == pygame.K_s:
                        hero.MOVE["DOWN"] = True            
                    if event.key == pygame.K_a:
                        hero.MOVE["LEFT"] = True                        
                    if event.key == pygame.K_d:
                        hero.MOVE["RIGHT"] = True                        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        hero.MOVE["UP"] = False
                    if event.key == pygame.K_s:
                        hero.MOVE["DOWN"] = False           
                    if event.key == pygame.K_a:
                        hero.MOVE["LEFT"] = False                        
                    if event.key == pygame.K_d:
                        hero.MOVE["RIGHT"] = False
        if menu:
            pygame.draw.rect(window, (103, 255, 166), button_start)
            pygame.draw.rect(window, (103, 255, 166), button_end)
            window.blit(font_start_end.render("START", True, (0, 0, 0)), (button_start.x + 65, button_start.y + 15))
            window.blit(font_start_end.render("END", True, (0, 0, 0)), (button_end.x + 85, button_end.y + 15))
            for event in events:
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            x, y = event.pos
                            if button_start.collidepoint(x, y):
                                pass
                            if button_end.collidepoint(x, y):
                                game = False
        clock.tick(60)
        pygame.display.flip()

run()