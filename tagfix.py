#!/usr/bin/env python
#
# Removes the 'revision' attribute from remotes
# on github so we can set the default revision
# to a tag such as 'refs/tags/cm-7.0.0' and rely
# on specific sha1 revisions for projects that are
# still on korg.
# 
# Creates a new file, default.xml.new, so you can
# make sure it looks correct before overwriting
# default.xml.

import re
newlines=[]
fd = open('default.xml')
for line in fd.readlines():
    if "remote=\"github\"" in line:
        line = re.sub("revision=\".*\"","",line)
    newlines.append(line)

for line in newlines:
    fd = open('default.xml.new','a')
    fd.write(line)
    fd.close()
