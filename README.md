# Improvement of liquid particle size distribution retrieval from dual-precipitation radar measurement using a deep neural network 
Notebooks that allows to replicate results obtained in Ladino et al. (2024) deep neural network particle size distribution retrieval for liquid particles

## Running the Notebooks
You can either run the notebook using [Binder](https://binder.projectpythia.org) or on your local machine.

### Running on Binder

The simplest way to interact with a Jupyter Notebook is through
[Binder](https://binder.projectpythia.org), which enables the execution of a
Jupyter Book in the cloud. The details of how this works are not
important for now. All you need to know is how to launch a Pythia
Foundations book chapter via Binder. Simply navigate your mouse to
the top right corner of the book chapter you are viewing and click
on the rocket ship icon, (see figure below), and be sure to select
“launch Binder”. After a moment you should be presented with a
notebook that you can interact with. I.e. you’ll be able to execute
and even change the example programs. You’ll see that the code cells
have no output at first, until you execute them by pressing
`Shift` `Enter`. Complete details on how to interact with
a live Jupyter notebook are described in [Getting Started with
Jupyter](https://foundations.projectpythia.org/foundations/getting-started-jupyter.html).

### Running on Your Own Machine
If you are interested in running this material locally on your computer, you will need to follow this workflow:

1. Clone the ["radar-cookbook"](https://github.com/ProjectPythia/radar-cookbook) repository
    ```bash
    git clone https://github.com/aladinor/Ladino_et_al_2024_DNN_PSD_retrieval.git
    ```

2. Move into the `radar-cookbook` directory
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
