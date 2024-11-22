import os
import shutil
import subprocess
import zipfile

# Paths to configure
repo_url = "https://github.com/07Snowman/Fs25Mods/archive/refs/heads/main.zip"
repo_download_folder = os.path.join(os.path.expanduser("~"), "Desktop", "Mods")
mods_folder = os.path.expanduser(r"~\Documents\My Games\FarmingSimulator25\Mods")
temp_zip_path = os.path.join(os.getcwd(), "repo.zip")

def download_and_extract_repo(repo_url, temp_zip_path, extract_folder):
    if os.path.exists(extract_folder):
        print(f"[DEBUG] Repository folder already exists: {extract_folder}")
    else:
        print(f"[DEBUG] Downloading repository from {repo_url} to {temp_zip_path}...")
        try:
            subprocess.run(["curl", "-L", "-o", temp_zip_path, repo_url], check=True)
            print(f"[DEBUG] Download completed: {temp_zip_path}")
        except subprocess.CalledProcessError as e:
            print(f"[ERROR] Failed to download repository: {e}")
            return

        print(f"[DEBUG] Extracting repository to {extract_folder}...")
        try:
            with zipfile.ZipFile(temp_zip_path, "r") as zip_ref:
                zip_ref.extractall(os.getcwd())
            print(f"[DEBUG] Extraction completed.")
        except zipfile.BadZipFile as e:
            print(f"[ERROR] Failed to extract zip file: {e}")
            return

        # Move extracted folder to the desired location
        extracted_folder = os.path.join(os.getcwd(), "Fs25Mods-main")
        if os.path.exists(extracted_folder):
            shutil.move(extracted_folder, extract_folder)
            print(f"[DEBUG] Moved extracted folder to: {extract_folder}")
        else:
            print("[ERROR] Extraction failed or folder not found.")

        os.remove(temp_zip_path)  # Clean up the zip file
        print(f"[DEBUG] Temporary zip file removed: {temp_zip_path}")

def move_zip_files(source_folder, destination_folder):
    if not os.path.exists(source_folder):
        print(f"[DEBUG] Source folder does not exist: {source_folder}")
        return

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"[DEBUG] Created destination folder: {destination_folder}")

    for root, _, files in os.walk(source_folder):  # Walk through all subdirectories
        for filename in files:
            source_path = os.path.join(root, filename)
            destination_path = os.path.join(destination_folder, filename)

            print(f"[DEBUG] Checking file: {filename}")
            if filename.endswith(".zip"):
                if not os.path.exists(destination_path) or os.path.getmtime(str(source_path)) > os.path.getmtime(str(destination_path)):
                    shutil.move(source_path, destination_path)
                    print(f"[DEBUG] Moved: {source_path} -> {destination_path}")
                else:
                    print(f"[DEBUG] Skipped (already exists and is up-to-date): {destination_path}")
            else:
                print(f"[DEBUG] Skipping non-zip file: {source_path}")

if __name__ == "__main__":
    print("[DEBUG] Starting script execution...")
    download_and_extract_repo(repo_url, temp_zip_path, repo_download_folder)
    move_zip_files(repo_download_folder, mods_folder)
    print("[DEBUG] Script execution completed.")