import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self, other):
        dist = self.position.distance_to(other.position)
        if dist < (self.radius + other.radius):
            exit("Game Over!")
            #print("Game Over!")
            #Exit()
        #print(f"{dist}")
    def shot_collision(self, other):
        dist = self.position.distance_to(other.position)
        if dist < (self.radius + other.radius):
            self.kill()
            other.kill()
