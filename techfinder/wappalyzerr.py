import pymongo
from wappalyzer.Wappalyzer import Wappalyzer, WebPage
import json


def techfind(siteurl):
    techs = []
    try:
        wappalyzer = Wappalyzer.latest()
        webpage = WebPage.new_from_url(siteurl)
        techs = list(wappalyzer.analyze(webpage))
    except Exception as e:
        print(e)
    if techs==[]:
        return  ['No Technologies Found !!']
    else:
        return techs
