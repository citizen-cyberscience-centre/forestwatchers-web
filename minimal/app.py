# This file is part of minimal.
# 
# minimal is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# minimal is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with minimal.  If not, see <http://www.gnu.org/licenses/>.

import os
from flask import Flask, render_template, abort, request
from datetime import datetime
from views.assets import assets

app = Flask(__name__)
print assets.static_folder
app.register_blueprint(assets, url_prefix="/assets")

import settings_local as settings

# Set up the configuration values for the application
app.config.from_object(settings)

# Pass all these variables to all the views
@app.context_processor
def global_template_context():
    return dict(
         brand = app.config['BRAND'],
         title = app.config['TITLE'],
         copyright = app.config['COPYRIGHT'],
         description = app.config['DESCRIPTION'],
         trackingcode = app.config['TRACKINGCODE'],
         herounit = app.config['HEROUNIT'],
         carousel = app.config['CAROUSEL'],
         year = datetime.now().year
         )

# Show the index page
@app.route('/')
def index():
    try:
        return render_template('index.html')
    except:
        return render_template('index.html.template')


@app.route('/<page>')
def page(page):
    try: 
        print "Trying to show %s" % page
        return render_template(page)
    except:
        print "Sorry, page not found"
        return abort(404)

if __name__ == '__main__':
    #configure_app(app)
    app.run()
