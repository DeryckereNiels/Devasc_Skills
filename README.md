# Devasc_Skills
**Github**
* Task preparation:
    * Go to github.com, create private repository and copy link to repository
    * Create folder Devasc_Skills => mkdir Devasc_Skills
* Task implementation:
    * Clone repository to directory Devasc_skills => git clone https://github.com/DeryckereNiels/Devasc_Skills.git Devasc_Skills/
    * The reason I used clone is because then you don't have problems with the branch naming (master => main)

* Task troubleshooting: Not Applicable
* Task verification:  
    * Link to repository https://github.com/DeryckereNiels/Devasc_Skills.git
    * screenshot Task1.png

**Ansible**
* Task preparation:
    * create a host file in directory Devacs_Skills and add CSr1kv
    * create a local ansible config file in directroy Devasc_skills
    * Set parameters "host", host_key_checking, retry_files_enabled, deprecation_warnings
    * create .yaml file and copy the code in there from url: touch ios_status.yaml
    * nano ios_status.yaml => copy from url
    * install dependencies: ansible-galaxy collection install cisco.ios
    
* Task implementation:
    * set execution rights on playbook ios_status.yaml: chomod +x ios_status.yaml
    * edit playbook and add "---" to mark the beginning of the playbook
    * edit playbook and set the name of the playbook, hosts, connection, gather_facts
    

* Task troubleshooting:
    * Problem: I encountered problems with the "clear counters task".
    * Solution: the [] had to be escaped to be correctly processed
* Task verification:
    * Link to repository https://github.com/DeryckereNiels/Devasc_Skills.git
    * screenshot Task2.png

**Docker**
* Task preparation:
    * create Dockerfile in Devasc_Skills directory: touch Dockerfile
    *
    
* Task implementation:
    * add neccesary config commands:
      * FROM debian
      * RUN apt-get update
      * RUN apt-get install -y apache2
      * EXPOSE 8081
    * build the docker container: docker build -t apache2_image .
    

* Task troubleshooting:
    * Problem: apache2 needs to install tzdata which gives a prompt for region verifications, this stops the build of the image
    * Solution: install tzdata seperately so it install with default settings
               
    * Problem: When starting a container based on the image, the docker container shuts down
    * Solution: When starting the apache2 service, it has to be run in the foreground. This is due to the way processes are handled
* Task verification:
    * screenshot Task3.png


