import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file(window, text_edit):
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")]) # opens a dialog and asks user to select a text file to open; filters only files with the 'txt' extension (otherwise returns empty).

    if not filepath:
        return
    
    text_edit.delete(1.0, tk.END) # clears existing content in the 'text_edit' widget
    with open(filepath, 'r') as f: # opens file selected in read mode
        content = f.read() # reads the content
        text_edit.insert(tk.END, content) # inserts the read content into 'text_edit' widget
    window.title(f"Open File: {filepath}") # sets the title of the window to indicate which file is currently open 

def save_file(window, text_edit):
    filepath = asksaveasfilename(filetypes=[("Text Files", "*.txt")]) # opens a dialog to choose the file name and location for saving

    if not filepath: # if there is no file name, exits the function
        return

    with open(filepath, 'w') as f:
        content = text_edit.get(1.0, tk.END) # gets the text from the 'text_edit' widget
        f.write(content) # writes tehecontent to the file 
    window.title(f"Open File: {filepath}") # sets the window title, showing name of file being saved 

def main():
    '''
    This function sets up the GUI.
    '''
    window = tk.Tk() #creates main window for application
    window.title("Text Editor") # sets the title of the main window
    window.rowconfigure(0, minsize=400) # configures the row and column sizes of the grid in the main window 
    window.columnconfigure(1, minsize=500) 

    text_edit = tk.Text(window, font='Helvetica 18') # creates text widget for the main window 
    text_edit.grid(row=0, column=1) # places the text widget in the grid layout 

    frame = tk.Frame(window, relief=tk.RAISED, bd=2) # creates a frame in the main window for organizing buttons
    save_button = tk.Button(frame, text='Save', command=lambda: save_file(window, text_edit))
    open_button = tk.Button(frame, text='Open', command=lambda: open_file(window, text_edit))

    save_button.grid(row=0, column=0, padx=5, pady=5, sticky='ew') # places buttons in the grid layout of the frame 
    open_button.grid(row=1, column=0, padx=5, sticky='ew')
    frame.grid(row=0, column=0, sticky='ns') # places the frame in the main window's grid layout 

    # To use keyboard shortcuts, need to bind a command to key
    window.bind("<Control-s>, lambda x: save_file(window, text_edit")
    window.bind("<Control-o>, lambda x: open_file(window, text_edit")

    window.mainloop() # starts the Tkinter event loop, which waits for user interaction

main()