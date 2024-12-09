import tkinter as tk
import math


def draw_koch_segment(canvas, x1, y1, x2, y2, depth):
    """
    Recursively draws a Koch segment on the canvas.
    """
    if depth == 0:
        canvas.create_line(x1, y1, x2, y2, fill="white")
    else:
        dx = (x2 - x1) / 3
        dy = (y2 - y1) / 3

        xA = x1 + dx
        yA = y1 + dy

        xB = x1 + 2 * dx
        yB = y1 + 2 * dy

        sin60 = math.sin(math.pi / 3)
        cos60 = math.cos(math.pi / 3)

        xC = xA + (dx * cos60 - dy * sin60)
        yC = yA + (dx * sin60 + dy * cos60)

        draw_koch_segment(canvas, x1, y1, xA, yA, depth - 1)
        draw_koch_segment(canvas, xA, yA, xC, yC, depth - 1)
        draw_koch_segment(canvas, xC, yC, xB, yB, depth - 1)
        draw_koch_segment(canvas, xB, yB, x2, y2, depth - 1)


def draw_koch_snowflake(canvas, size, depth):
    """
    Draws a complete Koch snowflake on the canvas.
    """
    width = canvas.winfo_reqwidth()
    height = canvas.winfo_reqheight()

    x1, y1 = width / 2 - size / 2, height / 2 + size / (2 * math.sqrt(3))
    x2, y2 = width / 2 + size / 2, height / 2 + size / (2 * math.sqrt(3))
    x3, y3 = width / 2, height / 2 - size / math.sqrt(3)

    # Draw the three sides of the triangle
    draw_koch_segment(canvas, x1, y1, x2, y2, depth)
    draw_koch_segment(canvas, x2, y2, x3, y3, depth)
    draw_koch_segment(canvas, x3, y3, x1, y1, depth)


def main():
    window = tk.Tk()
    window.title("Koch Snowflake")

    canvas = tk.Canvas(window, width=500, height=500, bg="#81ACD9")
    canvas.pack()

    size = 300
    depth = 5
    draw_koch_snowflake(canvas, size, depth)

    window.mainloop()


if __name__ == "__main__":
    main()
