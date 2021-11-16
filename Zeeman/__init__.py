# -*- coding: utf-8 -*-

import os
import pyarts

def run(ws, working_dir, show_diff):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    species = ['O2-66', "O2-68", "ClO-56", "ClO-76", "OH-61", "NO-46"]
    
    for spec in species:
        orig_fn = os.path.join(working_dir, f"{spec}.xml")
        assert os.path.exists(orig_fn), f"Cannot find> {orig_fn}"
   
        ws.Touch(ws.abs_lines)
        ws.abs_lines.value.readxml(orig_fn)
        
        if show_diff:
            diffout = os.path.join(working_dir, f"{spec}.xml.Zeeman.diff.txt")
            print(f"Generating diff log at: {diffout}")
            pyarts.cat.zeeman.set(ws, ws.abs_lines, current_dir, spec).value.savexml(orig_fn+'.tmp')
            os.system(f'diff {orig_fn}.tmp {orig_fn} > {diffout}')
            os.system(f'mv {orig_fn}.tmp {orig_fn}')
        else:
            pyarts.cat.zeeman.set(ws, ws.abs_lines, current_dir, spec).value.savexml(orig_fn)
        