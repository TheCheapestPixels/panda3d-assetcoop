from panda3d.core import LODNode
from direct.showbase.ShowBase import ShowBase


base = ShowBase()

base.model = loader.load_model('shapes.blend')
base.converted = render.attach_new_node('Shapes')

for shape_root in base.model.get_children():
    shape_root.detach_node()
    lod = base.converted.attach_new_node(
        LODNode(shape_root.name)
    )
    near, far = 0, 128
    children = list(shape_root.get_children())
    children.sort(key=lambda x: x.name, reverse=True)
    for s, shape in enumerate(children):
        shape.detach_node()
        shape.clear_transform()
        for stage in shape.find_all_texture_stages():
            shape.set_texture_off(stage)

        if s == len(children)-1:
            shape.reparent_to(lod)
            shape.set_billboard_point_eye()
        else:
            try:
                shape.get_child(0).reparent_to(lod)
            except AssertionError:
                shape.reparent_to(lod)
        lod.node().add_switch(far, near)
        near = far
        far *= 2
            
    furthest_out = lod.node().get_out(len(children)-1)
    lod.node().set_switch(len(children)-1, 1024**4, furthest_out)

        
base.converted.ls()
base.converted.write_bam_file('shapes.bam')