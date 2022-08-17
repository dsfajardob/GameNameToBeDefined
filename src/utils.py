from os import walk
import pygame



def import_folder(path):
    surface_list = []

    for _, __, img_files in walk(path):
        surface_list = [pygame.image.load(f"{path}/{image}").convert_alpha() \
            for image in img_files] 

    return surface_list
