
from pathlib import Path
import operator
import json


class DatasetTools:

    def __init__(self, path=Path('.')):
        self.path = path

    def get_n_more_present_words(self, n, out=Path('.')):
        densecap_file = self.path
        object_count = {}
        with open(str(densecap_file), 'r') as df:
            data = json.load(df)
            for image in data:
                for image_object in image["objects"]:
                    object_name = image_object["names"][0]
                    if object_name not in object_count:
                        object_count[object_name] = 1
                    else:
                        object_count[object_name] = object_count[object_name] + 1

            sorted_object_count = sorted(object_count.items(), key=operator.itemgetter(1), reverse=True)
            with open(str(out), 'w+') as itof:
                for i in range(n):
                    itof.write('{}\n'.format(sorted_object_count[i][0]))

