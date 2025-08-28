# PythonAnimationScript
Quick animation script to allow you to animate a spritesheet in pygame quickly.
Stolen partly from a youtube tutorial for pygame. The Mp4 saving thing that I'm adding is made by me.

# WARNING
## I am not a good developer, I may have inadvertently put something in here that could mess up your pc. It uses system commands. So please, use at your own risk. Check all the code before you use it, and do not use it if you don't understand what some of the code does/means, especially the os stuff. If you run into bugs, report them to me at stanvol234@gmail.com.

# How to use
### 1: Go into assets and place your spritesheet. Rename it to anim.png (I may change this later)
### 2: Open main.py (must have python interpreter installed on pc) and follow the instructions on screen. You may also need pygame installed, which can be installed through pip install pygame.
### 3: In theory, in the future, it will save as an mp4 file.
*Keep in mind. All this project does is take a spritesheep, seperate it into frames and convert those into an mp4 with ffmpeg. It might be faster in a lot of cases to take the frames and compile them yourself in ffmpeg. The only benefit with this project is that you can specify the ms delay without an online converter.*

# Dependencies
### FFMPEG is needed for it to work. On windows, ffmpeg can be installed through the official website. On linux, it can be installed through the terminal command sudo apt install ffmpeg.
### The Python interpreter is also needed for the project to run. Go to python.org and download the latest version,.
### Pygame is also needed for this to run properly, as I used it for the graphics (sorry). To install pygame, run pip install pygame in the terminal AFTER having installed python.

# Bugs
### If you're using ubuntu linux, depending on the video viewing software you're using, the video may look corrupted. Try opening it in different video viewers. I found that I could see it in vscode (ik, weird).
### I don't know what bugs this will have on windows, however I do know that sometimes python files have trouble with permissions on there. If this happens, run it as admin.
### If you find any other bugs, report them to me at the email listed earlier. 

# License and copyright
### Honestly, it's open source for a reason. Do what you want with it. Idc if you credit me or not. Have fun with it!
# Credits
### CodingWithRuss on youtube for the animation window in pygame. 
