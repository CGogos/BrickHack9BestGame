#import bad-words.txt as bw

def filesToList():
  with open('bad-words.txt', 'r') as file:
    lines = file.readline()
  return lines
  
badWordList = filesToList()