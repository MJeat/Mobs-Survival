
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


#     # def rotate_sword(self):
#     #     angle = degrees(atan2(self.player_direction.y, self.player_direction.x)) - 90
#     #     self.image = pygame.transform.rotozoom(self.gun_surf, -angle, 1)
#     #     self.rect = self.image.get_rect(center=self.player.rect.center + self.player_direction * self.distance)
    
#     def update(self, _):
#         self.get_direction()
#         self.rotate_gun()
#         # self.rotate_sword()
#         self.rect.center = self.player.rect.center + self.player_direction * self.distance
