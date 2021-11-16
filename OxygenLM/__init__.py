# -*- coding: utf-8 -*-

import os
import pyarts
import numpy as np

def run(ws, working_dir, show_diff):
    ws.Wigner6Init()
    ws.isotopologue_ratiosInitFromBuiltin()
    pyarts.cat.linemixing.init_ecs(ws)
    
    upp = pyarts.classes.QuantumNumbers.QuantumNumbers()
    upp["S"] = 1
    upp["Lambda"] = 0
    upp["v1"] = 0
    upp["ElectronState"] = 88
    low = pyarts.classes.QuantumNumbers.QuantumNumbers()
    low["S"] = 1
    low["Lambda"] = 0
    low["v1"] = 0
    low["ElectronState"] = 88
    qn = pyarts.classes.QuantumIdentifier()
    qn.low = low
    qn.upp = upp
    qn.type = "Transition"
    qn.spec_ind = pyarts.classes.SpeciesTag("O2-66").isot.index
    
    orig_fn = os.path.join(working_dir, "O2-66.xml")
    assert os.path.exists(orig_fn), f"Cannot find> {orig_fn}"
    
    ws.ReadXML(ws.abs_lines, orig_fn)
    
    if 'abs_lines_tmp__' not in dir(ws):
        ws.create_variable("ArrayOfAbsorptionLines", 'abs_lines_tmp__')
    ws.Copy(ws.abs_lines_tmp__, ws.abs_lines)
    
    pyarts.cat.select.select(ws, ws.abs_lines_tmp__, qn, 40e9, 130e9, 0)
    ws.abs_linesSetPopulation(ws.abs_lines_tmp__, "ByMakarovFullRelmat")
    print("Adapting oxygen band with ", len(ws.abs_lines_tmp__.value[0].lines), " lines")
    
    pyarts.cat.linemixing.adapt_lines(ws, ws.abs_lines_tmp__,
                                      t_grid=np.linspace(150, 350),
                                      pressure=1e5, order=1, robust=1,
                                      rosenkranz_adaptation=0)
    
    ws.abs_linesReplaceLines(ws.abs_lines, ws.abs_lines_tmp__)
    
    if show_diff:
        diffout = os.path.join(working_dir, "O2-66.xml.OxygenLM.diff.txt")
        print(f"Generating diff log at: {diffout}")
        ws.abs_lines.value.savexml(orig_fn+'.tmp')
        os.system(f'diff {orig_fn}.tmp {orig_fn} > {diffout}')
        os.system(f'mv {orig_fn}.tmp {orig_fn}')
    else:
        ws.abs_lines.value.savexml(orig_fn)
    