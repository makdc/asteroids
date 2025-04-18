# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame
from constants import *
from player import *
from circleshape import *




def main():
	pygame.init()

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	fps_time = pygame.time.Clock()
	dt = 0


	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	Player.containers = (group_a, group_b)
	screen.fill("black")
	player.update(dt)
	player.draw(screen)



	while True:
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
        			return






		dt = fps_time.tick(60)/1000
		pygame.display.flip()
		continue

	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")





if __name__ == "__main__":
	main()
