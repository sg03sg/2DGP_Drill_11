from pico2d import *
import game_framework
from pannel import Pannel
import game_world
import play_mode
def init():
    global pannel

    pannel = Pannel()
    game_world.add_object(pannel,2)
def handle_events():
    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.pop_mode()
            elif event.key == SDLK_0:
                play_mode.boy.item = None
                game_framework.pop_mode()
            elif event.key == SDLK_1:
                play_mode.boy.item = 'Ball'
                game_framework.pop_mode()
            elif event.key == SDLK_2:
                play_mode.boy.item = 'BigBall'
                game_framework.pop_mode()

def update():
    game_world.update()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def finifh():
    global pannel
    game_world.remove_object(pannel)
    del pannel

def pause():pass
def resume():pass

