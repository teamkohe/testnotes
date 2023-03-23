# comment for commit
echo "Any comment?"
read comment

# Quarto
arr=()
for file in *; do
  if [ -d "$file" ]; then
    arr+=($file)
  fi
done
for dir in ${arr[@]}; do
    if [ $dir != "main_files" ]; then
        quarto render $dir/main.qmd --to html,gfm
    fi
done
quarto render main.qmd --to html,gfm

# To PDF
python3 arrange.py
arr=()
for file in *; do
  if [ -d "$file" ]; then
    arr+=($file)
  fi
done
for dir in ${arr[@]}; do
    if [ $dir != "main_files" ]; then
        pandoc --pdf-engine=lualatex -V documentclass=jlreq -V geometry:margin=1in -V fontfamily:libertinus -V fontsize=12pt -V latex-clean: true -H template.tex $dir/README.md -o $dir/main.pdf
    fi
done
pandoc --pdf-engine=lualatex -V documentclass=jlreq -V geometry:margin=1in -V fontfamily:libertinus -V fontsize=12pt -V latex-clean: true -H template.tex README.md -o main.pdf

# Git
git add .
if [ -n "$comment" ]; then
  git commit -m "$comment"
else
  date_str=$(date "+%Y-%m-%d %H:%M")
  hostname_str=$(hostname)
  git commit -m "Changes made on $date_str from $hostname_str"
fi
git push origin HEAD