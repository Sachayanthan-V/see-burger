import sys
import re
import xml.etree.ElementTree as ET

def split_xml_by_root(input_data, output_prefix):
    wrapped_data = f"<root>{input_data}</root>"
    root = ET.fromstring(wrapped_data)
    
    for index, element in enumerate(list(root)):
        new_tree = ET.ElementTree(element)

        output_file = f"{output_prefix}_{index + 1}.xml"
        new_tree.write(output_file, encoding='utf-8', xml_declaration=True)
        print(f"Saved: {output_file}")

if len(sys.argv) != 3:
    print("Invalid command line arguments, requires Source File and Target File")
    exit(1)

infile = sys.argv[1]
outfile_prefix = sys.argv[2]

try:
    with open(infile, "r") as inFileHandle:
        fileData = inFileHandle.read()

    fileData = re.sub(r"\<\?xml.*\[CDATA\[", "", fileData, flags=re.MULTILINE)        # Remove text with regular expression
    fileData = re.sub(r"\]\]\>\<\/DataArea\>.*", "", fileData, flags=re.MULTILINE)    # Remove text with regular expression
    fileData = re.sub(r"\<psc\>.*\<\/mcd\>  ", "", fileData, flags=re.MULTILINE)      # Remove text with regular expression

    # Handle potential leading newline
    if fileData and fileData[0] == "\n":  # Remove new line if found in first line
        fileData = fileData[1:]

    # Split the processed data into multiple XML files
    split_xml_by_root(fileData, outfile_prefix)

except Exception as e:
    print("Error processing the file:", e)
