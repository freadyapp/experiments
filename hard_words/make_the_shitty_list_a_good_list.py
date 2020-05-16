import csv
import json

plip = {}

def allocate_word(w):
  key = w[0].lower() + str(len(w))
  
  if not key in plip:
    plip[key] = []
    
  plip[key].append(w.lower())


with open('difficult_words_shitty_list.csv', 'r') as csvfile:
  shity_list = csv.reader(csvfile, delimiter=' ', quotechar='|')
  for row in shity_list:
    allocate_word(row[0].split(',')[0])
    
  with open("good_list.txt", "w") as text_file:
    text_file.write(json.dumps(plip))