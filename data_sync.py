from mongodb_utils import MongoUtils
from image import Image


class DataSync:

    def __init__(self, local_connection: MongoUtils, remote_connection: MongoUtils):
        self.local_connection = local_connection
        self.remote_connection = remote_connection

    def save_image(self, image_metadata: Image):

        if self.local_connection is None or self.remote_connection is None:
            print("Connection not found")
            return

        try:
            self.local_connection.save_image(image_metadata)
            self.remote_connection.save_image(image_metadata)
        except Exception as e:
            print(e)
            print("Unknown Exception")

    def get_image(self, person_name):
        if self.local_connection is None:
            print("Connection not found")
            return
        return self.local_connection.get_image_metadata(person_name)

