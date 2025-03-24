import os
import subprocess

def setup_colab():
    """
    This function detects if the notebook is running in Google Colab.
    If so, it clones the GitHub repository and prepares the dataset.
    """
    
    if 'google.colab' in str(get_ipython()):
        print("🔹 Running in Google Colab, downloading dataset from GitHub...")

        repo_url = "https://github.com/aladinor/Ladino_et_al_2025_DNN_PSD_retrieval.git"
        
        # Clone the repository only if it hasn't been cloned already
        if not os.path.exists("/content/Ladino_et_al_2025_DNN_PSD_retrieval"):
            print(f"Cloning repository: {repo_url}")
            subprocess.run(["git", "clone", repo_url, "/content/Ladino_et_al_2025_DNN_PSD_retrieval"], check=True)
            print("Repository cloned successfully!")

        # Define dataset path
        dataset_path = "/content/Ladino_et_al_2025_DNN_PSD_retrieval/data/camp2ex_dtree.zarr"

        if os.path.exists(dataset_path):
            print(f"Dataset is available at {dataset_path}")
        else:
            print("Dataset not found in the repository! Please check the repo structure.")

setup_colab()
