import pygame
import pygame_gui
import numpy as np

width, height = 960, 800

pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

manager = pygame_gui.UIManager((width, height), 'theme.json')
progress_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((width - 120, 50), (80, 40)),
    text='Next',
    manager=manager

)

birth_text_entry = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((width - 120, 150), (80, 40)),
    manager=manager
)
birth_text_entry.set_text("3")

survival_text_entry = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect((width - 120, 250), (80, 40)),
    manager=manager
)
survival_text_entry.set_text("23")

birth_label = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((width - 100, 120), (40, 40)),
    text='Birth',
    manager=manager
)

survival_label = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((width - 120, 220), (80, 40)),
    text='Survival',
    manager=manager
)

autoplay_label = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((width - 140, 320), (120, 40)),
    text='Autoplay',
    manager=manager
)

autoplay_on_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((width - 120, 350), (80, 40)),
    text='ON',
    manager=manager,
)

autoplay_off_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((width - 120, 390), (80, 40)),
    text='OFF',
    manager=manager,
)
autoplay_off_button.disable()

speed_label = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((width - 140, 460), (120, 40)),
    text='Autoplay Speed',
    manager=manager
)
speed_slider = pygame_gui.elements.UIHorizontalSlider(
    relative_rect=pygame.Rect((width - 140, 490), (120, 20)),
    start_value=5,
    value_range=(0.5, 25),
    manager=manager
)
speed_value_label = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((width - 140, 510), (120, 40)),
    text='',
    manager=manager
)


scatter_random_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((width - 130, 580), (100, 40)),
    text='fill 10%',
    manager=manager,
)
reset_grid_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((width - 120, 670), (80, 40)),
    text='Reset',
    manager=manager,
)

game_related_elements = [progress_button, birth_text_entry, survival_text_entry, birth_label,
                         survival_label, speed_label, autoplay_label, autoplay_on_button, autoplay_off_button,
                         speed_slider, speed_value_label, scatter_random_button, reset_grid_button]

title_label = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((width / 2 - 200, height / 2 - 50), (400, 60)),
    text='THE Game of Life',
    manager=manager,
)
start_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((width / 2 - 80, height / 2), (160, 60)),
    text='START',
    manager=manager,
)

cell_label = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((width / 2 - 200, 500), (400, 60)),
    text='SELECT CELL SIZE',
    manager=manager,
)

s_cell_size_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((width / 2 - 160, 550), (80, 60)),
    text='S',
    manager=manager,
)
m_cell_size_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((width / 2 - 80, 550), (80, 60)),
    text='M',
    manager=manager,
)
l_cell_size_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((width / 2, 550), (80, 60)),
    text='L',
    manager=manager,
)
xxl_cell_size_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((width / 2 + 80, 550), (80, 60)),
    text='XXL',
    manager=manager,
)
size_buttons = [s_cell_size_button, m_cell_size_button, l_cell_size_button, xxl_cell_size_button]
start_related_elements = [title_label, start_button, cell_label, s_cell_size_button, m_cell_size_button,
                          l_cell_size_button, xxl_cell_size_button]

for element in game_related_elements:
    element.hide()


def parse_rules(birth_text, survival_text):
    try:
        birth = [int(b) for b in birth_text if b.isdigit()]
        survival = [int(s) for s in survival_text if s.isdigit()]
        return birth, survival
    except ValueError:
        return [3], [2, 3]


def update_grid(grid, birth_rules, survival_rules):
    new_grid = np.copy(grid)

    for i in range(n_cells_x):
        for j in range(n_cells_y):
            live_neighbors = np.sum(grid[(i - 1):(i + 2), (j - 1):(j + 2)]) - grid[i, j]

            if grid[i, j] == 1 and live_neighbors not in survival_rules:
                new_grid[i, j] = 0
            elif grid[i, j] == 0 and live_neighbors in birth_rules:
                new_grid[i, j] = 1

    return new_grid


def draw_grid():
    for i in range(n_cells_x):
        for j in range(n_cells_y):
            cell_color = (255, 255, 255) if grid[i, j] == 1 else (0, 0, 0)
            pygame.draw.rect(screen, cell_color, (i * cell_size, j * cell_size, cell_size - 1, cell_size - 1))


def start_screen():
    cell_sizes = {
        'S': 160,
        'M': 100,
        'L': 40,
        'XXL': 20
    }

    selected_cell_size = 'M'
    m_cell_size_button.disable()

    running = True

    while running:

        time_delta = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                for button in size_buttons:
                    button.enable()
                if event.ui_element == start_button:
                    global n_cells_y, cell_size, n_cells_x, grid

                    n_cells_y = cell_sizes[selected_cell_size]
                    cell_size = height // n_cells_y
                    n_cells_x = (width - 160) // cell_size
                    grid = np.zeros((n_cells_x, n_cells_y))
                    for element in start_related_elements:
                        element.hide()
                    for element in game_related_elements:
                        element.show()
                    return True

                elif event.ui_element == s_cell_size_button:
                    selected_cell_size = 'S'
                    s_cell_size_button.disable()
                elif event.ui_element == m_cell_size_button:
                    selected_cell_size = 'M'
                    m_cell_size_button.disable()
                elif event.ui_element == l_cell_size_button:
                    selected_cell_size = 'L'
                    l_cell_size_button.disable()
                elif event.ui_element == xxl_cell_size_button:
                    selected_cell_size = 'XXL'
                    xxl_cell_size_button.disable()
            manager.process_events(event)

        manager.update(time_delta)
        screen.fill((0, 0, 0))
        manager.draw_ui(screen)
        pygame.display.flip()

running = start_screen()
birth_rules, survival_rules = [3], [2, 3]

autoplay = False
last_update_time = 0

while running:
    time_delta = clock.tick(60) / 1000.0

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if x < n_cells_x * cell_size:
                i, j = x // cell_size, y // cell_size
                grid[i, j] = 1 - grid[i, j]

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == autoplay_on_button:
                autoplay = True
                autoplay_on_button.disable()
                autoplay_off_button.enable()
            elif event.ui_element == autoplay_off_button:
                autoplay = False
                autoplay_on_button.enable()
                autoplay_off_button.disable()
            elif event.ui_element == scatter_random_button:
                percent_to_turn_on = 0.1
                for _ in range(int(n_cells_x * n_cells_y * percent_to_turn_on)):
                    i = np.random.randint(n_cells_x)
                    j = np.random.randint(n_cells_y)
                    grid[i, j] = 1
            elif event.ui_element == reset_grid_button:
                grid = np.zeros((n_cells_x, n_cells_y))

        manager.process_events(event)

    manager.update(time_delta)

    if progress_button.check_pressed() or (
            autoplay and pygame.time.get_ticks() - last_update_time > 1000 / speed_slider.get_current_value()):
        last_update_time = pygame.time.get_ticks()
        birth_rules, survival_rules = parse_rules(birth_text_entry.get_text(), survival_text_entry.get_text())
        grid = update_grid(grid, birth_rules, survival_rules)
    speed_value_label.set_text(f'{speed_slider.get_current_value() :.1f} cycles/s')

    draw_grid()
    pygame.draw.line(screen, (255, 255, 255), (n_cells_x * cell_size, 0), (n_cells_x * cell_size, height), 2)

    manager.draw_ui(screen)
    pygame.display.flip()

pygame.quit()
