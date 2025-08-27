import pygame
import sys
import scripts.spritesheet as spritesheet
import os
import subprocess
import shutil
class Animation():
    def __init__(self):
        pygame.init()
        self.animation_cooldown = int(1)
    os.mkdir("frames")
    

    def animation(self):
        self.anim_list = []
        loop1 = True
        loop2 = True
        while loop1:
             try:
                self.anim_steps = int(input("Frames in animation: "))
                loop1 = False
             except ValueError:
                print("Please enter an integer.")

        self.frame = 0
        while loop2:
            try:
                self.animation_cooldown = int(input("Animation speed in milliseconds: "))
                loop2 = False
            except ValueError:
                print("Please enter an integer.")
        self.screen = pygame.display.set_mode((1000, 1000))
        self.image = pygame.image.load("assets/anim.png").convert_alpha()
        self.sprite_sheet = spritesheet.SpriteSheet(self.image)
        for i in range(self.anim_steps):   
            self.anim_list.append(self.sprite_sheet.get_image(i, 100, 100, 10))
        self.last_update = pygame.time.get_ticks()
        run = True
        frame_filenames = []
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.current_time = pygame.time.get_ticks()
            if self.current_time - self.last_update >= self.animation_cooldown:
                self.frame += 1
                self.last_update = self.current_time
                if self.frame >= self.anim_steps:
                    run = False
                    fps = 1000/self.animation_cooldown
                    os.system('cd frames')
                    command = "ffmpeg -framerate {fps} -i frame%04d.png output.mp4"
                    try:
                        os.system(command)
                    except: 
                        print("Do you have ffmpeg installed? Consult the README for more info")
                    output_file = "animation.mp4"
            if self.frame < self.anim_steps:
                self.screen.fill((50, 50, 50))
                self.screen.blit(self.anim_list[self.frame], (0, 0))
                frame_filename = f"frames/f_{self.frame:05d}.png"
                pygame.image.save(self.screen, frame_filename)
                frame_filenames.append(frame_filename)
            pygame.display.flip()
            pygame.time.delay(20)



Animation().animation()