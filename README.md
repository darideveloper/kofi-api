<div><a href='https://github.com/darideveloper/kofi-api/blob/master/LICENSE' target='_blank'>
                <img src='https://img.shields.io/github/license/darideveloper/kofi-api.svg?style=for-the-badge' alt='MIT License' height='30px'/>
            </a><a href='https://www.linkedin.com/in/francisco-dari-hernandez-6456b6181/' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=LinkedIn&color=0A66C2&logo=LinkedIn&logoColor=FFFFFF&label=' alt='Linkedin' height='30px'/>
            </a><a href='https://t.me/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Telegram&color=26A5E4&logo=Telegram&logoColor=FFFFFF&label=' alt='Telegram' height='30px'/>
            </a><a href='https://github.com/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=GitHub&color=181717&logo=GitHub&logoColor=FFFFFF&label=' alt='Github' height='30px'/>
            </a><a href='https://www.fiverr.com/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Fiverr&color=222222&logo=Fiverr&logoColor=1DBF73&label=' alt='Fiverr' height='30px'/>
            </a><a href='https://discord.com/users/992019836811083826' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Discord&color=5865F2&logo=Discord&logoColor=FFFFFF&label=' alt='Discord' height='30px'/>
            </a><a href='mailto:darideveloper@gmail.com?subject=Hello Dari Developer' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Gmail&color=EA4335&logo=Gmail&logoColor=FFFFFF&label=' alt='Gmail' height='30px'/>
            </a><a href='https://www.twitch.tv/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Twitch&color=b9a3e3&logo=Twitch&logoColor=ffffff&label=' alt='Twitch' height='30px'/>
            </a></div><div align='center'><br><br><img src='https://github.com/darideveloper/kofi-api-sheets-email/blob/master/logo.png?raw=true' alt='Kofi Api' height='80px'/>



# Kofi Api

Webhook to get Kofi payments and donations, save the data on Google Sheets, and submit confirmation emails to clients

Project type: **client**

</div><br><details>
            <summary>Table of Contents</summary>
            <ol>
<li><a href='#buildwith'>Build With</a></li>
<li><a href='#relatedprojects'>Related Projects</a></li>
<li><a href='#media'>Media</a></li>
<li><a href='#details'>Details</a></li>
<li><a href='#install'>Install</a></li>
<li><a href='#settings'>Settings</a></li>
<li><a href='#run'>Run</a></li>
<li><a href='#deploy'>Deploy</a></li>
<li><a href='#roadmap'>Roadmap</a></li></ol>
        </details><br>

# Build with

<div align='center'><a href='https://developer.mozilla.org/en-US/docs/Web/HTML' target='_blank'> <img src='https://i.imgur.com/OitgDfl.jpeg' alt='HTML + CSS' title='HTML + CSS' height='50px'/> </a><a href='https://www.python.org/' target='_blank'> <img src='https://cdn.svgporn.com/logos/python.svg' alt='Python' title='Python' height='50px'/> </a><a href='https://flask.palletsprojects.com/en/2.2.x/' target='_blank'> <img src='https://cdn.svgporn.com/logos/flask.svg' alt='Flask' title='Flask' height='50px'/> </a><a href='https://sheets.google.com/' target='_blank'> <img src='https://www.gstatic.com/images/branding/product/1x/sheets_2020q4_48dp.png' alt='Google Sheets' title='Google Sheets' height='50px'/> </a></div>

# Related projects

<div align='center'><a href='https://github.com/darideveloper/nyxtrackers' target='_blank'> <img src='https://github.com/darideveloper/nyxtrackers/raw/master/public/logo.png' alt='Nyx Trackers' title='Nyx Trackers' height='50px'/> </a><a href='https://github.com/darideveloper/pack-link-bot' target='_blank'> <img src='https://github.com/darideveloper/pack-link-bot/blob/master/logo.png?raw=true' alt='Pack Link Bot' title='Pack Link Bot' height='50px'/> </a></div>

# Details

