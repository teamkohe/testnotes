import os

# Get a list of subdirectories in the project directory
subdirs = [d for d in os.listdir() if os.path.isdir(d)]

# Loop through each subdirectory and generate a link to its index.html file
links = []
for subdir in subdirs:
    index_path = os.path.join(subdir, 'index.html')
    if os.path.exists(index_path):
        link = f'[{subdir}]({index_path})'
        links.append(link)

with open('main.qmd', 'w') as f:
    if links:
        f.write("---\n")
        f.write("format:\n")
        f.write("  html:\n")
        f.write("    output-file: \"index\"\n")
        f.write("    output-ext: \"html\"\n")
        f.write("  gfm:\n")
        f.write("    output-file: \"README\"\n")
        f.write("    output-ext: \"md\"\n")
        f.write("---\n")
        f.write("# Table of Contents\n")
        for link in links:
            f.write(f'- {link}\n')
