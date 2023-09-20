import os, sys
from types import SimpleNamespace

sys.set_int_max_str_digits(7000)
config = SimpleNamespace(
    BASE_DIR = "/home/sugarcat/Desktop/Data Engineering Assignment Abtahe/", #include original path of text file's parent directory
    input_file_name = "task1_output.txt",
    output_file_name = "task2_bucketsort_output.txt"
)


class BucketSort:
    def insertion_sort(self, unsorted_lst):
        for j in range(1, len(unsorted_lst)):
            key = unsorted_lst[j]

            i = j - 1
            while i > -1 and unsorted_lst[i] > key:
                unsorted_lst[i + 1] = unsorted_lst[i]
                i = i - 1

            unsorted_lst[i + 1] = key
        return unsorted_lst

    def sort(self, unsorted_lst):
        mid_lst = []
        n = len(unsorted_lst)

        for i in range(n):
            mid_lst.append([])

        for i in range(n):
            val = int(n * int(unsorted_lst[i][1]) / 100)
            mid_lst[val].append(unsorted_lst[i])

        sorted_list = []
        for i in range(n-1, -1, -1):  # Loop in reverse order
            mid_lst[i] = self.insertion_sort(mid_lst[i])
            sorted_list.extend(mid_lst[i])

        return sorted_list
"""
     @Utilies class contains the data loader and data writer.
     
      - the preprocessor processes the data in the required format.
"""

class Utilities:
    def data_loader():
        data_file = open(os.path.join(config.BASE_DIR, config.input_file_name), "r")
        file_contents = data_file.readlines()
        data_contents = []
        for line in file_contents:
            data_contents.append(line.strip().split("\t"))
        return data_contents

    def preprocessing(data_item):
        return data_item[0] + ", " + data_item[1] + "\n"

    def file_write(wr_content):
        _file = open(os.path.join(config.BASE_DIR, config.output_file_name), "a")
        _file.write(Utilities.preprocessing(wr_content))
        _file.close()



if __name__ == "__main__":
    unsorted_data = Utilities.data_loader()
    sorted_data = BucketSort().sort(unsorted_data)
    
    for sr_data_item in sorted_data:
        Utilities.file_write(sr_data_item)