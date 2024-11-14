import pygame, sys
from settings import *
from player import Player
from sprites import *
from random import choice
from pytmx.util_pygame import load_pygame
from groups import AllSprites



def home_screen(screen):
        screen= pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Mobs Survival')
        screen.fill((0, 0, 0))  # Background color for the home screen
        game_name_font = pygame.font.Font(None, 180)
        play_font = pygame.font.Font(None, 150)  # Adjust font size as needed
        quit_font = pygame.font.Font(None, 100)
        tips_font = pygame.font.Font(None, 30)

        # Render buttons
        game_name_text = game_name_font.render("MOBS SURVIVAL", True, (255, 255, 255))
        play_text = play_font.render("PLAY", True, (255, 255, 255))
        quit_text = quit_font.render("QUIT", True, (255, 0, 0))
        tip1_text = tips_font.render("Tip 1: Press p to pause and unpause the game.", True, (255, 255, 255))
        tip2_text = tips_font.render("Tip 2: Press 1 or 2 to switch weapons", True, (255, 255, 255))
        tip3_text = tips_font.render("Tip 3: Do not touch their white soul. You will die.", True, (255, 255, 255))

        # Get rect for button positions
        game_name_rect = game_name_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 -200))
        play_rect = play_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 +20))
        quit_rect = quit_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 +120))
        tip1_rect = tip1_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 200))
        tip2_rect = tip2_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 240))
        tip3_rect = tip3_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 280))

        # Draw buttons
        screen.blit(game_name_text,  game_name_rect)
        screen.blit(play_text, play_rect)
        screen.blit(quit_text, quit_rect)
        screen.blit(tip1_text, tip1_rect)
        screen.blit(tip2_text, tip2_rect)
        screen.blit(tip3_text, tip3_rect)
        
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if play_rect.collidepoint(event.pos):
                        return "play"
                    elif quit_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

