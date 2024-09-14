import pygame
import time

pygame.init()

BLACK = (0, 0, 0)
WHITE = (250, 250, 250)
backs = (700, 500)  # Розмір вікна (ширина, висота)
g = 0
dsd_color = (250, 1, 1)
text1 = '+2$ за клік-40... '
text2 = 'авто клік-100 '
text3 = 'Бонус +50 балів'
text4 = 'ускорення кликера 500-1000..'
text5 = '   start'
text6 = 'обнулити гроші'
text_the_money='-money'
mw = pygame.display.set_mode(backs)
back = (2, 250, 2)
mw.fill(back)

clock = pygame.time.Clock()
FPS = 60

pygame.display.update()
clock.tick(FPS)


class Area:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def fill(self):
        pygame.draw.rect(mw, self.color, self.rect)


class Label(Area):
    def set_text(self, text, font_size=25, font_style=None, text_color=BLACK):
        if font_style is None:
            self.font = pygame.font.SysFont(None, font_size)
        else:
            self.font = pygame.font.SysFont(font_style, font_size)
        self.image = self.font.render(text, True, text_color)

    def draw(self, shift_x, shift_y):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))



click = 1  # Початкове значення грошей за клік
money = 0
current_level = 0  # Початковий рівень
RED = (255, 0, 0)
GREEN = (0, 255, 51)
BLUE = (0, 0, 255)
ORANGE = (255, 123, 0)
YELLOW = (255, 255, 0)
LIGHT_GREEN = (200, 255, 200)
LIGHT_RED = (250, 128, 114)
DARK_BLUE = (0, 0, 100)
LIGHT_BLUE = (80, 80, 255)

main_dsd = Area(50, 100, 150, 150, dsd_color)
main_dsd.fill()

level_text = Label(0, 0, 230, 60, back)
level_text.set_text('Level: ' + str(current_level), 30, None, BLACK)
level_text.draw(5, 10)

price_dsd5 = Label(270, 230, 215, 40, ORANGE)
price_dsd5.set_text(text6, 25, None, WHITE)
price_dsd5.draw(5, 10)

price_dsd1 = Label(270, 50, 215, 40, ORANGE)
price_dsd1.set_text(text1, 25, None, WHITE)
price_dsd1.draw(5, 10)

price_dsd2 = Label(270, 110, 215, 40, ORANGE)
price_dsd2.set_text(text2, 25, None, WHITE)
price_dsd2.draw(5, 10)

price_dsd3 = Label(50, 140, 120, 40, dsd_color)
price_dsd3.set_text(text5, 50, None, WHITE)
price_dsd3.draw(5, 10)

price_dsd4 = Label(270, 170, 215, 40, ORANGE)
price_dsd4.set_text(text3, 25, None, WHITE)
price_dsd4.draw(5, 10)

price_dsd6 = Label(10, 300, 250, 40, ORANGE)
price_dsd6.set_text(text4, 25, None, WHITE)   
price_dsd6.draw(5, 10)

money_text = Label(10 ,50,250,40, back)
money_text.set_text('0-money', 30, None, BLACK)
money_text.draw(5, 10)

click_times = 0
dsd1_cost = 40  # Вартість першого оновлення
dsd2_cost = 100  # Вартість автоматичного кліку
dsd3_cost = 0
dsd6_cost = 500
click_counter = 0
click_bonus = 0
auto_click = False
last_click_time = time.time()
level_click = 0
bonus_claimed = False  # Додаємо змінну для відстеження бонусу
bonus_cliker=False
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            if main_dsd.collidepoint(x, y):
                money += click  # Додаємо гроші за клік
                money_text.set_text(str(money), 30, None, BLACK)
            if price_dsd1.collidepoint(x, y):
                if money >= dsd1_cost:  
                    money -= dsd1_cost
                    current_level += 1  
                    if current_level % 10 == 0:  
                        dsd1_cost = int(dsd1_cost * 1.25)  
                    else:
                        dsd1_cost += 40  
                    price_dsd1.set_text(text1 + f'Cost: {dsd1_cost}', 25, None, WHITE)  
                    price_dsd1.draw(5, 10)
                    click += 1  
                    money_text.set_text(str(money), 30, None, BLACK)  # Оновлення грошей
                    money_text.draw(5, 10)  # Оновлення грошей
                    level_text.set_text('Level: ' + str(current_level), 30, None, BLACK)  
                    level_text.draw(5, 10)
                    
            if money==0:
                money_text.draw(5,10)
            if price_dsd2.collidepoint(x, y):
                if not bonus_cliker:  # Перевірка чи бонус ще не отриманий
                    if money >= dsd2_cost:  # Перевірка достатньо грошей для автокліку
                        money -= dsd2_cost
                        auto_click = True
                        bonus_cliker = True
                        last_click_time = time.time()  # Початковий час для автокліку
                        
                        price_dsd2 = Label(270, 170, 215, 40, back)
                        price_dsd2.set_text(text3, 25, None, back)
                        money_text.set_text(str(money), 30, None, BLACK)
            if auto_click and time.time() - last_click_time >= 1:  # Кожну секунду додаємо гроші
                money += click
                money_text.set_text(str(money), 30, None, BLACK)
                last_click_time = time.time()  # Оновлюємо час для наступного кліку

            if price_dsd6.collidepoint(x, y):
                if money >= dsd6_cost:
                    money -= dsd6_cost
                    last_click_time -= 0.5
                    dsd6_cost += 500
                    money_text.set_text(str(money), 30, None, BLACK)
            if price_dsd4.collidepoint(x, y):
                if not bonus_claimed:  # Перевірка чи бонус ще не отриманий
                    money += 50
                    bonus_claimed = True
                    money_text.set_text(str(money), 30, None, BLACK)
                    price_dsd4 = Label(270, 170, 215, 40, back)
                    price_dsd4.set_text(text3, 25, None, back)
            if price_dsd5.collidepoint(x, y):
                if money >= 0:
                    money = 0
                    money_text.set_text(str(money), 30, None, BLACK)

    mw.fill(back)  # Очищення екрану перед малюванням нових елементів
    main_dsd.fill()
    price_dsd1.draw(5, 10)
    price_dsd2.draw(5, 10)
    price_dsd3.draw(5, 10)
    price_dsd4.draw(5, 10)
    price_dsd5.draw(5, 10)
    money_text.draw(5, 10)
    price_dsd6.draw(5, 10)
    level_text.draw(5, 10)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()

