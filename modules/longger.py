#!/usr/bin/env python
"""
Longger.py - @cghackspace
Initialy based on logger.py - Phenny Room Logging Module
License: AFL | New BSD
"""

from datetime import datetime as dt
from pymongo import Connection


def setup(phenny): 
    connection = Connection(phenny.config.longger_con_host, phenny.config.longger_con_port)
    db = connection[phenny.config.longger_db_logger]
    phenny.logger = db.logs

    # if we don't explicitly list channels to log, log them all:
    if not hasattr(phenny.config, "logchannels"):
        phenny.config.logchannels = phenny.config.channels


def log_message(phenny, teller, chan, msg):
    # only log the channels we care about
    if chan in phenny.config.logchannels:
        now = dt.utcnow()
        entry = {'time':now, 'channel':chan, 'author':teller, 'text':msg}
        #Should we separete in channels?
        phenny.logger.insert(entry)
 
def loggit(phenny, input):
    msg = input.group(1).encode('utf-8')
    log_message(phenny, input.nick, input.sender, msg)
loggit.rule = r'(.*)'
loggit.priority = 'high'    


if __name__ == '__main__': 
   print __doc__.strip()
