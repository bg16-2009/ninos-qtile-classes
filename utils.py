from pkgs import pkgs_esential
import os, shutil, sys

def install_pkg(pkg, v):
	if(v==True):
		print(f'Installing {pkg}....')
	os.popen(f'nohup sudo pacman -S {pkg} --noconfirm > ninos.log').read()

def install_from_list(pkgs, v):
	for pkg in pkgs:
		install_pkg(pkg, v)

def install_esentials(v):
	install_from_list(pkgs_esential, v)

def install_configs(v):
	home=os.popen('echo $HOME').read()
	if(v==True):
		print(f'Installing special configs in the {home} directory')
		print('If you are not using root as your user, you should run "python main.py" after this is done and choose modify and install configs')
		print('(If something goes wrong you can reinstall them from the modify menu)')
	os.system(f'mkdir {home}/.config/alacritty')
	shutil.copy(
		f'{os.getcwd()}/configs/alacritty/alacritty.yml', 
		f'{home}/.config/alacritty/'
	)
	shutil.copy(
		f'{os.getcwd()}/configs/.Xauthority', 
		f'{home}/'
	)
	shutil.copy(
		f'{os.getcwd()}/configs/config.py', 
		f'{home}/.config/qtile/'
	)

def print_text_center(text):
	#os.system('setterm -term linux -back blue -fore white -clear')
	rows, columns = os.popen('stty size', 'r').read().split()
	rows = int(rows)
	columns = int(columns)
	result=''
	for i in range(1, rows//2 - text.count('\n')//2 ):
		result += '\n'
	for line in text.split('\n'):
		result += line.center(columns)
		result+='\n'
	for i in range(1, rows//2 - text.count('\n')//2 ):
		result += '\n'
	os.system("clear")
	print(result)

def check_root():
	if(os.system("./check_root.sh")!=0):
		print_text_center('''Please run as root using command
"sudo ./venv/bin/python main.py"''')
		sys.exit()