#!/bin/bash
sqlite3 optiware.db .dump > dump.sql
mysqldump -h $AWSRDSHOST -u $AWSRDSADMIN -p$AWSRDSPASSWORD --databases optiware < dump.sql
rm -rf dump.sql
rm -rf optiware.db