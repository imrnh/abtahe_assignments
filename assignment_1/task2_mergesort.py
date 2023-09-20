import os
from types import SimpleNamespace

config = SimpleNamespace(
    BASE_DIR = "/home/sugarcat/Desktop/Data Engineering Assignment Abtahe/", #include original path of text file's parent directory
    input_file_name = "task1_output.txt",
    output_file_name = "task2_mergesort_output.txt"
)





class MergeSort:
    def sort(self, lst):
        if(len(lst) <= 1):
            return lst
        mid = len(lst) //2
        left = self.sort(lst[:mid])
        right = self.sort(lst[mid:])
        return self.merge(left, right)


    def merge(self, left, right):
        _output_arr = []
        i, j = 0, 0

        while i< len(left) and j<len(right):
            if(left[i][1] < right[j][1]):
                _output_arr.append(left[i])
                i+=1
            else:
                _output_arr.append(right[j])
                j+=1

        _output_arr += left[i:]
        _output_arr += right[j:]

        return _output_arr




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
    sorted_data = MergeSort().sort(unsorted_data)
    
    for sr_data_item in sorted_data:
        Utilities.file_write(sr_data_item)