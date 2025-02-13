import pygame
from os.path import join

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
SIZE = {"paddle": (40, 100), "ball": (30,30)}
SPEED = {"player": 500, "opponent": 450, "ball": 450}

POS = {"player": (WINDOW_WIDTH -50, WINDOW_HEIGHT/2), "opponent": (50, WINDOW_HEIGHT/2)}

COLORS = {
        "paddle": "#FF66AE",
        "paddle shadow": "#b12521",
        "ball": "#FF66AE",
        "ball shadow": "#c14f24",
        "bg": "#FFA3CE",
        "bg detail": "#004a63"
}