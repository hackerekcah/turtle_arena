from Tkinter import *
from Arena   import Arena
from Vector  import *
from Statue  import Statue
from Mouse   import Mouse
from Cat     import Cat
from Mouse import METER


tk = Tk()
arena = Arena(tk)
arena.pack()


statue  = Statue(Vector(200,200), 0)
mouse   = Mouse(Vector(230, 200), 0, METER)
cat     = Cat(Vector(350, 200), 0, 1.25*METER, mouse)


arena.add(statue)
arena.add(mouse)
arena.add(cat)

tk.mainloop()

