
# I wait for implementing switching weapons:

# class Gun(pygame.sprite.Sprite):
#     def __init__(self, player,groups):
#         #player connection
#         self.player = player
#         self.distance = 140
#         self.player_direction = pygame.Vector2(0,1)

#         #sprite setup
#         super().__init__(groups)
#         self.gun_surf = pygame.image.load(join("images", 'sword', 'sword2.png')).convert_alpha()
#         self.image = self.gun_surf
#         # Resize the image with a more reasonable scale factor, like 0.3 for 30% of the original size


#         scale_factor = 0.1 
#         new_width = int(self.gun_surf.get_width() * scale_factor)
#         new_height = int(self.gun_surf.get_height() * scale_factor)
#         self.image = pygame.transform.scale(self.gun_surf, (new_width, new_height)) # Scale the image
#         self.rect = self.image.get_rect(center = self.player.rect.center + self.player_direction*self.distance )
    
#     def get_direction(self):
#         mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
#         player_pos = pygame.Vector2(WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
#         self.player_direction = (mouse_pos - player_pos).normalize()
        
#         #  print(self.player_direction)
        
#     # def rotate_gun(self):
#     #     angle = degrees(atan2(self.player_direction.x, self.player_direction.y))-90
#     #     if self.player_direction.x>0:
#     #         self.image = pygame.transform.rotozoom(self.gun_surf, angle, 1)
#     #     else:
#     #         self.image = pygame.transform.rotozoom(self.gun_surf, abs(angle), 1)
#     #         self.image = pygame.transform.flip(self.image, False, True)    

#     def rotate_sword(self):
#         angle = degrees(atan2(self.player_direction.x, self.player_direction.y))-90
#         if self.player_direction.x>0:
#             self.image = pygame.transform.rotozoom(self.gun_surf, angle, 1)
#         else:
#             self.image = pygame.transform.rotozoom(self.gun_surf, abs(angle), 1)
#             self.image = pygame.transform.flip(self.image, False, True)  
    
#     def update (self, _):
#         self.get_direction()
#         # self.rotate_gun()
#         self.rotate_sword()
#         self.rect.center = self.player.rect.center + self.player_direction * self.distance   


# def rotate_sword(self):
#         angle = degrees(atan2(self.player_direction.y, self.player_direction.x)) - 90
#         self.image = pygame.transform.rotozoom(self.gun_surf, -angle, 1)
#         self.rect = self.image.get_rect(center=self.player.rect.center + self.player_direction * self.distance)

# This one works but imma try to flip the sword pic:
# def rotate_sword(self):
#         angle = degrees(atan2(self.player_direction.y, self.player_direction.x)) - 90
#         self.image = pygame.transform.rotozoom(self.gun_surf, -angle-90, 1)
#         self.rect = self.image.get_rect(center=self.player.rect.center + self.player_direction * self.distance)

# This is for gun class cuz im working on switching weapons:

# class Gun(pygame.sprite.Sprite):
#     def __init__(self, player, groups):
#         # Player connection
#         self.player = player
#         self.distance = 140
#         self.player_direction = pygame.Vector2(0, 1)

#         # Sprite setup
#         super().__init__(groups)
#         self.gun_surf = pygame.image.load(join("images", 'gun', 'gun.png')).convert_alpha()
#         self.image = self.gun_surf

#         # self.sword_surf = pygame.image.load(join("images", 'sword', 'sword2.png')).convert_alpha()
#         # self.image = self.sword_surf
#         # scale_factor = 0.1
#         # new_width = int(self.gun_surf.get_width() * scale_factor)
#         # new_height = int(self.gun_surf.get_height() * scale_factor)
#         # self.image = pygame.transform.scale(self.gun_surf, (new_width, new_height)
#         self.rect = self.image.get_rect(center=self.player.rect.center + self.player_direction * self.distance)

