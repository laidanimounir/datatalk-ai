import pandas as pd
from pathlib import Path


excel_folder = Path("data/exel")
excel_files = list(excel_folder.glob("*.xlsx")) + list(excel_folder.glob("*.csv"))

print(f" nbr ficheir exel{len(excel_files)}")
print("\nles ficheir disponible")
for file in excel_files:
    print(f"  - {file.name}")

# lire 1er ficheir exel
if excel_files:
    first_file = excel_files[0]
    print(f"\n read file {first_file.name}")
    
    if first_file.suffix == '.csv':
        df = pd.read_csv(first_file)
    else:
        df = pd.read_excel(first_file)
    
    print(f"\nعnbr ligne{len(df)}")
    print(f"\n nbr colonn{len(df.columns)}")
    print(f"\nاcolonn disponible:\n{df.columns.tolist()}")
    print(f"\n les premier 3 ligne\n{df.head(3)}")
else:
    print("لno fichir exel disponibl")

