# # from math import sqrt,pi
# # from collections import Counter

# # print(sqrt(16))
# # print(pi)

# with open("sample.txt","w") as f:
#   f.write("the quick brown fox jumps over the lazy dog the fox runs")


# def word_frequency(filename):
#   freq = {}
#   with open(filename,"r") as f:
#     content = f.read()
  
#   words = content.lower().split()

#   for word in words:
#     freq[word] = freq.get(word,0)+1
  
#   return freq

# result = word_frequency("sample.txt")
# print(result)


from collections import Counter

def word_frequency_v2(filename):
    with open(filename, "r") as f:
        content = f.read()
    words = content.replace("\n", " ").split()
    return Counter(words)

result = word_frequency_v2("sample.txt")
print(result)

# def write_unique_words(input_file, output_file):
#     with open(input_file, "r") as f:
#         content = f.read()

#     words = content.lower().split()
#     unique_words = set(words)

#     with open(output_file, "w") as f:
#         for word in sorted(unique_words):
#             f.write(word + "\n")

# write_unique_words("sample.txt", "unique_words.txt")


# from collections import Counter

# def word_frequency_v3(filename):
#   with open(filename,"r") as f:
#     words = f.read().lower().split()
#   return Counter(words)