import pygame
import random
from constants import *

from circleshape import *

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
		#self.velocity = 


	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, 2)

	def update(self, dt):
		self.position += (self.velocity * dt)

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		random_angle = self.velocity.rotate(random.uniform(20, 50))
		old_radius = self.radius
		new_radius = self.radius - ASTEROID_MIN_RADIUS
		new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
		new_asteroid.velocity = random_angle * 1.2
		new_asteroid0 = Asteroid(self.position.x, self.position.y, new_radius)
		new_asteroid0.velocity = -random_angle * 1.2

