from tkinter import *

def paint_text(x, y, txt):
    canvas.create_text(x, y, fill="#F4F4F4", font="Calibri 16", text=txt)


def is_prime(n):
    # Проверка на простое число
    # return True - если простое
    # return False - если нет


width = 500
height = 500
bg_color = "#0A0921"
size = 13
point = str(1)

window = Tk()
window.title("Спираль простых чисел")
window.geometry(str(width+10)+"x"+str(height))
window.config(bg=bg_color)

canvas = Canvas(
    window,
    width=width,
    height=height,
    bg=bg_color
)
canvas.pack()

previous_x = width / 2
previous_y = height / 2
paint_text(previous_x, previous_y, point)
point = str(int(point)+1)
to_right = True
to_top = True
step = 40

for i in range(size):
    for j1 in range(i):
        if to_right:
            previous_x = previous_x - step
        else:
            previous_x = previous_x + step
        if is_prime(int(point)):
            paint_text(previous_x, previous_y, point)
        point = str(int(point) + 1)
    for j2 in range(i):
        if to_top:
            previous_y = previous_y - step
        else:
            previous_y = previous_y + step
        if is_prime(int(point)):
            paint_text(previous_x, previous_y, point)
        point = str(int(point)+1)
    to_right = not to_right
    to_top = not to_right

window.mainloop()
