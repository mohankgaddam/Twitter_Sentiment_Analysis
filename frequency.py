import sys
import json


def main():
    tweet_file = open(sys.argv[1])
    
    
    Total_list_of_words = []
    for line in tweet_file:
        parsed_data = json.loads(line)
        
        if "text" in parsed_data and parsed_data["lang"] == "en":
           unicode_string =  parsed_data["text"]
           encoded_string = unicode_string.encode('utf-8')
           list_of_words = encoded_string.split(" ")
           for word in list_of_words:
               word = str(word.lstrip())
               Total_list_of_words.append(word)
    #print len(Total_list_of_words)

    Iterated_words = {}
    for word in Total_list_of_words:
        if word not in Iterated_words:
           frequency = Total_list_of_words.count(word) / float(len(Total_list_of_words))
           print "%s %f"%(word,frequency)
           Iterated_words[word] = "true"
           
              
                     

if __name__ == '__main__':
    main()
