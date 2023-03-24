import os
import re

def arrange(folder):
    '''
    folder/README.mdファイルの文字をGithubやPDFでちゃんと出力できるように整える関数。

    $に囲まれていないアポストロフィの挙動が嫌だったので修正した。
    $に囲まれているアスタリスクの挙動が不安定だったので修正した。
    $$に囲まれているアスタリスクの挙動が不安定だったので修正した。
    '''
    if folder is None:
        foldername = ""
    else:
        foldername = folder + "/"
    with open(foldername + "README.md", "r") as f:
        original_text = f.read()

    # TODO: ダブルクォーテーションの挙動
    # original_text = original_text.replace('“', '"').replace('”', '"')

    # Remove text between <script> and </script> tags
    pattern = re.compile(r'<script.*?</script>', flags=re.DOTALL)
    original_text = pattern.sub('', original_text)

    # Remove text between <style> and </style> tags
    pattern = re.compile(r'<style.*?</style>', flags=re.DOTALL)
    original_text = pattern.sub('', original_text)

    # For single dollar
    is_in_delimiter = False
    modified_text = ""
    for i in range(len(original_text)):
        if original_text[i] == "$":
            is_in_delimiter = not is_in_delimiter
            modified_text += original_text[i]

        # if it is not a math environment
        elif not is_in_delimiter and original_text[i] == "’":
            modified_text += "&apos;"

        # if it is a math environment
        elif is_in_delimiter and original_text[i] == "*":
            modified_text += "\\ast"

        else:
            modified_text += original_text[i]

    # For double dollars
    is_in_double_delimiter = False
    result = ""
    i = 0
    while i < len(modified_text):
        if modified_text[i:i+2] == "$$":
            is_in_double_delimiter = not is_in_double_delimiter
            result += modified_text[i:i+2]
            i += 2
        elif is_in_double_delimiter and modified_text[i] == "*":
            result += "\\ast"
            i += 1
        else:
            result += modified_text[i]
            i += 1

    with open(foldername + "README.md", "w") as f:
        f.write(result)



def replace_index_with_readme():
    '''
    メイン・ディレクトリのREADME.mdのsubdir/index.htmlをsubdir/README.mdに変える関数。
    '''
    # Define the path to the markdown file
    path_to_file = "README.md"

    # Open the file for reading
    with open(path_to_file, "r") as f:
        # Read the file contents
        file_contents = f.read()

        # Replace all instances of "index.html" with "README.md"
        new_file_contents = file_contents.replace("index.html", "README.md")

    # Open the file for writing
    with open(path_to_file, "w") as f:
        # Write the updated contents to the file
        f.write(new_file_contents)

    # Rename the file if it contains "index.html" in its name
    if "index.html" in os.path.basename(path_to_file):
        new_file_name = os.path.join(os.path.dirname(path_to_file), "README.md")
        os.rename(path_to_file, new_file_name)




subdirs = next(os.walk('.'))[1]
for folder in subdirs:
    if folder in ['main_files', '.git', '.vscode']:
        continue
    arrange(folder)
replace_index_with_readme()