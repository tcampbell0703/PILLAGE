import os
import process

tagged_path = './data/test_data/csv/momentum-tagged/'
file_list = []
for ifile, file_name in enumerate(os.listdir(tagged_path)):
    file_path = tagged_path + file_name
    file_list.append(file_path)

process.process_files(file_list,"0000")


