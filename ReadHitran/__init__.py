# -*- coding: utf-8 -*-

import os
import tqdm
import pyarts

def run(ws, infile, tmpdir):
    
    a = open(infile, 'r').readlines()
    test = {}
    for line in tqdm.tqdm(a, ascii=True, desc="Reading and splitting lines"):
        key = line[:3]
        fname = os.path.join(tmpdir, key)
        
        if key not in test:
            test[key] = open(fname, 'w')
        test[key].write(line)
    
    for key in tqdm.tqdm(test, ascii=True, desc="Converting to ARTS"):
        fname = os.path.join(tmpdir, key)
        test[key].close()
        ws.abs_linesWriteSpeciesSplitXML("ascii", pyarts.cat.hitran.read(ws, fname), tmpdir + '/')
        os.remove(fname)