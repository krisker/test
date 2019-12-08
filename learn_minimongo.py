#! /usr/bin/env/python
# -*- coding: utf-8 -*-

from minimongo import Model, Index, collection
import json

from bson import ObjectId
from bson.json_util import dumps
from flask import make_response


class TryModel(Model):
    class Meta:
        host = "127.0.0.1"
        port = 27017
        database = "test"
        collection = "platform"

        indices = (
            Index("try_no", unique=True),
            Index("try_no1", unique=True)
        )

        # 两个唯一索引，都必须是唯一，不同于联合索引




class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


def resp(success, message, data=None):
    """
    格式化json数据
    :param success:
    :param message:
    :param data:
    :return:
    """
    return_data = dict()
    return_data['success'] = success
    return_data['msg'] = message
    return_data['data'] = json.loads(JSONEncoder().encode(data))
    # return json.dumps(return_data)
    # resp = make_response(dumps(return_data))
    # resp.headers['Content-Type'] = 'application/json'
    return return_data



if __name__ == '__main__':
    # print resp(False, u"发生了错误", {"data": "123456"})
    # print JSONEncoder().default({"sjon": 45})
    # TryModel.collection.insert_one({"try_no": 5, "try_no1": 5, "use": "test", "ui": {"uiui": "456"}})
    # TryModel.collection.insert_one({"use": "test", "ui": {"uiui": "456"}})
    TryModel({"try_no": 1, "try_no1": 12}).save()
    TryModel({"try_no": 1, "try_no1": 12}).ooo = "io"
    TryModel({"try_no": 1, "try_no1": 12}).save()

    # TryModel.collection.insert_one({})
    # import json
    # print TryModel.collection.find_one_and_replace({'use': "test"}, {"use": "test1"})
    # cursor = TryModel.collection.find({"try_no": {"$eq": 5}})
    # cursor = TryModel.collection.distinct("use")
    # print cursor
    # print cursor.count()
    # for x in cursor:
    #     print x
        # x.use = ["12", 32, 23, 456]
        # x.save()
