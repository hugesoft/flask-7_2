#-*- coding: utf-8 -*-

import os
import re
import json

from flask import render_template, session, redirect, \
    url_for,make_response,request
from . import editor
from .. import db
from ..models import User
from uploader import Uploader

@editor.route('/')
def edit():
    return render_template('edit/editor.html')
