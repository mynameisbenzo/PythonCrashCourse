import unittest
import requests
from python_repos import make_call, make_call_with

class CallTest(unittest.TestCase):
	# test api call
	def test_make_call(self):
		r = make_call()
		self.assertEqual(r.status_code, 200)
		
	# test api call with given string
	def test_make_call_with(self):
		r = make_call_with("https://hacker-news.firebaseio.com/v0/topstories.json")
		self.assertEqual(r.status_code, 200)
	
	# test for failure in invalid url (not a url)
	def test_make_call_with_fail(self):
		with self.assertRaises(Exception):
			r = make_call_with("https://NOTAURL -hacker-news.firebaseio.com/v0/topstories.json")
		
	# test for failure in call to wrong url
	def test_make_call_with_wrong(self):
		r = make_call_with("https://hackme-news.firebaseio.com/v0/topstories.json")
		self.assertNotEqual(r.status_code, 200)
		
unittest.main()