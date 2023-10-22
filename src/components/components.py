import pygame
from enum import Enum
from dataclasses import dataclass as component

# ENUMS 

class Event(Enum):

    # Ball events
    ball_horizontal_collision = 1
    ball_vertical_collision = 2
    score_point = 3

class Direction(Enum):
    none = None
    up = 0
    down = 1
    left = 2
    right = 3

class EntityType(Enum):
    void = 0
    ball = 1
    player = 2
    enemy = 3

# COMPONENTS

@component
class Position:
    x: int = 0
    y: int = 0

@component
class Velocity:
    value: int = 0

@component
class CurrentDirection:
    horizontal_value: Direction = Direction.none
    vertical_value: Direction = Direction.none

@component
class RenderableRectangle:
    w: int = 0
    h: int = 0

@component
class GuiElement:
    string_value: str = ""

@component
class CustomFont:
    value: pygame.font.Font = None

@component 
class ActiveElement:
    value: bool = True
        
@component
class Color:
    r: int = 0
    g: int = 0
    b: int = 0

@component
class Inputs:
    up: bool = False
    down: bool = False

@component 
class DeltaTime:
    value: int = 0

@component
class Timer:
    total_duration: int = 0
    current_value_integer: int = 0
    current_value_integer_countdown: int = 0
    current_value_millis: int = 0
    active: bool = False