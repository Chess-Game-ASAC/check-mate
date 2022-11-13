
## Python Pygame 

* Python Pygame (Game Development Library)

* Pygame is a cross-platform set of Python modules which is used to create video games.

* It consists of computer graphics and sound libraries designed to be used with the Python programming language.

* Installing through pip (which is what python uses to install packages)
  > py -m pip install -U pygame --user  

  then : 

  > import pygame  

* Here is the simple program of pygame which gives a basic idea of the syntax.

>import pygame  
 .  
pygame.init()  
screen = pygame.display.set_mode((400,500))  
done = False  
.
while not done:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  
    pygame.display.flip()  

* understand the basic syntax of the above program line by line:

**import pygame** - This provides access to the pygame framework and imports all functions of pygame.

**pygame.init()** - This is used to initialize all the required module of the pygame.

**pygame.display.set_mode((width, height))** - This is used to display a window of the desired size. The return value is a Surface object which is the object where we will perform graphical operations.

**pygame.event.get()** - This is used to empty the event queue. If we do not call this, the window messages will start to pile up and, the game will become unresponsive in the opinion of the operating system.

**pygame.QUIT** - This is used to terminate the event when we click on the close button at the corner of the window.

**pygame.display.flip()** - Pygame is double-buffered, so this shifts the buffers. It is essential to call this function in order to make any updates that you make on the game screen to make visible.

* **Pygame Draw** : Pygame provides geometry functions to draw simple shapes to the surface. These functions will work for rendering to any format to surfaces. Most of the functions accept a width argument to signify the size of the thickness around the edge of the shape. If the width is passed 0, then the shape will be solid(filled).

**All the drawing function takes the color argument that can be one of the following formats:

   - A pygame.Color objects
   - An (RGB) triplet(tuple/list)
   - An (RGBA) quadruplet(tuple/list)
   - An integer value that has been mapped to the surface's pixel format

* **Draw a rectangle :**
The following functions are used to draw a rectangle on the given surface.

>pygame.draw.rect(surface, color, rect)  
pygame.draw.rect(surface, color, rect, width=0)  

Parameters: 
  - surface - Screen to draw on.
  - color- This argument is used to color the given shape. The alpha value is optional if we are using a tuple.
  - rect(Rect)- Draw rectangle, position, and dimensions.
  - width(int)- This is optional to use the line thickness or to indicate that the rectangle is filled.

  >if width == 0, (default) fill the rectangle  
if width > 0, used for line thickness  
if width < 0, nothing will be drawn  

## Refrences: 

[www.javatpoint.com/pygame](https://www.javatpoint.com/pygame#:~:text=Pygame%20is%20a%20cross%2Dplatform,Pete%20Shinners%20to%20replace%20PySDL)