from utility import *
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

	
	
	os.system("explorer "+user_startup_folder_link)
	os.system("explorer "+common_startup_folder_link)
	


def main():
	debloat()
	clear_startups()

if __name__ == '__main__':
	run_with_UAC_permission(main)
