

### разновидность Pygame - arcade (special)


# ->#

import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)

    running = True
    while running:
        # внутри игрового цикла ещё один цикл
        # приема и обработки сообщений
        for event in pygame.event.get():
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False

        # отрисовка и изменение свойств объектов
        # ...

        # обновление экрана
        pygame.display.flip()
    pygame.quit()
# ->#
screen.fill((0, 0, 0))
pygame.draw.circle(screen, (255, 0, 0), (x_pos, 200), 20)
x_pos += 1
# ->#

import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Движущийся круг 2')
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)

    running = True
    x_pos = 0
    v = 20  # пикселей в секунду
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (255, 0, 0), (int(x_pos), 200), 20)
        x_pos += v * clock.tick() / 1000  # v * t в секундах
        pygame.display.flip()
    pygame.quit()

# ->#

import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Движущийся круг 2')
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)

    running = True
    x_pos = 0
    v = 20  # пикселей в секунду
    fps = 60
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (255, 0, 0), (int(x_pos), 200), 20)
        x_pos += v / fps
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()

# ->#

running = True

while running:
    # внутри игрового цикла ещё один цикл
    # приёма и обработки сообщений
    for event in pygame.event.get():
        # при закрытии окна
        if event.type == pygame.QUIT:
            running = False
        # РЕАКЦИЯ НА ОСТАЛЬНЫЕ СОБЫТИЯ
        # ...
    # отрисовка и изменение свойств объектов
    # ...
    pygame.display.flip()

# ->#

fps = 50 # количество кадров в секунду
clock = pygame.time.Clock()
running = True
while running: # главный игровой цикл
    for event in pygame.event.get():
    	if event.type == pygame.QUIT:
    		running = False
    	# обработка остальных событий
    	# ...
    # формирование кадра
    # ...
    pygame.display.flip() # смена кадра
    # изменение игрового мира
    # ...
    # временная задержка
    clock.tick(fps)

# ->#

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.circle(screen, (0, 0, 255), event.pos, 20)
    pygame.display.flip()
    clock.tick(50)
# ->#

'''Хорошо помогает разобраться с событиями пример eventlist. Его можно запустить из командной строки

python -m pygame.examples.eventlist
Или кодом (из среды программирования):

import pygame.examples.eventlist
pygame.examples.eventlist.main()
А еще лучше — узнать местоположение папки с примерами с помощью следующей мини-программы:

import pygame.examples
print(pygame.examples.__file__)
и скопировать оттуда в среду исходный код из файла eventlist.py. Тогда его можно будет изменять.'''
# ->#

MYEVENTTYPE = pygame.USEREVENT + 1

pygame.time.set_timer(MYEVENTTYPE, 10)

for event in pygame.event.get():
    if event.type == MYEVENTTYPE:
        print("Мое событие сработало")

pygame.time.set_timer(MYEVENTTYPE, 0)

# ->#

# очищаем экран один раз в самом начале
screen.fill((0, 0, 0))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.circle(screen, (0, 0, 255), event.pos, 20)

    pygame.display.flip()

# ->#

screen2 = pygame.Surface(screen.get_size())
x1, y1, w, h = 0, 0, 0, 0
drawing = False  # режим рисования выключен
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True  # включаем режим рисования
            # запоминаем координаты одного угла
            x1, y1 = event.pos
        if event.type == pygame.MOUSEBUTTONUP:
            # сохраняем нарисованное (на втором холсте)
            screen2.blit(screen, (0, 0))
            drawing = False
            x1, y1, w, h = 0, 0, 0, 0
        if event.type == pygame.MOUSEMOTION:
            # запоминаем текущие размеры
            if drawing:
                w, h = event.pos[0] - x1, event.pos[1] - y1
    # рисуем на экране сохранённое на втором холсте
    screen.fill(pygame.Color('black'))
    screen.blit(screen2, (0, 0))
    if drawing:  # и, если надо, текущий прямоугольник
        if w > 0 and h > 0:
            pygame.draw.rect(screen, (0, 0, 255), ((x1, y1), (w, h)), 5)
    pygame.display.flip()

# ->#

font = pygame.font.Font(None, 50)
text = font.render("Hello, Pygame!", 1, (100, 255, 100))
text_x = width // 2 - text.get_width() // 2
text_y = height // 2 - text.get_height() // 2
text_w = text.get_width()
text_h = text.get_height()
screen.blit(text, (text_x, text_y))

# ->#
# ->#
# ->#
