# -*- coding: utf-8 -*-
"""
Author: Kristianne Bossie
CSIT505 Project

Given a spell, the program can tell you which character would have cast it and how many times.

Project Plan
1. Gather Datasets
2. import all books to be readable in program
3. Search for all instances that spell is used in books
4. Search within sentence in order to determine which character said spell.
5. Count all instances when character said which spell.
6. Based on numeric count, input a spell.
7. Output will be character who said spell the most.

"""

#import character and spells into separate lists

Lspells = []
Lchar = []

with open('spells.txt', 'r') as spell_file:
        for line in spell_file:
            line = line.strip() #remove \n before splitting line
            Lspells.append(line.split('.'))
            
# print("Spell List:", Lspells) - tested to see if list prints properly

with open('characters.txt', 'r') as char_file:
        for line in char_file:
            line = line.strip() #remove \n before splitting line
            Lchar.append(line.split(' .'))
            
# print("Character List:", Lchar)

#find sentences within book that contain the spells

def spell_sent():
    with open('HPall.txt', 'r', encoding='utf-8') as hpfile, open('spellsentence.txt', 'w') as hpfilew:
      text = hpfile.read()
      result_string = ''

      words = ['Accio', 'Aguamenti', 'Alohomora', 'Aparecium', 'Avada Kedavra', 'Avifors', 'Avis', 
'Bombarda', 'Colloportus', 'Confringo', 'Confundus', 'Conjunctivitis', 'Crucio', 'Deletrius', 
'Densaugeo', 'Diffindo', 'Dissendium', 'Duro', 'Enervate', 'Engorgio', 'Episkey', 'Evanesco', 
'Expecto Patronum', 'Expelliarmus', 'Fera Verto', 'Ferula', 'Fidelius', 'Finite Incantatem', 'Flagrate', 
'Flipendo', 'Furnunculus', 'Geminio', 'Homorphus', 'Immobulus', 'Impedimenta', 'Imperio', 'Impervius', 
'Incarcerous', 'Incendio', 'Legilimens', 'Levicorpus', 'Liberacorpus', 'Locomotor Mortis', 'Lumos', 
'Mobiliarbus', 'Mobilicorpus', 'Morsmordre or Morsmorde', 'Muffliato', 'Nox', 'Obliviate', 'Orchideous', 
'Petrificus Totalus', 'Point Me', 'Portus', 'Prior Incantato', 'Protego', 'Quietus', 'Reducio', 'Reducto', 
'Relashio', 'Rennervate', 'Reparo', 'Repello', 'Repello Muggletum', 'Revelio', 'Rictusempra', 'Riddikulus', 
'Salvio Hexia', 'Scourgify', 'Sectumsempra', 'Serpensortia', 'Silencio', 'Sonorus', 'Stupefy', 
'Tarantallegra', 'Tergeo', 'Waddiwasi', 'Wingardium Leviosa']
      
      text2 = text.split(".")
      for itemIndex in range(len(text2)):
          for word in words:
              if word in text2[itemIndex]:
                  if text2[itemIndex][0] ==' ':
                      print(text2[itemIndex][1:])
                      result_string += text2[itemIndex][1:]+'. '
                      break
                  else:
                      print(text2[itemIndex])
                      result_string += text2[itemIndex]
                      break
      # print(result_string)
      hpfilew.write(result_string)
spell_sent()

# Associate word(spell) with character
"""
Using spellsentence.txt - would have found code to find pattern for "spell" and if character is in sentence - associate character with
spell occurence


"""


