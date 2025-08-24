#Funkcja przyjmująca dwa argumenty
def do_action(action, parameter):
	print(f'action: {action}')
	print(f'parameter: {parameter}')
	return

do_action('buy','shoes')

print('\n') 

def do_action2(action, *parameter):
	print(f'action: {action}')
	print(f'parameter: {parameter}')
	for element in parameter:
		print(f'element is {parameter}')
	return

do_action2('buy','shoes','socks','t-shirt')
