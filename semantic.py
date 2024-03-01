import spacy

nlp = spacy.load("en_core_web_lg")

tokens = nlp("cat monkey apple banana")

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
       
#Cat and Monkey are more similar than Banana and Monkey (Both cat and monkey are animals)
#Cat and Banana are the least similar
#Most similar are banana and apple (both are fruits)
#en_core_web_sm makes monkey and banana the most similar but not much difference

sentence_to_compare ="Why is my cat on the car"

sentences = ["where did my dog go",
            "Hello, there is my car",
            "I\'ve lost my car in my car",
            "I\'d like my boat back",
            "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - " + str(similarity))
    
#"Hello, there is my car" is most similar to "Why is my cat on the car" as both sentences are referring to a car as the subject


movie_input = """Will he save their world or destroy it? When the Hulk becomes too 
dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace.
Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."""

def most_simular(movie_input):
    
    #Keep track of highest similarity
    max_similarity_score = 0        
    max_similarity_score_name = ""
    
    try:
        #Open file and split to put each line into a list
        file = open("./movies.txt", "r")
        movies = file.read()
        movies_list = movies.split("\n")
        
        #Convert input string into a token format
        movie_input = nlp(movie_input)
        
        for movie in movies_list:
            
            if ":" in movie:
                
                #Split name of movie and description
                movie_split = movie.split(":")
                
                movie_label = movie_split[0]
                movie_description = nlp(movie_split[1])
                
                #Find simularity
                similarity_score = movie_description.similarity(movie_input)
                
                #Check if simularity score is greater than the current highest
                if similarity_score > max_similarity_score:
                    max_similarity_score = similarity_score
                    max_similarity_score_name = movie_label
                
        file.close()
        
    except FileNotFoundError:
        print("Cant find file")
        
    return max_similarity_score_name, max_similarity_score


print(most_simular(movie_input))
