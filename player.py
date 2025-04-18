import pygame
from circleshape import *
from constants import *


class Player(CircleShape):

	#shot_timer = 0

	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0
		self.radius = PLAYER_RADIUS
		self.shot_timer = 0


	# in the player class
	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]

	def draw(self, screen):
		pygame.draw.polygon(screen, "white", self.triangle(), 2)

	def rotate(self, dt):
		self.rotation += PLAYER_TURN_SPEED * dt


	def update(self, dt):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_a]:
			self.rotate(-dt)
		if keys[pygame.K_d]:
			self.rotate(+dt)
		if keys[pygame.K_w]:
			self.move(+dt)
		if keys[pygame.K_s]:
			self.move(-dt)
		if keys[pygame.K_SPACE]:
			self.shoot(dt)

	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt

	def shoot(self, dt):
		self.shot_timer -= dt
		if self.shot_timer > 0:
			return
		self.shot_timer = PLAYER_SHOT_LIMIT
		shot = Shot(self.position.x, self.position.y)
		shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED


class Shot(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, SHOT_RADIUS)
		self.radius = SHOT_RADIUS
		#self.

	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, 2)

	def update(self, dt):
		self.position += self.velocity * dt
