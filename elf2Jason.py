import json
from elftools.elf.elffile import ELFFile
import pandas as pd


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

    return json.dumps(elf_dict)  # ,indent=2

# sumfaild = 0
# sumwork = 0
# sumoverall = 0

# # print(elf_to_json("training-sample"))

# with open('elfAdress.txt', 'r') as f:

#     combined_data = []
#     for line in f:
#         sumoverall += 1
#         s = line.rstrip('\n')
#         try:
#           data = (elf_to_json(s))
#           data = data.rstrip('\n')
#           combined_data.append(data)
#           sumwork += 1
#         except:
#           sumfaild += 1

# data = (elf_to_json(s))
# Write the combined data to a new file
# with open('combined.json', 'w') as f:
#     json.dump(combined_data, f)

# print("res: oa = ",sumoverall,"\twork = ",sumwork,"\tfialed = ",sumfaild ,"\tprecent = ",sumwork/sumoverall)
# print("done!")

# ea1 = "/home/david/elf/VirusShare_ELF_20140617/VirusShare_861f1925ee367c5d7b95610fee2c4969"

# ea2 = "/home/david/elf/VirusShare_ELF_20140617/VirusShare_830ad2439d9b9206794e5d1a527f8ee0"
# # data1 = (elf_to_json(ea1))
# # df1 = pd.json_normalize(data1)
# f1 = elf_to_json(ea1)
# raw_ds1 = json.loads(f1)
# df1 = pd.json_normalize(raw_ds1)
# f2 = elf_to_json(ea2)
# raw_ds2 = json.loads(f2)
# df2 = pd.json_normalize(raw_ds2)
# # df1 = pd.DataFrame(data1)
# # data2 = (elf_to_json(ea2))
# # df2 = pd.json_normalize(data2)
# # df2 = pd.DataFrame(data2)
# # df1 = pd.merge(df1, df2)
# result = pd.concat([df1, df2])

# print(result.head())

def make_df_norm():
    ea1 = "/home/david/elf/VirusShare_ELF_20140617/VirusShare_861f1925ee367c5d7b95610fee2c4969"
    f1 = elf_to_json(ea1)
    raw_ds1 = json.loads(f1)
    df = pd.json_normalize(raw_ds1)
    with open('elfAdress.txt', 'r') as f:
        index = 0 
        for line in f:
            index += 1
            if index != 1:
                try:
                    s = line.rstrip('\n')
                    data = (elf_to_json(s))
                    raw_ds1 = json.loads(data)
                    df_tmep = pd.json_normalize(raw_ds1)
                    df = pd.concat([df, df_tmep])

                except:
                    continue
    df.to_pickle("packed_df.pkl")  # where to save it, usually as a .pkl



make_df_norm()
df = pd.read_pickle("packed_df.pkl")
print(df.head)
