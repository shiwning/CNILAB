# License
*This is Project 3 of CNI course in Department of Software Engineering, School of Informatics, Xiamen University.*  

## Dependencies 
- Python 3
- SQLite 3
- Django 3
- Bootstrap 3

## Protocol
### Client
```
PURC:[username]:[password]:[userNum] # Purchase license from the server
HELO:[license]                       # Say hello to the server with license
CKAL:[license]:[ticket]              # Check ticket alive
RELS:[license]:[ticket]              # Release ticket
```
### Server
```
UKNW:[info]                          # Cannot recognize unknown request
PERM:[license]                       # Permit license request
FAIL:[info]                          # Fail to give a license
WELC:[ticket]                        # Give a ticket
RFUS:[info]                          # Refuse to give a ticket,
                                     # or to keep a client alive
GOOD:                                # Permit the alive check
WARN:[info]                          # Receive an unused ticket from a client
GBYE:[info]                          # Say goodbye to a client
```

## Usage
### Client
```
python client.py [--mode]
```
Mode list:
 - -p, --purchse
 - -r, --run
### Server
```
python server.py
```
Automatically run the Django server (Port:8000):  
(Please check and edit `ult/ServerAct.py` from Line 22 to 28)
```
python manage.py runserver
```

## Compile with PyInstaller in Windows
### Client
```
pyinstaller client.py [-F]
```
### Server
- 1. Check and edit `ult/ServerAct.py` from Line 22 to 28.
- 2. Compile `manage.py` and `client.py`. It is not recommended to pack `manage` only as an exe file because of the huge file size of the Django project after compilation.
```
pyinstaller manage.py
pyinstaller client.py [-F]
```
- 3. Put `client.exe`, `manage.exe`, `/static` and `/templates` under the same folder.

**Because of some problem in PyInstaller, we don't guarantee that the web UI can work normally in Firefox browser!!!**
