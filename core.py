

 #########
# core.py #
 #########
# the core code of the bot, essential for its operation

def irc_upper(string):
  '''converts the characters in a string to upper case according to the IRC
  standard'''
  
  string = string.upper()
  string = string.replace('{', '[')
  string = string.replace('}', ']')
  string = string.replace('|', '\\')
  string = string.replace('^', '~')
  
  return string
