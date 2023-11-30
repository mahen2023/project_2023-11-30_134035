import pygame
from game_config import WINDOW_WIDTH, WINDOW_HEIGHT
from game_clock import GameClock
from snake import Snake
from food import Food
from draw_utils import draw_snake, draw_food
from input_handler import handle_input
from collision import check_collisions
from growth import handle_growth
from food_position import randomize_food_position
from scoring import Scoring
from score_display import display_score
from game_over import handle_game_over
from game_reset import reset_game
from start_screen import display_start_screen

def main():
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Snake Game')

    clock = GameClock()
    snake = Snake()
    food = Food()
    scoring = Scoring()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            handle_input(event, snake)

        snake.move()
        if check_collisions(snake, WINDOW_WIDTH, WINDOW_HEIGHT):
            handle_game_over(window, scoring.score)
            running = False

        if snake.head == food.position:
            handle_growth(snake)
            randomize_food_position(food, snake)
            scoring.increment_score()

        window.fill((0, 0, 0))  # Clear screen
        draw_snake(window, snake)
        draw_food(window, food)
        display_score(window, scoring.score)
        pygame.display.update()
        clock.tick()

    pygame.quit()

if __name__ == '__main__':
    display_start_screen()
    main()
