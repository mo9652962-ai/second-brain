import Mesh, os

ref = r"C:\Users\31954\Desktop\CAD-手机支架\iStand_reference"

# 列出所有 stl
for f in sorted(os.listdir(ref)):
    if f.endswith('.stl') and os.path.getsize(os.path.join(ref,f)) > 50000:
        m = Mesh.Mesh()
        m.read(os.path.join(ref, f))
        bb = m.BoundBox
        print(f"{f[:40]:40s} {bb.XLength:6.0f} x {bb.YLength:6.0f} x {bb.ZLength:6.0f} mm")
