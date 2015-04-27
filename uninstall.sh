#!/bin/bash
# ------------------------------------------------------------------
# [Mark Birger] RedHead Calculator uninstaller
#          Removes mathlib library and rhcalc command.
# ------------------------------------------------------------------

python3 setup.py install --record files.txt
tr '\n' '\0' < files.txt | xargs -0 rm -f --
rm -f ./files.txt
