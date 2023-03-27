import cadquery as cq

# Based on the Gridfinity Design Reference v5:
# https://gridfinity.xyz/specification/

bottom_sketch = (
    cq.Sketch()
    .rect(35.6, 35.6)
    .vertices()
    .fillet(1.6/2)
)

result = (
    cq.Workplane("XY")
    .placeSketch(bottom_sketch)
    .extrude(0.8, taper=-45)
    .faces(">Z").wires().toPending()
    .extrude(1.8)
    .faces(">Z").wires().toPending()
    .extrude(2.15, taper=-45)
    .faces(">Z").wires().toPending()
    .extrude(24, taper=-45)
    .edges(">Z")
    .toPending()
    .offset2D(-5)
    .cutBlind(-5, taper=45)
)

show_object(result, options={"alpha": 0.0, "color": (255, 108, 47)})

# Export the object
cq.exporters.export(result, 'gridfinity-eufy-solo-indoorcam-c24-v2.3mf')
cq.exporters.export(result, 'gridfinity-eufy-solo-indoorcam-c24-v2.step')
cq.exporters.export(result, 'gridfinity-eufy-solo-indoorcam-c24-v2.stl')
