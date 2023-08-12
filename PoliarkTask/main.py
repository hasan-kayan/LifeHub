import FreeCAD
import Draft
import Arch

p1 = FreeCAD.Vector(0, 0, 0)
p2 = FreeCAD.Vector(5000, 0, 0)

# Sadece Duvar Oluşturma Kısmı
wall = Arch.makeWall(p1, p2)
FreeCAD.ActiveDocument.recompute()

# Şimdi sadece Pencere Oluşturma Kısmı
base_line = Draft.makeLine(p1, p2)
window = Arch.makeWindow(base_line, width=1000, height=1500)
FreeCAD.ActiveDocument.recompute()
