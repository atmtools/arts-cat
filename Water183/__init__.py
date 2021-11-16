# -*- coding: utf-8 -*-

import os
import pyarts

def run(ws, working_dir, show_diff):
    orig_fn = os.path.join(working_dir, "H2O-161.xml")
    repl_fn = os.path.join(os.path.dirname(os.path.abspath(__file__)), "repl_line.xml")
    
    assert os.path.exists(orig_fn), f"Cannot find> {orig_fn}"
    assert os.path.exists(repl_fn), f"Cannot find> {repl_fn}"
    
    if 'abs_lines_tmp__' not in dir(ws):
        ws.create_variable("ArrayOfAbsorptionLines", 'abs_lines_tmp__')
    
    ws.Touch(ws.abs_lines_tmp__)
    ws.abs_lines_tmp__.value.readxml(repl_fn)
    
    ws.Touch(ws.abs_lines)
    ws.abs_lines.value.readxml(orig_fn)
    
    ws.abs_linesReplaceLines(ws.abs_lines, ws.abs_lines_tmp__)
    
    if show_diff:
        diffout = os.path.join(working_dir, "H2O-161.xml.Water183.diff.txt")
        print(f"Generating diff log at: {diffout}")
        ws.abs_lines.value.savexml(orig_fn + '.tmp')
        os.system(f'diff {orig_fn}.tmp {orig_fn} > {diffout}')
        os.system(f'mv {orig_fn}.tmp {orig_fn}')
    else:
        ws.abs_lines.value.savexml(orig_fn)
    