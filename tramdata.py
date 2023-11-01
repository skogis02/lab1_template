import sys
import json
import csv

# files given
STOP_FILE = './data/tramstops.json'
LINE_FILE = './data/tramlines.txt'

# file to give
TRAM_FILE = './tramnetwork.json'

def build_tram_stops(jsonobject):
    with open(jsonobject, 'r') as infile:
        data = json.load(infile)
        stop_dictionary = {tramstops:  dict(lat = float(data[tramstops]['position'][0]),lon = float(data[tramstops]['position'][1])) for tramstops in data}                         
        print(stop_dictionary)
    

def build_tram_lines(lines):
    with open(lines, 'r') as infile:
        rows = csv.reader(infile, delimiter='\t')
        rows.__next__()

        print(data)



def build_tram_network(stopfile, linefile):
    ## YOUR CODE HERE
    pass

def lines_via_stop(linedict, stop):
    ## YOUR CODE HERE
    pass

def lines_between_stops(linedict, stop1, stop2):
    ## YOUR CODE HERE
    pass

def time_between_stops(linedict, timedict, line, stop1, stop2):
    ## YOUR CODE HERE
    pass

def distance_between_stops(stopdict, stop1, stop2):
    ## YOUR CODE HERE
    pass

def answer_query(tramdict, query):
    ## YOUR CODE HERE
    pass

def dialogue(tramfile=TRAM_FILE):
    ## YOUR CODE HERE
    pass

if __name__ == '__main__':
    if sys.argv[1:] == ['init']:
        build_tram_network(STOP_FILE,LINE_FILE)
    else:
        dialogue()
     

build_tram_lines(LINE_FILE)