from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle, Line
import random

class GameWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.block_size = 40
        self.world = {}
        self.build_mode = "destroy" # "destroy" или "build"
        self.world_initialized = False # Флаг, чтобы не генерировать мир дважды
        
        self.colors = {
            'grass': (34/255, 139/255, 34/255),
            'dirt': (139/255, 69/255, 19/255),
            'stone': (128/255, 128/255, 128/255),
            'deepslate': (64/255, 64/255, 64/255),
            'ore': (255/255, 215/255, 0),
            'bedrock': (0, 0, 0),
            'sky': (135/255, 206/255, 235/255)
        }
        
        # Создаем кнопку переключения режимов сразу
        self.mode_btn = Button(
            text="Режим: Ломать",
            size_hint=(None, None),
            size=(180, 50),
            background_color=(1, 0, 0, 1)
        )
        self.mode_btn.bind(on_press=self.toggle_mode)
        self.add_widget(self.mode_btn)

    # Этот метод автоматически срабатывает, когда Kivy РЕАЛЬНО растягивается на весь экран
    def on_size(self, *args):
        # Корректируем положение кнопки под новый верхний угол экрана
        self.mode_btn.pos = (10, self.height - 60)
        
        # Генерируем мир только один раз, когда экран окончательно принял форму ландшафта
        if not self.world_initialized and self.width > 100:
            self.init_world()
            self.world_initialized = True
        else:
            # Если экран просто повернулся/обновился, просто перерисовываем картинку под новый размер
            self.redraw()

    def init_world(self):
        self.cols = int(self.width // self.block_size) + 1
        self.rows = int(self.height // self.block_size) + 1
        surface_height = self.rows // 4

        for x in range(self.cols):
            for y in range(self.rows):
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

    def toggle_mode(self, instance):
        if self.build_mode == "destroy":
            self.build_mode = "build"
            self.mode_btn.text = "Режим: Ставить"
            self.mode_btn.background_color = (0, 1, 0, 1)
        else:
            self.build_mode = "destroy"
            self.mode_btn.text = "Режим: Ломать"
            self.mode_btn.background_color = (1, 0, 0, 1)

    def redraw(self):
        self.canvas.clear()
        with self.canvas:
            # Небо теперь гарантированно займет весь экран
            Color(*self.colors['sky'])
            Rectangle(pos=self.pos, size=self.size)
            
            # Отрисовка блоков строго по текущим экранным координатам
            for (x, y), block_type in self.world.items():
                if block_type:
                    Color(*self.colors[block_type])
                    pos_x = x * self.block_size
                    pos_y = y * self.block_size
                    Rectangle(pos=(pos_x, pos_y), size=(self.block_size, self.block_size))
                    
                    Color(50/255, 50/255, 50/255, 0.3)
                    Line(rectangle=(pos_x, pos_y, self.block_size, self.block_size), width=1)

    def on_touch_down(self, touch):
        if self.mode_btn.collide_point(*touch.pos):
            return super().on_touch_down(touch)

        # Теперь touch.x и touch.y идеально совпадают с блоками на экране
        block_x = int(touch.x // self.block_size)
        block_y = int(touch.y // self.block_size)
        
        if (block_x, block_y) in self.world:
            if self.build_mode == "destroy":
                if self.world[(block_x, block_y)] != 'bedrock':
                    self.world[(block_x, block_y)] = None
                    self.redraw()
            elif self.build_mode == "build":
                if self.world[(block_x, block_y)] is None:
                    self.world[(block_x, block_y)] = 'dirt'
                    self.redraw()
        return True

class MinecraftMobileApp(App):
    def build(self):
        return GameWidget()

if __name__ == '__main__':
    MinecraftMobileApp().run()
