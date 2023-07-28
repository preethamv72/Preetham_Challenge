# PROVISIONING A WEB SERVER AND DEPLOYING A STATIC WEB APP USING ANSIBLE #

**Prerequisites**:
Before starting with the tutorial, make sure you have a Linux machine or virtual environment set up with the Ansible and AWS CLI installed. To begin with, create an AWS user with programmatic access and say the key or use AWS CLI i.e 

```aws configure```

This will give the API access key ID and secret key for the programmatic access.

Run the following command

```ansible-playbook environment-details.yml```

Running this will populate the env_vars.yml file with the necessary values like region, VPC_Subnet, SEC_GROUP_NAME

Verify if the information is right.


Now run the playbook.yml by using the following command

```ansible-playbook playbook.yml```

This will have multiple plays which will create a Key pair, an EC2 instance,  adds the EC2 instance to an inventory group, installs Apache httpd and runs the static app provided

To test it, use:

```curl <PUBLIC-IP-ADDRESS>/index.html```

If it shows up the "Hello World!" text, then it's a success. 

Thank you