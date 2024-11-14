import ctypes
def raise_if_0(result, func, arguments):
    if result == 0:
        exit()

def color_print(text, color):
    _k32 = ctypes.WinDLL('kernel32', use_last_error=True)
    _GetStdHandle = _k32.GetStdHandle
    _GetStdHandle.restype = ctypes.c_void_p
    _GetStdHandle.argtypes = [ctypes.c_void_p]
    _SetConsoleTextAttribute = _k32.SetConsoleTextAttribute
    _SetConsoleTextAttribute.restype = ctypes.c_bool
    _SetConsoleTextAttribute.argtypes = [ctypes.c_void_p, ctypes.c_uint16]
    _SetConsoleTextAttribute.errcheck = raise_if_0            
    hout = _GetStdHandle(ctypes.c_void_p(-11))
    _SetConsoleTextAttribute(hout, color)
    print(text, end='', flush=True)
    _SetConsoleTextAttribute(hout, 7)

def goto_xy(x,y):
    _k32 = ctypes.WinDLL('kernel32', use_last_error=True)
    _GetStdHandle = _k32.GetStdHandle
    _GetStdHandle.restype = ctypes.c_void_p
    _GetStdHandle.argtypes = [ctypes.c_void_p]
    _SetConsoleCursorPosition = _k32.SetConsoleCursorPosition
    _SetConsoleCursorPosition.restype = ctypes.c_bool
    _SetConsoleCursorPosition.argtypes = [ctypes.c_void_p, ctypes.c_ulong]
    _SetConsoleCursorPosition.errcheck = raise_if_0            
    hout = _GetStdHandle(ctypes.c_void_p(-11))
    _SetConsoleCursorPosition(hout, ctypes.c_ulong(x + (y << 16)))


class Object:
    def __init__(self, x, y, w, h, color, label):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.label = label
        self.objects = []
        self.parent = None

    def add_object(self, obj):
        self.objects.append(obj)
        obj.parent = self

    def add_objects(self, *obj):
        for i in obj:
            self.objects.append(i)
            i.parent = self

    def draw(self):
        for i in self.objects:
            i.draw()

class Button(Object):
    def __init__(self, x, y, w, h, color, label):
        super().__init__(x, y, w, h, color, label)
        self.composed_line = "+" + "-" * (self.w - 2) + "+"
        self.middle_line = "|" + " " * (self.w - 2) + "|"
        self.panel_label = f"|{self.label:^{self.w-2}}|"

    def draw(self):
        if not self.parent:
            return
        for i in range(self.h):
            goto_xy(self.x + self.parent.x, self.y + self.parent.y + i)
            if i == 0 or i == self.h-1:
                color_print(self.composed_line, self.color)
            elif i == self.h//2:
                color_print(self.panel_label, self.color)
            else:
                color_print(self.middle_line, self.color)
            
        super().draw()


class Window(Object):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

        self.composed_line = "+" + "-" * (self.w - 2) + "+"
        self.middle_line = "|" + " " * (self.w - 2) + "|"
        self.window_label = "|" + self.label + " " * (self.w - 2 - len(self.label)) + "|"

    def draw(self):
        for i in range(self.h):
            goto_xy(self.x, self.y+i)
            if i == 0 or i == 2 or i == self.h-1:
                color_print(self.composed_line, self.color)
            elif i == 1:
                color_print(self.window_label, self.color)
            else:
                color_print(self.middle_line, self.color)

        super().draw()


class Panel(Object):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

        self.composed_line = "+" + "-" * (self.w - 2) + "+"
        self.middle_line = "|" + " " * (self.w - 2) + "|"
        self.panel_label = f"|{self.label:^{self.w-2}}|"

    def draw(self):
        if not self.parent:
            return
        for i in range(self.h):
            goto_xy(self.x + self.parent.x, self.y + self.parent.y + i)
            if i == 0 or i == self.h-1:
                color_print(self.composed_line, self.color)
            elif i == self.h//2:
                color_print(self.panel_label, self.color)
            else:
                color_print(self.middle_line, self.color)
            
        super().draw()

my_window = Window(5, 5, 200, 50, 0x1F, "Window")

# creating panels
left_panel = Panel(5, 5, 50, 30, 0x71, "Panel 1")
right_panel = Panel(60, 5, 50, 30, 0x71, "Panel 2")
panel_3 = Panel(10, 10, 40, 15, 0x2E, "Panel 2")
panel_4 = Panel(10, 10, 40, 15, 0x24, "Panel 2")


ok_button = Button(11, 15, 12, 3, 0xA0, "OK")
cancel_button = Button(27, 15, 12, 3, 0x4F, "Cancel")

left_panel.add_object(panel_3)
my_window.add_objects(left_panel, right_panel)
panel_3.add_objects(ok_button, cancel_button)

my_window.draw()









    
    
    


# goto_xy(120,60)
# color_print("Hello", 0x1D)