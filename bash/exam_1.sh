
seq 10 | xargs
seq 10 | paste -d" " -s
seq 10 | sed ':a;$!N;s/\n/ /;ta'
seq 10 | awk -v ORS=" " '1;END{printf "\n"}'
