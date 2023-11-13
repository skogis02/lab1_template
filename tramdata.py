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
    

def build_tram_lines(lines_file):
    line_dict = {}
    time_dict = {}

    with open(lines_file, 'r', encoding='utf-8') as file:
        current_line = None
        current_line_stops = []
        current_line_times = []

        for line in file:
            # Remove leading and trailing whitespaces
            line = line.strip()

            if line.endswith(':'):
                # Save the previous line information if any
                if current_line is not None:
                    line_dict[current_line] = current_line_stops

                    current_line_stops = []
                    current_line_times = []
                # Set the current line
                current_line = line[:-1]  # Remove the colon
            else:
                stop_time_parts = line.rsplit(' ', 1)

                if len(stop_time_parts) == 2:
                    stop = stop_time_parts[0].rstrip()
                    time = stop_time_parts[1]

                    minutes = int(time.split(':')[1])

                    current_line_stops.append(stop)
                    current_line_times.append(minutes)

                # Add stop and transition time to time_dict
                    if stop not in time_dict:
                        time_dict[stop] = {}

                    for i in range(len(current_line_stops) - 1):
                        source_stop = current_line_stops[i]
                        dest_stop = current_line_stops[i + 1]
                        transition_time = current_line_times[i+1] - current_line_times[i]
                        time_dict[source_stop][dest_stop] = transition_time
            
            if current_line is not None: 
                line_dict[current_line] = current_line_stops
    return line_dict, time_dict
    

def build_tram_network(stopfile, linefile):
    tram_network = {
        "stops": build_tram_stops(stopfile),
        "lines": build_tram_lines(linefile)[0],
        "times": build_tram_lines(linefile)[1]
    }
    return tram_network


def lines_via_stop(linedict, stop): #tar in min linedictionary {'1': ['Östra Sjukhuset', 'Tingvallsvägen', 'Kaggeledstorget'
    lines_via = []

    for line, stops in linedict.items():
        if any(stop.lower() == s.lower() for s in stops):
            lines_via.append(line)
    return lines_via


def lines_between_stops(linedict, stop1, stop2):
    lines_between = []

    for line, stops in linedict.items(): 
        if any(stop1.lower() == s.lower() for s in stops) and any(stop2.lower() == d.lower() for d in stops): 
            lines_between.append(line)
    return lines_between

def time_between_stops(linedict, timedict, line, stop1, stop2):
    time_between = 0
    stops = linedict[line] #Plockar ut listan med stops från line#
    if any(stop1.lower() == s.lower() for s in stops) and any(stop2.lower() == d.lower() for d in stops): 
        if stops.index(stop1) < stops.index(stop2):
            return str('rätt ordning')
        else: 
            stop1_1 = stop2
            stop2_2 =  stop1
            print(stop1_1, stop2_2)
            return str('klara är dum')
    else:
        return str('False')
        

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
     

#print(build_tram_lines(LINE_FILE))
#print(build_tram_network(STOP_FILE, LINE_FILE))
#print(lines_via_stop(build_tram_lines(LINE_FILE)[0],'Östra Sjukhuset'))
print(time_between_stops(build_tram_lines(LINE_FILE)[0],build_tram_lines(LINE_FILE)[1],'6','Chalmers','Korsvägen'))