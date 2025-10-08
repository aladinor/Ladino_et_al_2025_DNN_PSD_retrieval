# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This repository contains research code for "Improvement of liquid particle size distribution retrieval from dual-precipitation radar measurement using a deep neural network" (Ladino et al. 2025). It implements deep neural networks to retrieve Normalized Gamma Size Distribution (NGSD) parameters from dual-frequency precipitation radar measurements.

## Environment Setup

The project uses conda for environment management. Set up the environment with:

```bash
conda env create -f environment.yml
conda activate psd-retrievals
```

The environment includes scientific computing packages (TensorFlow, scikit-learn, pandas, xarray, matplotlib, seaborn) and specialized atmospheric science tools (MetPy, netCDF4).

## Development Commands

### Code Quality
- **Formatting**: `black .` (configured in .pre-commit-config.yaml)
- **Pre-commit hooks**: Run automatically on commit (checks YAML, fixes trailing whitespace, applies black formatting)

### Jupyter Notebooks
```bash
cd notebooks/
jupyter lab
```

### Running Notebooks
Notebooks can be executed in three ways:
1. **Locally**: Follow setup above
2. **Binder**: Use the Binder link in README.md
3. **Google Colab**: Use the Colab badge - data downloads automatically via `scripts/colab_setup.py`

## Architecture

### Data Pipeline
1. **CSAB Filtering** (`1.CSAB-filter.ipynb`): Initial data filtering and preprocessing
2. **K-means Clustering** (`2.K-means-psd.ipynb`): Particle size distribution clustering analysis
3. **DNN Training** (`3.PSD_DNN_Training.ipynb`): Deep neural network training for parameter retrieval
4. **Rain Retrieval** (`4.Rain_retrieval.ipynb`): Application of trained models to retrieve rain parameters

### Key Components

**Data Structure:**
- `data/df_cluster.parquet`: Clustered particle size distribution data (main dataset)
- `data/camp2ex_dtree.zarr`: CAMP2EX campaign data in Zarr format
- `data/*.keras`: Trained neural network models
- `data/*.nc`: NetCDF atmospheric data files

**Neural Network Architecture:**
- 6 hidden layers with 16 neurons each
- ReLU activation functions
- Input: Radar reflectivity (Z_Ku), dual-frequency ratio (DFR), specific attenuation (K_Ka)
- Output: NGSD parameters (Dm, Nw, μ)
- Optimizer: Adamax with learning rate 0.001
- Loss function: Mean Absolute Error

**Model Variants:**
- Two-input model: Z_Ku and DFR only (`dnn_zku_zka_16x6.keras`)
- Three-input model: Z_Ku, DFR, and K_Ka (`dnn_zku_Dfr_ka_16x6.keras`)

### Notebook Structure

Each notebook follows this pattern:
- Environment detection (Colab vs local)
- Data loading from parquet/zarr files
- Dask cluster initialization for parallel processing
- Standardization using scikit-learn scalers
- Model training with early stopping
- Performance evaluation with custom metrics
- Visualization using matplotlib/seaborn

### Key Functions

**`metrics_pd(x, xpred)`**: Computes RMSE, MAE, and correlation coefficient for model evaluation
**`build_model()`**: Creates TensorFlow/Keras sequential model with specified architecture
**`PrintDot`**: Keras callback for training progress visualization

### Data Processing Patterns

- All input features are standardized using `StandardScaler`
- Train/test split: 80/20 with stratification by k-means clusters
- Early stopping with patience=20 to prevent overfitting
- Inverse transformation required for predictions since inputs are scaled

## Important Notes

- The codebase uses atmospheric science domain knowledge extensively
- Models are designed specifically for liquid particle size distribution retrieval
- Colab setup script (`scripts/colab_setup.py`) handles automatic data downloading and environment setup
- Images directory contains generated plots and figures from analysis
- All notebooks are designed to work both locally and in cloud environments (Colab/Binder)