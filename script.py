# -*- coding: utf-8 -*-
# script.py Replace Artifact Hero Names from a language to other. Created by Desvelao^^ (iamdesvelao@gmail.com)

import asyncio, os, json, traceback, sys, configparser
from aiohttp import ClientSession
import encodings.idna

CWD = os.getcwd()

APIURL = 'https://playartifact.com/cardset/'
CDNURL = 'https://steamcdn-a.akamaihd.net'
AUTHOR = 'Desvelao^^'
VERSION = '0.0.1'
REPOSITORY_URL = 'https://github.com/Desvelao/artifact-hero-names-replacer'

def load_config():
    parser = configparser.ConfigParser()
    parser.read('ahnr_config.txt')
    config = {}
    for key in parser['DEFAULT']:
        config[key] =  parser['DEFAULT'][key] if not key in ['files','files_sets','sets'] else [value.strip() for value in parser['DEFAULT'][key].split(',')]
    return config

def printSeparator():
    print('-------------------------------------')   

CONFIG = load_config()
# CONFIG['files'] = CONFIG['files'].split(',')

class Collection:
    def __init__(self,lst):
        self.lst = lst
    def __str__(self):
        return f"{self.__class__.__name__} {','.join([str(v) for v in self.lst])}"
    def filter(self,fn):
        return Collection(Collection.to_list(filter(fn,self.lst)))
    def map(self,fn):
        return Collection(Collection.to_list(map(fn,self.lst)))
    @property
    def length(self):
        return len(self.lst)
    @staticmethod   
    def to_list(lst):
        return list(lst)

def get_file_path(relative_path_file,set_id = ''):
    # path_file = f"{CWD}/{relative_path_file}"
    path_file = f"{relative_path_file}"
    return path_file.replace('<SETID>', set_id).replace('<LANG>',CONFIG['replace_from'])
    
async def get_url(url, session):
    print(f'    Fetching... {url}')
    async with session.get(url) as response:
        # print(response)
        return await response.json()

async def get_api_info():
    async with ClientSession() as session:
        tasks = [get_url(f"{APIURL}/{set_id}", session) for set_id in CONFIG['sets']]
        set_urls = await asyncio.gather(*tasks)
        info_sets = [get_url(f"{CDNURL}/{set_url['url']}", session) for set_url in set_urls]
        return await asyncio.gather(*info_sets)

def replace(text, data):
    new_text = text
    count = 0
    for d in data:
        count += text.count(d['from'])
        new_text = new_text.replace(d['from'],d['to'])
    return new_text, count

def replace_file(file_path, heroes):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        text = file.read()
        if (text.endswith('//PATCHED')):
            print("   " + u"\u274C" + f" It is patched: {file_path}")
            return 0
        
        text_modified, count = replace(text,heroes)
        
        if (text_modified == text):
            print("   " + u"\u274C" + f" Without changes: {file_path}")
            return 0
        with open(file_path, 'w+', encoding='utf-8', errors='ignore') as output_file:
            output_file.write(f"{text_modified}\n//PATCHED")
            print("   " + u"\u2705" + f" FILE PATCHED: {file_path} [{count} changes]")
            return count

def exists_file(file_path):
    if( not os.path.isfile(file_path)):
        print(f"WARNING: File doesn't exist: {file_path}")
        # raise Exception(f"ERROR: File doesn't exists: {file_path}")
        return False
    return True

async def ahnr():
    print(f"Welcome to Artifact Hero Name Replacer (AHNR)")
    printSeparator()
    print('Replace hero names from a language to other using Artifact API.')
    print(f"Version: v{VERSION}")
    print(f"Author: {AUTHOR}")
    print(f"Repository: {REPOSITORY_URL}")
    printSeparator()
    await asyncio.sleep(5)
    print('Configuration\n')
    print(f"replace from: {CONFIG['replace_from']}")
    print(f"replace to: {CONFIG['replace_to']}")
    print(f"sets: {CONFIG['sets']}")
    files = []
    for set_id in CONFIG['sets']:
        # print(f"SetID: {set_id}")
        for f in CONFIG['files_sets']:
            file = get_file_path(f, set_id)
            if exists_file(file):
                files.append(file)
    for relative_path_file in CONFIG['files']:
        file = get_file_path(relative_path_file)
        if exists_file(file):
            files.append(file)
    
    # print(heroes)
    print('Files to replace:')
    for file_path in files:
        print(f"   - {file_path}")
        
    printSeparator()
    await asyncio.sleep(2)
    print('Downloading API info...')
    data_sets = await get_api_info()
    print('\nSets found:')
    heroes = []
    for data_set in data_sets:
        cards = Collection(data_set['card_set']['card_list'])
        heroes_found = cards.filter(lambda card: card['card_type'] == 'Hero')
        print(f"   - {data_set['card_set']['set_info']['name']['english']}: {heroes_found.length} heroes")
        heroes = [*heroes, *heroes_found.map(lambda hero: {"from" : hero["card_name"][CONFIG["replace_from"]], "to": hero["card_name"][CONFIG["replace_to"]]}).lst]
    
    printSeparator()
    print('Results:')
    total_replace = 0
    for i,file_path in enumerate(files):
        total_replace += replace_file(file_path, heroes)
    
    printSeparator()
    
    return total_replace
    
    
    
                
async def main():
    try:
        total_replace = await ahnr()
        if total_replace > 0:
            print(f"   Changes done: {total_replace}")
        else:
            print('   No changes')
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(e, exc_value, exc_traceback, limit=2, file=sys.stdout)
    print('')
    input("Press Enter to close...")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()