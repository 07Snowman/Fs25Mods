import os
import shutil
import subprocess
import zipfile

# Paths to configure
repo_url = "https://github.com/07Snowman/Fs25Mods/archive/refs/heads/main.zip"
repo_download_folder = os.path.join(os.getcwd(), "Mods")
mods_folder = os.path.expanduser(r"~\\Documents\\My Games\\FarmingSimulator25\\Mods")
temp_zip_path = os.path.join(os.getcwd(), "repo.zip")

def download_and_extract_repo(repo_url, temp_zip_path, extract_folder):
    if os.path.exists(extract_folder):
        print(f"Repository folder already exists: {extract_folder}")
    else:
        print(f"Downloading repository from {repo_url}...")
        subprocess.run(["curl", "-L", "-o", temp_zip_path, repo_url], check=True)

        print(f"Extracting repository to {extract_folder}...")
        with zipfile.ZipFile(temp_zip_path, "r") as zip_ref:
            zip_ref.extractall(os.getcwd())

        # Move extracted folder to the desired location
        extracted_folder = os.path.join(os.getcwd(), "Fs25Mods-main")
        if os.path.exists(extracted_folder):
            shutil.move(extracted_folder, extract_folder)
        else:
            print("Extraction failed or folder not found.")

        os.remove(temp_zip_path)  # Clean up the zip file

def move_zip_files(source_folder, destination_folder):
    if not os.path.exists(source_folder):
        print(f"Source folder does not exist: {source_folder}")
        return

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"Created destination folder: {destination_folder}")

    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)

        if os.path.isfile(source_path) and filename.endswith(".zip"):
            if not os.path.exists(destination_path) or os.path.getmtime(source_path) > os.path.getmtime(destination_path):
                shutil.move(source_path, destination_path)
                print(f"Moved: {source_path} -> {destination_path}")
            else:
                print(f"Skipped (already exists and is up-to-date): {destination_path}")
        else:
            print(f"Skipping non-zip file: {source_path}")

if __name__ == "__main__":
    download_and_extract_repo(repo_url, temp_zip_path, repo_download_folder)
    move_zip_files(repo_download_folder, mods_folder)
