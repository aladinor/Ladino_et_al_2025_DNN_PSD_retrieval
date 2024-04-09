# Improvement of liquid particle size distribution retrieval from dual-precipitation radar measurement using a deep neural network 
Notebooks that allows to replicate results obtained in Ladino et al. (2024) deep neural network particle size distribution retrieval for liquid particles

[![DOI](https://zenodo.org/badge/767055605.svg)](https://zenodo.org/doi/10.5281/zenodo.10905712)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/aladinor/Ladino_et_al_2024_DNN_PSD_retrieval/main)
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aladinor/Ladino_et_al_2024_DNN_PSD_retrieval/blob/main)

## Running the Notebooks
You can either run the notebook using [Binder](https://mybinder.org/) or on your local machine.

### Running on Binder

The simplest way to interact with a Jupyter Notebook is through
[Binder](https://mybinder.org/), which enables the execution of a
Jupyter Book in the cloud. You’ll be able to execute
and even change the example programs. You’ll see that the code cells
have no output at first, until you execute them by pressing
`Shift` `Enter`. Complete details on how to interact with
a live Jupyter notebook are described in [Getting Started with
Jupyter](https://foundations.projectpythia.org/foundations/getting-started-jupyter.html).

### Running on Your Own Machine
If you are interested in running this material locally on your computer, you will need to follow this workflow:

1. Clone the ["dnn-pds-retrieval"](https://github.com/aladinor/Ladino_et_al_2024_DNN_PSD_retrieval) repository
    ```bash
    git clone https://github.com/aladinor/Ladino_et_al_2024_DNN_PSD_retrieval.git
    ```

2. Move into the `dnn-pds-retrieval` directory
    ```bash
    cd Ladino_et_al_2024_DNN_PSD_retrieval
    ```

3. Create and activate your conda environment from the `environment.yml` file
    ```bash
    conda env create -f environment.yml
    conda activate psd-retrievals
    ```

4.  Move into the `notebooks` directory and start up Jupyterlab
    ```bash
    cd notebooks/
    jupyter lab
    ```
