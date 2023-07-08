# CSIRT/SOC Services mapping to Popular Automation Tools

Tables below shows mapping of different automation tools usend by numerious CSIRTs, SOC and ISACs for automation of particular services.

Services are taken and aligned with definitions of FIRST CSIRT Services Framework (v2.1) https://www.first.org/standards/frameworks/csirts/csirt_services_framework_v2.1 .


## 5. Service Area: Information Security Event Management

The following services are targeted by automation:
1. 5.1 Service: Monitoring and detection
2. 5.2 Service: Event analysis

| Tool Category | Tool | Purpose | Used mostly by |
| ---- | -------- | ----------- | ---- |
| NDS | | |
| |Suricata | Analyse network traffic and create alerts on detection rules | Internal SOCs, Sectorial CSIRTs
| |Zeek | Analyse network traffic, create alerts on atomic IOCs as detection rules, and log chosen network activities | Internal SOCs, Sectorial CSIRTs
| HIDS | | |
| |Sysmon | Analyse MS Windows OS activities, create alerts on detection rules and log chosen OS activities | SOCs who seek visibility into workstations
| |Ossec / Wazuh agent | Analyse Linux / Windows / Linux/ UNIX OS activities, create alerts on detection rules, log chosen transactions | SOCs who seek visibility into servers and workstations
| OSINT automation| | |
| | AIL | Monitor different sources for leaked data and create alerts when mathing defined rules | All CSIRTs and SOCs
| Triage automation | | |
| | tines-io | Workflow automation for detected alerts triage and response | Internal SOCs
| | shuffler| Workflow automation for detected alerts triage and response | Internal SOCs


## 6. Service Area: Information Security Incident Management

The following services are targeted by automation:
1. 6.1 Service: Information security incident report acceptance
2. 6.2 Service: Information security incident analysis
3. 6.3 Service: Artifact and forensic evidence analysis
4. 6.4 Service: Mitigation and recovery
5. 6.5 Service: Information security incident coordination
6. 6.6 Service: Crisis management support

| Tool category | Tool | Purpose | Used mostly by |
| ---- | -------- | ----------- | ---- |
| Ticketing Automation tools| | |
| | Shared manual mailbox | To receive incident Reports and work on them manually | Small CSIRT/SOC teams
| | RTIR | Register incoming Incident Report (from email, API, webinterface) and automate incident coordination workflows towards incident closure, including automated communication with reporters and handlers. Provides customisible workflow engine. Default workflows have mostly manual incident analysis capabilities | Coordinating CSIRTs
| | OTRS Storm | Register incoming Incident Report (from email, API, webinterface) and automate incident coordination workflows towards incident closure, including automated communication with reporters and handlers. | Coordinating CSIRTs
| | ServiceNow Security Operations | Register incoming Incident Report and automate incident coordination workflows towards incident closure, including automated communication with reporters and handlers. | Internal CSIRT/SOCs in big organisations
| | Jira | Register incoming Incident Report and automate incident coordination workflows towards incident closure, including automated communication with reporters and handlers. | Internal CSIRT/SOCs
|Analysis automation | | |
| | theHive5 | Artifact analysis workflow automation | CSIRTs
| | cortex| Artifact analysis workflow automation, mostly from theHive| CSIRTs
| Threat analysis and hunting| | |
| | osquery| Query enpoints for threat-related artifacts | Internal SOCs, IR teams
| | velociraptor| Query enpoints for threat-related artifacts | Internal SOCs, IR teams
| | Dissect| Query images of virtual machines and other media to analyse incidents | Internal SOCs, IR teams
| Response automation| | |
| |Ossec / Wazuh agent | Analyse Linux / Windows / Linux/ UNIX OS activities, execute action on chosen alert | Internal SOCs

## 7. Service Area: Vulnerability Management

The following services are targeted by automation:
1. 7.1 Service: Vulnerability discovery / research
2. 7.2 Service: Vulnerability report intake
3. 7.3 Service: Vulnerability analysis
4. 7.4 Service: Vulnerability coordination
5. 7.5 Service: Vulnerability disclosure
6. 7.6 Service: Vulnerability response


| Tool category | Tool | Purpose | Used mostly by |
| ---- | -------- | ----------- | ---- |
| Vulnerability scanners| | |
| | OpenVAS| Scanning websites for vulnerabilities | Smaller CSIRTs
| | Nessus Pro| Scan infrastructure for vulnerabilities | All CSIRTs
| | nmap| Scan infrastructure for vulnerabilities | All CSIRTs 
| | Netsparker/Acunetix | Scan websites for vulnerabilities | All CSIRTs
| Vulnerability analysis| | |
| | taranis / taranis-ng| Monitor new vulnerabilities published, analyse and publish advisories | Coordinating CSIRTs




## 8. Service Area: Information Situational Awareness

The following services are targeted by automation:
1. 8.1 Service: Data acquisition
2. 8.2 Service: Analysis and synthesis
3. 8.3 Service: Communication


| Tool category | Tool | Purpose | Used mostly by |
| ---- | -------- | ----------- | ---- |
| Threat intelligence processors and portals| | |
| | MISP | Automated and manual ingestion of threat intelligence, analysis (enriching, correlation, search, manual analysis and report writing), and automated sharing | all CSIRTs, SOCs, ISACs
| | OpenCTI| Automated and manual ingestion of threat intelligence, analysis (enriching, correlation, search, manual analysis and report writing), and sharing out |  all CSIRTs, SOCs, ISACs
| | ArcticHub| Automated and manual ingestion of threat intelligence, analysis (enriching, correlation, search, manual analysis and report writing), and sharing out |  all CSIRTs, SOCs, ISACs
| | EclecticIQ| Automated and manual ingestion of threat intelligence, analysis (enriching, correlation, search, manual analysis and report writing), and sharing out | all CSIRTs, SOCs, ISACs
| | Anomaly| Automated and manual ingestion of threat intelligence, analysis (enriching, correlation, search, manual analysis and report writing), and sharing out | all CSIRTs, SOCs, ISACs
| | ThreatConnect| Automated and manual ingestion of threat intelligence, analysis (enriching, correlation, search, manual analysis and report writing), and sharing out | all CSIRTs, SOCs, ISACs
| Threat intelligence routing | | |
| | intelmq| ingest, process (normalise, enrich) and communicate out threat intelligence data | Coordinating CSIRTs
| Threat intelligence feeds on infrastructure toxicity | | |
| | ShadowServer | Automated feeds on infrastructure misbehaviour | All SOCs and coordinating CSIRTs
| | TeamCymru | Automated feeds on infrastructure misbehaviour | All SOCs and coordinating CSIRTs
| Enriching automation|  |  |
| | Cortex | enrich data on indicators from different sources | all SOCs and CSIRTs, especially who uses theHive





## 9. Service Area: Knowledge Management

The following services are targeted by automation:
1. 9.1 Service: Awareness building
2. 9.2 Service: Training and education
3. 9.3 Service: Exercises (CTF and table top)
4. 9.4 Service: Technical and policy advisory (no automation suggested)


| Tool category | Tool | Purpose | Used mostly by |
| ---- | -------- | ----------- | ---- |
| Information Portals| | |
| | Wordpress | Public website for awareness sharing | coordinating CSIRTs
| Information distribution| | |
| | phpList | Share advisories for awareness | Coordinating CSIRTs
| Exercise and training systems| | |
| | ​CTFd | Capture the Flag exercises scoring automation | Coordinating CSIRTs

