import unittest
from SI507project5_code import *

class Part1(unittest.TestCase):
    def setUp(self):
        self.blogs = open("posts.csv",'r')
        self.bloggers = open("bloggers.csv",'r')

    def test_csv_files_exist(self):
        self.assertTrue(self.blogs.read())
        self.assertTrue(self.bloggers.read())

    def tearDown(self):
        self.blogs.close()
        self.bloggers.close()

class Part2(unittest.TestCase):
    def setUp(self):
        self.cache = open("cache_contents.json")

    def test_files_exist(self):
        self.assertTrue(self.cache.read())

    def tearDown(self):
        self.cache.close()

class Part3(unittest.TestCase):
    def setUp(self):
        blog_url = 'https://api.tumblr.com/v2/tagged'
        CACHE_DICTION = json.loads(cache_json)
        tumblr_search_params = {"tag":"meditation","limit":"10"}    
        tumblr_result = get_data_from_api(blog_url,"Tumblr",tumblr_search_params)
        self.post_list = tumblr_result['response']  

    def test_response_type(self):
        self.assertEqual(type(self.post_list),type([]))

class Part4(unittest.TestCase):
    def setUp(self):
        blog_url = 'https://api.tumblr.com/v2/tagged'
        CACHE_DICTION = json.loads(cache_json)
        tumblr_search_params = {"tag":"meditation","limit":"10"}    
        tumblr_result = get_data_from_api(blog_url,"Tumblr",tumblr_search_params)
        self.post_dict = tumblr_result['response'][0]
        self.tag_list = tumblr_result['response'][0]['tags']

    def test_post_data(self):
        self.assertEqual(type(self.post_dict['blog_name']),type(u"s"))
        self.assertEqual(type(self.post_dict['date']),type('2017-11-10 17:39:00 GMT'))
        self.assertEqual(type(self.tag_list),type([]))

    def tearDown(self):
        pass

class Part5(unittest.TestCase):
    def setUp(self):
        self.fileref = open("secret_data.py",'r')
        lines = self.fileref.readlines()
        cred_list = []
        for lin in lines:
            cred_list.append(lin)
        for cred in cred_list:
            if cred[0:10] == 'client_key':
                self.client_key = cred
            else:
                self.client_secret = cred

    def test_key(self):
        self.assertTrue(len(self.client_key) > 13)
    def test_secret(self):
        self.assertTrue(len(self.client_secret) >  16)

    def tearDown(self):
        self.fileref.close()

class Part6(unittest.TestCase):
    def setUp(self):
        blog_url = 'https://api.tumblr.com/v2/blog/witches-ofcolor/info'
        CACHE_DICTION = json.loads(cache_json)
        tumblr_search_params = {"0":"0","0":"0"}    
        tumblr_result = get_data_from_api(blog_url,"Tumblr",tumblr_search_params)
        self.blogger_dict = tumblr_result['response']

    def test_post_data(self):
        self.assertEqual(type(self.blogger_dict['blog']['description']),type(u"s"))
        self.assertEqual(type(self.blogger_dict['blog']['posts']),type(1))

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main(verbosity=2)
