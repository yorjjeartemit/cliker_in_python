import pygame
import time

pygame.init()

BLACK = (0, 0, 0)
WHITE = (250, 250, 250)
backs = (600, 444)

pygame.display.set_caption("cliker 2D")
background_image = pygame.image.load("C:\\Users\\User\\f9b129db1bed0649f9be3639f6e79fb7.jpg")
mw = pygame.display.set_mode(backs)
background_image = pygame.transform.scale(background_image, backs)
clock = pygame.time.Clock()
FPS = 120

class Area:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def fill(self):
        pass  

class Label(Area):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.font = None
        self.image = None
    def set_text(self, text, font_size=25, font_style=None, text_color=BLACK):
        if font_style is None:
            self.font = pygame.font.SysFont(None, font_size)
        else:
            self.font = pygame.font.SysFont(font_style, font_size)
        self.image = self.font.render(text, True, text_color)

    def draw(self, shift_x, shift_y, border_color=BLACK, border_width=1, border_sors=2):
        pygame.draw.rect(mw, border_color, self.rect, border_width, border_sors)
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
dsd7_cost = 150
click = 1
money = round(0)
current_level = 0
cost_rebith = 1000
level_rebith = 0
dsd6_cost = 500
rebith_level=0
dsd1_cost = 40
dsd2_cost = 100
auto_click = False
auto_click_delay = 2.0 
last_click_time = time.time()
bonus_claimed = False
running = True
max_limit_work=False
max_limit_dsd1_cost=25

main_dsd = Label(0, 120, 230, 240)

level_text = Label(0, 0, 230, 60)
level_text.set_text('Level: ' + str(current_level), 30, None, BLACK)

price_dsd5 = Label(240, 240, 315, 40)
price_dsd5.set_text('reset money', 30, None, WHITE)

price_dsd1 = Label(240, 120, 315, 40)
price_dsd1.set_text(f'click+1= {dsd1_cost}', 30, None, WHITE)

price_dsd2 = Label(240, 160, 315, 40)
price_dsd2.set_text('auto clicker-100', 30, None, WHITE)

price_dsd4 = Label(240, 200, 315, 40)
price_dsd4.set_text('bonus +50 money', 30, None, WHITE)

price_dsd6 = Label(240, 280, 315, 40)
price_dsd6.set_text(f'auto click acceleration: {dsd6_cost}', 30, None, WHITE)

money_text = Label(0, 60, 230, 40)
money_text.set_text('0-money', 30, None, BLACK)

rebith = Label(230, 60, 230, 40)
rebith.set_text('rebirth: ' + str(cost_rebith), 30, None, BLACK)

close = Label(170, 370, 215, 40)
close.set_text('close', 30, None, WHITE)

price_dsd7 = Label(240,320, 315, 40)
price_dsd7.set_text(f'-1% from everything={dsd7_cost}',30,None,WHITE)

level_rebith = Label(230, 0, 230, 60)
level_rebith.set_text('rebirth: ' + str(rebith_level), 30, None, BLACK)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            if close.collidepoint(x, y):
                running = False
            if main_dsd.collidepoint(x, y):
                money += click
                money_text.set_text(str(money), 30, None, BLACK)

            if price_dsd1.collidepoint(x, y):
                if money >= dsd1_cost:
                    money -= dsd1_cost
                    current_level += 1
                    dsd1_cost = round(dsd1_cost * 1.50) if current_level % 10 == 0 else round(dsd1_cost + 40)
                    price_dsd1.set_text(f'click+1= {dsd1_cost}', 30, None, WHITE)
                    click += 1
                    
                    money = round(money)
                    money_text.set_text(str(money), 30, None, BLACK)
                    level_text.set_text('Level: ' + str(current_level), 30, None, BLACK)

                            
            if price_dsd2.collidepoint(x, y):
                if not auto_click and money >= dsd2_cost:
                    money -= dsd2_cost
                    auto_click = True
                    price_dsd2.set_text("autoclicker is activated", 30, None, (2, 250, 2))
                    money_text.set_text(str(money), 30, None, BLACK)

            if price_dsd6.collidepoint(x, y):
                if money >= dsd6_cost:
                    money -= dsd6_cost
                    auto_click_delay = max(0.1, auto_click_delay - 0.2)
                    dsd6_cost += 500
                    price_dsd6.set_text('auto click acceleration:' + f" {dsd6_cost}", 30, None, WHITE)

            if price_dsd4.collidepoint(x, y):
                if not bonus_claimed:
                    money += 50
                    bonus_claimed = True
                    price_dsd4.set_text("bonus action", 30, None, (2, 250, 2))

            if price_dsd5.collidepoint(x, y):
                money = 0
                money_text.set_text(str(money), 30, None, BLACK)
            if price_dsd7.collidepoint(x, y):
                if money >= dsd7_cost:
                    money -= dsd7_cost
                    dsd1_cost = round(dsd1_cost - dsd1_cost * 0.01, 2)

                    dsd7_cost += 20

                    price_dsd7.set_text(f"-1% from everything = {dsd7_cost}", 30, None, WHITE)

                    money_text.set_text(str(money), 30, None, BLACK)
                    price_dsd1.set_text(f'click+1= {dsd1_cost}', 30, None, WHITE)
            if rebith.collidepoint(x, y):
                if money >= cost_rebith:
                    money -= cost_rebith
                    current_level = 0
                    level_text.set_text('Level: ' + str(current_level), 30, None, BLACK)
                    rebith_level += 1
                    level_rebith.set_text("Rebirth Level: " + str(rebith_level), 30, None, BLACK)
                    
                    click = 1
                    money = 0
                    cost_rebith += 1000
                    rebith.set_text('rebith: ' + str(cost_rebith), 30, None, BLACK)
                    money_text.set_text(str(money), 30, None, BLACK)

                    dsd1_cost = 40
                    price_dsd1.set_text(f'click+1= {dsd1_cost}', 30, None, WHITE)

                    bonus_claimed = False
                    price_dsd4.set_text('bonus +50 money', 30, None, WHITE)

                    auto_click = False  
                    auto_click_delay = 2.0  
                    price_dsd2.set_text("auto click-100", 30, None, WHITE)  
            
    if auto_click and time.time() - last_click_time >= auto_click_delay:
        money += click
        money_text.set_text(str(money), 30, None, BLACK)
        last_click_time = time.time()

    mw.blit(background_image, (0, 0))
    main_dsd.fill()
    price_dsd1.draw(5, 10)
    price_dsd2.draw(5, 10)
    price_dsd4.draw(5, 10)
    price_dsd5.draw(5, 10)
    money_text.draw(5, 10)
    price_dsd6.draw(5, 10)
    level_text.draw(5, 10)
    price_dsd7.draw(5, 10)
    level_rebith.draw(5, 10)
    rebith.draw(5, 10)
    close.draw(5, 10)
    pygame.draw.rect(mw, BLACK, main_dsd.rect, 2)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
