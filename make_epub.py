import os
import zipfile

# Change this if you want to name the file something else
OUTPUT_EPUB = 'Reverend Insanity 蛊真人.epub'
BASE_DIR = os.getcwd()

def pack_epub():
    print(f"Packaging strict standard EPUB: {OUTPUT_EPUB}...")
    
    # Remove the old epub if it exists so we don't zip the zip
    if os.path.exists(OUTPUT_EPUB):
        os.remove(OUTPUT_EPUB)
    
    with zipfile.ZipFile(OUTPUT_EPUB, 'w') as epub:
        # RULE 1: Mimetype must be added first, with ZERO compression (ZIP_STORED)
        mimetype_path = os.path.join(BASE_DIR, 'mimetype')
        if os.path.exists(mimetype_path):
            epub.write(mimetype_path, 'mimetype', compress_type=zipfile.ZIP_STORED)
            print(" -> Added uncompressed mimetype.")
        else:
            print("ERROR: mimetype file not found! Your EPUB will likely fail.")
            return
        
        # RULE 2: Add everything else with standard compression (ZIP_DEFLATED)
        for root, dirs, files in os.walk(BASE_DIR):
            # Ignore git folders and Python scripts
            if '.git' in dirs: dirs.remove('.git')
            
            for file in files:
                if file.endswith('.py') or file == 'mimetype' or file == OUTPUT_EPUB:
                    continue
                
                file_path = os.path.join(root, file)
                # Keep the internal folder structure (Volumes, META-INF, etc.) intact
                arcname = os.path.relpath(file_path, BASE_DIR)
                epub.write(file_path, arcname, compress_type=zipfile.ZIP_DEFLATED)
                
    print("Success! Your EPUB is ready to read.")

if __name__ == "__main__":
    pack_epub()