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
    line_dictionary = {}
    line_times = {}
    stop_last = None
    last_time = None
    with open(lines, 'r') as linefile:
        for line in linefile:
            line = line.strip()
            if not line:
                continue
            elif line[-1] == ":":
                current_line = line[:-1]
                line_dictionary[current_line] = []
            elif current_line:
                stop_name = " ".join(line.split()[:-1])
                line_dictionary[current_line].append(stop_name)
                stop_time_str = line.split()[:-1]
                stop_time = int(stop_time_str.split(':')[1])
                
                if stop_last:
                    transport_time = (stop_last - last_time)%60
                    if stop_last not in line_times:
                        line_times[stop_last] = {}
                    line_times[stop_last][stop_name]=transport_time
       
    desired_key = '2'
    print(line_dictionary[desired_key])
        
        

        



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