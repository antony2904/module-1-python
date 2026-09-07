# apple (input)
# output should be 'a'-1 
#                  'p'-2
#                  'l'-1 
#                  'e'-1
                    
def characters_count(word):
    counts = {}
    for char in word:
        counts [char] = counts.get(char,0)+1

    for char,count in counts.items():
        print(f"'{char}'-'{count}'")

user= input("Enter a word: ")

#characters_count('apple')        
characters_count(user)