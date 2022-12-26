![alt text](https://images.g2crowd.com/uploads/product/image/social_landscape/social_landscape_31684b1b76816fe94b83a436fe672fad/gitguardian.jpg)

# git-guardian


## Questions 
1. What would you do differently on a managed cluster (EKS, GKE…) regarding step 4?
    Managed cluster come with their own ingress controller and load balancer. One thing that I would do different would be to expose my app using the ingress controller which would create a VIP in the Load Balancer instead of exposing the app as a nodeport.  

2. How would you monitor the application?
    There are multiple ways to monitor the app. If I wanted to keep things in the open source world I would leverage prometheus and grafana for observability and performance analysis, fluentd or fluentBit for logging (probably sending the logs to Kafka) and Jaeger for tracing. That would be a full stack on Open Source for application monitoring. 

3. What would you change to add a PostgreSQL container?
    Adding a PostgresSQL DB container to my application would make my application look like a Restful API app with a frontend and backend. We could create the DB outside the app container and change the app to point to the DB URL and authenticate with basic auth. 
    We could also create the DB as a separate deployment and point the flask app to it as mentioned above. 
    The last option I would do is to deploy the DB as second container inside the POD. I would not recommend this since it would create a single point of failure. 

4. Provide us some feedback on this test:
    - Duration: is it too long, too short or adequate?
        The exam was in between adequate and long. It took me a little over 3 hours of work specially on the part where I had to test my scripts and debug issues with the app. 
    - Difficulty: on a scale from 0 (easy) to 10 (hard), how would you rate the difficulty
of this test?
        I would give the test a 8/10. 
    - Did you find the test interesting? If not, please tell us why.
        I found the test very interesting but I think there are better ways of testing the candidate's knowledge of kubernetes. The fact that I used scripts to alter the app did not feel realistic. From my point of view, ConfigMaps and environment variables should be used for containers to consume and not to alter the app code. One of the main purposes of kubernetes is to simplify developers code lifecycle, knowing or having to change the code using scripts landed in a grey area between k8s admin and software developer knowledge. Having your own lab environemnt where the candidate could debbug/fix broken pods/deployments, create netpol so that certains apps can't talk or even implement a open source ingress controller like contour would be good adds to the test. 
        From a developer perpespective, creating your own flask app, pushing it do dockerHub (you can create a free account) and than using the image to create a pod that has the message (Hello GitGuardian) would also be a interesting thing to ask. 



