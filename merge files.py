from pprint import pprint


def read_files(file_name):
    with open(file_name, encoding="utf-8") as f:
        data = f.readlines()
        return data


def read_files_str(file_name):
    with open(file_name, encoding="utf-8") as f:
        data = ""
        for el in f.readlines():
            data += el.strip("\n")
        return data


file_1 = read_files("1.txt")
file_2 = read_files("2.txt")
file_3 = read_files("3.txt")
file_1_text = read_files_str("1.txt")
file_2_text = read_files_str("2.txt")
file_3_text = read_files_str("3.txt")

merge_list = [["1.txt", len(file_1), file_1_text],
              ["2.txt", len(file_2), file_2_text],
              ["3.txt", len(file_3), file_3_text]]

sorted_list = sorted(merge_list, key=lambda k: k[1])
final_list = []
for i in sorted_list:
    final_list.append(i[0])
    final_list.append(i[1])
    final_list.append(i[2])

pprint(final_list)

with open("merge file.txt", "w+") as f:
    for i in final_list:
        f.write(f"{i} \n")
