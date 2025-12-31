import pandas as pd
import os

# 1. Load the Taxon names
print("Loading taxon names...")
taxon_df = pd.read_csv('taxon.txt', sep='\t', usecols=['id', 'scientificName'])
name_map = dict(zip(taxon_df['id'], taxon_df['scientificName']))

# 2. Setup output
output_dir = 'sanbi_flora_fixed'
if os.path.exists(output_dir):
    import shutil
    shutil.rmtree(output_dir) # Clear old folder
os.makedirs(output_dir, exist_ok=True)

# REDUCED: 6,000 rows per file to stay under the 500k word limit
rows_per_file = 6000 
file_count = 1
row_counter = 0

print("Merging and splitting into smaller chunks...")
current_file = open(f"{output_dir}/flora_part_{file_count}.txt", "w", encoding="utf-8")

for chunk in pd.read_csv('description.txt', sep='\t', chunksize=5000):
    for _, row in chunk.iterrows():
        species_name = name_map.get(row['id'], "Unknown Taxon")
        lang = row['language'] if pd.notna(row['language']) else "Unspecified"
        dtype = row['type'] if pd.notna(row['type']) else "Note"
        desc = str(row['description']).replace('\n', ' ')
        
        formatted_line = f"{species_name} | {dtype} ({lang}): {desc}\n\n"
        current_file.write(formatted_line)
        row_counter += 1
        
        if row_counter >= rows_per_file:
            current_file.close()
            print(f"Finished {output_dir}/flora_part_{file_count}.txt")
            file_count += 1
            row_counter = 0
            current_file = open(f"{output_dir}/flora_part_{file_count}.txt", "w", encoding="utf-8")

current_file.close()
print(f"\nSUCCESS: Created {file_count} files.")
