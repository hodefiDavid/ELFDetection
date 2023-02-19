import elf2Jason as e2j
import pandas as pd

# with open('elfAdress.txt', 'r') as f:
#     df1 = pd.DataFrame()

#     sumoverall=0
#     sumwork=0
#     sumfaild=0
#     combined_data = []
#     for line in f:
#         sumoverall += 1
#         s = line.rstrip('\n')
#         try:
#           data = (e2j.elf_to_json(s))
#           df2 = pd.DataFrame(data)
#           df1 = pd.merge(df1, df2)
#           data = data.rstrip('\n')
#           combined_data.append(data)
#           sumwork += 1 
#         except:
#           sumfaild += 1 
#     print(df1.head())
ea1 = "/home/david/elf/VirusShare_ELF_20140617/VirusShare_861f1925ee367c5d7b95610fee2c4969"
ea2 = "/home/david/elf/VirusShare_ELF_20140617/VirusShare_830ad2439d9b9206794e5d1a527f8ee0"
data1 = (e2j.elf_to_json(ea1))
df1 = pd.DataFrame(data1)
data2 = (e2j.elf_to_json(ea2))
df2 = pd.DataFrame(data2)
df1 = pd.merge(df1, df2)
print(df1.head())
