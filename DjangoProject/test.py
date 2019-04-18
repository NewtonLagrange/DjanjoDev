import re
import sys
s = 'index/'
result = re.search(r'.*[^/]$', s)
print(result)
a = str(b'0xa6', encoding='gbk')
print(sys.getfilesystemencoding())