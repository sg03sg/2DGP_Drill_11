from pico2d import *
import game_framework
import logo_mode

open_canvas()
game_framework.run(logo_mode)
# logo_mode.init()
# #game loop
# while logo_mode.running:
#     logo_mode.handle_events()
#     logo_mode.update()
#     logo_mode.draw()
#     delay(0.01)
# logo_mode.finish()
close_canvas()