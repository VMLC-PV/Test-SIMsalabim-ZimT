#####################################################
#### Clean output in folder for SIMsalabim/ZimT #####
#####################################################
# by Vincent M. Le Corre
import os
from pathlib import Path
from VLC_useful_func import clean_up_output

path2folder= Path(os.getcwd()) /'Simulation_program/DDSuite_v418/SIMsalabim'

## Clean-up outputs from folder
clean_up_output('JV', path2folder)
clean_up_output('Var', path2folder)
clean_up_output('tj', path2folder)
clean_up_output('tVG', path2folder)
clean_up_output('scPars', path2folder)
print('Ouput data was deleted from '+ str( path2folder))