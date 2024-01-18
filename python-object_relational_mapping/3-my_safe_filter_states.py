#!/usr/bin/env python3

import sys
import MySQLdb

def filter_states(username, password, database, state_name):
    """Connects to a MySQL server and lists all states in the hbtn_0e_0_usa database with names matching the state_name argument, using a parameterized query to prevent SQL injection."""

    db = MySQLdb.connect(user=username, passwd=password, db=database, host="localhost", port=3