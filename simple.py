from Tkinter import *                  # Import everything from Tkinter
from Arena   import Arena              # Import our Arena
from WalkingTurtle  import WalkingTurtle             # Import our WalkingTurtle
from Vector  import *                  # Import everything from our Vector

tk = Tk()                              # Create a Tk top-level widget
arena = Arena(tk)                      # Create an Arena widget, arena
arena.pack()                           # Tell arena to pack itself on screen
arena.add(WalkingTurtle(Vector(200,200), 0,5))  # Add a very simple, basic WalkingTurtle
tk.mainloop()                          # Enter the Tkinter event loop
