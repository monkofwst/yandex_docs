# ->#

import pygame

if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    size = width, height = 800, 600
    # screen — холст, на котором нужно рисовать:
    screen = pygame.display.set_mode(size)
    # формирование кадра:
    # команды рисования на холсте
    # ...
    # ...
    # смена (отрисовка) кадра:
    pygame.display.flip()
    # ожидание закрытия окна:
    while pygame.event.wait().type != pygame.QUIT:
        pass
    # завершение работы:
    pygame.quit()


# ->#

def draw(screen):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("Hello, Pygame!", True, (100, 255, 100))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10,
                                           text_w + 20, text_h + 20), 1)


# ->#


'''
Рисование
Конечно, при оценке игры в первую очередь смотрят на ее графику.
 Обычно в играх используют готовые изображения, которые загружаются из дополнительных файлов. 
 Но на этом занятии мы принципиально не будем использовать изображения. Наша основная задача
  «привыкнуть» к экранным координатам и изучить возможности модуля
   
   !!!draw.
   
   
   https://www.pygame.org/docs/ref/draw.html#comment_pygame_draw_rect
  
  
  '''


# ->#


def draw_square(screen):
    color = pygame.Color(50, 150, 50)
    # рисуем "тень"
    pygame.draw.rect(screen, color,
                     (20, 20, 100, 100), 0)
    hsv = color.hsva
    # увеличиваем параметр Value, который влияет на яркость
    color.hsva = (hsv[0], hsv[1], hsv[2] + 30, hsv[3])
    # рисуем сам объект
    pygame.draw.rect(screen, color, (10, 10, 100, 100), 0)


# нарисуем красный квадрат
pygame.draw.rect(screen, (255, 0, 0), (10, 10, 100, 100), 0)

# ->#


screen.fill((0, 255, 0))
screen.fill(pygame.Color('red'), pygame.Rect(10, 10, 60, 60))

# ->#

screen.fill(pygame.Color('red'), (10, 10, 60, 60))

# ->#
for i in range(10000):
    screen.fill(pygame.Color('white'),
                (random.random() * width,
                 random.random() * height, 1, 1))

# ->#

line(Surface, color, start_pos, end_pos, width=1)

# ->#

'''прямоугольник быстрее рисовать методом 
 !!!fill()
 https://www.pygame.org/docs/ref/surface.html#pygame.Surface.fill
  
  
  холста. Вт
'''

# ->#


'''

Разберитесь по 
!!!документации
 https://www.pygame.org/docs/ref/draw.html
 
 с функциями рисования окружности, эллипса и дуг самостоятельно.
'''
