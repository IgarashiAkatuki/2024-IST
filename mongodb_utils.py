from image import Image
from pymongo import MongoClient
import gridfs


class MongoUtils:

    def __init__(self, localhost, port):
        self.client = MongoClient(localhost, port)
        self.database = self.client['image']
        self.fs = gridfs.GridFS(self.database)
        self. images_collection = self.database['image_metadata']

    def save_image(self, image_url):
        with open(image_url, "rb") as image:
            temp = image.read()
            file_id = self.fs.put(temp)
            print("Image " + image_url + " have been saved successfully")
            return file_id

    def save_image_metadata(self, image_metadata: Image):
        datas = image_metadata.to_dict()

        filepath_1 = datas['filepath_1']
        filepath_2 = datas['filepath_2']
        id_1 = self.save_image(filepath_1)
        id_2 = self.save_image(filepath_2)
        datas['filepath_1'] = id_1
        datas['filepath_2'] = id_2
        result = self.images_collection.insert_one(datas)

        print("All data has been saved successfully")
        return result

    def get_image(self, image_id):
        image = self.fs.get(image_id)
        with open("./resources/images/" + str(image_id) + ".png", "wb") as f:
            f.write(image.read())
            f.close()

    def get_image_metadata(self, person_name):
        metadata = self.images_collection.find_one({
            'person_name': person_name
        })
        if metadata is None:
            print("No image metadata found")
        else:
            self.get_image(metadata['filepath_1'])
            self.get_image(metadata['filepath_2'])
            print(str(metadata))
            print("Find image metadata successfully")
            return metadata
