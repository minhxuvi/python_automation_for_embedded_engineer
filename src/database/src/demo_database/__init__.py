"""Communicate with MongoDB."""

import pymongo
from pymongo import MongoClient

from test_builder import TestInput

DB = MongoClient(MONGODB_URL)

# print(DB.list_database_names())

# DB["test_builder"]["TestBuilder"] = {"dummy": 1}
test_input = TestInput(
    build_dir="/Users/moc/Projects/python_automation_for_embedded_engineer/src/demo1/_data",
    target="clean",
    os_="autosar",
    compiler="iar",
    core="M7",
)
test_input2 = TestInput(
    build_dir="/Users/moc/Projects/python_automation_for_embedded_engineer/src/demo1/_data",
    target="clean",
    os_="autosar",
    compiler="iar",
    core="M33",
)
test_input3 = TestInput(
    build_dir="/Users/moc/Projects/python_automation_for_embedded_engineer/src/demo1/_data",
    target="clean",
    os_="autosar",
    compiler="iar",
    core="A53",
)
# print(test_input.model_dump())
# print(DB["test_builder"]["TestBuilder"].insert_one(test_input.model_dump()))
# print(DB["test_builder"]["TestBuilder"].insert_one(test_input2.model_dump()))
# print(DB["test_builder"]["TestBuilder"].insert_one(test_input3.model_dump()))
test_builder_collection = DB["test_builder"]["TestBuilder"]
print(test_builder_collection.find({"target": "clean"}))
for item in test_builder_collection.find({"target": "clean"}):
    print(item)
