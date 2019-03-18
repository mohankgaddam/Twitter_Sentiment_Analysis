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
           
           
           positive = 0
           negative = 0
           for word in list_of_words:
               if word in scores:
                  if scores[word] > 0 :
                     positive = positive +scores[word]
                  else:
                     negative = negative + scores[word]        
           
           for word in list_of_words:
               if word not in scores :
               	  if positive == 0 and negative ==0:
               	  	 sentiment_score = 0
               	  elif positive == 0:
               	     sentiment_score = negative
               	  elif negative == 0:
               	     sentiment_score = positive   	 
               	  else:
                     sentiment_score = positive/(negative *-1)
                  print word+" "+str(sentiment_score)
                  
                                   

if __name__ == '__main__':
    main()
