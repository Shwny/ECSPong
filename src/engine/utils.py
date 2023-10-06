from components.components import Position, RenderableRectangle, Event

# FUNCTIONS

def util_rectangle_collide_check(entity1_position: Position, 
                                entity1_dimensions: RenderableRectangle,
                                entity2_position: Position,
                                entity2_dimensions: RenderableRectangle) -> (bool):
    
    first_check: bool = entity1_position.x < entity2_position.x + entity2_dimensions.w
    second_check: bool = entity1_position.x + entity1_dimensions.w > entity2_position.x
    third_check: bool = entity1_position.y < entity2_position.y + entity2_dimensions.h
    fourth_check: bool = entity1_position.y + entity1_dimensions.h > entity2_position.y
    
    horizontal_collision = True if (first_check and second_check) else False
    vertical_collision = True if (third_check and fourth_check) else False
    
    if horizontal_collision and vertical_collision:
        return True
                
    return False

def util_handle_horizontal_collision(entity1_position: Position, 
                                entity1_dimensions: RenderableRectangle,
                                entity2_position: Position,
                                entity2_dimensions: RenderableRectangle) -> None:
    # Left-side collision
    if entity1_position.x < entity2_position.x:
        entity1_position.x = entity2_position.x - entity1_dimensions.w    
    # Right-side collision
    elif entity1_position.x > entity2_position.x:
        entity1_position.x = entity2_position.x + entity2_dimensions.w

def util_handle_vertical_collision(entity1_position: Position, 
                                entity1_dimensions: RenderableRectangle,
                                entity2_position: Position,
                                entity2_dimensions: RenderableRectangle) -> None:
    # Bottom-side collision
    if entity1_position.y < entity2_position.y:
        entity1_position.y = entity2_position.y - entity1_dimensions.h
    # Top-side collision
    elif entity1_position.y > entity2_position.y:
        entity1_position.y = entity2_position.y + entity2_dimensions.h