from utility import *
from zipfile import ZipFile
import wget
import ctypes, sys
import os

def is_winapp_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_with_UAC_permission(func):
	if is_winapp_admin():
	    # Code of your program here
	    func()
	else:
	    # Re-run the program with admin rights
	    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)



filename = 'config.ini'
config = read_configuration_ini(filename)

def update_blocker():
	
	update_blocker_exe_url = config['urls']['update_blocker_url']
	update_blocker_filename = config['urls']['update_blocker_filename']
	updater_exe = config['urls']['updater_exe']
	container_folder = config['urls']['file_container_folder']
	dirname = os.path.dirname(__file__)

	if not os.path.exists(container_folder):
		os.mkdir(container_folder)

	container_folder = os.path.join(dirname,container_folder)
	os.chdir( container_folder )

	#update_blocker_filename = os.path.join( container_folder, update_blocker_filename )

	wget.download(update_blocker_exe_url,update_blocker_filename)


	# Create a ZipFile Object and load sample.zip in it
	with ZipFile(update_blocker_filename, 'r') as zipObj:
	   # Extract all the contents of zip file in current directory
	   zipObj.extractall()
	

	
	filename = os.path.join(container_folder, updater_exe)
	os.startfile(filename)

	os.chdir('..')

def debloat():
	#os.system('taskmgr')
	debloater_url = config['urls']['bloater_power_shell_script']
	debloating_meta_command = config['urls']['debloating_command']
	#-NoExit
	debloating_command = debloating_meta_command.replace('<debloater_url>',debloater_url)

	os.system(debloating_command)


def clear_startups():
	#windowuser_name = config['urls']['username_folder_name']
	windowuser_name = os.getlogin()
	user_startup_folder_link = config['urls']['startup_url'].replace('<username_folder_name>',windowuser_name)
	common_startup_folder_link = config['urls']['common_startup_url']

	
	os.system("taskmgr")
	os.system("explorer "+user_startup_folder_link)
	os.system("explorer "+common_startup_folder_link)
	


def main():
	print("Make sure you updated your computer, before cleaning process")
	
	print(" Step1 : Block Auto-Updating your pc \n Beginning file download for update blocker. \n Unziping and running update blocker. \n Check at Disable Updates and Protect service settings and click Apply Now.")
	update_blocker()
	
	print(" Step2 : Debloating windows10 , click yes or no to go through process\n Click no when asked to reboot your computer.")
	debloat()
	
	print(" Step3 : Got to taskmanager, click on More Details, then startup.\n Disable any unnecessary progras at startups.\n Then go to 2 opened startup folder at file explorer and clean all unnecessary startup programs")
	clear_startups()

if __name__ == '__main__':
	run_with_UAC_permission(main)
	