#     def get_direction(self):
#         mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
#         player_pos = pygame.Vector2(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)  # Player is centered in view
#         self.player_direction = (mouse_pos - player_pos).normalize()

#     def rotate_gun(self):
#         angle = degrees(atan2(self.player_direction.x, self.player_direction.y))-90
#         if self.player_direction.x>0:
#             self.image = pygame.transform.rotozoom(self.gun_surf, angle, 1)
#         else:
#             self.image = pygame.transform.rotozoom(self.gun_surf, abs(angle), 1)
#             self.image = pygame.transform.flip(self.image, False, True)

#----------------------------
# Here's the main file:
# import pygame, sys
# from settings import *
# from player import Player
# from sprites import *
# from random import randint, choice
# from pytmx.util_pygame import load_pygame
# from groups import AllSprites



# def home_screen(screen):
#         screen.fill((0, 0, 0))  # Background color for the home screen
#         game_name_font = pygame.font.Font(None, 180)
#         play_font = pygame.font.Font(None, 150)  # Adjust font size as needed
#         quit_font = pygame.font.Font(None, 100)
#         tips_font = pygame.font.Font(None, 30)

#         # Render buttons
#         game_name_text = game_name_font.render("MOBS SURVIVAL", True, (255, 255, 255))
#         play_text = play_font.render("PLAY", True, (255, 255, 255))
#         quit_text = quit_font.render("QUIT", True, (255, 0, 0))
#         tip1_text = tips_font.render("Tip 1: Press p to pause and unpause the game.", True, (255, 255, 255))
#         tip2_text = tips_font.render("Tip 2: Press 1 or 2 to switch weapons", True, (255, 255, 255))

#         # Get rect for button positions
#         game_name_rect = game_name_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 -200))
#         play_rect = play_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 +20))
#         quit_rect = quit_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 +120))
#         tip1_rect = tip1_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 200))
#         tip2_rect = tip2_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 240))

#         # Draw buttons
#         screen.blit(game_name_text,  game_name_rect)
#         screen.blit(play_text, play_rect)
#         screen.blit(quit_text, quit_rect)
#         screen.blit(tip1_text, tip1_rect)
#         screen.blit(tip2_text, tip2_rect)
        
#         pygame.display.flip()

#         while True:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     sys.exit()
#                 elif event.type == pygame.MOUSEBUTTONDOWN:
#                     if play_rect.collidepoint(event.pos):
#                         return "play"
#                     elif quit_rect.collidepoint(event.pos):
#                         pygame.quit()
#                         sys.exit()

# class Game:
#     def __init__(self):
#         #Setup
#         pygame.init()
        
#         self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#         pygame.display.set_caption('Mobs Survival')
#         self.clock = pygame.time.Clock()
#         self.running = True

#         #groups
#         self.collision_sprites = pygame.sprite.Group()
#         self.all_sprites  = AllSprites()
#         self.collision_sprites = pygame.sprite.Group()
#         self.bullet_sprites = pygame.sprite.Group()
#         self.enemy_sprites = pygame.sprite.Group()
#         self.create_borders()
        
        
#         # gun timer
#         self.can_shoot = True
#         self.shoot_time = 0
#         self.gun_cooldown = 200
        
#         # enemy timer
#         self.enemy_event = pygame.event.custom_type()
#         pygame.time.set_timer(self.enemy_event, 300)
#         self.spawn_positions  = []

#         #sprites
#         # self.player = Player((500,300), self.all_sprites,self.collision_sprites)
        
#         # audio
#         self.shoot_sound = pygame.mixer.Sound(join("audio", 'shoot.wav'))
#         self.shoot_sound.set_volume(0.4)
#         self.impact_sound  = pygame.mixer.Sound(join("audio", 'impact.ogg'))
#         self.music = pygame.mixer.Sound(join("audio", 'music.wav'))
#         # setup 
#         self.music.set_volume(0.3)
#         self.music.play(loops=-1)
#         self.load_images()
#         self.setup()

