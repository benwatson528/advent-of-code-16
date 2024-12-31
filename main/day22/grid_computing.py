import tkinter
from itertools import combinations


def solve_viable(grid) -> int:
    counter = 0
    for coord_pairs in list(combinations(grid.keys(), 2)):
        counter += 1 if is_viable(coord_pairs, grid) else 0
        counter += 1 if is_viable((coord_pairs[1], coord_pairs[0]), grid) else 0
    return counter


def is_viable(coord_pairs, grid):
    a_coords, a_props = coord_pairs[0], grid[coord_pairs[0]]
    b_coords, b_props = coord_pairs[1], grid[coord_pairs[1]]
    if a_props[1] == 0:
        return False
    if a_coords == b_coords:
        return False
    if a_props[1] > b_props[2]:
        return False
    return True


def solve_traverse(input_grid) -> int:
    global start
    global end
    global count
    global grid
    global clicked
    start = max(x for x, _ in input_grid.keys()), 0
    end = 0, 0
    count = 0
    grid = input_grid
    clicked = None
    root = tkinter.Tk()
    root.title("Grid Computing")
    root.geometry("2000x1300")

    frame = tkinter.Frame(root)
    frame.pack(pady=10)

    max_x, max_y = max(x for x, _ in grid.keys()), max(y for _, y in grid.keys())
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            button = create_button(frame, x, y)
            button.grid(row=y, column=x)

    root.mainloop()
    return -1


def create_button(frame, x, y):
    size, used, available, usage_pct = grid[(x, y)]
    button = tkinter.Button(frame, text=f"{used}/{size}")
    button.config(height=2, width=5, bg=set_colour(x, y), command=lambda: on_click(button, x, y))
    return button


def set_colour(x, y):
    if (x, y) == start:
        return "yellow"
    elif (x, y) == end:
        return "green"
    else:
        return "white"


def on_click(button, x, y):
    global count, grid, start, end, clicked

    if not clicked:
        clicked = (button, x, y)
    else:
        c_button, c_x, c_y = clicked
        b_size, b_used, b_available, b_usage_pct = grid[(x, y)]
        c_size, c_used, c_available, c_usage_pct = grid[(c_x, c_y)]

        if c_used > b_available or (c_x, c_y) == (x, y):
            clicked = None
            return

        if (c_x, c_y) == start:
            start = (c_x, c_y)
            button["bg"] = "yellow"
        grid[(x, y)] = b_size, b_used + c_used, b_available - c_used, int(((b_used + c_used) / b_available) * 100)
        grid[(c_x, c_y)] = c_size, 0, c_size, 0
        c_button["text"] = f"0/{c_size}"
        button["text"] = f"{b_used + c_used}/{b_size}"

        clicked = None
        count += 1
        print(f"count = {count} moving ({c_x},{c_y}) to ({x},{y})")
