Modify Gmail signatures based on http://wescpy.blogspot.com/2016/12/modifying-email-signatures-with-gmail.html

# Setup

* Install and activate Virtualenv https://virtualenv.pypa.io/en/stable/

      virtualenv env
      source env/bin/activate

* Install Python Dependencies

      pip install -r requirements.txt

# Google API Console

* https://console.developers.google.com/apis/credentials
* Create an OAuth 2.0 client ID of type "Other"
* Download as `client_secret.json`

# Configure

* Set name in `name.txt`
* Set quotes in `quotes.txt`

# Change Signature

    python change-signature.py

* Refresh Gmail, compose new message

# Delete Signature

    python delete-signature.py

* Refresh Gmail, compose new message