#     def create_borders(self):
#         # Top and bottom borders
#         for x in range(0, MAP_WIDTH, TILE_SIZE):
#             CollisionSprite((x, 0), pygame.Surface((TILE_SIZE, TILE_SIZE)), [self.collision_sprites])  # Top border
#             CollisionSprite((x, MAP_HEIGHT - TILE_SIZE), pygame.Surface((TILE_SIZE, TILE_SIZE)), [self.collision_sprites])  # Bottom border

#         # Left and right borders
#         for y in range(0, MAP_HEIGHT, TILE_SIZE):
#             CollisionSprite((0, y), pygame.Surface((TILE_SIZE, TILE_SIZE)), [self.collision_sprites])  # Left border
#             CollisionSprite((MAP_WIDTH - TILE_SIZE, y), pygame.Surface((TILE_SIZE, TILE_SIZE)), [self.collision_sprites])  # Right border

#     def load_images(self):
#         self.bullet_surf = pygame.image.load(join("images", 'gun', 'bullet.png')).convert_alpha()

#         folders =list(walk(join('images', 'enemies')))[0][1]
#         self.enemy_frames = {}
#         for folder in folders:
#             for folder_path, _, file_names in walk(join('images', 'enemies', folder)):
                
#                 self.enemy_frames[folder] = []
#                 for file_name in sorted(file_names, key = lambda name: int(name.split(".")[0])):
#                     full_path = join(folder_path, file_name)
#                     surf = pygame.image.load(full_path).convert_alpha()
#                     self.enemy_frames[folder].append(surf)

#         print("Loaded enemy frames:")
#         for enemy_type, frames in self.enemy_frames.items():
#             print(f"Enemy type '{enemy_type}' has {len(frames)} frames.")

#     def input(self):
#         keys = pygame.key.get_pressed()
#         # Switch to gun
#         if keys[pygame.K_1]:
#             self.gun.switch_weapon("gun")
#         if self.gun.weapon_type == "gun" and pygame.mouse.get_pressed()[0] and self.can_shoot:
#             self.shoot_sound.play()
#             pos= self.gun.rect.center +self.gun.player_direction * 50
#             Bullet(self.bullet_surf, pos, self.gun.player_direction, (self.all_sprites, self.bullet_sprites))
#             self.can_shoot  = False
#             self.shoot_time = pygame.time.get_ticks()

#         # Switch to sword
#         elif keys[pygame.K_2]:
#             self.gun.switch_weapon("sword")
            
#     def gun_timer(self):
#         if not self.can_shoot:
#             current_time = pygame.time.get_ticks()
#             if current_time -self.shoot_time >= self.gun_cooldown:
#                 self.can_shoot = True

#     def setup(self):
#         map = load_pygame(join('data', 'maps', 'world.tmx'))
#         # Load non-collision sprites from the 'Ground' layer
#         for x, y, image in map.get_layer_by_name('Ground').tiles():
#             Sprite((x*TILE_SIZE, y*TILE_SIZE), image, [self.all_sprites])
#         # Load collision sprites from the 'Objects' layer
#         for obj in map.get_layer_by_name('Objects'):
#             CollisionSprite((obj.x, obj.y), obj.image, [self.all_sprites, self.collision_sprites])

#         # for obj in map.get_layer_by_name('Collisions'): This is for making u not falling down the cliff
#         #     CollisionSprite((obj.x, obj.y), pygame.Surface((obj.width, obj.height)), self.collision_sprites)

#         for obj in map.get_layer_by_name('Entities'):
#             if obj.name == "Player":
#                 self.player = Player((obj.x,obj.y), self.all_sprites, self.collision_sprites)
#                 self.gun = Gun(self.player, self.all_sprites)
#             else:
#                 self.spawn_positions.append((obj.x, obj.y))

