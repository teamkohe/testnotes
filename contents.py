import os
from bs4 import BeautifulSoup

def main():
    '''
    各サブ・ディレクトリのindex.htmlへのリンクをメイン・ディレクトリのREADME.mdに書き込む関数。
    各index.htmlの最初のヘッダー1がリンクの名前になる。
    '''
    # Get a list of subdirectories in the project directory
    subdirs = [d for d in os.listdir() if os.path.isdir(d)]

    # Loop through each subdirectory and generate a link to its index.html file
    links = []
    for subdir in subdirs:
        index_path = os.path.join(subdir, 'index.html')
        # readme_path = os.path.join(subdir, 'README.md')
        if os.path.exists(index_path):
            with open(index_path, 'r') as f:
                soup = BeautifulSoup(f.read(), 'html.parser')
                h1 = soup.find('h1')
                if h1:
                    text = h1.text.strip()
                else:
                    text = subdir
            link = f'[{text}]({index_path})'
            # link = f'[{text}]({index_path}) ([For repository]({readme_path}))'
            links.append(link)
    links.sort()

    with open('main.qmd', 'w') as f:
        if links:
            f.write("---\n")
            f.write("format:\n")
            f.write("  html:\n")
            f.write("    output-file: \"index\"\n")
            f.write("    output-ext: \"html\"\n")
            f.write("    css: styles.css\n")
            f.write("  gfm:\n")
            f.write("    output-file: \"README\"\n")
            f.write("    output-ext: \"md\"\n")
            f.write("---\n")
            f.write("# Table of Contents\n")
            for link in links:
                f.write(f'- {link}\n')

if __name__ == "__main__":
    main()