For run the project, you should host it, or use a tool link [Ngrok](https://ngrok.com/), to make public a localhost project. 

You need also your `Kofi Token`, `Google Sheet API Key`, and `Email Credentials`. 

More details are in the `Settings` section.

## Data from Kofi

### Donations
Each time donation, the project gets: 

* date
* time 
* user name
* **message**
* amount
* email
* currency
* url

### Sales
Each time sales, the project gets: 

* date
* time 
* user name
* amount
* email
* currency
* shop items
* shop items links
* shipping name
* country
* shipping
* url

### Commissions
* date
* time 
* user name 
* amount 
* email
* currency 
* country
* full address
* url

# Install

## Third party modules

Install all the python modules from pip: 

``` bash
$ pip install -r requirements.txt
```

# Settings

## Enviroment variables

In the file *.env*, are the main options and settings of the project.

Create a **.env** file, and place the following content

```bash
KOFI_TOKEN=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
GOOGLE_SHEETS=https://docs.google.com/spreadsheets/d/{random-chars}/edit?usp=sharing
EMAIL_USER=youremail@mail.com
EMAIL_PASS=yourpass123*
EMAIL_SUBJECT_STORE=your-store-name
DEBUG_EMAIL_TO=yourotheremail@mail.com
```

*Note: you can see as reference the **sample.env** file*

### KOFI_TOKEN

You Kofi token. You can get it [ko-fi.com/manage/webhooks](https://ko-fi.com/manage/webhooks), in the `advanced` section.

![kofi token](https://github.com/darideveloper/kofi-api-sheets-email/blob/master/screenshots/kofi-token.png?raw=true)

### GOOGLE_SHEETS

The link of the google sheet where data will be saved. 


1. The file can be named as you like, but you should have a sheet named `kofi donations`, and the following columns in the same order:

* date
* time 
* user name
* **message**
* amount
* email
* currency
* url

2. And a sheet names `kofi sales` with the columns: 

* date
* time 
* user name
* amount
* email
* currency
* shop items
* shop items links
* shipping name
* country
* shipping
* url

3. And a sheet names `kofi commissions` with the columns: 

* date
* time 
* user name 
* amount 
* email
* currency 
* country
* full address
* url

3. After create them, be sure to generate the link with edit permisions. You can do it, following the [this tutorial](https://github.com/darideveloper/tutorials/blob/master/share%20google%20sheet%20with%20edit%20permissions/README.md)

### EMAIL_USER

Your email user, who will send the notifications email to the clients. 
The project supports *gmail, outlook, hotmail, live, yahoo* and *aol*.

### EMAIL_PASS

You email password. 

Usually, the email services **don't allow you to connect directly with your password**, instead of that, you should create a secondary password, and use it. 
Here a tutorial about **[how to generate an alternative password (application password) in gmaill](https://github.com/darideveloper/tutorials/tree/master/generate%20gmail%20application%20password)**

### EMAIL_SUBJECT_STORE

Store name to generate the thanks email subject, like: 

* Thanks for your support to **your-store-name**
* Thanks for purchasing **your-store-name**

 ### DEBUG_EMAIL_TO
 
An email where you'll get a notification if something was wrong. It can be the same as `EMAIL_USER`

## Google Sheets credentials

You should create a credentials file from your Google Console, with the same account owner of the Google Sheets file,  to allow connect to it. 

1. Generate if following [this tutorial](https://github.com/darideveloper/tutorials/blob/master/generate%20google%20sheets%20api%20key/README.md).
2. Download the json file.
3. Place in the project folder as `credentials.json`

## Setup Kofi Webhook

After deploying the project, update the link provided by your hosting, in [ko-fi.com/manage/webhooks](https://ko-fi.com/manage/webhooks)

![kofi setup webhook](https://github.com/darideveloper/kofi-api-sheets-email/blob/master/screenshots/kofi-setup-webhook.png?raw=true)

## HTML TEMPLATE

You can edit the HTML to submit to the client, after a sale or donation, editing the file `templates/thanks.html`. 

You render the user name, using "user_name" and the event type (Donation, or Shop Order) using "res_type".

Here is the default code and the result email.

*Note: if you want to use images, upload then to an image server or github, and place in the HTML only the link*

```html
<style>
  @import url('https://fonts.googleapis.com/css2?family=Asap+Condensed:wght@700&display=swap');

  h1 {
    font-family: 'Asap Condensed', sans-serif;
    font-size: 2.5rem;
    text-align: center;
    color:#2c3333;
  }

</style>

<h1>user_name Thanks for your res_type</h1>
<img width="800" src="https://raw.githubusercontent.com/darideveloper/kofi-api-sheets-email/master/imgs/banner.webp">
```

![email sample](https://github.com/darideveloper/kofi-api-sheets-email/blob/master/screenshots/email.png?raw=true)

# Run

Run the flask app with python
```sh
python app.py
```

# Deploy

The project has been created to be hosted in [Heroku](https://www.heroku.com/), this is because it is the recommended hosting.

# Roadmap

* [X] WebHook for get donations and payments
* [X] Save donations data in google sheets
* [X] Save sales data in google sheets
* [X] Send email to clients with html template
* [X] Send email when error happens

