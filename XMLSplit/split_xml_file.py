import xml.etree.ElementTree as ET

def split_xml_by_root(input_file, output_prefix):
    # Parse the XML document
    tree = ET.parse(input_file)
    root = tree.getroot()

    # Iterate over all direct children of the root
    for index, element in enumerate(list(root)):
        # Create a new XML tree for the current element
        new_root = ET.Element(root.tag)
        new_root.append(element)
        new_tree = ET.ElementTree(new_root)

        # Write the new XML tree to a file
        output_file = f"{output_prefix}_{index + 1}.xml"
        new_tree.write(output_file, encoding='utf-8', xml_declaration=True)
        print(f"Saved: {output_file}")

# Example usage
input_file = 'sample.xml'  # Path to your input XML file
output_prefix = 'output'  # Prefix for the output files
split_xml_by_root(input_file, output_prefix)
