# this allows us to use code from
# the open-source pygame library
# throughout this file

import pygame
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *


def main():
	pygame.init()

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	fps_time = pygame.time.Clock()
	dt = 0

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()


	Player.containers = (updatable, drawable)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = updatable
	asteroid_field = AsteroidField()
	Shot.containers = (shots, updatable, drawable)
	#shot

#player.update(dt)
	#player.draw(screen)


	while True:
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
        			return

		screen.fill("black")

		for u in updatable:
			u.update(dt)

		for d in drawable:
			d.draw(screen)

		for a in asteroids:
			a.collision(player)

			for s in shots:
				a.shot_collision(s)



		dt = fps_time.tick(60)/1000
		pygame.display.flip()
		continue

	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")





if __name__ == "__main__":
	main()
