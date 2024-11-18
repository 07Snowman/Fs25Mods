# Define repository download URL and file paths
$repoUrl = "https://github.com/07Snowman/Fs25Mods/archive/refs/heads/main.zip"
$zipFile = "repo.zip"
$extractPath = [System.IO.Path]::Combine($env:USERPROFILE, "Desktop", "Mods")
$batFile = [System.IO.Path]::Combine($extractPath, "Fs25Mods-main", "run.bat")


# Step 1: Download repository as a ZIP file
Write-Host "[INFO] Downloading repository..."
Invoke-RestMethod -Uri $repoUrl -OutFile $zipFile
Write-Host "[INFO] Download complete: $zipFile"

# Step 2: Extract the ZIP file
Write-Host "[INFO] Extracting repository..."
Expand-Archive -Path $zipFile -DestinationPath $extractPath -Force
Write-Host "[INFO] Extraction complete: $extractPath"

# Step 3: Clean up the ZIP file
Remove-Item $zipFile
Write-Host "[INFO] Cleaned up temporary files."

# Step 4: Automatically run the run.bat script
if (Test-Path $batFile) {
    Write-Host "[INFO] Running the batch file: $batFile"
    Start-Process -FilePath $batFile -NoNewWindow -Wait
    Write-Host "[INFO] Batch file execution completed."
} else {
    Write-Host "[ERROR] Batch file not found: $batFile"
}

# Step 5: Notify completion
Write-Host "[INFO] Setup completed successfully!"
