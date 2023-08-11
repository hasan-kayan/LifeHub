import FreeCAD as App
import Part
import Arch

# Yeni bir belge oluştur
doc = App.newDocument("MyDocument")

# Duvarı oluştur
wall = Arch.makeWall(length=5000, width=200, height=3000)
doc.addObject("Arch", wall)

# Pencereyi oluştur
window = Arch.makeWindow(baseobj=wall, width=800, height=1200, placement=App.Placement(App.Vector(2100, 0, 900), App.Rotation()))
doc.addObject("Arch", window)

# Belgeyi kaydet
doc.saveAs("/path/to/save/my_architecture.FCStd")

print("Duvar ve pencere oluşturuldu. Dosya kaydedildi.")
