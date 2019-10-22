

import os
import re
import shutil
import tarfile
import tempfile

import urllib.request as ureq
# from zipfile import ZipFile as zf


tar_gz_base = r'http://www.cs.cornell.edu/people/pabo/movie-review-data/review_polarity.tar.gz'



tar = tarfile.open("sample.tar.gz", "r:gz")
for tarinfo in tar:
    print(tarinfo.name, "is", tarinfo.size, "bytes in size and is", end="")
    if tarinfo.isreg():
        print("a regular file.")
    elif tarinfo.isdir():
        print("a directory.")
    else:
        print("something else.")
tar.close()


td = tempfile.TemporaryDirectory()
print(td.name)

shutil.rmtree(td.name)


with ureq.urlopen(tar_gz_base) as resp:
    targz = resp.read()
    with tarfile.open(targz, mode='r:gz') as tf:
        mems = tf.extractall()



    with tarfile.open(targz, 'r') as tgzf:
        for f in tgzf:
            print(f.name)


    with tempfile.TemporaryDirectory() as td:


with tarfile.open(tar_gz_base, 'r') as tf:
    for f in tf:
        print(f.name)