#!/bin/sh
sed -i "3 i import os" app.py
sed -i 's/World/GitGuardian/g' /app/app.py

sed -i "8 i \
    @app.route('/pod-id')\n\
def pod_id():\n\
   POD = os.getenv('POD_ID')\n\
   return (POD)" app.py
