from kivy.app import App
from kivy.uix.graphics import RenderContext
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle, Line
import random

# Задаем ландшафтную ориентацию для тестов на ПК
Window.size = (800, 480)

class GameWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.block_size = 40
        self.world = {}
        
        # Цвета (RGB от 0.0 до 1.0)
        self.colors = {
            'grass': (34/255, 139/255, 34/255),
            'dirt': (139/255, 69/255, 19/255),
            'stone': (128/255, 128/255, 128/255),
            'deepslate': (64/255, 64/255, 64/255),
            'ore': (255/255, 215/255, 0),
            'bedrock': (0, 0, 0),
            'sky': (135/255, 206/255, 235/255)
        }
        
        # Ждем реальных размеров экрана устройства
        Clock.schedule_once(self.init_world, 0.1)

    def init_world(self, dt):
        self.cols = int(self.width // self.block_size) + 1
        self.rows = int(self.height // self.block_size) + 1
        surface_height = self.rows // 4

        for x in range(self.cols):
            for y in range(self.rows):
                # Координаты инвертированы для привычного рисования сверху вниз
                inv_y = self.rows - 1 - y
                if inv_y < surface_height:
                    self.world[(x, y)] = None
                elif inv_y == surface_height:
                    self.world[(x, y)] = 'grass'
                elif inv_y < surface_height + 3:
                    self.world[(x, y)] = 'dirt'
                elif inv_y < surface_height + 15:
                    self.world[(x, y)] = 'ore' if random.random() < 0.1 else 'stone'
                elif inv_y < self.rows - 2:
                    self.world[(x, y)] = 'ore' if random.random() < 0.15 else 'deepslate'
                else:
                    self.world[(x, y)] = 'bedrock'
        self.redraw()

    def redraw(self):
        self.canvas.clear()
        with self.canvas:
            # Рисуем небо
            Color(*self.colors['sky'])
            Rectangle(pos=self.pos, size=self.size)
            
            # Рисуем блоки
            for (x, y), block_type in self.world.items():
                if block_type:
                    Color(*self.colors[block_type])
                    pos_x = x * self.block_size
                    pos_y = y * self.block_size
                    Rectangle(pos=(pos_x, pos_y), size=(self.block_size, self.block_size))
                    # Сетка
                    Color(50/255, 50/255, 50/255, 0.5)
                    Line(rectangle=(pos_x, pos_y, self.block_size, self.block_size), width=1)

    def on_touch_down(self, touch):
        # Определение блока по нажатию пальца (работает и мышь, и тач)
        block_x = int(touch.x // self.block_size)
        block_y = int(touch.y // self.block_size)
        
        if (block_x, block_y) in self.world:
            if self.world[(block_x, block_y)] != 'bedrock':
                self.world[(block_x, block_y)] = None
                self.redraw()
        return True

class MinecraftMobileApp(App):
    def build(self):
        return GameWidget()

if __name__ == '__main__':
    MinecraftMobileApp().run()
