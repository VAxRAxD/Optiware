#!/bin/bash
mysqldump -h $AWSRDSHOST -u $AWSRDSADMIN -p$AWSRDSPASSWORD --databases optiware > optiware.sql
./mysql2sqlite optiware.sql | sqlite3 optiware.db
rm -rf optiware.sql