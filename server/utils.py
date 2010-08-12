"""
   Copyright 2010 Daniel Graziotin <daniel.graziotin@acm.org>

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

"""
This module holds some utility functions.
"""

import time

import datetime
import models

def now():
    """
    Returns a timestamp representing the current time, suitable for XML-RPC
    """
    now_seconds = time.time()
    now_date = datetime.datetime.fromtimestamp(now_seconds)
    return now_date.isoformat(' ')

def now_plus_minutes(num_minutes):
    """
    Returns a timestamp representing the current time plus a given number
    of minutes, suitable for XML-RPC
    """
    now_seconds = time.time()
    now_date = datetime.datetime.fromtimestamp(now_seconds)
    now_plus = now_date + timedelta(minutes=num_minutes)
    return now_plus.isoformat(' ')

def now_minus_minutes(num_minutes):
    """
    Returns a timestamp representing the current time minus a given number
    of minutes, suitable for XML-RPC
    """
    now_seconds = time.time()
    now_date = datetime.datetime.fromtimestamp(now_seconds)
    now_minus = now_date - timedelta(minutes=num_minutes)
    return now_minus.isoformat(' ')


def clean_ids(dictionary):
    """
    Removes attributes with key 'id' from dictionaries. Suitable for XML-RPC
    returns
    """
    try:
        del dictionary['id']
    except KeyError:
        pass
    return dictionary

def populate_object_from_dictionary(obj, dictionary):
    """
    Given an object and a dictionary, it updates all the object's
    attributes with name matching a key of the dictionary
    """
    obj.__dict__.update(dictionary)
    return obj

def synchronize_objects(old_obj, new_obj):
    """
    Synchronizes attributes values of two objects
    """
    for key in old_obj.__dict__:
        if key != 'id' and key != '_state':
            old_obj.__dict__[key] = new_obj.__dict__[key]
    return old_obj

def get_location_from_array(locations, point="dest"):
    for location in locations:
        if location["point"] == point:
            return location
    return none

def get_xmlrpc_user(kwargs):
    """
    Returns the Person object that is performing an XML-RPC call
    """
    try:
        return models.Person.objects.get(
                                         username=kwargs['request'].META['REMOTE_USER']
                                         )
    except (models.Person.DoesNotExist, KeyError):
        return None

def get_rest_user(request):
    """
    Returns the Person object that is performing a REST call
    """
    try:
        return models.Person.objects.get(
                                         username=request.META['REMOTE_USER']
                                         )
    except (models.Person.DoesNotExist, KeyError):
        return None

    