from components.components import Position, RenderableRectangle, CollisionAxis

# FUNCTIONS

def util_rectangle_collide_check(entity1_position: Position, 
                                entity1_dimensions: RenderableRectangle,
                                entity2_position: Position,
                                entity2_dimensions: RenderableRectangle) -> (bool, CollisionAxis):
    
    first_check: bool = entity1_position.x < entity2_position.x + entity2_dimensions.width 
    second_check: bool = entity1_position.x + entity1_dimensions.width > entity2_position.x
    third_check: bool = entity1_position.y < entity2_position.y + entity2_dimensions.height
    fourth_check: bool = entity1_position.y + entity1_dimensions.height > entity2_position.y
    
    horizontal_collision = True if (first_check and second_check) else False
    vertical_collision = True if (third_check and fourth_check) else False
    
    # TODO: finish the function implementation
    if horizontal_collision and vertical_collision:
        pass
                
    
    return False