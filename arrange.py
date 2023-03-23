import os

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



subdirs = next(os.walk('.'))[1]

for folder in subdirs:
    if folder in ['main_files', '.git', '.vscode']:
        continue
    arrange(folder)
arrange(None)
