from pathlib import Path

# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/fl9ppy/Programming/pico-ducky_flashapp/assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1093x620")
window.configure(bg = "#7727F9")


canvas = Canvas(
    window,
    bg = "#7727F9",
    height = 620,
    width = 1093,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    569.0,
    330.0,
    image=image_image_1
)

canvas.create_text(
    21.0,
    17.0,
    anchor="nw",
    text="Pico Ducky Flashapp (・-・)",
    fill="#FFFFFF",
    font=("Inter Thin", 47 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=638.0,
    y=347.0,
    width=219.0,
    height=47.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=691.0,
    y=440.0,
    width=219.0,
    height=47.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=343.0,
    y=547.0,
    width=370.0,
    height=47.0
)

canvas.create_rectangle(
    19.0,
    339.0,
    601.0,
    404.0,
    fill="#E58DD1",
    outline="")

canvas.create_rectangle(
    79.0,
    431.0,
    661.0,
    496.0,
    fill="#582264",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    304.0,
    371.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#E58DD1",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=39.0,
    y=347.0,
    width=530.0,
    height=47.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    365.5,
    463.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#582264",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=86.0,
    y=440.0,
    width=559.0,
    height=45.0
)
window.resizable(False, False)
window.mainloop()
