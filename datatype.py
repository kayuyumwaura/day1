def data_type(n):
	#checks if input is string.
	if isinstance (n, str):
		#checks if input is none else returns the length of string 
		if (n == 'none'): 
			print ('no value')
		else:
			print (len(n))

	#checks if input is an integer
	elif isinstance (n, int):
		if n>100:
	        return 'more than 100'

	    elif n<100:
			return 'less than 100'

    	else:
    		return 'equal to 100'len(n)

    #checks if input is a boolean if so prints the value of boolean
    elif isinstance (n, bool):
    	print (n)

    #checks if input is a list and prints the third item
    elif isinstance (n, list):
    	print (n[2])
