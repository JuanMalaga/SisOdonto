import ctypes 
user32 = ctypes.windll.user32 
width = user32.GetSystemMetrics(0)
height = user32.GetSystemMetrics(1)

print(width, height)