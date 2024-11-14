from ntpath import join
import pygame
from math import atan2, degrees
from settings import *

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):

        super().__init__(groups)
        self.image = surf if surf else pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft=pos)
        self.ground = True
    

class CollisionSprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf if surf else pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft=pos)


class Gun(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        # Player connection
        self.player = player
        self.distance = 140
        self.player_direction = pygame.Vector2(0, 1)

        # Sprite setup
        super().__init__(groups)
        self.gun_surf = pygame.image.load(join("images", 'gun', 'gun.png')).convert_alpha()
        self.sword_surf = pygame.image.load(join("images", 'sword', 'sword2.png')).convert_alpha()
        self.image = self.gun_surf  # Default to gun
        self.weapon_type = "gun"  # Current weapon type

        self.rect = self.image.get_rect(center=self.player.rect.center + self.player_direction * self.distance)
        # Create a mask for the sword (used for collision detection)
        self.sword_mask = pygame.mask.from_surface(self.sword_surf)

    def update(self, _):
        self.get_direction()
        if self.weapon_type == "gun":
            self.rotate_gun()
        else:
            self.rotate_sword()
            self.mask = pygame.mask.from_surface(self.image)  # Update mask during sword use
        self.rect.center = self.player.rect.center + self.player_direction * self.distance

    def get_direction(self):
        mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
        player_pos = pygame.Vector2(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)  # Player is centered in view
        self.player_direction = (mouse_pos - player_pos).normalize()

    def switch_weapon(self, weapon_type):
        self.weapon_type = weapon_type
        # Set image based on the selected weapon
        self.image = self.gun_surf if weapon_type == "gun" else self.sword_surf

    def rotate_gun(self):
        angle = degrees(atan2(self.player_direction.x, self.player_direction.y)) - 90
        if self.player_direction.x > 0:
            self.image = pygame.transform.rotozoom(self.gun_surf, angle, 1)
        else:
            self.image = pygame.transform.rotozoom(self.gun_surf, abs(angle), 1)
            self.image = pygame.transform.flip(self.image, False, True)

    def rotate_sword(self):
        angle = degrees(atan2(self.player_direction.y, self.player_direction.x)) - 90
        self.image = pygame.transform.rotozoom(self.sword_surf, -angle, 1)
        self.rect = self.image.get_rect(center=self.player.rect.center + self.player_direction * self.distance)


class Bullet(pygame.sprite.Sprite):
    def __init__(self,surf, pos, direction, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(center = pos)
        self.spawn_time = pygame.time.get_ticks()
        self.lifetime = 1000


        self.direction = direction
        self.speed = 1200

    def update(self,dt):
        self.rect.center += self.direction * self.speed*dt
        if pygame.time.get_ticks()-self.spawn_time >= self.lifetime:
            self.kill()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, frames, groups, player, collision_sprites, game):
        super().__init__(groups)
        self.game = game  # Store a reference to the game instance
        self.player = player

        # image and animation setup
        self.frames, self.frame_index = frames, 0
        self.image = self.frames[self.frame_index]
        self.animation_speed = 6

        # rect setup
        self.rect = self.image.get_rect(center=pos)
        self.hitbox_rect = self.rect.inflate(-20, -40)  # More precise hitbox for collision
        self.collision_sprites = collision_sprites

        # movement and speed
        self.direction = pygame.Vector2()
        self.speed = 200

        # timer for death animation
        self.death_time = 0
        self.death_duration = 100

        # Health of the enemy
        self.health = 100  # Example health, can be changed

    def animate(self, dt):
        """Handle enemy animation."""
        self.frame_index += self.animation_speed * dt
        self.image = self.frames[int(self.frame_index) % len(self.frames)]

    def move(self, dt):
        """Move enemy towards the player."""
        player_pos = pygame.Vector2(self.player.rect.center)
        enemy_pos = pygame.Vector2(self.rect.center)

        # Calculate the direction towards the player
        self.direction = (player_pos - enemy_pos)
        if self.direction.length() != 0:
            self.direction = self.direction.normalize()

        # Move the enemy and handle collisions
        self.hitbox_rect.x += self.direction.x * self.speed * dt
        self.collision('horizontal')
        self.hitbox_rect.y += self.direction.y * self.speed * dt
        self.collision('vertical')
        self.rect.center = self.hitbox_rect.center

    def collision(self, direction):
        """Handle collision with the environment."""
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.hitbox_rect):
                # Horizontal collision
                if direction == 'horizontal':
                    if self.direction.x > 0:  # Moving right; hit the left side of the obstacle
                        self.hitbox_rect.right = sprite.rect.left
                    elif self.direction.x < 0:  # Moving left; hit the right side of the obstacle
                        self.hitbox_rect.left = sprite.rect.right

                # Vertical collision
                elif direction == 'vertical':
                    if self.direction.y > 0:  # Moving down; hit the top of the obstacle
                        self.hitbox_rect.bottom = sprite.rect.top
                    elif self.direction.y < 0:  # Moving up; hit the bottom of the obstacle
                        self.hitbox_rect.top = sprite.rect.bottom

    def take_damage(self, amount):
        """Reduce health when hit by a bullet or other attacks."""
        self.health -= amount
        if self.health <= 0:
            self.destroy()

    def destroy(self):
        """Handle enemy destruction, play animation, and award points."""
        self.death_time = pygame.time.get_ticks()

        # Award points when the enemy is destroyed
        self.game.update_score(1)  # Award 1 point per kill

        # Change the image
        surf = pygame.mask.from_surface(self.frames[0]).to_surface()
        surf.set_colorkey('black')
        self.image = surf
        
    def death_timer(self):
        """Remove the enemy after the death animation time has passed."""
        if pygame.time.get_ticks() - self.death_time >= self.death_duration:
            self.kill()  # Remove from all groups

    def update(self, dt):
        """Update the enemy behavior."""
        if self.death_time == 0:  # Not dead
            self.move(dt)  # Move the enemy towards the player
            self.animate(dt)  # Animate the enemy
        else:  # If dead, trigger the death sequence
            self.death_timer()  # Wait for the death animation to finish before removal
