# Preetham_Challenge

Static web application infra deployment and hosting via Ansible:

Steps to deploy a static application:

1. **Prerequisites**: A local machine with the following packages installed:
- Python
- Pip
- Git
- AWS Cli - Refer to https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
  
2. **Installing Ansible**: Use the following command to install Ansible on your local machine
pip install ansible

3. Now clone the existing repo:
```git clone https://github.com/preethamv72/Preetham_Challenge.git```

4. Use the following commands to run the play-book:

```cd Preetham_Challenge```

```ansible-playbook -i localhost, ansible/playbook.yml```

# File Structure

```
Preetham_Challenge/
|-- ansible/
|   |-- playbook.yml    # Ansible playbook to configure the EC2 instance and web server
|   |-- roles/
|       |-- webserver/
|           |-- tasks/
|               |-- main.yml    # Tasks to install and configure the web server
|           |-- templates/
|               |-- index.html   # Html template for the "Hello World" page
|-- tests/
|   |-- test_hello_world.py   # Automated tests for the web application
|-- README.md    # Documentation and instructions for the project
```


 