#     def restrict_camera(self):
#     # Get the player's position for camera centering
#         camera_x = max(0, min(self.player.rect.centerx - WINDOW_WIDTH // 2, MAP_WIDTH - WINDOW_WIDTH))
#         camera_y = max(0, min(self.player.rect.centery - WINDOW_HEIGHT // 2, MAP_HEIGHT - WINDOW_HEIGHT))
        
#         # Ensure the camera doesn't show beyond the borders
#         if camera_x == 0 or camera_x == MAP_WIDTH - WINDOW_WIDTH:
#             camera_x = min(max(0, self.player.rect.centerx - WINDOW_WIDTH // 2), MAP_WIDTH - WINDOW_WIDTH)

#         if camera_y == 0 or camera_y == MAP_HEIGHT - WINDOW_HEIGHT:
#             camera_y = min(max(0, self.player.rect.centery - WINDOW_HEIGHT // 2), MAP_HEIGHT - WINDOW_HEIGHT)

#         return camera_x, camera_y

#     def bullet_collision(self):
#         if self.bullet_sprites:
#             for bullet in self.bullet_sprites:
#                 collision_sprites = pygame.sprite.spritecollide(bullet, self.enemy_sprites, False, pygame.sprite.collide_mask)
#                 if collision_sprites:
#                     self.impact_sound.play()
#                     for sprite in collision_sprites:
#                         sprite.destroy()

#                     bullet.kill()

#     def sword_collision(self):
#         if self.gun.weapon_type == "sword":
#             for enemy in self.enemy_sprites:
#                 # Check for pixel-perfect collision between the sword and the enemy
#                 if pygame.sprite.collide_mask(self.gun, enemy):
#                     self.impact_sound.play()
#                     enemy.destroy()

        
#     def player_collision(self):
#         if pygame.sprite.spritecollide(self.player, self.enemy_sprites, False, pygame.sprite.collide_mask):
#             self.game_over()

#     def game_over(self):
#         self.display_surface.fill((40, 0, 0))
#         font = pygame.font.Font(None, 200)
#         game_over_text = font.render("YOU DIE", True, (255, 0, 0))
#         game_over_rect = game_over_text.get_rect(center=(self.display_surface.get_width() // 2, self.display_surface.get_height() // 2))
#         self.display_surface.blit(game_over_text, game_over_rect)
#         pygame.display.flip()
#         pygame.time.wait(5000)
#         self.running = False

#     def toggle_pause(self):
#         self.paused = not self.paused

#     def run(self):
#         self.paused = False
#         blurred_background = None  # Store the blurred background image when paused

#         while self.running:
#             dt = self.clock.tick() / 500  # Delta time

#             # Event loop
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     self.running = False
#                 elif event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_p:
#                         self.toggle_pause()
#                         if self.paused:
#                             # Capture and blur the screen once on pause
#                             screen_copy = self.display_surface.copy()
#                             small_size = (self.display_surface.get_width() // 10, self.display_surface.get_height() // 10)
#                             blurred_background = pygame.transform.smoothscale(screen_copy, small_size)
#                             blurred_background = pygame.transform.smoothscale(blurred_background, self.display_surface.get_size())
#                 elif event.type == self.enemy_event:
#                     # Spawn enemies regardless of pause state
#                     Enemy(
#                         choice(self.spawn_positions),
#                         choice(list(self.enemy_frames.values())),
#                         (self.all_sprites, self.enemy_sprites),
#                         self.player,
#                         self.collision_sprites,
#                     )

#             if not self.paused:
#                 # Update and draw only when not paused
#                 self.input()
#                 self.sword_collision()
#                 self.gun_timer()
#                 self.all_sprites.update(dt)
#                 self.bullet_collision()
#                 self.player_collision()

#                 # Adjust the camera based on the player's position
#                 camera_x, camera_y = self.restrict_camera()

#                 # Fill the background and adjust all sprites positions based on the camera
#                 self.display_surface.fill('black')

