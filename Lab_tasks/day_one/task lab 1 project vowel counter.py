def vowel_counter(word):
 vowels = "aeiouAEIOU"
 counter=0
 for char in word:
    if char in vowels:
        counter+=1
 return counter


print(vowel_counter("Hello Python"))