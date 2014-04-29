#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

#asp = zqaqzamavpjelxui

import os
import urllib

from google.appengine.api import users
from google.appengine.ext import db

import jinja2
import webapp2

import models
import gviz_api

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class DataHandler(webapp2.RequestHandler):
	def get(self):
	  	listings = db.GqlQuery("SELECT * FROM Listing")
	  	description = [("username", "string"),
					   ("name", "string"),
				 	   ("year", "string"),
					   ("section", "string"),
					   ("title", "string"),
					   ("category", "string"),
					   ("description", "string"),
					   ("partcipant_count", "string"),
					   ("donor_list", "string"),
					   ("email", "string"),
					   ("opening_bid", "string")]
		data = []
		for listing in listings:
		  data.append([listing.username, 
		    listing.name,
		    listing.year,
		    listing.section,
		    listing.title, 
		    listing.category,
		    listing.description,
		    listing.partcipant_count,
		    listing.donor_list,
		    listing.email,
		    listing.opening_bid])
		data_table = gviz_api.DataTable(description)
		data_table.LoadData(data)
		self.response.write(data_table.ToJSonResponse())

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	template_values = {}
    	template = JINJA_ENVIRONMENT.get_template('index.htm')
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/query', DataHandler)
], debug=True)