class Game:
    def __init__(self):
        # Setup
        pygame.mouse.set_visible(False)
        pygame.event.set_grab(True)  # This locks the mouse inside the window

        pygame.init()

        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Mobs Survival')
        self.clock = pygame.time.Clock()
        self.running = True

        # Score initialization
        self.score = 0

        # Groups
        self.collision_sprites = pygame.sprite.Group()
        self.all_sprites = AllSprites()
        self.collision_sprites = pygame.sprite.Group()
        self.bullet_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        self.create_borders()

        # gun timer
        self.can_shoot = True
        self.shoot_time = 0
        self.gun_cooldown = 200

        # enemy timer
        self.enemy_event = pygame.event.custom_type()
        pygame.time.set_timer(self.enemy_event, 300)
        self.spawn_positions = []

        # sprites
        # self.player = Player((500, 300), self.all_sprites, self.collision_sprites)

        # audio
        self.shoot_sound = pygame.mixer.Sound(join("audio", 'shoot.wav'))
        self.shoot_sound.set_volume(0.4)
        self.impact_sound = pygame.mixer.Sound(join("audio", 'impact.ogg'))
        self.music = pygame.mixer.Sound(join("audio", 'music.wav'))
        # setup 
        self.music.set_volume(0.3)
        self.music.play(loops=-1)
        self.load_images()
        self.setup()

    def update_score(self, points):
        """Updates the score and returns the updated value."""
        self.score += points

    def draw_score(self):
        """Draws the score on the screen."""
        score_font = pygame.font.Font(None, 50)
        score_text = score_font.render(f"Score: {self.score}", True, (255, 255, 255))
        score_rect = score_text.get_rect(topleft=(10, 10))
        self.display_surface.blit(score_text, score_rect)

    def create_borders(self):
        # Top and bottom borders
        for x in range(0, MAP_WIDTH, TILE_SIZE):
            CollisionSprite((x, 0), pygame.Surface((TILE_SIZE, TILE_SIZE)), [self.collision_sprites])  # Top border
            CollisionSprite((x, MAP_HEIGHT - TILE_SIZE), pygame.Surface((TILE_SIZE, TILE_SIZE)), [self.collision_sprites])  # Bottom border

        # Left and right borders
        for y in range(0, MAP_HEIGHT, TILE_SIZE):
            CollisionSprite((0, y), pygame.Surface((TILE_SIZE, TILE_SIZE)), [self.collision_sprites])  # Left border
            CollisionSprite((MAP_WIDTH - TILE_SIZE, y), pygame.Surface((TILE_SIZE, TILE_SIZE)), [self.collision_sprites])  # Right border

    def load_images(self):
        self.bullet_surf = pygame.image.load(join("images", 'gun', 'bullet.png')).convert_alpha()

        folders =list(walk(join('images', 'enemies')))[0][1]
        self.enemy_frames = {}
        for folder in folders:
            for folder_path, _, file_names in walk(join('images', 'enemies', folder)):
                
                self.enemy_frames[folder] = []
                for file_name in sorted(file_names, key = lambda name: int(name.split(".")[0])):
                    full_path = join(folder_path, file_name)
                    surf = pygame.image.load(full_path).convert_alpha()
                    self.enemy_frames[folder].append(surf)
            
    def input(self):
        keys = pygame.key.get_pressed()
        # Switch to gun
        if keys[pygame.K_1]:
            self.gun.switch_weapon("gun")
        if self.gun.weapon_type == "gun" and pygame.mouse.get_pressed()[0] and self.can_shoot:
            self.shoot_sound.play()
            pos= self.gun.rect.center +self.gun.player_direction * 50
            Bullet(self.bullet_surf, pos, self.gun.player_direction, (self.all_sprites, self.bullet_sprites))
            self.can_shoot  = False
            self.shoot_time = pygame.time.get_ticks()

        # Switch to sword
        elif keys[pygame.K_2]:
            self.gun.switch_weapon("sword")
            
    def gun_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time -self.shoot_time >= self.gun_cooldown:
                self.can_shoot = True

    def setup(self):
        map = load_pygame(join('data', 'maps', 'world.tmx'))
        # Load non-collision sprites from the 'Ground' layer
        for x, y, image in map.get_layer_by_name('Ground').tiles():
            Sprite((x*TILE_SIZE, y*TILE_SIZE), image, [self.all_sprites])

        # Load collision sprites from the 'Objects' layer
        for obj in map.get_layer_by_name('Objects'):
            CollisionSprite((obj.x, obj.y), obj.image, [self.all_sprites, self.collision_sprites])

        # for obj in map.get_layer_by_name('Collisions'): This is for making u not falling down the cliff
        #     CollisionSprite((obj.x, obj.y), pygame.Surface((obj.width, obj.height)), self.collision_sprites)

        for obj in map.get_layer_by_name('Entities'):
            if obj.name == "Player":
                self.player = Player((obj.x, obj.y), self.all_sprites, self.collision_sprites)
                self.gun = Gun(self.player, self.all_sprites)
            else:
                self.spawn_positions.append((obj.x, obj.y))

    def restrict_camera(self):
    # Get the player's position for camera centering
        camera_x = max(0, min(self.player.rect.centerx - WINDOW_WIDTH // 2, MAP_WIDTH - WINDOW_WIDTH))
        camera_y = max(0, min(self.player.rect.centery - WINDOW_HEIGHT // 2, MAP_HEIGHT - WINDOW_HEIGHT))
        
        # Ensure the camera doesn't show beyond the borders
        if camera_x == 0 or camera_x == MAP_WIDTH - WINDOW_WIDTH:
            camera_x = min(max(0, self.player.rect.centerx - WINDOW_WIDTH // 2), MAP_WIDTH - WINDOW_WIDTH)

        if camera_y == 0 or camera_y == MAP_HEIGHT - WINDOW_HEIGHT:
            camera_y = min(max(0, self.player.rect.centery - WINDOW_HEIGHT // 2), MAP_HEIGHT - WINDOW_HEIGHT)

        return camera_x, camera_y

    def bullet_collision(self):
        if self.bullet_sprites:
            for bullet in self.bullet_sprites:
                collision_sprites = pygame.sprite.spritecollide(bullet, self.enemy_sprites, False, pygame.sprite.collide_mask)
                if collision_sprites:
                    self.impact_sound.play()
                    for sprite in collision_sprites:
                        sprite.destroy()

                    bullet.kill()

    def sword_collision(self):
        if self.gun.weapon_type == "sword":
            for enemy in self.enemy_sprites:
                # Check for pixel-perfect collision between the sword and the enemy
                if pygame.sprite.collide_mask(self.gun, enemy):
                    self.impact_sound.play()
                    enemy.destroy()

    def player_collision(self):
        if pygame.sprite.spritecollide(self.player, self.enemy_sprites, False, pygame.sprite.collide_mask):
            self.game_over()

    def game_over(self):
        self.display_surface.fill((40, 0, 0))
        font = pygame.font.Font(None, 200)
        reminder_text_font = pygame.font.Font(None, 30)

        game_over_text = font.render("YOU DIE", True, (255, 0, 0))
        reminder_text = reminder_text_font.render("DID YOU TOUCH THEIR SOULS or DID YOU GET TOUCHED?", True, (255, 0, 0))

        game_over_rect = game_over_text.get_rect(center=(self.display_surface.get_width() // 2, self.display_surface.get_height() // 2))
        reminder_rect = reminder_text.get_rect(center=(self.display_surface.get_width() // 2, self.display_surface.get_height() // 2 + 100))
        

        self.display_surface.blit(game_over_text, game_over_rect)
        self.display_surface.blit(reminder_text, reminder_rect)
        pygame.display.flip()
        pygame.time.wait(5000)
        self.running = False

    def toggle_pause(self):
        self.paused = not self.paused

    def run(self):
        self.paused = False
        blurred_background = None  # Store the blurred background image when paused

        while self.running:
            dt = self.clock.tick() / 500  # Delta time

            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.toggle_pause()
                        if self.paused:
                            # Capture and blur the screen once on pause
                            screen_copy = self.display_surface.copy()
                            small_size = (self.display_surface.get_width() // 10, self.display_surface.get_height() // 10)
                            blurred_background = pygame.transform.smoothscale(screen_copy, small_size)
                            blurred_background = pygame.transform.smoothscale(blurred_background, self.display_surface.get_size())
                elif event.type == self.enemy_event:
                    if self.spawn_positions:
                        spawn_position = choice(self.spawn_positions)
                        Enemy(
                            spawn_position,
                            choice(list(self.enemy_frames.values())),
                            (self.all_sprites, self.enemy_sprites),
                            self.player,
                            self.collision_sprites,
                            self,  # Pass game instance to the enemy
                        )
                    else:
                        print("No spawn positions available.")  # Debugging line

            if not self.paused:
                # Update and draw only when not paused
                self.input()
                self.sword_collision()
                self.gun_timer()
                self.all_sprites.update(dt)
                self.bullet_collision()
                self.player_collision()

                # Adjust the camera based on the player's position
                camera_x, camera_y = self.restrict_camera()

                # Fill the background and adjust all sprites positions based on the camera
                self.display_surface.fill('black')

                # Draw all sprites
                for sprite in self.all_sprites:
                    # Apply camera offset to each sprite's position
                    self.display_surface.blit(sprite.image, sprite.rect.topleft - pygame.Vector2(camera_x, camera_y))

                # Draw the score on the screen
                self.draw_score()

                pygame.display.update()
            else:
                # Draw the blurred background only when paused
                self.display_surface.blit(blurred_background, (0, 0))

                # Display the "Game Paused" message
                pause_font = pygame.font.Font(None, 100)  # Adjust font size if needed
                pause_text = pause_font.render("Game Paused", True, (255, 255, 255))
                pause_rect = pause_text.get_rect(center=(self.display_surface.get_width() // 2, self.display_surface.get_height() // 2))

                # Blit the pause text over the blurred background
                self.display_surface.blit(pause_text, pause_rect)
                pygame.display.flip()




if __name__ == '__main__': # Use this only if you want this file to run the entire game. Like you cant run the game in other files. 
                                # Only this file can.
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    result = home_screen(screen)
    if result == "play":
        game = Game()
        game.run()


'''
Extra:

'''