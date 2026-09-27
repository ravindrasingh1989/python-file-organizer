import os
import shutil
from pathlib import Path

# Mapping file extensions to corresponding directories
DIRECTORY_MAP = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Media": [".mp4", ".mkv", ".mp3", ".wav"],
    "Code": [".py", ".html", ".css", ".js", ".json"]
}

def organize_folder(target_dir="."):
    path = Path(target_dir)
    if not path.exists():
        print(f"Directory {target_dir} does not exist.")
        return

    for item in path.iterdir():
        if item.is_file() and item.name != "organizer.py":
            ext = item.suffix.lower()
            moved = False
            for folder, extensions in DIRECTORY_MAP.items():
                if ext in extensions:
                    dest_folder = path / folder
                    dest_folder.mkdir(exist_ok=True)
                    shutil.move(str(item), str(dest_folder / item.name))
                    print(f"Moved: {item.name} -> {folder}/")
                    moved = True
                    break
            if not moved and ext:
                other_folder = path / "Others"
                other_folder.mkdir(exist_ok=True)
                shutil.move(str(item), str(other_folder / item.name))
                print(f"Moved: {item.name} -> Others/")

if __name__ == "__main__":
    target = input("Enter directory path to organize (press Enter for current folder): ").strip()
    if not target:
        target = "."
    organize_folder(target)
    print("Organization completed successfully!")