#                 # Draw all sprites
#                 for sprite in self.all_sprites:
#                     # Apply camera offset to each sprite's position
#                     self.display_surface.blit(sprite.image, sprite.rect.topleft - pygame.Vector2(camera_x, camera_y))

#                 # Optionally, you could render the player's position here, making sure it's drawn relative to the camera position

#                 pygame.display.update()
#             else:
#                 # Draw the blurred background only when paused
#                 self.display_surface.blit(blurred_background, (0, 0))

#                 # Display the "Game Paused" message
#                 pause_font = pygame.font.Font(None, 100)  # Adjust font size if needed
#                 pause_text = pause_font.render("Game Paused", True, (255, 255, 255))
#                 pause_rect = pause_text.get_rect(center=(self.display_surface.get_width() // 2, self.display_surface.get_height() // 2))

#                 # Blit the pause text over the blurred background
#                 self.display_surface.blit(pause_text, pause_rect)
#                 pygame.display.flip()

#         pygame.quit()



# if __name__ == '__main__': # Use this only if you want this file to run the entire game. Like you cant run the game in other files. 
#                                 # Only this file can.
#     pygame.init()
#     screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#     result = home_screen(screen)
#     if result == "play":
#         game = Game()
#         game.run()



# And here's the sprites file:

# from ntpath import join
# import pygame
# from math import atan2, degrees
# from settings import *

# class Sprite(pygame.sprite.Sprite):
#     def __init__(self, pos, surf, groups):

#         super().__init__(groups)
#         self.image = surf if surf else pygame.Surface((TILE_SIZE, TILE_SIZE))
#         self.rect = self.image.get_rect(topleft=pos)
#         self.ground = True
    

# class CollisionSprite(pygame.sprite.Sprite):
#     def __init__(self, pos, surf, groups):
#         super().__init__(groups)
#         self.image = surf if surf else pygame.Surface((TILE_SIZE, TILE_SIZE))
#         self.rect = self.image.get_rect(topleft=pos)


# class Gun(pygame.sprite.Sprite):
#     def __init__(self, player, groups):
#         # Player connection
#         self.player = player
#         self.distance = 140
#         self.player_direction = pygame.Vector2(0, 1)

#         # Sprite setup
#         super().__init__(groups)
#         self.gun_surf = pygame.image.load(join("images", 'gun', 'gun.png')).convert_alpha()
#         self.sword_surf = pygame.image.load(join("images", 'sword', 'sword2.png')).convert_alpha()
#         self.image = self.gun_surf  # Default to gun
#         self.weapon_type = "gun"  # Current weapon type

#         self.rect = self.image.get_rect(center=self.player.rect.center + self.player_direction * self.distance)
#         # Create a mask for the sword (used for collision detection)
#         self.sword_mask = pygame.mask.from_surface(self.sword_surf)

#     def update(self, _):
#         self.get_direction()
#         if self.weapon_type == "gun":
#             self.rotate_gun()
#         else:
#             self.rotate_sword()
#             self.mask = pygame.mask.from_surface(self.image)  # Update mask during sword use
#         self.rect.center = self.player.rect.center + self.player_direction * self.distance

#     def get_direction(self):
#         mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
#         player_pos = pygame.Vector2(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)  # Player is centered in view
#         self.player_direction = (mouse_pos - player_pos).normalize()

#     def rotate_gun(self):
#         angle = degrees(atan2(self.player_direction.x, self.player_direction.y)) - 90
#         if self.player_direction.x > 0:
#             self.image = pygame.transform.rotozoom(self.gun_surf, angle, 1)
#         else:
#             self.image = pygame.transform.rotozoom(self.gun_surf, abs(angle), 1)
#             self.image = pygame.transform.flip(self.image, False, True)

#     def rotate_sword(self):
#         angle = degrees(atan2(self.player_direction.y, self.player_direction.x)) - 90
#         self.image = pygame.transform.rotozoom(self.sword_surf, -angle, 1)
#         self.rect = self.image.get_rect(center=self.player.rect.center + self.player_direction * self.distance)

