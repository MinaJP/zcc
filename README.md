# Zendesk Ticket Viewer CLI


### Set Up 
Set up the Virtual environment

```
   python3 -m venv venv
```

Activate the Virtual environment

```
   source venv/bin/activate
```

Install the Requirements

```
   pip install -r requirements.txt
```

(run `deactivate ` to deactivate the virtualenv)

Add .env file to the directory
.env file should contains:
```
DOMAIN=yourdomainname
EMAIL=youremail@..
PASSWORD=yourp@ssw0rd
```
### Usage
Activate the command line by running
```
python3 main.py
```
and follow the instructions.

Basic commands:
* help -view list of commands and description
* list - shows maximum of 25 tickets available on the current page. It is defualt to first page when it is first call
* ticket {id} - shows detail page of ticket with the id:{id}
* prev_page - will display previous page if available
* next_page - will display next page if available

### Test
Run
```
python3 test.py
```
for unit test


