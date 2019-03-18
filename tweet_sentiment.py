import sys
import json


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    scores = {} # initialize an empty dictionary
    for line in sent_file:
    	term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    #print scores.items() # Print every (term, score) pair in the dictionary

    for line in tweet_file:
        parsed_data = json.loads(line)
        if "text" in parsed_data:
           unicode_string =  parsed_data["text"]
           encoded_string = unicode_string.encode('utf-8')
           #print encoded_string
           list_of_words = encoded_string.split(" ")
           #print list_of_words
           count = 0
           for word in list_of_words:
               if word in scores:
                  count = count + scores[word]
           print count    
                     

if __name__ == '__main__':
    main()
