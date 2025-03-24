import os
import subprocess
import shutil
import sys

def setup_colab():
    """
    Set up a clean environment when running in Google Colab:
    - Deletes previous clones and cached data
    - Installs required Python packages
    - Clones the GitHub repo
    - Prepares the dataset
    """
    if 'google.colab' in str(get_ipython()):
        print("🔹 Detected Google Colab environment.")

        # 🧹 Clean up any existing repo or data
        repo_dir = "/content/Ladino_et_al_2025_DNN_PSD_retrieval"
        if os.path.exists(repo_dir):
            print("🧹 Removing previous repo clone...")
            shutil.rmtree(repo_dir)

        # 🧼 Optionally clean other cached files here
        dataset_path = "/content/Ladino_et_al_2025_DNN_PSD_retrieval/data/camp2ex_dtree.zarr"
        if os.path.exists(dataset_path):
            print("🧹 Removing old dataset...")
            shutil.rmtree(dataset_path)

        # 📦 Install required packages
        print("📦 Installing required packages...")
        subprocess.run([
            "pip", "install", "-q",
            "jupyterlab", "h5netcdf", "h5py", "netCDF4", "cf_xarray",
            "xarrayutils", "zarr", "pandas", "dask", "matplotlib",
            "scipy", "xlrd", "ipywidgets", "seaborn", "xhistogram",
            "imbalanced-learn", "s3fs", "hvplot", "opencv-python", "metpy",
            "scikit-learn==1.4", "tensorflow", "sphinx-pythia-theme", "pydata-sphinx-theme",
            "git+https://github.com/pydata/xarray.git"
        ], check=True)
        print("✅ Package installation complete.\n")

        # 📥 Clone fresh repo
        repo_url = "https://github.com/aladinor/Ladino_et_al_2025_DNN_PSD_retrieval.git"
        print(f"📥 Cloning repository: {repo_url}")
        subprocess.run(["git", "clone", repo_url, repo_dir], check=True)
        print("✅ Repository cloned successfully!\n")

        # ➕ Add repo to Python path
        if repo_dir not in sys.path:
            sys.path.append(repo_dir)

        # 📂 Check for dataset
        if os.path.exists(dataset_path):
            print(f"✅ Dataset is available at: {dataset_path}")
        else:
            print("⚠️ Dataset not found! Please verify the repo structure.")

# Run setup
setup_colab()
