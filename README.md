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

