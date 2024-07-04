import time

# Image类，用于映射MongoDB中的image


class Image:
    def __init__(self, filepath_1, filepath_2, is_deleted=False,
                 description="", person_name="ZhangWeiwei"):
        self.filepath_1 = filepath_1  # 没有经过处理的原始图片路径
        self.filepath_2 = filepath_2  # 经过处理的图片路径
        self.is_deleted = is_deleted  # 是否被删除
        self.description = description  # 图片描述
        self.time = time.time()  # 时间戳
        self.person_name = person_name

    def to_dict(self):
        return {
            'filepath_1': self.filepath_1,
            'filepath_2': self.filepath_2,
            'is_deleted': self.is_deleted,
            'description': self.description,
            'time': self.time,
            'person_name': self.person_name
        }

    @staticmethod
    def from_dict(dictionary):
        return Image(dictionary['filepath_1'], dictionary['filepath_2'],
                     dictionary['is_deleted'], dictionary['description'], dictionary['person_name'])

    def __str__(self):
        return str(self.to_dict())