def count_words(data):
    listofwords=data.split()
    return len(listofwords)

def get_character_count(data):
    characters={}
    for character in data:
        if character.lower() in characters:
            characters[character.lower()]+=1
        else:
            characters[character.lower()]=1
    return characters
            

