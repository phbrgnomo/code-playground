def decode(message_file):
    # Read the contents of the file
    with open(message_file, 'r') as file:
        lines = file.readlines()

    # Extract the numbers and words from each line
    pyramid_data = [line.strip().split(' ', 1) for line in lines if line.strip()]

    print("Original Data:", pyramid_data)

    # Sort the data based on the numbers
    pyramid_data.sort(key=lambda x: int(x[0]))

    print("Sorted Data:", pyramid_data)

    # Build the pyramid
    pyramid = []
    i = 0

    for n in range(1, len(pyramid_data) + 1):  # Adjusted the range to avoid an extra line
        row = [pyramid_data[j] for j in range(i, min(i + n, len(pyramid_data)))]  # Ensure not to go out of range
        pyramid.append(row)
        i += n

    # Remove any empty lines that might have been added
    pyramid = [line for line in pyramid if line]

    print("Constructed Pyramid:")
    for line in pyramid:
        print(line)

    # Extract the last word from each line in the pyramid
    last_words = [step[-1][1] for step in pyramid]

    print("Last Words:", last_words)

    # Build the decoded message based on the pyramid structure
    decoded_message = ' '.join(last_words)

    return decoded_message

# Example usage:
decoded_message = decode('message_file.txt')
print("Decoded Message:", decoded_message)