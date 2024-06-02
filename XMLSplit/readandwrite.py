import sys
import re
 
if  len(sys.argv) != 3:
    print("Invalid command line arguments, requires Source File and Target File")
    exit(1)
infile = sys.argv[1]
outfile = sys.argv[2]
try:
    with open(infile,"r+") as inFileHandle:
        fileData = inFileHandle.read()
 
    fileData = re.sub(r"\<\?xml.*\[CDATA\[","",fileData, flags=re.MULTILINE)        # Remove text with regular expression
    fileData = re.sub(r"\]\]\>\<\/DataArea\>.*","",fileData, flags=re.MULTILINE)    # Remove text with regular expression
    fileData = re.sub(r"\<psc\>.*\<\/mcd\>  ","",fileData, flags=re.MULTILINE)      # Remove text with regular expression
    try:
        outFileHandle = open(outfile, "w+")
        fileData.splitlines
        if fileData[0] == "\n":				# Remove new line if found in first line
            outFileHandle.write(fileData[1:])
        else:
            outFileHandle.write(fileData)
    except Exception as e:
        print("Error Processing the file", e)
    finally:
        inFileHandle.close()
        outFileHandle.close()
except Exception as e:
    print("Error Processing the file", e)