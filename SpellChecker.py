# Import Libraries pyspellchecker, pyperclip, ttk, and tk
from spellchecker import SpellChecker
import pyperclip
from tkinter import ttk
import tkinter as tk

# Logic of the Spell Checker
## Assign variable to spellchecker tool
spell = SpellChecker()

## determine user's copied text (clipboard)
pyperclip.determine_clipboard()

# Spell Checking Logic
def spellcheck(event=None):
    ## stores the output of a copied text, a paste, into a variable
    variable = pyperclip.paste()
    ## splits multiple words into a list that can be reiterated through
    sentence_variable = variable.split()
    ## strips away punctuations
    sentence_variable2 = [s.strip(',.?:;"!') for s in sentence_variable]
    ## For Loop that shows misspelled words along with potential corrections
    for correction in sentence_variable2:
        ## Assigning the list of misspelled words and the list of potential fixes to variables
        misspelled = spell.unknown([correction])
        fixes = spell.candidates(correction)
        ## joining together misspelled and fixes so they lose the {''}, indicative of them being sets
        join_misspelled = ' '.join(misspelled)
        join_fixes = ' '.join(fixes)
        ## Pasting misspelled and fixes into text box, if ensures only misspelled words pop up
        if misspelled:
            TextBox.insert(tk.END, join_misspelled + ' ' + '->' + ' ' + join_fixes + '\n\n')


## Setting Keybind Activation to False
KeyBindActive = False

## Keybind function to activate spellcheck on activation
def keybind():
    global KeyBindActive
    KeyBindActive = not KeyBindActive
    if KeyBindActive:
        root.bind('<Command-P>', spellcheck)
        KeyBindButton.config(text='Disable KeyBind')
    else:
        root.unbind('<Command-P>')
        KeyBindButton.config(text='Enable KeyBind')

# GUI with Tkinter
## Establishing Root and frm variable to handle the frames
root = tk.Tk()
frm = ttk.Frame(root, padding=10)

## Title, Window Geometry, and creating a .grid function
root.title('Python Spell Checker :)')
root.geometry('400x500')
frm.grid()

## Configurations on a label that ensures it remains centered
root.columnconfigure(0, weight=1)
frm.columnconfigure(0, weight=1)
ttk.Label(frm, text='Python Spell Checker :)', anchor='center').grid(column=0, row=0, sticky='EW', padx=5, pady=5)

## Quit button that terminates the program
ttk.Button(frm, text='Quit', command=root.destroy).grid(column=0, row=10)

## Clipboard button that checks the current clipboard and pastes the output
ClipboardButton = ttk.Button(frm, text='Check Clipboard', command=spellcheck)
ClipboardButton.grid(column=0, row=4)

## Keybind button GUI
KeyBindButton = ttk.Button(frm, text='Enable Keybind', command=keybind)
KeyBindButton.grid(column=0, row=6)

## Text box where the output of the clipboard will be pasted
TextBox = tk.Text(frm, width=40, height=15)
TextBox.grid(column=0, row=2, sticky='EW', padx=5, pady=5)

## Button for clearing the text box
ClearButton = ttk.Button(frm, text='Clear Text', command=lambda: TextBox.delete(1.0, tk.END))
ClearButton.grid(column=0, row=8)

## Loop to keep the GUI Window open
root.mainloop()