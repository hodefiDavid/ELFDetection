from pwn import ELF
import json

def read_elf_sections(elf_file):
  elf = ELF(elf_file)
  for section in elf.sections:
    # print(section.name, hex(section.header.p_vaddr), section.header.p_memsz)
    print("\n",section.name)
    if section.data is not None:
        tmp = section.header
        # print((tmp.p_memsz))

# read_elf_sections("/home/david/elf/training-sample")

with open('elfAdress.txt', 'r') as f:
    combined_data = []
    for line in f:
        s = line.rstrip('\n')
        try:
          data = (read_elf_sections(s))
          combined_data.append(data)
        except:
          print(s)
                    
# Write the combined data to a new file
with open('combined.json', 'w') as f:
    json.dump(combined_data, f)
print("done!")