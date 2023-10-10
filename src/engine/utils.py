from components.components import Position, RenderableRectangle, Event

# FUNCTIONS

## !!!! I CAN MERGET THE TWO FUNCTIONS AND CREATE A SINGLE COLLISION DETECTION AND RESPONSE FUNCTION !!!! ##

# COLLISION BETWEEN TWO ENTITIES

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

# COLLISION RESPONSE BETWEEN TWO OBJECT COLLISION

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

### NEW VERSION ###
### TESTING REQUIRED ###

def util_collide_resolve(entity1_position: Position, 
                                entity1_dimensions: RenderableRectangle,
                                entity2_position: Position,
                                entity2_dimensions: RenderableRectangle) -> (bool):
    
    # X axis intersection
    first_check: bool = entity1_position.x < entity2_position.x + entity2_dimensions.w
    second_check: bool = entity1_position.x + entity1_dimensions.w > entity2_position.x
    
    # Y axis intersection
    third_check: bool = entity1_position.y < entity2_position.y + entity2_dimensions.h
    fourth_check: bool = entity1_position.y + entity1_dimensions.h > entity2_position.y
    
    # checking conditions for intersection on each axis
    horizontal_collision = True if (first_check and second_check) else False
    vertical_collision = True if (third_check and fourth_check) else False
    
    # if there is a collision (overlap) on both axis then we respond to the collision 
    # by pushing out the first body from the second one (so entity2 is "immobile" while
    # entity1 gets its position modified)
    if horizontal_collision and vertical_collision:
        # Left-side collision
        if entity1_position.x < entity2_position.x:
            entity1_position.x = entity2_position.x - entity1_dimensions.w    
        # Right-side collision
        elif entity1_position.x > entity2_position.x:
            entity1_position.x = entity2_position.x + entity2_dimensions.w
        # Bottom-side collision
        if entity1_position.y < entity2_position.y:
            entity1_position.y = entity2_position.y - entity1_dimensions.h
        # Top-side collision
        elif entity1_position.y > entity2_position.y:
            entity1_position.y = entity2_position.y + entity2_dimensions.h
        return True
                
    return False