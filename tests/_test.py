""" Python Script for Scrapping """
""" author : Matthieu Cabrera """
""" mail : cabreramat@cy-tech.fr """
""" version : 1.0.0 """
""" GitHub : https://github.com/cabreScrumMaster/Scrapper """
""" Date : 16th of November 2022 """
""" File : test.py """
""" Test Unit Program """

import sys
sys.path.append('.')
sys.path.append('../')
import unittest
import scrapper as code_file

import requests
from bs4 import BeautifulSoup

class Test(unittest.TestCase):

    ## Test File Manager
    def test_init(self):
        file_manager = code_file.FileManager()
        self.assertEqual(file_manager.input, "")
        self.assertEqual(file_manager.output, "")

    def test_init_with_files(self):
        file_manager = code_file.FileManager("input.json", "output.json")
        self.assertEqual(file_manager.input, "input.json")
        self.assertEqual(file_manager.output, "output.json")

    def test_reading_input_files(self):
        file_manager = code_file.FileManager("input.json", "output.json")
        list_ip = file_manager.read_file()
        self.assertEqual(len(list_ip["videos_id"]), 2)

    def test_file_exists(self):
        file_manager = code_file.FileManager("input.json", "output.json")
        bool = file_manager.exist_file("input.json")
        self.assertTrue(bool)

    def test_write_file_exists(self):
        file_manager = code_file.FileManager("input.json", "output.json")
        code_file.lauchProgram(file_manager)
        self.assertTrue(file_manager.exist_file("output.json"))
        
    ##Test Scrapper
    def test_title_ok(self):
        scrapper = code_file.Scrapper()
        url : str = "https://www.youtube.com/watch?v=NDM3rrF2HUM"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        self.assertEqual(scrapper.get_title(soup), 'Vous utilisez mal votre iPhone 👎 (et iOS 16)')

    def test_author_ok(self):
        scrapper = code_file.Scrapper()
        url : str = "https://www.youtube.com/watch?v=NDM3rrF2HUM"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        self.assertEqual(scrapper.get_author(soup), 'iphone 14')
    
    