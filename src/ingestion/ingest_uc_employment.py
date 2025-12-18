from pathlib import Path
import shutil

from src.utils.paths import RAW_DIR

# Source CSV manually downloaded from DWP Stat-Xplore
SOURCE_FILE = Path.home() / "Downloads" / "uc_employment_status_by_gender.csv"
DEST_FILE = RAW_DIR / "uc_employment_status_by_gender.csv"

def ingest():
    # Copies raw UC employement status CSV from local Downloads into the project's raw data directory
    if not SOURCE_FILE.exists():
        raise FileNotFoundError(f"Source file not found: {SOURCE_FILE}")
    
    print(f"Ingesting {SOURCE_FILE.name} into raw layer")
    shutil.copy(SOURCE_FILE, DEST_FILE)

# Allows script to be run directly
if __name__ == "__main__":
    ingest()