import __builtin__
from flask import Flask
from flask import url_for, redirect, render_template, request, abort

from foxycart import FoxyData
import urllib


__SECRET_KEY = 'YOUR SECRET API KEY'

app = Flask(__name__)


def foxyDataFeed():
    rawData = request.get_data()
    parameter = 'FoxyData='

    if (len(rawData) <= len(parameter)):
        abort(401)

    if rawData[:len(parameter)].lower() != parameter.lower():
        abort(401)

    rawData = rawData[len(parameter):];

    encrypedData = urllib.unquote_plus(rawData)

    fData = FoxyData.from_crypted_str(encrypedData, __SECRET_KEY)

    print("=========== FOXY DATA =========================")
    print(fData)
	
	# Look at django example for what you can do with FoxyData
	
    return ""


if __name__ == '__main__':
   app.run(debug=True)
