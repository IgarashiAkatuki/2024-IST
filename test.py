import mongodb_utils as mu
from image import Image
from  mongodb_utils import MongoUtils
if __name__ == '__main__':

    test_image = Image("./resources/before.jpg", "./resources/after.jpg",
                       False, "Test", "IDK")

    # mu.save_image_metadata(image_metadata=test_image)
    connection_local = MongoUtils("localhost", 27017)
    connection_remote = MongoUtils("192.144.225.34", 3306)

    connection_remote.save_image_metadata(test_image)
    connection_local.save_image_metadata(test_image)