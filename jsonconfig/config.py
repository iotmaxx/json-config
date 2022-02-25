""" 
json-config - JSON configuration file handler
Copyright (C) 2022 IoTmaxx GmbH

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import os
import json

class JSONConfig:
    filename = None
    defaults = None

    def __init__(self, filename):
        self.filename = filename
        self.load()

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.defaults = json.loads(f.read())
        else :
            self.defaults = {}
        return
    
    def save(self):
        if self.defaults == None:
            self.defaults = {}
        with open(self.filename, "w") as f:
            f.write(json.dumps(self.defaults, sort_keys=True, indent=4))
            f.close()
        return

    def read(self, domain, key, default = None):
        if self.defaults == None :
            return default
        if domain in self.defaults:
            if key in self.defaults[domain] :
                return self.defaults[domain][key]
        return default
    
    def write(self, domain, key, value):
        if self.defaults == None:
            self.defaults = {}
        if domain in self.defaults:
            self.defaults[domain][key] = value
        else:
            self.defaults[domain] = {}
            self.defaults[domain][key] = value
        return
        
    def hasEntries(self):
        return bool(self.defaults)
        
    def get(self):
        return self.defaults
        


