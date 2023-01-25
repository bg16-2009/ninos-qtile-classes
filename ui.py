import utils, pyfiglet, os

class UI():
	def __init__(self):
		self.banner()
		print(f'''
[1] Install ninOS
[2] Modify your current system

Select your option: ''', end='')
		choice=int(input())
		if choice==1:
			os.system("clear")
			utils.check_root()
			self.install()
		elif choice==2:
			os.system("clear")
			self.modify()

	def install(self):
		print('''
Welcome to ninOS installer!

Do you want to install extra packages via a separate menu? [Y/n] ''', end='')
		opt=input()
		opt_pkg_choice=[]
		if(opt.lower()=='y'):
			os.system("clear")
			print("Opening menu....")
			time.sleep(1)
			opt_pkg_choice=self.menu()
		os.system("clear")
		print('Installing ninOS.....')
		v = input('Do you want details about the install? [Y/n] ')
		if(v.lower()=='y'):
			v=True
		elif(v.lower()=='n'):
			v=False
		utils.install_esentials(v)
		utils.install_from_list(opt_pkg_choice, v)
		utils.install_configs(v)
		os.system('sudo systemctl enable NetworkManager')
		os.system('sudo systemctl enable sddm')
		os.system("clear")
		print('Install complete!')
		print('You now have ninOS in your system!')
		print('You should reboot your compuer!')

	def modify(self):
		print('''
Welcome to ninOS!

Here you can modify your current install!
What do you want to do?
[1] Add more software via a separate menu
[2] Install configs

Type the number with your choice: ''', end='')
		choice=input()
		if(choice=='1'):
			pkg_choices=menu()
			install_from_list(pkg_choices, True)
		elif(choice=='2'):
			install_configs(False)
			print('Configs installed succesfully!')

	def banner(self):
		print(pyfiglet.figlet_format("ninOS", font="slant"))
		print(pyfiglet.figlet_format("qtile", font="digital"))

	def menu(self):
		pkgs = []
		for key, pair_list in opt_pkgs.items():
			os.system("clear")
			print('---> ' + key)
			print('\n')
			for index, pair in zip(range(0,len(pair_list)),pair_list):
				print (f'{index+1}. {pair[1]}')
			data=input('Type choices numbers separated by " " (space): ')
			if data != '':
				index_pkgs=data.split()
				for index_pkg in index_pkgs:
					pkgs.append(opt_pkgs[key][int(index_pkg)-1][0])
		os.system("clear")
		return pkgs