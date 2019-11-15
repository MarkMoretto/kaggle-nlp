
"""
Purpose: Get data for kaggle NLP script
Date created: 2019-11-14

Contributor(s):
    Mark M.
"""



import os
import re
import shutil
import tarfile
import tempfile
import urllib.request as ureq



tar_gz_uri = r'http://www.cs.cornell.edu/people/pabo/movie-review-data/review_polarity.tar.gz'

tar_basename = os.path.basename(tar_gz_uri)
tar_filename, tar_extension = os.path.splitext(tar_basename)


with tempfile.TemporaryDirectory() as td:

    tar_path = os.path.join(td, tar_basename)
    tar_filename, tar_headers = ureq.urlretrieve(tar_gz_uri, tar_path)

    tar = tarfile.open(tar_path, "r:gz")

    for tarinfo in tar:
        print(tarinfo.name, "is", tarinfo.size, "bytes in size and is", end="")
        if tarinfo.isreg():
            print("a regular file.")
        elif tarinfo.isdir():
            print("a directory.")
        else:
            print("something else.")
    tar.close()
#- Remove directory once complete
shutil.rmtree(td.name)

tst1 = '/pos/cv999_13106.txt'

base_pat = r'.*\b{type}\b/.*\.txt'
pos_pat = base_pat.format(type='pos')
neg_pat = base_pat.format(type='neg')

re.match(pos_pat, tst1)


class Corpus:
    def __init__(self, uri):
        self.uri = uri
        self.base_name = os.path.basename(self.uri)



    def make(self):
        with tempfile.TemporaryDirectory() as td:
        
            tar_path = os.path.join(td, tar_basename)
            tar_filename, tar_headers = ureq.urlretrieve(tar_gz_uri, tar_path)
        
            tar = tarfile.open(tar_path, "r:gz")
        
            for tarinfo in tar:








