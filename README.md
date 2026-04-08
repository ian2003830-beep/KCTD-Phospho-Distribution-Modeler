# KCTD-Phospho-Distribution-Modeler

[![DOI](https://zenodo.org/badge/1203405178.svg)](https://doi.org/10.5281/zenodo.19447172)

This repository contains the Python-based simulation script used in the manuscript **"Mass Spectrometry Unveils Structural and Functional Divergence of KCTDs associated with GABA-mediated Signaling"**. It implements a deterministic combinatorial model to simulate the random reassembly of phosphorylated KCTD pentamers following higher-energy collisional dissociation (HCD).

## Core Methodology

Upon HCD-induced dissociation, monomers bearing different phosphorylation states are released. Using empirically estimated relative abundances of these monomeric states, the model simulates all possible pentameric combinations under the assumption of random reassembly from a common monomer pool. 

The script enumerates all valid 5-monomer combinations utilizing Python’s standard `itertools` module. The occurrence probability for each pentameric configuration is calculated using the multinomial distribution formula:

$$P = \frac{N!}{\prod c_i!} \prod p_i^{c_i}$$

where $c_i$ represents the counts of each phosphorylation state within the pentamer, and $p_i$ is the normalized frequency of monomer species $i$ as derived from experimental measurements.

## System Requirements

### Hardware Requirements
The script is computationally efficient and requires only a standard desktop computer with sufficient RAM to handle basic Excel file generation via `pandas`. No non-standard hardware is required.

### Software Requirements
* **Operating System:** Tested on **Windows 11**.
* **Programming Language:** **Python 3.11.9**.
* **Dependencies:**
    * `pandas == 2.2.3`
    * `openpyxl == 3.1.5` 
    * `numpy == 2.2.6`

## Installation Guide

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/](https://github.com/)[Your-Username]/KCTD-Phospho-Distribution-Modeler.git
    cd KCTD-Phospho-Distribution-Modeler
    ```

2.  **Install dependencies:**
    The required packages can be installed via pip:
    ```bash
    pip install pandas openpyxl numpy
    ```
    **Typical Installation Time:** < 3 minutes on a standard desktop.

## Demo & Instructions for Use

To verify the installation and reproduce the findings presented in our manuscript:

1.  **Run the script with default parameters:**
    For the first run, we recommend keeping the pre-configured values to ensure your environment is set up correctly. Simply execute:
    ```bash
    python Main.py
    ```

2.  **Reproduction of Manuscript Results:**
    The `CONFIGURATION SECTION` at the bottom of `Main.py` is pre-loaded with the actual experimental parameters used for the **KCTD12 oligomer phosphorylation state simulation** described in the manuscript:
    * `VALUES = [0, 1, 2, 3]` (Phosphorylation states)
    * `RAW_PROBABILITIES = [100, 48.33, 22.16, 6.38]` (Empirical intensities for KCTD12)
    * `ELEMENT_COUNT = 5` (Pentameric state)
    
    The resulting distribution probabilities in the output Excel file will be identical to the simulation data reported in the manuscript.

3.  **Applying to Your Own Data:**
    To run the simulation with your own experimental data, open `Main.py` and navigate to the **CONFIGURATION SECTION** at the bottom. You can directly input your parameters (such as `VALUES` and `RAW_PROBABILITIES`) without altering the core simulation functions. The script will automatically normalize your raw inputs and calculate the multinomial distribution for your specified oligomeric state.

**Expected Execution Time:** < 5 seconds on a standard desktop.
