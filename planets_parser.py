import xml.etree.ElementTree as tree

planets_tree = tree.parse('planets.xml')
root = planets_tree.getroot()

print root.attrib

for child in root:
    print "tag=", child.tag, "attrib=", child.attrib['name']

for element in planets_tree.iter(tag='moon'):
    print element.attrib 




