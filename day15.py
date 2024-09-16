from tkinter import filedialog
from pathlib import Path
import shutil

src_: str=filedialog.askopenfilename(title='Browse for a file')
direc_: str=filedialog.askdirectory(title='pick location of file')
destination_path:str=Path(direc_) / 'copy.png'

print(src_)
print(direc_)
print(destination_path)

