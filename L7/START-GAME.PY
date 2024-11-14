import ctypes
import random
import time

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

def reset(mat):
    for i in range(len(mat)):
        mat[i] = [0]*len(mat[0])

def my_print(x, y, mat):
    for i in range(len(mat)):        
        line = "".join([b'\xdb'.decode('cp437') if mat[i][j] == 1 else ' ' for j in range(len(mat[0]))])
        goto_xy(x, y+i)
        color_print(line, 0x1f)    

mat = [
    [1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1],    
]

my_print(10,10,mat)

