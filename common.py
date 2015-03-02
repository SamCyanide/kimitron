
#############
# common.py #
#############
# functions not part of the core of the bot but useful for multiple commands

# TODO: clean up a little, possibly add maximum recursion level
def html_to_irc(root):
  '''returns a string that consists of the content of an HTML element
  replacing common formatting elements with approximate IRC formatting'''
  
	if root.text == None:
		message = ''
	else:
		message = root.text
	for el in root.iterchildren():
		if el.tail == None:
			el.tail = ''
		if el.tag.lower() == 'a':
			message += html_to_irc(el)
			if el.get('href', None) == None:
				continue
			else:
				if el.get('href').startswith('/'):
					href = 'http://knowyourmeme.com' + el.get('href')
				else:
					href = el.get('href')
			if message[-1] in ' \r\n':
				message += message[:-1] + ' (' + href + ')' + message[-1]
			else:
				message += ' (' + href + ')'
			message += el.tail
		elif el.tag.lower() == 'blockquote':
			message += ' \x0301,00'
			message += html_to_irc(el)
			message += '\x0301,99 '
			message += el.tail
		elif el.tag.lower() == 'img':
			if el.get('src', None) == None:
				continue
			else:
				src = el.get('src')
			message += '{' + src + '}'
			message += el.tail
		elif el.tag.lower() == 'b' or el.tag.lower() == 'strong':
			message += '\x02'
			message += html_to_irc(el)
			message += '\x02'
			message += el.tail
		elif el.tag.lower() == 'i' or el.tag.lower() == 'em':
			message += '\x1d'
			message += html_to_irc(el)
			message += '\x1d'
			message += el.tail
		elif el.tag.lower() == 'u':
			message += '\x1f'
			message += html_to_irc(el)
			message += '\x1f'
			message += el.tail
		elif el.tag.lower() == 'div' or el.tag.lower() == 'p':
			message += ' ' + html_to_irc(el) + ' '
			message += el.tail
		elif el.tag.lower() == 'br':
			message += ' ' + el.tail
		else:
			message += html_to_irc(el)
			message += el.tail
	return message
