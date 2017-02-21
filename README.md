# misc_codes_Nuke
A collection of miscellaneous QOL scripts for nuclear structure

Recoilbeta_calculator.py calculates the initial recoil velocity of a target molecule after it has been struck by a bombarding particle of some A and Energy. 

SEMF.py is a quick utility to calculate the pairing gap in nuclei, defined in "Pairing Gaps from Nuclear Mean-Field Models" (M. Bender and K. Rutz and P.~G. Reinhard and J.~A. Maruhn)

Weisskopf_units.py calculates the Weisskopf estimates for a given nuclear isotope, defined solely by its atomic mass number, A.

delta_correction.py is a helper designed to convert old University of Kentucky outputs that give a quantity in terms of its nominal value and its upper/lower bounds instead of the nominal value and upper/lower uncertainties. This calculator will also calculate the measure of E2/M1 multipolarity mixing for a given value of delta.

gap_helper.py is the definition of a custom user script that I needed for binding energy lookups to help me calculate pairing gaps. For a particular combination of Z,A (Atomic Number, Atomic mass number, respectively), this script will output the required values for the binding energies needed to lookup manually (Note: Feb21, I never integrated this to work with SEMF.py )
