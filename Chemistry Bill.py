#matching elements with atomic number
def get_num(element):
	elements={'H':1, 'He':2, 'Li':3, 'Be':4, 'B':5, 'C':6, 'N':7, 'O':8, 'F':9, 'Ne':10, 'Na':11, 'Mg':12, 'Al':13, 'Si':14, 'P':15, 'S':16, 'Cl':17, 'Ar':18, 'K':19, 'Ca':20, 'Ga':31, 'Ge':32, 'As':33, 'Se':34, 'Br':35, 'Kr':36, 'Rb':37, 'Sr':38, 'In':49, 'Sn':50, 'Sb':51, 'Te':52, 'I':53, 'Xe':54, 'Cs':55, 'Ba':56, 'Tl':81, 'Pb':82, 'Bi':83, 'Po':84, 'At':85, 'Rn':86, 'Fr':87, 'Ra':88, 'Nh':113, 'Fl':114, 'Mc':115, 'Lv':116, 'Ts':117, 'Og':118}
	if element in elements:
		num=int(elements[element])
		print('  Z=', num)
	else:
		print("Element Not Supported!!")
		raise SystemExit
	return num
	
def get_element(num):
	nums={1:'H',2:'He',3:'Li',4:'Be',5:'B',6:'C',7:'N',8:'O',9:'F',10:'Ne',11:'Na',12:'Mg',13:'Al',14:'Si',15:'P',16:'S',17:'Cl',18:'Ar',19:'K',20:'Ca',31:'Ga',32:'Ge',33:'As',34:'Se',35:'Br',36:'Kr',37:'Rb',38:'Sr',49:'In',50:'Sn',51:'Sb',52:'Te',53:'I',54:'Xe',55:'Cs',56:'Ba',81:'Tl',82:'Pb',83:'Bi',84:'Po',85:'At',86:'Rn',87:'Fr',88:'Ra',113:'Nh',114:'Fl',115:'Mc',116:'Lv',117:'Ts',118:'Og'}
	if num in nums:
#		num=int(num)
		element=nums[num]
		print('  Element:', element)
	else:
		print("\033[1;31;40m")
		print("Number Not Supported!")
		raise SystemExit
	return num

#get period line			
def get_period(num):
	if num<=2:
		per=1
	elif num<=10:
		per=2
	elif num<=18:
		per=3
	elif num<=36:
		per=4
	elif num<=54:
		per=5
	elif num<=86:
		per=6
	elif num<=118:
		per=7
	print('  Period line:',per)

def get_group(num):
	if num==1:
		group=1
	elif num==2:
		group=18
	elif num<=10:
		ll= num - 2
		if ll <=2:
			group = ll
		else:
			group = ll + 10
	elif num<=18:
		ll = num - 10
		if ll <= 2:
			group = ll
		else:
			group = ll + 10
	elif num<=36:
		if num <= 20:
			ll= num - 18
			group = ll
		else:
			ll= num - 28
			group = ll + 10 
	elif num<=54:
		if num <= 38:
			ll = num - 36
			group = ll
		else:
			ll = num - 46
			group = ll + 10
	elif num<=86:
		if num <= 56:
			ll = num - 46
			group = ll
		else:
			ll = num - 78
			group = ll + 10
	elif num<=118:
		if num <= 88:
			ll = num - 86
			group = ll
		else:
			ll = num - 110
			group = ll + 10
	print('  Group :',group)
		
#painting
def painting():
	print("\033[1;34;40m ")
	print( '   * o          ')
	print('         ' )
	print('  \  o /   ')
	print(  '   \  /    ')
	print('   / \                  Python program for chemistry')
	print('  /o   \ ' )   
	print(' /______\                 Made by ~Bill~')
	print("\033[1;37;40m")		


#allocate layers
def allocate(num):
	global k, l, m, n, o, p, q
	if num<2:
		k = 1
		num=0
	elif num>=2:
		k = 2
		num=num - 2
	if num <= 8:
		l = num
		num=0
	elif num>8:
		l = 8
		num=num-8

	if num<9:
		m = num
		num=0
	elif num>8 and num<19:
		m = 8
		num=num-8
	elif num>18:
		m= 18
		num=num-18
		
	if num<9:
		n = num
		num=0
	elif num>8 and num<19:
		n = 8
		num=num-8
	elif num>18 and num<33:
		n = 18
		num=num-18
	elif num>32:
		n = 32
		num=num-32 

	if num<9:
		o = num
		num=0
	elif num>8 and num<19:
		o = 8
		num=num-8
	elif num>18 and num<33:
		o = 18
		num=num-18
	elif num>32:
		o = 32
		num=num-32 

	if num<9:
		p= num
		num=0
	elif num>8 and num<19:
		p = 8
		num=num-8
	elif num>18 and num<33:
		p = 18
		num=num-18
	elif num>32:
		p = 32
		num=num-32 

	if num<9:
		q = num
		num=0
	elif num>8 and num<19:
		q= 8
		num=num-8

#input and modes
painting()
print('   [1] Give an element')
print('   [2] Give a number')
print('   [3] Give period line and group')
mode=input("Choose a mode:")
if mode=='1':
	element=input(" Type an element from 	the A group:")
	num=get_num(str(element))
	print("\033[1;33;40m")
	period=get_period(num)
	group=get_group(num)
	allocate(num)
elif mode=='2':
	num=input('Type an atomic number:')
	element=get_element(str(num))
	print("\033[1;33;40m")
	period=get_period(num)
	group=get_group(num)
	allocate(num)


print("\033[1;36;40m")
print(' K',[k],'L',[l],'M',[m],'N',[n],'O',[o],'P',[p],'Q',[q])
