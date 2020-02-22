# check why all programs is not listed
import wmi
w = wmi.WMI()
for p in w.Win32_Product():
	print(p.Name)
	if 'Box, Inc.' == p.Vendor and p.Caption and 'Box Sync' in p.Caption:
		print('Installed {}'.format(p.Version))