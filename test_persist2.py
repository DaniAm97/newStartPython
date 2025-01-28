import pytest
from processor import persist
import psycopg2

def test_my_test():
    assert 3==3

def test_read_from_pg():
    dbObject = persist.PersistData('postgres')
    courses = dbObject.read_from_pg('futurexschema.futurex_course_catalog')
    print(len(courses[0]))  # the length should be 5
    assert 5 == (len(courses[0]))


def test_read_from_pg2():
    dbObject = persist.PersistData('postgres')
    with pytest.raises(psycopg2.errors.UndefinedTable):
        dbObject.read_from_pg('futurexschema.asdasdasdasdasdad')  # invaild table name
