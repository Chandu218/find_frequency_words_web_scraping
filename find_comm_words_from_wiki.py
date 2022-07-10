import requests
from nltk import word_tokenize
import nltk
from nltk.corpus import stopwords
import pandas as pd
nltk.download('stopwords')
nltk.download('punkt')

def find_common_words_from_wiki_page(page_id, number_of_words):
    """
    The function takes a page id of wiki and return the n top words with title.

    Input Parms:
    number_of_words: number of words.
    page_id: page id.

    Returns:
    the list containing all top n word count and Title.

    """
    # Building the URL.
    url = "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&pageids={}&explaintext&format=json".format(page_id)
    response = requests.request('GET',url=url)

    #Extraction of JSON text
    if response.status_code == 200:
        response = response.json()
        result_text = response['query']['pages'][str(page_id)]['extract']
        title = "Title: {} ".format(response['query']['pages'][str(page_id)]['title'])

        #splits a given sentence into words
        words_list = word_tokenize(result_text)

        #converting all to lower words
        words_list = [word.lower() for word in words_list]

        #cleaning part1
        # remove stop words
        stop_words = stopwords.words('english')
        words_clean_1 = [word for word in words_list if word not in stop_words]

        #cleaning part2
        # remove alpha_numaric and integers and special char words
        words_clean_2 = [word for word in words_clean_1 if word.isalpha()]

        #Create pandas dataframe
        words_df = pd.DataFrame({"word":words_clean_2})

        #Grouping the words which gives words with count
        word_count = words_df.groupby('word').size().sort_values(ascending=False)
        response_dict = dict()
        for k, v in dict(word_count).items():
            if response_dict.get(v):
                response_dict[v] = response_dict.get(v)+ ", "+ k
            else:
                response_dict[v] = k

        #Create response Output
        final_output = title + "\nTop {} words:".format(number_of_words)
        for x in list(response_dict.items())[:int(number_of_words)]:
            final_output = final_output + "\n" + "{} {}".format(x[0],x[1])

        # returning the final output.
        #return final_output
        print(final_output)
    else:
        print("Error : {}".format(response.text))

#calling function by passing prompt inputs
if __name__ == "__main__":
    page_id = input("Enter the page id: ")
    number_of_words = input("Enter the number of top words: ")
    find_common_words_from_wiki_page(page_id, number_of_words)
