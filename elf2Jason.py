import json
from elftools.elf.elffile import ELFFile


def elf_to_json(elf_file_path):

    with open(elf_file_path, 'rb') as f:

        elf_file = ELFFile(f)

        sections = []
        
        for section in elf_file.iter_sections():
                
            section_dict = {}           
            section_dict['name'] = section.name                                       
            section_dict['type'] = section['sh_type']
            section_dict['flags'] = section['sh_flags']
            section_dict['addr'] = section['sh_addr']
            section_dict['offset'] = section['sh_offset']
            section_dict['size'] = section['sh_size']
            section_dict['link'] = section['sh_link']
            section_dict['info'] = section['sh_info']
            section_dict['align'] = section['sh_addralign']
            section_dict['entsize'] = section['sh_entsize']
            sections.append(section_dict)
                                                                                                                                                                                                                                                                                                                            
        elf_dict = {}
  
        elf_dict['header'] = {}
        elf_dict['header']['type'] = elf_file.header['e_type']
        elf_dict['header']['machine'] = elf_file.header['e_machine']
        elf_dict['header']['version'] = elf_file.header['e_version']
        elf_dict['header']['entry'] = elf_file.header['e_entry']
        elf_dict['header']['phoff'] = elf_file.header['e_phoff']
        elf_dict['header']['shoff'] = elf_file.header['e_shoff']
        elf_dict['header']['flags'] = elf_file.header['e_flags']
        elf_dict['header']['ehsize'] = elf_file.header['e_ehsize']
        elf_dict['header']['phentsize'] = elf_file.header['e_phentsize']
        elf_dict['header']['phnum'] = elf_file.header['e_phnum']
        elf_dict['header']['shentsize'] = elf_file.header['e_shentsize']
        elf_dict['header']['shnum'] = elf_file.header['e_shnum']
        elf_dict['header']['shstrndx'] = elf_file.header['e_shstrndx']
        elf_dict['sections'] = sections


    return json.dumps(elf_dict) # ,indent=2

sumfaild = 0
sumwork = 0 
sumoverall = 0

# print(elf_to_json("training-sample"))

with open('elfAdress.txt', 'r') as f:
    
    combined_data = []
    for line in f:
        sumoverall += 1
        s = line.rstrip('\n')
        try:
          data = (elf_to_json(s))
          data = data.rstrip('\n')
          combined_data.append(data)
          sumwork += 1 
        except:
          sumfaild += 1 

data = (elf_to_json(s))                    
# Write the combined data to a new file
with open('combined.json', 'w') as f:
    json.dump(combined_data, f)

print("res: oa = ",sumoverall,"\twork = ",sumwork,"\tfialed = ",sumfaild ,"\tprecent = ",sumwork/sumoverall)
print("done!")