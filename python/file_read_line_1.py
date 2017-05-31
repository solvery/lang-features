# lang-features
# 去除文本中的空行

import sys
import re

p = re.compile(r'(^\n$)')

filename=sys.argv[1]
with open (filename, "r") as fd_in:
    for line in fd_in.readlines():
        m = p.search(line)
        if not m:
            print line,
