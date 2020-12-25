from numpy import random

from tkinter import Tk, Canvas, Frame, BOTH


class Example(Frame):
    tiles = []
    canvas = None
    def __init__(self):
        super().__init__()

        self.add_all()
        self.draw_all()

    def add_all(self):
        for i in range(50):
            x = random.randint(500)
            y = random.randint(500)
            tile = [x, y, x + random.randint(500), y + random.randint(500), self.random_color()]
            self.tiles.append(tile)

    def random_color(self):
        rgbl = [255, 0, 0]
        random.shuffle(rgbl)
        return "#{:02x}{:02x}{:02x}".format(rgbl[0], rgbl[1], rgbl[2])

    def draw_all(self):
        self.master.title("Colours")
        self.pack(fill=BOTH, expand=1)
        if self.canvas is not None:
            self.canvas.delete("all")
        self.canvas = Canvas(self)

        for i in range(len(self.tiles)):
            self.canvas.create_rectangle(self.tiles[i][0], self.tiles[i][1], self.tiles[i][2], self.tiles[i][3],
                                    outline="#000000", fill=self.tiles[i][4])
        self.canvas.pack(fill=BOTH, expand=1)


def raises(event):
    for i in range(len(ex.tiles)):
        if ex.tiles[i][0] < event.x < ex.tiles[i][2] and event.y > ex.tiles[i][1] and event.y > ex.tiles[i][3]:
            ex.tiles = swapPositions(ex.tiles, i, len(ex.tiles) - 1)
            ex.draw_all()
            break


def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


root = Tk()
ex = Example()
root.geometry("1000x1000")
root.bind("<Button 1>", raises)
root.mainloop()























































































































