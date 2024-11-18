import os
import shutil
import subprocess

# Paths to configure
repo_url = "https://github.com/07Snowman/Fs25Mods"
repo_download_folder = os.path.join(os.getcwd(), "Mods")
mods_folder = os.path.expanduser(r"~\\Documents\\My Games\\FarmingSimulator25\\Mods")

def clone_repo(repo_url, clone_folder):
    if os.path.exists(clone_folder):
        print(f"Repository folder already exists: {clone_folder}")
    else:
        print(f"Cloning repository from {repo_url}...")
        subprocess.run(["git", "clone", repo_url, clone_folder], check=True)

def move_files(source_folder, destination_folder):
    if not os.path.exists(source_folder):
        print(f"Source folder does not exist: {source_folder}")
        return

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"Created destination folder: {destination_folder}")

    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)

        if os.path.isfile(source_path):
            shutil.move(source_path, destination_path)
            print(f"Moved: {source_path} -> {destination_path}")
        else:
            print(f"Skipping non-file: {source_path}")

if __name__ == "__main__":
    clone_repo(repo_url, repo_download_folder)
    move_files(repo_download_folder, mods_folder)
