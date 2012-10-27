#!/usr/bin/env python
#coding: utf8
import datetime
from apigen import db


class GetRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    params = db.Column(db.Text)
    resp = db.Column(db.Text)
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)

    def __init__(self, params, resp, create_time=None, update_time=None):
        self.params = params
        self.resp = resp
        now = datetime.datetime.now()
        self.create_time = create_time or now
        self.update_time = update_time or now

    def __repr__(self):
        return '<GetRequest %s %s>' % (self.id, self.params)
