import FreeCAD

# Create a new document
doc = FreeCAD.new()

# Get the "Arch" workbench
wb = doc.getWorkbench("Arch")

# Select the wall where the window will be placed
wall = wb.getObject("Wall")

# Create a window
window = wb.addObject("Arch_Window")

# Set the window's dimensions and properties
window.Width = 1000
window.Height = 500
window.Material = "Wood"

# Add the window to the wall
wall.addObject(window)

# Update the document
doc.recompute()
