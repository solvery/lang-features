
for file in $(ls .); do
    if [ -d $file ]; then
        echo $(ls $file | wc -l ) $file
    fi
done | sort -n 

