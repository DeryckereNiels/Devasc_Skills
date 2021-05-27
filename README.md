# Devasc_Skills
**Task 1: Github**
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

**Task 2: Ansible**
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

**Task 3:Docker**
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

** Task4: Jenkins **
* Task preparation:
  * build and run jenkins docker container
* Task implementation
  * create a job for building the apache2 image and run a container based on it: BuildApache2Container 
  * The job references my remote github repository, clones it in the jenkins_container and then user the Dockerfile
  * create a job for testing: TestappJob => in this job I fetch the apache start page with curl and check if "Ubuntu Apache Default page" is present
  * create a pipeline with the BuildApache2Container and the TestAppJob
* Task troubleshooting:
  *Problem: I had problems with the assignments of portnumbers. port 8081 was in use but i couldn't find any container using it.
  *Solution: I checked via the command netstat which service was using it and then i shut down that service

  *Problem: portmapping is incorrectly configured
  *Solution: after searching for a while I realized that the apache2 port.conf file had to be changed to reflect the correct port mapping
   I used the command Apache2 sed -i '0,/Listen [0-9]*/s//Listen 8081/' /etc/apache2/ports.conf

** Task 5: Rest API **
* Task preparation:
  * create python file: Touch task5.py
  * set correct permissions: chmod +x task5.py

*Task implementation
 *Import correct python modules: json, requests
 * create api_url
 * create variable with authentication info
 * set headers
 * created for each webrequest a python method

* Task troubleshooting
  *Problem: some URL's in the curl request are not correct
  *Solution: updated URL's
  
  *Problem: with PUT and PATCH I get a 409 error. When I try it in Postman I don't get the problem
  *Solution: Missed with the http method. corrected it to reflect to correct put or patch method
* Task verification
  * see screenshot task5.png

**Task 6- Webex Teams API ***
*Task preparation:
 *create python file: touch create-space.py
 *set correct permissions: chmod +x create-space.py

* Task implementation
  * import necessary modules
  * I have created a method for every step necessary
    * CreateSpace method to create a room in Teams
    * getRooms to get the roomid and pass it to method addMember
    * addMember method to add user to room 
    * postMessage method to post a message in the room
    * postFiles method to post the screenshots in the room

*Task troubleshooting: NONE
*Task verification: see made webex space

**Task 7 BASH**
* Task preparation:
  * create .sh file and make it executable: touch checkHostname.sh && chmod +x checkHostname.sh
  * create directory io_configs and download config files

*Task implementation
 *first I enumerate all the txt files in the directory ios_configs
 *second I create the file check_ios.rep
 *third I append the date to the check_ios.rep file => $(date) >> check_ios.rep
 *Lastly for every txt file in the directory I search wih "grep" for the hostname and ad it to my file

* Task troubleshooting:/
* Task Verification: see screenshot task7.png
