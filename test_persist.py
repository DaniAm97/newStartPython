import unittest

import psycopg2.errors

from processor import persist

class PersistDataTest(unittest.TestCase):
    def test_read_from_pg(self):
        dbObject  =persist.PersistData('postgres')
        courses = dbObject.read_from_pg('futurexschema.futurex_course_catalog')
        print(len(courses[0])) # the length should be 5
        self.assertEqual(len(courses[0]), 5)

    def test_read_from_pg2(self):
        dbObject = persist.PersistData('postgres')
        with self.assertRaises(psycopg2.errors.UndefinedTable):
            dbObject.read_from_pg('futurexschema.asdasdasdasdasdad')  # invaild table name




if __name__ == '__main__':
    unittest.main()