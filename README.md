Nanodegree P§ Item Catalog
================================

Creating a web application using flask, SQLite and OAuthentification

Requirements
------------
1. Install Vagrant and VirtualBox
2. Clone the fullstack-nanodegree-vm repository
3. Launch the Vagrant VM

Dependencies and supported Python versions
------------------------------------------
- Python version 2.7.6
- flask
- sqlalchemy
- database_setup_JSON
- httplib2
- oauth2client.client
- os
- werkzeug

Creating Database
----------------- 
In order to setup the database and populate the data, please run this commands:

    python database_setup.py
    python init_events.py

Test
------
Run the web server using:
```python
python application.py
```