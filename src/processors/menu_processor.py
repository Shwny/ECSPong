import esper
from components.components import Inputs, MenuList, GuiElementSelected

class MenuProcessor(esper.Processor):

    def __init__(self, inputs_entity, menu_list):
        super().__init__()
        self._inputs_entity = inputs_entity
        self._menu_list_entity = menu_list
        
    def process(self):
        inputs_component = esper.try_component(self._inputs_entity, Inputs)
        menu_list_component = esper.try_component(self._menu_list_entity, MenuList)

        assert(inputs_component != None)
        assert(menu_list_component != None)
        
        if inputs_component.up and menu_list_component.current_index > 0:
            current_active_voice_entity = menu_list_component.entities_list[menu_list_component.current_index] 
            current_gui_element_selected = esper.try_component(current_active_voice_entity, GuiElementSelected)
            current_gui_element_selected.value = False
            
            menu_list_component.current_index -= 1
            
            new_active_voice_entity = menu_list_component.entities_list[menu_list_component.current_index] 
            new_gui_element_selected = esper.try_component(new_active_voice_entity, GuiElementSelected)
            new_gui_element_selected.value = True

        if inputs_component.down and menu_list_component.current_index < len(menu_list_component.entities_list)-1:
            current_active_voice_entity = menu_list_component.entities_list[menu_list_component.current_index] 
            current_gui_element_selected = esper.try_component(current_active_voice_entity, GuiElementSelected)
            current_gui_element_selected.value = False
            
            menu_list_component.current_index += 1

            new_active_voice_entity = menu_list_component.entities_list[menu_list_component.current_index] 
            new_gui_element_selected = esper.try_component(new_active_voice_entity, GuiElementSelected)
            new_gui_element_selected.value = True