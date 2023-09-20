import os, re
from types import SimpleNamespace
from mrjob.job import MRJob
from mrjob.step import MRStep


config = SimpleNamespace(
    BASE_DIR = "/home/sugarcat/Desktop/Data Engineering Assignment Abtahe/", #include original path of text file's parent directory
    input_file_name = "task1_output.txt",
    output_file_name = "task1_output.txt"
)

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        tokens = re.findall(r"\b\w+\b", line)
        yield tokens, 1

    def reducer(self, key, values):
        year = key[0]
        publisher = " ".join(key[1:])
        occ_count = sum(values)
        yc_count_str = f'"{year}, {publisher}"\t{occ_count}'
        file_write(yc_count_str)
        


def file_write(wr_str):
    _fi = open(os.path.join(config.BASE_DIR, config.output_file_name), "a")
    _fi.write(str(wr_str) + "\n")
    _fi.close()


if __name__ == '__main__':
    MRWordFrequencyCount.run()
         