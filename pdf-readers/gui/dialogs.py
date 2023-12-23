from tkinter import Tk, filedialog

def select_files(file_type):
    """
    Selects files from the file dialog.

    Parameters
    ----------
    file_type : str
        The file type to select.

    Returns
    -------
    file_paths : list
        The selected file paths.
    """
    root = Tk()
    root.withdraw()
    file_paths = filedialog.askopenfilenames(title=f"Select files {file_type}", filetypes=[(f"{file_type} files", f"*.{file_type}")])
    return file_paths