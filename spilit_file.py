def split_file_by_delimiter(input_file, output_prefix, delimiter='\n'):
    # Read the entire content of the input file
    with open(input_file, 'r') as file:
        content = file.read()

    # Split the content by the specified delimiter
    chunks = content.split(delimiter)

    # Write each chunk to a separate file if it's not empty
    for i, chunk in enumerate(chunks):
        if chunk.strip():  # Skip empty chunks
            output_file = f"{output_prefix}_{i+1}.txt"
            with open(output_file, 'w') as file:
                file.write(chunk)

# Example usage
split_file_by_delimiter('checker.txt', 'srivarshini', delimiter='\n')
