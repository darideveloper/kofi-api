<div><a href='https://github.com/tree/master/blob/master/LICENSE' target='_blank'>
                <img src='https://img.shields.io/github/license/tree/master.svg?style=for-the-badge' alt='MIT License' height='30px'/>
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

<div align='center'><a href='https://github.com/darideveloper/nyxtrackers' target='_blank'> <img src='https://github.com/darideveloper/nyxtrackers/raw/master/public/logo.png' alt='Nyx Trackers' title='Nyx Trackers' height='50px'/> </a></div>

# Details

For run the project, you should host it, or use a tool link [Ngrok](https://ngrok.com/), to make public a localhost project. 

You need also your `Kofi Token`, `Google Sheet API Key`, and `Email Credentials`. 

More details are in the `Settings` section.

## Data from Kofi

Each time (donation or sale), the project gets: 

* date
* time 
* user name
* message
* amount
* email
* currency
* shop_items (if apply)
* shipping (if apply)

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
```

*Note: you can see as reference the **sample.env** file*

### KOFI_TOKEN

You Kofi token. You can get it [ko-fi.com/manage/webhooks](https://ko-fi.com/manage/webhooks), in the `advanced` section.

![kofi token](https://github.com/darideveloper/kofi-api-sheets-email/blob/master/screenshots/kofi-token.png?raw=true)

### GOOGLE_SHEETS

The link of the google sheet where data will be saved. 

The file can be named as you like, but you should have a sheet named "kofi", and the following columns in the same order:

* date
* time
* user name
* message
* amount
* email
* currency
* shop items
* shipping

After create it, be sure to generate the link with edit permisions. You can do it, following the [this tutorial](https://github.com/darideveloper/tutorials/blob/master/share%20google%20sheet%20with%20edit%20permissions/README.md)

## Google Sheets credentials

You should create a credentials file from your Google Console, with the same account owner of the Google Sheets file,  to allow connect to it. 

1. Generate if following [this tutorial](https://github.com/darideveloper/tutorials/blob/master/generate%20google%20sheets%20api%20key/README.md).
2. Download the json file.
3. Place in the project folder as `credentials.json`

## Setup Kofi Webhook

After deploying the project, update the link provided by your hosting, in [ko-fi.com/manage/webhooks](https://ko-fi.com/manage/webhooks)

![kofi setup webhook](https://github.com/darideveloper/kofi-api-sheets-email/blob/master/screenshots/kofi-setup-webhook.png?raw=true)

# Run

Run the flask app with python
```sh
python app.py
```

# Deploy

The project has been created to be hosted in [Heroku](https://www.heroku.com/), this is because it is the recommended hosting.

# Roadmap

* [ ] WebHook for get donations and payments
* [ ] Save data in google sheets
* [ ] Send email to clients

