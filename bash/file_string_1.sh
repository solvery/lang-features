
file="thisfile.txt"

echo "filename: ${file%.*}"
echo "extension: ${file##*.}"
