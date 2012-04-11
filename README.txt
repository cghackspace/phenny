Installation &c.

1) Run ./phenny - this creates a default config file
2) Edit ~/.phenny/default.py
3) Run ./phenny - this now runs phenny with your settings

Enjoy!

-- 
Sean B. Palmer, http://inamidst.com/sbp/

========================================================================
Using Longger!

Longger is a IRC logger that uses MongoDB to store logs!
To use it at PHENNY, after configure it (as described above, you should:

- Edit the ~/.phenny/default file to add this three lines (at the end)

longger_con_host = 'localhost'
longger_con_port = 27017
longger_db_logger = 'longger'

All of them are related to your MongoDB setting, so change as you need.
Please remember that before starting PHENNY next time, you should start
MongoDB first, possibly using "mongod" command!

Regards.
@cghackspace

PS.: This is a not well tested module!
=======================================================================
