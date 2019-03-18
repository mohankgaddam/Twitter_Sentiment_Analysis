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

    
    sentiment_score_of_each_state = {}
    states_list = []
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
           #print count

        if "user" in parsed_data :
           if isinstance(parsed_data["user"]["location"], unicode): 
              unicode_string =  parsed_data["user"]["location"]
              #print type(unicode_string)
              encoded_string = unicode_string.encode('utf-8')
              #print encoded_string
              if len(encoded_string.split(",")) ==2:
                 state = str(encoded_string.split(",")[1]).lstrip(' ')
                 if len(state) == 2:
                    #print state
                    states_list.append(state)
                    if state not in sentiment_score_of_each_state:
                       sentiment_score_of_each_state[state] = count
                    else:
                       sentiment_score_of_each_state[state] = sentiment_score_of_each_state[state]+count        
    
    Max_val = -99999999999999     
    for state_name in states_list:
        val = sentiment_score_of_each_state[state_name]/float(states_list.count(state_name))
        if val > Max_val:
           Max_val = val                 
           answer  = str(state_name)

    print answer      

if __name__ == '__main__':
    main()
