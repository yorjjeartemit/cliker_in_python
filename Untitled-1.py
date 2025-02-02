import cProfile

def main():
    import pygame
    import time

    pygame.init()
    backs = (600, 480)
    BLACK = (0, 0, 0)
    WHITE = (250, 250, 250)
    GRAY=(128, 128, 128)
    pygame.display.set_caption("Clicker 2D")

    cost_full_list = {
        'dsd2_cost': 100,
        'dsd6_cost': 500,
        'dsd7_cost': 150,
        'dsd1_cost': 40
    }
    def input_box(screen, font, rect, active_color, inactive_color):
        """
        Текстове поле вводу.
        Повертає введений текст після підтвердження Enter.
        """
        active = False
        nickname = ""
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None  # Вихід із програми

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Перевірка, чи натиснули на текстове поле
                    if rect.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False

                if event.type == pygame.KEYDOWN and active:
                    if event.key == pygame.K_RETURN:  # Enter підтверджує ввід
                        return nickname
                    elif event.key == pygame.K_BACKSPACE:  # Видалити символ
                        nickname = nickname[:-1]
                    else:
                        nickname += event.unicode  # Додати символ

            # Колір рамки в залежності від активності
            color = active_color if active else inactive_color

            # Малюємо текстове поле
            pygame.draw.rect(screen, color, rect, 2)

            # Відображаємо текст
            text_surface = font.render(nickname, True, (255, 255, 255))
            screen.blit(text_surface, (rect.x + 10, rect.y + 10))

            # Оновлення екрану
            pygame.display.flip()
            clock.tick(30)
    # Функція для завантаження і масштабування фону
    def load_background(image_path, size):
        background_image = pygame.image.load(image_path)
        background_image = pygame.transform.scale(background_image, size)
        return background_image
    #ще одна функція для регістера
    def Register_id():
        info_running = True

        # Шрифт та кольори
        font = pygame.font.SysFont(None, 30)
        input_rect = pygame.Rect(150, 150, 300, 50)  # Координати та розміри текстового поля
        active_color = (0, 255, 0)  # Зелений колір рамки, коли активний
        inactive_color = (255, 0, 0)  # Червоний колір рамки, коли неактивний

        while info_running:
            mw.fill(GRAY)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    info_running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    info_running = False  # Закриття вікна ESC

            # Малювання тексту "Інструкції"
            text = font.render("Instructions:", True, WHITE)
            mw.blit(text, (20, 20))

            # Малювання текстового поля для введення
            nickname = input_box(mw, font, input_rect, active_color, inactive_color)
            if nickname:  # Якщо введений нік не порожній
                print(f"Ваш нікнейм: {nickname}")
                info_running = False

            pygame.display.flip()

    #ще одна функція
    def show_info_window():
        info_running = True
        while info_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    info_running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    info_running = False  # Закриття вікна ESC
                
            # Малювання інформаційного вікнаgg
            mw.fill(GRAY)
            font = pygame.font.SysFont(None, 30)
            text = font.render("Instructions:", True, WHITE)
            instructions = [
                "1. Press 'f' for fullscreen",
                "2. Click buttons to earn points",
                "3. Upgrade features by spending points",
                "4. Press 'g' for stop music"
                "5. Press 'esc' to exit this window",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "                                   moder:artem"
            ]

            mw.blit(text, (20, 20))
            for i, line in enumerate(instructions):
                rendered_line = font.render(line, True, WHITE)
                mw.blit(rendered_line, (20, 60 + i * 30))

            pygame.display.update()
            clock.tick(FPS)
    def price_dsd1_func():
        for key in cost_full_list.keys():
            
            cost_full_list[key] = round(cost_full_list[key] * (1 - rebith_discount * rebith_level), 2)


    running = True

    click_sound = pygame.mixer.Sound("D:\\knopka-schelchok-shumnyii-blizkii-dvoinoi1.wav")
    click_sound_false=pygame.mixer.Sound("D:\\knopka-schelchok-shumnyii-blizkii-dvoinoi1.wav")
    ch=pygame.mixer.music.load("D:\\ಪೋಪೊ\\7244038022_25_tiktok.mp3")
    
    ch=pygame.mixer.music.play(-1)

    # Початковий екран
    mw = pygame.display.set_mode(backs, pygame.RESIZABLE)
    background_image = load_background("C:\\Users\\User\\f9b129db1bed0649f9be3639f6e79fb7.jpg", backs)
    clock = pygame.time.Clock()
    FPS = clock.get_fps()
    clock.tick(1000)
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

        def draw(self, shift_x, shift_y, hover_color=None, border_color=BLACK, border_width=2, border_sors=4):
            mouse_pos = pygame.mouse.get_pos()
            color = hover_color if self.rect.collidepoint(mouse_pos) and hover_color else border_color
            pygame.draw.rect(mw, color, self.rect, border_width, border_sors)
            mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
    # Початкові змінні
    dsd7_cost = 150
    click = 1
    money = round(100000)
    current_level = 0
    cost_rebith = 1000
    level_rebith = 0
    dsd6_cost = 500
    rebith_level = 0
    dsd1_cost = 40
    dsd2_cost = 100
    auto_click = False
    auto_click_delay = 0.5
    last_click_time = time.time()
    bonus_claimed = False
    running = True
    max_lvl_price1=24


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

    close = Label(240, 370, 215, 40)
    close.set_text('close', 30, None, WHITE)

    price_dsd7 = Label(240, 320, 315, 40)
    price_dsd7.set_text(f'-5% from click x2={dsd7_cost}', 30, None, WHITE)

    level_rebith = Label(230, 0, 230, 60)
    level_rebith.set_text('rebirth: ' + str(rebith_level), 30, None, BLACK)

    info = Label(15, 370, 215, 40)
    info.set_text('Info', 30, None, WHITE)

    register= Label(15,425,215,40)
    register.set_text('Register',30,None, WHITE)

    fullscreen = False
    current_level6=0
    max_lvl_price6=5
    current_level7=0
    max_lvl_price7=5
    rebith_discount = 0.10
    flPause=False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    fullscreen = not fullscreen
                    if fullscreen:
                        mw = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    else:
                        mw = pygame.display.set_mode(backs, pygame.RESIZABLE)
                    background_image = load_background("C:\\Users\\User\\f9b129db1bed0649f9be3639f6e79fb7.jpg", mw.get_size())
                if  event.type==pygame.K_g:
                    flPause = not flPause
                    if flPause:
                        ch.pygame.mixer.music.pause()
                    else:
                        ch.pygame.mixer.music.unpause()
            if event.type == pygame.VIDEORESIZE:
                new_size = event.size
                mw = pygame.display.set_mode(new_size, pygame.RESIZABLE)
                background_image = load_background("C:\\Users\\User\\f9b129db1bed0649f9be3639f6e79fb7.jpg", new_size)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos

                if close.collidepoint(x, y):
                    click_sound.play()
                    running = False

                if main_dsd.collidepoint(x, y):
                    money += click
                    money_text.set_text(str(money), 30, None, BLACK)

                if price_dsd1.collidepoint(x, y):
                    if current_level < max_lvl_price1:
                        if money >= dsd1_cost:
                            money -= dsd1_cost
                            current_level += 1
                            dsd1_cost = round(dsd1_cost * 1.25) if current_level % 10 == 0 else round(dsd1_cost + 40)
                            price_dsd1.set_text(f'click+1= {dsd1_cost}', 30, None, WHITE)
                            click += 1

                            money = round(money)
                            money_text.set_text(str(money), 30, None, BLACK)
                            level_text.set_text('Level: ' + str(current_level), 30, None, BLACK)
                            click_sound.play()
        
                        else:
                            click_sound_false.play()
                            price_dsd1.set_text(f"no money cost:{dsd1_cost}",30, None,(255,0,0))
                    else:
                        price_dsd1.set_text("Max level reached", 30, None, (0, 255, 0))
                        level_text.set_text(f"Sorry, it's full", 30, None, (0, 255, 0))
                        click_sound_false.play()
                
                if price_dsd2.collidepoint(x, y):
                    if not auto_click:
                        if money >= dsd2_cost:
                            money -= dsd2_cost
                            click_sound.play()
                            auto_click = True
                            price_dsd2.set_text("autoclicker is activated", 30, None, (2, 250, 2))
                            money_text.set_text(str(money), 30, None, BLACK)
                        else:
                            click_sound_false.play()
                            price_dsd2.set_text(f"no money cost:{dsd2_cost}",30, None,(255,0,0))
                    else:
                        click_sound_false.play()
                        price_dsd2.set_text(f"it's max lvl",30, None,(0,255,0))
                if price_dsd6.collidepoint(x, y):
                    if current_level6<max_lvl_price6:
                        if money >= dsd6_cost:
                            money -= dsd6_cost
                            auto_click_delay = max(0.1, auto_click_delay - 0.1)
                            dsd6_cost += 500
                            current_level6+=1
                            click_sound.play()
                            price_dsd6.set_text('auto click acceleration:' + f" {dsd6_cost}", 30, None, WHITE)
                        else:
                            click_sound_false.play()
                            price_dsd6.set_text(f"no money cost:{dsd6_cost}",30, None,(255,0,0))
                    else:
                        click_sound_false.play()
                        price_dsd6.set_text("it's max lvl",30, None,(0, 255,0))

                if price_dsd4.collidepoint(x, y):
                    if not bonus_claimed:
                        money += 50
                        bonus_claimed = True
                        price_dsd4.set_text("bonus action", 30, None, (2, 250, 2))
                    else:
                        click_sound_false.play()
                        price_dsd4.set_text(f"no bonus",30, None,(255,0,0))                        
                if price_dsd5.collidepoint(x, y):
                    if money>=50:
                        money = 0
                        click_sound.play()
                        money_text.set_text(str(money), 30, None, BLACK)
                    else:
                        click_sound_false.play()
                        price_dsd5.set_text(f"don't hesitate money={money}",30, None, BLACK)
                if price_dsd7.collidepoint(x, y):
                    if current_level7<max_lvl_price7:
                        if money >= dsd7_cost:
                            money -= dsd7_cost
                            dsd1_cost = round(dsd1_cost - dsd1_cost * 0.05, 2)
                            dsd7_cost += 20
                            click_sound.play()
                            current_level7+=1
                            price_dsd7.set_text(f"-5% from click x2 = {dsd7_cost}", 30, None, WHITE)
                            money_text.set_text(str(money), 30, None, BLACK)
                            price_dsd1.set_text(f'click+1= {dsd1_cost}', 30, None, WHITE)
                        else:
                            click_sound_false.play()
                            price_dsd7.set_text(f"no money cost:{dsd7_cost}",30, None,(255,0,0))
                    else:
                        price_dsd7.set_text("Max level reached", 30, None, (0, 255, 0))
                        click_sound_false.play()
                rebith_discount = 0.10
                if rebith.collidepoint(x, y):
                    if money >= cost_rebith:
                        if rebith_level<=4:
                            
                            money -= cost_rebith
                            current_level = 0
                            rebith_level += 1
                            click = rebith_level*2.5
                            max_lvl_price1+=25
                            money = round(1000000)
                            cost_rebith += 1000
                            auto_click = False
                            auto_click_delay = 2.0
                            bonus_claimed = False
                            
                            # Оновлення цін зі знижкою
                            price_dsd1_func()
                            # Оновлення змінниҗх
                            dsd1_cost = cost_full_list['dsd1_cost']
                            dsd2_cost = cost_full_list['dsd2_cost']
                            dsd6_cost = cost_full_list['dsd6_cost']
                            dsd7_cost = cost_full_list['dsd7_cost']
                            click_sound.play()

                            # Оновлення відображення
                            level_text.set_text('Level: ' + str(current_level), 30, None, BLACK)
                            level_rebith.set_text("Rebirth Level: " + str(rebith_level), 30, None, BLACK)
                            rebith.set_text('rebirth: ' + str(cost_rebith), 30, None, BLACK)
                            money_text.set_text(str(money), 30, None, BLACK)
                            price_dsd1.set_text(f'click+1= {dsd1_cost}', 30, None, WHITE)
                            price_dsd7.set_text(f"-5% from click x2 = {dsd7_cost}", 30, None, WHITE)
                            price_dsd4.set_text('bonus +50 money', 30, None, WHITE)
                            price_dsd2.set_text(f"auto clicker = {dsd2_cost}", 30, None, WHITE)
                        else:
                            click_sound_false.play()
                            rebith.set_text("it's full rebith",30, None,(255,0,0))
                    else:
                        click_sound_false.play()
                        rebith.set_text(f"no money cost:{cost_rebith}",30, None,(255,0,0))
                if info.collidepoint(x, y):
                    show_info_window()
                    info.set_text('Info', 30, None, WHITE)

                if auto_click and time.time() - last_click_time >= auto_click_delay:
                    money += click
                    money_text.set_text(str(money), 30, None, BLACK)
                    last_click_time = time.time()
                if register.collidepoint(x,y):
                    Register_id()

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
        info.draw(5, 10)
        register.draw(5, 10)
        pygame.draw.rect(mw, BLACK, main_dsd.rect, 3)

        pygame.display.update()
        clock.tick(FPS)
    
    pygame.quit()
    
cProfile.run('main()')
