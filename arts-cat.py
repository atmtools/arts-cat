# -*- coding: utf-8 -*-

import os
import pyarts
import argparse
import importlib
import ReadHitran

parser = argparse.ArgumentParser(description='Run all required updates for the Artscat')
parser.add_argument('infile', metavar='hitran_file', type=str, help='The path to the latest version of Hitran')
parser.add_argument('-w', '--working_dir', type=str, help='The path to be generated where generated data is stored', default='./tmp')
parser.add_argument('-d', '--show_diff',action='store_true', help='Show what the update did')
parser.add_argument('-x', '--skip_hitran', action='store_true', help='Skip reading hitran')
parser.add_argument('-s', '--skip_steps', help='Skip performing some steps (Reading Hitran is the 1st step)', type=int, default=0)

args = parser.parse_args()

print(args)

# create local variables
infile = os.path.abspath(args.infile)
working_dir = os.path.abspath(args.working_dir)
show_diff = True if args.show_diff else False
skip_hitran = True if args.skip_hitran else False
skip_steps = args.skip_steps

ws = pyarts.workspace.Workspace()

# create temporary work directory
if not os.path.exists(working_dir):
    print (f"Attempting to create the working directory: {working_dir}")
    os.mkdir(working_dir)
    print ("Created the working directory.  Note, this will not be removed at the end of the run, though several files might be.")
else:
    assert os.path.isdir(working_dir)
    print (f"Using the working directory: {working_dir}")

# optional skipping of reading Hitran as it takes a long time (in case there's a crash)
if not skip_hitran and not (skip_steps > 0):
    print (f"Attempting to read Hitran data from: {infile}")
    ReadHitran.run(ws, infile, working_dir)
else:
    skip_steps -= 1
    print ("Attempting to use already prepared Hitran data from the temporary directory")

# create the steps of the changes by naming the subfolders to import and run
steps = [
    "Water183",
    "Zeeman",
    "OxygenLM",
    ]

for step in steps:
    if skip_steps > 0:
        skip_steps -= 1
        print(f"Skipping step: {step}")
        continue
    
    print(f"Importing step: {step}")
    importlib.import_module(step).run(ws, working_dir, show_diff)
    print(f"Completed step: {step}")
