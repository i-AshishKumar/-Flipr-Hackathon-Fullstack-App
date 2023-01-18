# Flipr Hackathon Fullstack Web Application

## Installation

Clone this repository (Make sure you have 'git' and python installed)

```bash
git clone https://github.com/i-AshishKumar/Flipr-Hackathon-Fullstack-App.git
```
Move to the application directory
```bash
cd Flipr-Hackathon-Fullstack-App
```
Install the requirements to run the application from requiremnets.txt
```bash
pip install -r requirements.txt
```
Run the application on the local server
```bash
python manage.py runserver
```


## Usage

* A user should be authenticated (logged in) to access the NSE/BSE or Companies tab, else the data won't be displayed.
* Click on Sign Up to register for a new account, after signup user will be redirected to home page where the user can access the NSE/BSE and Companies tabs on the navigation bar 
* In NSE/BSE page, there is a button group with NSE and BSE buttons click on either of them to see the data and their respective chart
* In Companies tab there will be a dropdown menu with 5 companies upon choosing one their respective data and chart will be displayed.
* After accessing the data, the user can log out using the logout button in the top right corner of the nav bar.

All Data Access API endpoints can be accessed through the list below:

>[https://stockindex.up.railway.app/api/bse/](https://stockindex.up.railway.app/api/bse/)

>[https://stockindex.up.railway.app/api/nse/](https://stockindex.up.railway.app/api/nse/)

>[https://stockindex.up.railway.app/api/ashok/](https://stockindex.up.railway.app/api/ashok/)

>[https://stockindex.up.railway.app/api/cipla/](https://stockindex.up.railway.app/api/cipla/)

>[https://stockindex.up.railway.app/api/eicher/](https://stockindex.up.railway.app/api/eicher/)

>[https://stockindex.up.railway.app/api/reliance/](https://stockindex.up.railway.app/api/reliance/)

>[https://stockindex.up.railway.app/api/tata/](https://stockindex.up.railway.app/api/tata/)

Register and Login API endpoints can be accessed through the list below:
>[https://stockindex.up.railway.app/api/register/](https://stockindex.up.railway.app/api/register/)

> [https://stockindex.up.railway.app/api/login/](https://stockindex.up.railway.app/api/login/)


If you want to access these endpoints locally, just replace https://stockindex.up.railway.app with **localhost or 127.0.0.1:8000**

## NOTE: 
Please wait for a minute after clicking on 'NSE/BSE' tab or 'Companies' tab as the data is processed by extracting it from the API.
