Deploy the flask-app 
Expose the port as a nodePort since we dont have LB configured 
k expose pod flask-app --name flask-svc --type NodePort --port 80


root@master:~# k get svc
NAME         TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
flask-svc    NodePort    10.99.195.82   <none>        80:30475/TCP   56s
kubernetes   ClusterIP   10.96.0.1      <none>        443/TCP        52m

Check if the pod is exposed:
http://<public IP>:30475/

Exec the pod and change the code:
- k exec flask -it -- /bin/bash
vim main.py

Create a configmap scripts that alters the code:
#!/bin/sh

sed -i 's/World/GitGuardian/g' /app/app.py

kubectl create configmap wrapper --from-file=wrapper.sh

If the script does not run, manually had to run it. 
k exec flask-app -it -- /scripts/wrapper.sh

For some reason the commands below were not persisting 
sed "8 i @app.route('/pod-id')" app.py
sed '9 i def pod_id():)' app.py
sed '10 i return "'<POD ID SHOULD COME HERE'"' app.py


sed -i "8 i \
    @app.route('/pod-id')\
    def pod_id():\
        pod = os.environ.POD_ID\
        return (pod)"


sed -i "8 i \
    @app.route('/pod-id')\n\
def pod_id():\n\
   pod = os.environ.POD_ID\n\
   return (pod)" app.py



    signingConfigs {\
        release {\
            storeFile file("$keystorefile")\
            storePassword "$keystorepass"\
            keyAlias "$keystorealias"\
            keyPassword "$keystorepass"\
        }\
    }\ \ " app.py