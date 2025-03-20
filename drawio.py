
from drawpyo import TreeDiagram, NodeObject, List, Page, File
from os import path

tree = TreeDiagram(
    file_path = path.join("Test Drawpyo Charts"),
    file_name = "Coffee Grinders.drawio",
    direction = "down",
    link_style = "orthogonal",
 )


new_list = List(title="List Test", tree=tree, width=200)

new_list.add_item("item 1")
new_list.add_item("item B")
new_list.add_item("item iii")

new_list.autosize()

# Top object
grinders = NodeObject(tree=tree, value="Appliances for Grinding Coffee", base_style="rounded rectangle")

# Main categories
blade_grinders = NodeObject(tree=tree, value="Blade Grinders", tree_parent=grinders)
burr_grinders = NodeObject(tree=tree, value="Burr Grinders", tree_parent=grinders)
blunt_objects = NodeObject(tree=tree, value="Blunt Objects", tree_parent=grinders)

# Other
elec_blade = NodeObject(tree=tree, value="Electric Blade Grinder", tree_parent=blade_grinders)
mnp = NodeObject(tree=tree, value="Mortar and Pestle", tree_parent=blunt_objects)

# Conical Burrs
conical = NodeObject(tree=tree, value="Conical Burrs", tree_parent=burr_grinders)
elec_conical = NodeObject(tree=tree, value="Electric", tree_parent=conical)
manual_conical = NodeObject(tree=tree, value="Manual", tree_parent=conical)

# Test List
test = NodeObject(tree=tree, value=new_list, tree_parent=grinders, tree_children=[conical, elec_conical])


tree.auto_layout()
tree.write()