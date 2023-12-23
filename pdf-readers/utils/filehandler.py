
def save_to_txt(content, filename):
    """
    Saves the content to a text file.
    
    Parameters
    ----------
    content : str
    filename : str
    
    Returns
    -------
    
    """
    file = f"{filename}.txt"
    with open(file, 'w', encoding="utf-8") as output:
        output.write(content)

def open_file(file_path):
    return open(file_path, 'rb')