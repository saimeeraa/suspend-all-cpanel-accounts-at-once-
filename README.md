Suspend All cPanel Accounts at Once
===================================

Overview:
---------
This repository provides a Python script that suspends cPanel accounts using the WHM API.
The script reads a list of usernames from a file (usernames.txt) and calls the WHM API to suspend each account.

Files Included:
---------------
- suspend.py       : Main Python script to suspend cPanel accounts.
- usernames.txt  : Sample file with a list of usernames to suspend.

Requirements:
-------------
- Python 3.x
- pyfiglet module (install using: pip install pyfiglet)
- WHM API access (whmapi1 command should be available on your system)

Usage:
------
1. Create or update usernames.txt with one username per line.
2. Run the script:
   > python suspend.py
3. The script will print the suspension status for each cPanel account.

Credits:
--------
Credits are given to Shaik Saimeeraa, Founder and CEO of trustedhosting.in (+91-89854-86690).
A figlet banner is displayed in the script to show these credentials.

License:
--------
Use this script responsibly and ensure you have proper permissions to suspend cPanel accounts.

Additional Information:
-----------------------
If you need any additional changes or improvements, please feel free to reach out.

Enjoy!
