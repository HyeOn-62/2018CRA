# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 19:42:37 2018

@author: hyeOn
"""

import urllib.request, urllib.parse
key = "4c099619fc8751d5693b8a368b769a79"

def get_info(Mname, open_year) :
    encoded_name = urllib.parse.quote(Mname)

    api_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json"
    api_option = "?key=" + key + "&movieNm=" + encoded_name + "&openStartDt=" + open_year
    url = api_url + api_option

    response = urllib.request.urlopen(url)

    if response.getcode() != 200 :
        print("Error Code : " + str(response.getcode()))
	
    import json
    content = json.loads(response.read())
    content = content['movieListResult']['movieList'][0]

    return content


