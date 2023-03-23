import os

def arange(folder):
    if folder is None:
        foldername = ""
    else:
        foldername = folder + "/"
    with open(foldername + "README.md", "r") as f:
        original_text = f.read()

    # original_text = original_text.replace('“', '"').replace('”', '"')

    modified_text = ""
    is_in_delimiter = False
    for i in range(len(original_text)):
        if original_text[i] == "$":
            is_in_delimiter = not is_in_delimiter
            modified_text += original_text[i]
        elif not is_in_delimiter and original_text[i] == "’":
            modified_text += "&apos;"
        else:
            modified_text += original_text[i]

    with open(foldername + "README.md", "w") as f:
        f.write(modified_text)


subdirs = next(os.walk('.'))[1]

for folder in subdirs:
    if folder in ['main_files', '.git', '.vscode']:
        continue
    arange(folder)

arange(None)
