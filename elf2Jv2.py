import json
from elftools.elf.elffile import ELFFile

# def elf_to_json(filename):
#     with open(filename, 'rb') as f:
#         elf = ELFFile(f)

#         # Extract information about each section
#         sections = []
#         for section in elf.iter_sections():
#             section_dict = {}
#             section_dict['name'] = section.name
#             section_dict['size'] = section.header.sh_size
#             section_dict['link'] = section.header.sh_link
#             sections.append(section_dict)

#         # Format the output as a table with columns for each value
#         output = []
#         column_names = ['name', 'size', 'link']
#         output.append('\t'.join(column_names))
#         for section in sections:
#             row = [str(section.get(column, '')) for column in column_names]
#             output.append('\t'.join(row))

#         return '\n'.join(output)

def elf_to_dict(filename):
    with open(filename, 'rb') as f:
        elf = ELFFile(f)

        elf_dict = {}
        elf_dict['file_type'] = elf.header.e_type
        elf_dict['machine'] = elf.header.e_machine
        elf_dict['entry_point'] = elf.header.e_entry

        # Extract information about each section
        sections = {}
        for section in elf.iter_sections():
            sections[section.name] = {
                'name': section.name,
                'size': section.header.sh_size,
                'type': section.header.sh_type,
                'flags': section.header.sh_flags,
                'address': section.header.sh_addr,
                'offset': section.header.sh_offset,
                'link': section.header.sh_link,
                'info': section.header.sh_info,
                'addralign': section.header.sh_addralign,
                'entsize': section.header.sh_entsize,
                'data': section.data().hex()
            }
        elf_dict['sections'] = sections

        # Extract information about each program header
        program_headers = []
        for segment in elf.iter_segments():
            program_header = {
                'type': segment.header.p_type,
                'offset': segment.header.p_offset,
                'vaddr': segment.header.p_vaddr,
                'paddr': segment.header.p_paddr,
                'filesz': segment.header.p_filesz,
                'memsz': segment.header.p_memsz,
                'flags': segment.header.p_flags,
                'align': segment.header.p_align
            }
            program_headers.append(program_header)
        elf_dict['program_headers'] = program_headers

        return elf_dict 
def flatten_dict(d):
    result = {}
    for key, value in d.items():
        if isinstance(value, str) or not hasattr(value, '__iter__'):
            result[key] = value
        else:
            for i, item in enumerate(value):
                result[f"{key}_{i}"] = item
    return result
     
ea1 = "/home/david/ELFDetection/ELFDetection/output/0-avelf"
# ej = elf_to_json(ea1)
ej = elf_to_dict(ea1)
# print(ej)
print(type(ej))
print(ej.keys())
nj = flatten_dict(ej)
print(nj.keys())
