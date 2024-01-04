from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
# import pyautogui

app = Ursina()

player = FirstPersonController()
Sky()

# is_fullscreen = True
window.title = 'The lab'
window.borderless = False
# window.fullscreen = is_fullscreen
window.exit_button.visible = False
window.fps_counter.enabled = True

# latest_mouse_pos = pyautogui.position()
# pyautogui.FAILSAFE = False
# sensibility = 2.5
# mouse.visible = True

materials = ['images/stone.png', 'images/dosky.png', 'images/grass.png', 'images/penis.png', 'images/heart.png'] 
newBoxMeterial = 0
boxes = []
for z in range(40):
    for x in range(40):
        box = Button(color = color.white, model = 'cube', position = (x, 0, z),
                    texture = materials[newBoxMeterial], parent = scene, origin_y = 0.5)
        boxes.append(box)



def input(key):
    global newBoxMeterial
    if key == '1':
       newBoxMeterial = 0
       return
    elif key == '2':
       newBoxMeterial = 1
       return
    elif key == '3':
       newBoxMeterial = 2
       return
    elif key == '4':
       newBoxMeterial = 3
       return
    elif key == '5':
       newBoxMeterial = 4
       return
    for box in boxes:
        if box.hovered:
            if key == 'right mouse down':
                new = Button(color = color.white, model = 'cube', position = box.position + mouse.normal,
                            texture = materials[ newBoxMeterial], parent = scene, origin_y = 0.5)
                boxes.append(new)

            elif key == 'left mouse down':
                boxes.remove(box)
                destroy(box)



app.run()