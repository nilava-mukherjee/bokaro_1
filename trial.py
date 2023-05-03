import pandas as pd
import datetime
import requests
from requests.exceptions import ConnectionError
import bs4
from bs4 import BeautifulSoup
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import numpy as np
import pandas as pd
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import mysql.connector
import threading
import time
import select
import json
from configparser import ConfigParser
import pandas as pd
import subprocess
import datetime
import pyodbc
from flask import Flask, make_response, Response
from flask import Flask, render_template, jsonify, redirect, request
import threading
from datetime import datetime, time, timedelta
import csv
from flask import Flask, g, redirect, render_template, request, session, url_for, make_response, Response
import os
Meter_id="m1"

    
try:
        db2 = mysql.connector.connect(user="ajarcake4", password="xJkuyOKBizuim9M42mukRA", host="server050641860.mysql.database.azure.com", database="bokaro_ems", port="3306")
        db2_cursor = db2.cursor()
        db2_cursor.execute("SELECT Voltage_V31 from trialbsl WHERE Meter_id =%s",(Meter_id,))
        data2 = db2_cursor.fetchall()
        db2.commit()
        db2.close()
        d1_values = pd.DataFrame(data2)
        d1_val = ((d1_values.T).values.tolist())
        d1_value = d1_val[-1][-1]
        print(d1_value)
except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))