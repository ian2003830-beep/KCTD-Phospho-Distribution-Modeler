# KCTD-Phospho-Distribution-Modeler
Python simulation script for the manuscript 'Mass Spectrometry Unveils Structural and Functional Divergence of KCTDs associated with GABA-mediated Signaling'. It implements a combinatorial model to simulate the random reassembly of phosphorylated KCTD pentamers after HCD-induced dissociation.

## Overview


This repository contains the Python-based simulation script used in the manuscript "Mass Spectrometry Unveils Structural and Functional Divergence of KCTDs associated with GABA-mediated Signaling". The script implements a deterministic combinatorial model to simulate the random reassembly of phosphorylated KCTD pentamers following higher-energy collisional dissociation (HCD).


## Core Methodology


Upon HCD-induced dissociation, monomers bearing different phosphorylation states are released. Using empirically estimated relative abundances of these monomeric states, the model simulates all possible pentameric combinations under the assumption of random reassembly from a common monomer pool.The script enumerates all valid 5-monomer combinations utilizing Python’s standard itertools module. The occurrence probability for each pentameric configuration is calculated using the multinomial distribution formula:


$$P = \frac{N!}{\prod c_i!} \prod p_i^{c_i}$$


where $c_i$ represents the counts of each phosphorylation state within the pentamer, and $p_i$ is the normalized frequency of monomer species $i$ as derived from experimental measurements.


## Usage & Configuration


To run the simulation with your own experimental data, open Main.py and navigate to the bottom of the script. You can directly input your parameters in the CONFIGURATION SECTION without altering the core simulation functions.


## Parameter Definitions


CUSTOM_FILENAME: The base name for your output Excel file. If you leave this as an empty string "", the script will automatically generate a timestamped filename to prevent overwriting previous results.

VALUES: A list of integers representing the possible states of the individual monomers. In the context of KCTD, [0, 1, 2, 3] denotes monomeric states carrying 0 to 3 phosphates, respectively.

ELEMENT_COUNT: An integer defining the oligomeric state of the final assembled protein complex. Set this to 5 to simulate KCTD pentamers.

RAW_PROBABILITIES: A list of empirically derived relative abundances or MS intensities for each monomeric state. The order of these values must strictly match the order in the VALUES list. The script will automatically calculate the sum and normalize these raw inputs into true probabilities during the simulation.
