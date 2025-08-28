import pygame
import sys
import scripts.spritesheet as spritesheet
import os
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
                self.animation_cooldown = int(input("Animation delay in milliseconds (how much delay you want between frames, bigger = slower): "))
                loop2 = False
            except ValueError:
                print("Please enter an integer.")
        loop3 = True
        while loop3:
            try:
                self.animation_scale_x = int(input("screen scale 1 (how wide you want the screen to be. For frames 100x100, this is 1000) "))
                loop3 = False
            except:
                print("Please enter an integer.")
        loop4 = True
        while loop4:
            try:
                self.animation_scale_y = int(input("screen scale 2 (how wide you want the screen to be. For frames 100x100, this is 1000) "))
                loop4 = False
            except:
                print("Please enter an integer.")
        loop5 = True
        while loop5:
            try:
                self.frame_width = int(input("how wide is each frame? (y axis) "))
                loop5 = False
            except:
                print("Please enter an integer.")
        loop6 = True
        while loop6:
            try:
                self.frame_height = int(input("how tall is each frame? (x axis) "))
                loop6 = False
            except:
                print("Please enter an integer.")
        loop7 = True
        while loop7:
            try:
                self.frame_space = int(input("how much space is in between each frame (usually about 10, tweak it a bit to find the exact value) "))
                loop7 = False
            except:
                print("Please enter an integer")
        loop8 = True
        while loop8:
                self.frame_keep = input("do you want to keep each frame as a png? (y/n) ").lower()
                if self.frame_keep == "y":
                    self.keep_frames = True
                    loop8 = False
                elif self.frame_keep == "n":
                    self.keep_frames = False
                    loop8 = False
                else:
                    print("Please enter y or n")
                    continue
                loop8 = False

        self.screen = pygame.display.set_mode((self.animation_scale_x, self.animation_scale_y))
        self.image = pygame.image.load("assets/anim.png").convert_alpha()
        self.sprite_sheet = spritesheet.SpriteSheet(self.image)
        for i in range(self.anim_steps):   
            self.anim_list.append(self.sprite_sheet.get_image(i, self.frame_width, self.frame_height, self.frame_space))
        self.last_update = pygame.time.get_ticks()
        run = True
        frame_filenames = []
        while run:
            if self.frame < self.anim_steps:
                self.screen.fill((50, 50, 50))
                self.screen.blit(self.anim_list[self.frame], (0, 0))
                frame_filename = f"frames/f_{self.frame:04d}.png"
                frame_filenames.append(frame_filename)
            pygame.image.save(self.screen, frame_filename)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.current_time = pygame.time.get_ticks()
            if self.current_time - self.last_update >= self.animation_cooldown:
                self.frame += 1
                self.last_update = self.current_time
                if self.frame >= self.anim_steps:
                    output_file = "animation.mp4"
                    run = False
                    fps = 1000/self.animation_cooldown * 0.9
                    os.system('cd frames')
                    command = f'ffmpeg -framerate {fps} -i frames/f_%04d.png {output_file}'
                    try:
                        os.system(command)
                        loop8 = True
                        if self.keep_frames:
                            print("kept frames")
                        else:
                            shutil.rmtree("frames")
                        
                    except: 
                        print("Do you have ffmpeg installed? Consult the README for more info")


            
            pygame.display.flip()
            pygame.time.delay(20)



Animation().animation()