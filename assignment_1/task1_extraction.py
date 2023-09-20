import pymongo, os
from types import SimpleNamespace

config = SimpleNamespace(
    BASE_DIR = "/home/sugarcat/Desktop/Data Engineering Assignment Abtahe/", #include original path of text file's parent directory
    output_file_name = "year_and_company.txt",
)


class DataFetcher:
    def __init__(self):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["abtahe"]
        col = db["movies"]

        self.cursor = col.find({}, {'companies': 1, 'date': 1})
        
    
    def __iterate__(self):
        for single_item in self.cursor:
            year = single_item['date'][-4:]
            publishers = single_item['companies']

            for idx, publisher in enumerate(publishers):
                if idx > 2: 
                    break
                yc_pair = year, publisher['name']
                self.write_file(yc_pair)

    
    def write_file(self, writeable_obj):
        _file = open(os.path.join(config.BASE_DIR, config.output_file_name), "a")
        _file.write(f'{writeable_obj[0]} {writeable_obj[1]}\n')
        _file.close()

    
if __name__ == "__main__":
    data_fetcher = DataFetcher() 
    data_fetcher.__iterate__()