import os
import shutil

# Paths
BASE_DIR = r"D:\Reverend Insanity\RI"
OEBPS_DIR = os.path.join(BASE_DIR, "OEBPS")
VOLUMES_DIR = os.path.join(BASE_DIR, "Volumes")

volumes = [
    {"n": 1, "t": "A Demon's Nature Doesn't Change", "s": 0, "e": 199},
    {"n": 2, "t": "The Demon Leaves the Mountain", "s": 200, "e": 405},
    {"n": 3, "t": "The Demon Wreaks Chaos in the World", "s": 406, "e": 649},
    {"n": 4, "t": "The Demon Lord Rampages Unhindered", "s": 650, "e": 1021},
    {"n": 5, "t": "Demon King's Domination", "s": 1022, "e": 1966},
    {"n": 6, "t": "Demon Venerable's Eternal Life", "s": 1967, "e": 2334}
]

def main():
    if not os.path.exists(OEBPS_DIR):
        print(f"❌ ERROR: The folder {OEBPS_DIR} does not exist!")
        return
        
    all_files = os.listdir(OEBPS_DIR)
    print(f"✅ Found {len(all_files)} total files in the OEBPS folder. Beginning copying...\n")

    os.makedirs(VOLUMES_DIR, exist_ok=True)

    for vol in volumes:
        folder_name = f"Volume {vol['n']} - {vol['t']}"
        folder_path = os.path.join(VOLUMES_DIR, folder_name)
        
        # Clean up any broken files from previous PowerShell errors
        if os.path.isfile(folder_path):
            os.remove(folder_path)
            
        os.makedirs(folder_path, exist_ok=True)
        print(f"Processing {folder_name}...")
        
        copied_count = 0
        for i in range(vol['s'], vol['e'] + 1):
            
            possible_names = [
                f"Chapter_{i}.xhtml", 
                f"chapter_{i}.xhtml", 
                f"Chapter {i}.xhtml",
                f"chapter {i}.xhtml"
            ]
            
            for name in possible_names:
                src_path = os.path.join(OEBPS_DIR, name)
                
                if os.path.exists(src_path):
                    dest_path = os.path.join(folder_path, name)
                    # Using copy2 instead of move to preserve original files and metadata
                    shutil.copy2(src_path, dest_path)
                    copied_count += 1
                    break 
                    
        print(f"  -> Successfully copied {copied_count} chapters.")

    print("\n🎉 Done! Chapters have been copied and organized.")

if __name__ == "__main__":
    main()