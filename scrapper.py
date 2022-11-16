""" Python Script for Scrapping """
""" author : Matthieu Cabrera """
""" mail : cabreramat@cy-tech.fr """
""" version : 1.0.0 """
""" GitHub : https://github.com/cabreScrumMaster/Scrapper """
""" Date : 16th of November 2022 """
""" File : scrapper.py """
""" Main Program """

import json
import os
import sys
from dataclasses import dataclass
from typing import List

import requests
from bs4 import BeautifulSoup


@dataclass
class Video :

    title : str
    author:str
    thumbs:int
    description:str
    links:List[str]
    id:str
    nb_commentaires:int
    commentaires:List[str]
        
    def __init__(self, title = "", author = "", thumbs=0, description = "", links = [], id = "0", nb_commentaires = 5, commentaires = []):
        self.title = title
        self.author = author
        self.thumbs = thumbs
        self.description = description
        self.links = links
        self.id = id
        self.nb_commentaires = nb_commentaires
        self.commentaires = commentaires

    ##Getters
    def _get_title(self):
        return self._title

    def _get_author(self):
        return self._author
    
    def _get_thumbs(self):
        return self._thumbs
    
    def _get_description(self):
        return self._description
    def _get_links(self):
        return self._links
    
    def _get_id(self):
        return self._id
    
    def _get_nb_commentaires(self):
        return self._nb_commentaires
    
    def _get_commentaires(self):
        return self._commentaires
    
    ##Setters
    def _set_title(self, title):
        self._title = title

    def _set_author(self, author):
        self._author = author
    
    def _set_thumbs(self, thumbs):
        self._thumbs = thumbs
    
    def _set_description(self, description):
        self._description = description
    def _set_links(self, links):
        self._links = links
    
    def _set_id(self, id):
        self._id= id
    
    def _set_nb_commentaires(self, nb_commentaires):
        self._nb_commentaires = nb_commentaires
    
    def _set_commentaires(self, commentaires):
        self._commentaires = commentaires
    
    ##Properties

    title = property(
        fget=_get_title,
        fset=_set_title
    )
    author = property(
        fget=_get_author,
        fset=_set_author
    )
    thumbs = property(
        fget=_get_thumbs,
        fset=_set_thumbs
    )
    description = property(
        fget=_get_description,
        fset=_set_description
    )
    links = property(
        fget=_get_links,
        fset=_set_links
    )
    id = property(
        fget=_get_id,
        fset=_set_id
    )
    nb_commentaires = property(
        fget=_get_nb_commentaires,
        fset=_set_nb_commentaires
    )
    commentaires = property(
        fget=_get_commentaires,
        fset=_set_commentaires
    )

@dataclass
class Scrapper:

    list_ip: list
    list_videos : list

    def __init__(self, input = "input.json", output = "output.json"):
        self.input = input
        self.output = output
        self.list_videos = []

    ##get title in the html
    def get_title(self, soup) : 
        return soup.find("meta", property="og:title")["content"]

    ## get author in the html
    def get_author(self, soup):
        return soup.find("meta", property="og:video:tag")["content"]

    ##get description in the html
    def get_description(self, soup):
        return soup.find("meta", property="og:description")["content"]

    ##retrieve the html
    def retrieve_html(self, list_ip):
        for id in list_ip["videos_id"]:
            url : str = "https://www.youtube.com/watch?v="+id
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            title = self.get_title(soup)
            author = self.get_author(soup)
            description = self.get_description(soup)
            self.list_videos.append(Video(title = title, author = author, description=description, id=id))
    
    def _get_list_videos(self):
        return self._list_videos

    def _set_list_videos(self, list_videos):
        self._list_videos = list_videos
    
    list_videos = property(
        fget = _get_list_videos,
        fset = _set_list_videos
    )


@dataclass
class FileManager:

    input : str
    output : str

    def __init__(self, input = "", output = ""):
        self.input = input
        self.output = output

    # Check if the file exists
    def exist_file(self, file) -> bool:
        return os.path.exists(file)
    
    #Read file
    def read_file(self) -> list:
        list_ip = []
        with open(self.input) as fp:
            list_ip = json.load(fp)
        return list_ip
    
    ## Create output file
    def write_file(self, list_ip , list_videos):
        dict_videos = dict(zip(list_ip["videos_id"],list(map(lambda x : x.__dict__, list_videos))))
        with open(self.output, 'w') as of:
            json.dump(dict_videos, of, indent = 4)

    def _get_input(self):
        return self._input

    def _get_output(self):
        return self._output

    def _set_input(self, input):
        self._input = input
    
    def _set_output(self, output):
        self._output = output

    input = property(
        fget=_get_input,
        fset=_set_input
    )

    output = property(
        fget = _get_output,
        fset = _set_output
    )

def lauchProgram(file_manager : FileManager):
    scrapper = Scrapper(file_manager.input, file_manager.output)
    list_ip = file_manager.read_file()
    scrapper.retrieve_html(list_ip)
    file_manager.write_file(list_ip, scrapper.list_videos)

if __name__ == "__main__" :
    if (len(sys.argv) == 5):
        if (sys.argv[1] == "--input") and (sys.argv[3] == "--output"):
            file_manager = FileManager(sys.argv[2], sys.argv[4])
            if (file_manager.exist_file(sys.argv[2])):
                lauchProgram(file_manager)
        elif (sys.argv[3] == "--input") and (sys.argv[1] == "--output"):
            file_manager = FileManager(sys.argv[4], sys.argv[2])
            if (file_manager.exist_file(sys.argv[4])):
                lauchProgram(file_manager)
        else:
            exit("invalid arguments")
    else : 
        exit("invalid number of arguments")