#     def switch_weapon(self, weapon_type):
#         self.weapon_type = weapon_type
#         # Set image based on the selected weapon
#         self.image = self.gun_surf if weapon_type == "gun" else self.sword_surf

#     def update(self, _):
#         self.get_direction()
#         # Rotate only the selected weapon
#         if self.weapon_type == "gun":
#             self.rotate_gun()
#         else:
#             self.rotate_sword()
#         self.rect.center = self.player.rect.center + self.player_direction * self.distance



# class Bullet(pygame.sprite.Sprite):
#     def __init__(self,surf, pos, direction, groups):
#         super().__init__(groups)
#         self.image = surf
#         self.rect = self.image.get_rect(center = pos)
#         self.spawn_time = pygame.time.get_ticks()
#         self.lifetime = 1000


#         self.direction = direction
#         self.speed = 1200

#     def update(self,dt):
#         self.rect.center += self.direction * self.speed*dt
#         if pygame.time.get_ticks()-self.spawn_time >= self.lifetime:
#             self.kill()


# class Enemy(pygame.sprite.Sprite):
#     def __init__(self, pos, frames, groups, player, collision_sprites):
#         super().__init__(groups)
#         self.player = player

#         # image
#         self.frames, self.frame_index = frames, 0
#         self.image = self.frames[self.frame_index]
#         self.animation_speed  = 6

#         # rect
#         self.rect = self.image.get_rect(center = pos)
#         self.hitbox_rect = self.rect.inflate(-20,-40)
#         self.collision_sprites = collision_sprites
#         self.direction = pygame.Vector2()
#         self.speed = 200

#         #timer
#         self.death_time = 0
#         self.death_duration = 400

#     def animate(self,dt):
#         self.frame_index += self.animation_speed * dt
#         self.image = self.frames[int(self.frame_index)% len(self.frames)]

#     def move(self,dt):
#         # get direction
#         player_pos = pygame.Vector2(self.player.rect.center) 
#         enemy_pos = pygame.Vector2(self.rect.center) 
#         self.direction = (player_pos - enemy_pos)
#         if self.direction.length() != 0:
#             self.direction = self.direction.normalize()
        

#         #update the rect position + collision
#         self.hitbox_rect.x += self.direction.x * self.speed * dt
#         self.collision('horizontal')
#         self.hitbox_rect.y += self.direction.y * self.speed * dt
#         self.collision('vertical')
#         self.rect.center = self.hitbox_rect.center

#     def collision(self, direction):
#         for sprite in self.collision_sprites:
#             if sprite.rect.colliderect(self.hitbox_rect):
#                 # Horizontal collision
#                 if direction == 'horizontal':
#                     if self.direction.x > 0:  # Moving right; hit the left side of the obstacle
#                         self.hitbox_rect.right = sprite.rect.left
#                     elif self.direction.x < 0:  # Moving left; hit the right side of the obstacle
#                         self.hitbox_rect.left = sprite.rect.right

#                 # Vertical collision
#                 elif direction == 'vertical':
#                     if self.direction.y > 0:  # Moving down; hit the top of the obstacle
#                         self.hitbox_rect.bottom = sprite.rect.top
#                     elif self.direction.y < 0:  # Moving up; hit the bottom of the obstacle
#                         self.hitbox_rect.top = sprite.rect.bottom

#     def destroy(self):
#         # start timer
#         self.death_time = pygame.time.get_ticks()

#         # change the image
#         surf = pygame.mask.from_surface(self.frames[0]).to_surface()
#         surf.set_colorkey('black')
#         self.image =surf

#     def death_timer(self):
#         if pygame.time.get_ticks() - self.death_time >=self.death_duration:
#             self.kill()

#     def update(self,dt):
#         if self.death_time == 0:
#             self.move(dt)
#             self.animate(dt)
#         else:
#             self.death_timer()
