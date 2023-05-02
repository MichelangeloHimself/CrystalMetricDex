import os

# THIS CODE SUCCESSFULLY PARSES THE HEIGHT AND WEIGHT VALUES FOUND IN THE POKEMON CRYSTAL
# DEX_ENTRIES, CONVERTS THEM TO CENTIMETERS AND HECTOGRAMS FOR USE WITH THE METRIC SYSTEM
# POKEDEX ENTRY FILES ARE FOUND IN (data/pokemon/dex_entries)
 
def parse_asm_files():
    for filename in os.listdir():
        if filename.endswith(".asm"):
            with open(filename, "r+") as f:
                lines = f.readlines()
                name_line = lines[0]
                height_weight_line = lines[1].strip()
                height_weight_line = height_weight_line.replace("dw ", "")
                height_weight_line = height_weight_line.split(';')[0].strip()
                height_str = height_weight_line.split(',')[0]
                height = int(height_str[-2:]) if len(height_str[:-2]) == 0 else int(height_str[:-2]) * 12 + int(height_str[-2:])
                weight = int(height_weight_line.split(',')[1])
                cm = round((height * 2.54))
                hg = round((weight * 0.45359237))
                new_line = f"\tdw {cm}, {hg} ; height, weight\n"
                lines[1] = new_line
                f.seek(0)
                f.writelines(lines)


parse_asm_files()
