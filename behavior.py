#FIXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX регает когда ввел существующий в системе логин 
def check(username, password):
	''' checks if user IN or NOT '''
	status = False
	status2 = False

	file = open('.lp.txt')
	for line in file:
		if username in line:
			status = True
			break
	file.close()

	file = open('.lp.txt')
	row = username+":"+password
	for line in file:
		if row in line:
			status2 = True
			break
	file.close()

	if status and status2:
		return True
		

def register(username, password, confirm):
	''' checks if password = confirm
	user IN or NOT
	if NOT func will registrate him'''
	search_name = True
	flag = False


	file = open('.lp.txt')
	for line in file:
		if username in line:
			search_name = False
			break
	file.close()

	file = open('.lp.txt', 'a')
	if password == confirm:
		flag = True
		file.write(username + ":" + password + "\n")
		file.close()
		
	if search_name and flag:
		output = True
	else:
		output = False

	return output















