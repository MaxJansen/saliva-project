# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 15:37:38 2021

@author: Max Jansen
"""

import urllib.parse
import urllib.request
import pandas as pd
import io

# Take csv with uniprot id's as input
human_csv = 'csv_data/Overview human salivary prot.csv'
pea_csv = 'csv_data/uniprot-organism__pisum+sativum_.csv'
soybean_csv = 'csv_data/uniprot-organism__glycine+max_.csv'
whey_csv = 'csv_data/Whey proteome (Bos Taurus).csv'

def get_pdb_map(input_csv):
    """ Takes in csv data for each organism,
    converts to DataFrame, makes one big list of UniProtKB/AC for a query,
    submits query and takes back list of PDBs"""
    
    df = pd.read_csv(input_csv)
    a = list(df['UniProt Accession'])
    b = ' '.join(str(e) for e in a)
    
    url = 'https://www.uniprot.org/uploadlists/'
    
    params = {
    'from': 'ACC+ID',
    'to': 'PDB_ID',
    'format': 'tab',
    'query': b
    }
    
    data = urllib.parse.urlencode(params)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    
    
    with urllib.request.urlopen(req) as f:
       response = f.read()
       #print(response.decode('utf-8'))
       
    foo = io.StringIO(response.decode('utf-8'))
    bar = pd.read_csv(foo, sep = "\t")
    bar = bar.drop_duplicates(subset = ["From"])
    return bar

human = get_pdb_map(human_csv)
pea = get_pdb_map(pea_csv)
soybean = get_pdb_map(soybean_csv)
whey = get_pdb_map(whey_csv)

# Give space-delimited csv as 
human.to_csv(r'csv_data/human_uniprot_pdb.txt', header=None, index=None, 
             sep=' ', mode='a')
pea.to_csv(r'csv_data/pea_uniprot_pdb.txt', header=None, index=None, 
             sep=' ', mode='a')
soybean.to_csv(r'csv_data/soybean_uniprot_pdb.txt', header=None, index=None, 
             sep=' ', mode='a')
whey.to_csv(r'csv_data/whey_uniprot_pdb.txt', header=None, index=None, 
             sep=' ', mode='a')

