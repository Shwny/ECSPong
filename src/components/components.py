from enum import Enum
from dataclasses import dataclass as component

# ENUMS 

class Event(Enum):
    ball_horizontal_collision = 1
    ball_vertical_collision = 2

class Direction(Enum):
    none = None
    up = 0
    down = 1
    left = 2
    right = 3

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
class Color:
    r: int = 0
    g: int = 0
    b: int = 0

@component
class Inputs:
    up: bool = False
    down: bool = False