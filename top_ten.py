import sys
import json
import operator


def main():
    tweet_file = open(sys.argv[1])
    
    
    Total_list_of_hashtags = []

    for line in tweet_file:
        parsed_data = json.loads(line)
        
        if "entities" in parsed_data:
           hashtag_list =  parsed_data["entities"]["hashtags"]
           
           for item in hashtag_list:
               unicode_string = item["text"]
               encoded_string = unicode_string.encode('utf-8')
               Total_list_of_hashtags.append(encoded_string)


    hashtag_count = {}
    for hashtag in Total_list_of_hashtags:
        if hashtag not in hashtag_count:
           hashtag_count[hashtag] = Total_list_of_hashtags.count(hashtag)

    #for item in hashtag_count:
        #print item+" "+str(hashtag_count[item])

    #sorted _data is a list of tuples obtained by sorting hashtag_count dictionary with respect to values of the dictionary
    sorted_data = sorted(hashtag_count.items(), key=operator.itemgetter(1), reverse=True)       
     

    for i in range(1,11):
        print sorted_data[i][0]+" "+str(sorted_data[i][1])

                  
                     

if __name__ == '__main__':
    main()
