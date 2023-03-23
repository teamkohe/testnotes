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
python3 contents.py
quarto render main.qmd --to html,gfm

# PDF
python3 arrange.py
arr=()
for file in *; do
  if [ -d "$file" ]; then
    arr+=($file)
  fi
done
for dir in ${arr[@]}; do
    if [ $dir != "main_files" ]; then
        pandoc --pdf-engine=lualatex -V documentclass=jlreq -V geometry:margin=1in -V fontfamily:libertinus -V fontsize=12pt -H template.tex $dir/README.md -o $dir/main.pdf
    fi
done

# Git
git add .
if [ -n "$comment" ]; then
  git commit -m "$comment"
else
  date_str=$(date "+%Y-%m-%d %H:%M")
  hostname_str=$(hostname)
  # git commit -m "Changes made on $date_str from $hostname_str"
  git commit -m "Changes made on $date_str"
fi
git push origin HEAD