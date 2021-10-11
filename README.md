# Test-SIMsalabim-ZimT

## Author
Vincent M. Le Corre (Main)\

## Description
All these codes are written to be used with the open-source drift-diffusion suit written by Prof. L. Jan Anton Koster from University of Groningen. (See [GitHub repository](https://github.com/kostergroup)) They can be used to run the simulation, plot and do analysis of the output from the simulations for both steady-state with [SIMsalabim](https://github.com/kostergroup/SIMsalabim) and transient with [ZimT](https://github.com/kostergroup/SIMsalabim).\
Codes can be ran on Windows and Linux. However, the running simulations in parallel is not possible on Windows yet. 

## Test SIMsalabim/ZimT vs Scaps
"Test_SIMsalabim_vs_SCAPS.py" and "Test_ZimT_vs_SCAPS.py" can be used to test new versions of SIMsalabim and ZimT and compare it with [SCAPS](http://scaps.elis.ugent.be/) output for different case scenarios defined in *SIMsalabim_vs_SCAPS.pptx*. Please note that as the SCAPS simulations were already ran one need to use specific parameters for a meaningful comparison, see parameters in "device_parameters_test_scaps.txt" file.

## Test SIMsalabim/ZimT physics
"Test_SIMsalabim_ZimT_physics.py" can be used to test new versions of SIMsalabim and ZimT against simple models to check if the physics is correct but also if SIMsalabim and ZimT results are consistent.

## Functions package
- "VLC_useful_func.py" contains all the necessary functions used by the different scripts.
- "SCLC_func.py" contains all the necessary functions to analyze SCLC simulation results.
- "plot_settings_screen.py" control the default setting for the plotting functions (Font size, line thickness...)
- "Clean_output_in_folder.py" additional script to easily clean the output from the simulation folder.
