#!/usr/bin/env python3

import sys
import os
import json
import datetime
import functools

TIMELINE_CHAR_LENGTH = 100

class Person:
    def __init__(self, firstname=None, lastname=None, nickname=None, dob=None, nationality=None):
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
        self.nationality = nationality
        if firstname == None and lastname == None and nickname == None:
            raise Exception("Person must have a name")

        # Each person must be identifyable by a name, the nickname should always be filled
        if nickname == None:
            if firstname == None:
                self.nickname = lastname
            else:
                self.nickname = firstname

class AssociatedPerson(Person):
    pass

class MemoirOwner(Person):
    pass

class Location:
    def __init__(self, street=None, suburb=None, city=None, state=None, country=None, region=None, lat=None, lon=None):
        self.street = street
        self.suburb = suburb
        self.city = city
        self.state = state
        self.country = country
        self.region = region
        self.lat = lat
        self.lon = lon

    def reproject(from_crs, to_crs):
        print("Nothing setup for this yet")

@functools.total_ordering
class Event:
    def __init__(self, story, on_year, on_month=None, on_day=None, on_hour=None, on_minute=None, people_involved=None, location=None, keywords=None, photo_details=None):
        self.story = story
        self.on_year = on_year

        if on_month is None:
            self.on_month = 1
            self.on_month_unknown = True
        else:
            self.on_month = on_month
            self.on_month_unknown = False

        if on_day is None:
            self.on_day = 1
            self.on_day_unknown = True
        else:
            self.on_day = on_day
            self.on_day_unknown = False

        if on_hour is None:
            self.on_hour = 0
            self.on_hour_unknown = True
        else:
            self.on_hour = on_hour
            self.on_hour_unknown = False

        if on_minute is None:
            self.on_minute = 0
            self.on_minute_unknown = True
        else:
            self.on_minute = on_minute
            self.on_minute_unknown = False

        self.people_involved = people_involved
        self.location = location
        self.keywords = keywords
        self.photo_details = photo_details

    def datetuple(self):
        return (self.on_year, self.on_month, self.on_day, self.on_hour, self.on_minute)

    def datetime(self):
        return datetime.datetime(year = self.on_year,
                                 month = self.on_month,
                                 day = self.on_day,
                                 hour = self.on_hour,
                                 minute = self.on_minute)

    def __lt__(self, other):
        return ((self.on_year, self.on_month, self.on_day, self.on_minute) <
                (other.on_year, other.on_month, other.on_day, other.on_minute))

    def __eq__(self, other):
        return ((self.on_year, self.on_month, self.on_day, self.on_minute) ==
                (other.on_year, other.on_month, other.on_day, other.on_minute))

class Timeline:
    def __init__(self, list_of_events):
        assert type(list_of_events) is list
        self.list_of_events = list_of_events
        self.list_of_events.sort()
        self.start_date = list_of_events[0].datetime()
        self.end_date = list_of_events[-1].datetime()

    def print_timeline(self):
        start_string = "[start] {}".format(self.start_date)
        end_string = "[end] {}".format(self.end_date)
        print(start_string)
        print("|")
        for i in range(TIMELINE_CHAR_LENGTH):
            print("=", end='')
        print()
        for i in range(TIMELINE_CHAR_LENGTH-1):
            print(" ", end='')
        print("|")
        for i in range(TIMELINE_CHAR_LENGTH-len(end_string)):
            print(" ", end='')
        print(end_string)
        print()
        for event in self.list_of_events:
            print(event.datetime())



event_list = []
event_list.append(Event("something happened here when", 1995, 4, 1, 12, 3))
event_list.append(Event("something else happened here", 1999, 12, 4))
event_list.append(Event("nothing happened", 1988, 2, 3, 16, 1))

timeline1 = Timeline(event_list)
timeline1.print_timeline()