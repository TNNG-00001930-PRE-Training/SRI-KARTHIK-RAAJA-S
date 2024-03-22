def print_even_length_words(string): 
    words = string.split() # Split
    
    for word in words:
        if len(word) % 2 == 0:
            print(word)

input_string = "This is an example string with words of even length"
print("Words with even length:")
print_even_length_words(input_string)
