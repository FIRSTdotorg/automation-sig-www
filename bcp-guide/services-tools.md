# CSIRT/SOC Services mapping to Popular Automation Tools

Tables below shows mapping of different automation tools used by numerous CSIRTs, SOC and ISACs for automation of particular services.

Services are taken and aligned with definitions of FIRST CSIRT Services Framework (v2.1) [https://www.first.org/standards/frameworks/csirts/csirt_services_framework_v2.1](https://www.first.org/standards/frameworks/csirts/csirt_services_framework_v2.1) .

## 5. Service Area: Information Security Event Management

The following services are targeted by automation:

1. 5.1 Service: Monitoring and detection
2. 5.2 Service: Event analysis

| Tool Category | Tool | Used mostly by | To do following | In order to serve objective |
| --- | --- | --- | --- | --- |
| NDS |  |  |  |  |
|  | Suricata | Internal SOCs, Sectorial CSIRTs | Analyse ingested copy of network traffic to 1) create alerts based on detection rules and 2) use as historical dataset for incident analysis | Incident detection via network traffic inspection |
|  | Zeek | Internal SOCs, Sectorial CSIRTs | Analyse ingested copy of network traffic to 1) create alerts on atomic IOCs, 2) log chosen protocol transactions 3) use as historical dataset for incident analysis | Incident detection via network traffic inspection |
| HIDS |  |  |  |  |
|  | Sysmon | SOCs who seek visibility into activities of MS Windows workstations and servers | Analyse MS Windows OS activities, create alerts on detection rules and log chosen OS activities | Incident detection via host activity inspection |
|  | Ossec / Wazuh agent | SOCs who seek visibility into servers and workstations | Analyse Linux / Windows / Linux/ UNIX OS activities, create alerts on detection rules, log chosen transactions | Incident detection via host activity inspection |
| OSINT automation |  |  |  |  |
|  | AIL | All CSIRTs and SOCs | Monitor different online sources (pastebins, darknet, ..) for leaked data in order to create alerts when matching some defined rules | Incident detection via inspection of public sources of leaked information |
| Triage automation |  |  |  |  |
|  | tines-io | Internal SOCs | Workflow automation for detected alerts triage and response | Incident identification automation from detected alerts |
|  | shuffler | Internal SOCs | Workflow automation for detected alerts triage and response | Incident identification automation from detected alerts |

## 6. Service Area: Information Security Incident Management

The following services are targeted by automation:

1. 6.1 Service: Information security incident report acceptance
2. 6.2 Service: Information security incident analysis
3. 6.3 Service: Artifact and forensic evidence analysis
4. 6.4 Service: Mitigation and recovery
5. 6.5 Service: Information security incident coordination
6. 6.6 Service: Crisis management support

| Tool category | Tool | Used mostly by | Purpose | To serve objective |
| --- | --- | --- | --- | --- |
| Ticketing Automation Tools |  |  |  |  |
|  | Shared manual mailbox | Small CSIRT/SOC teams | To manage communication for incident reports and related communications receive incident Reports and work on them manually | To coordinate incident handling |
|  | RTIR | Coordinating CSIRTs | Register incoming Incident Report (from email, API, web interface) and automate incident coordination workflows towards incident closure, including automated communication with reporters and handlers. Provides customizable workflow engine. Default workflows have mostly manual incident analysis capabilities | To coordinate incident handling |
|  | OTRS Storm | Coordinating CSIRTs | Register incoming Incident Report (from email, API, web interface) and automate incident coordination workflows towards incident closure, including automated communication with reporters and handlers. | To coordinate incident handling |
|  | ServiceNow Security Operations | Internal CSIRT/SOCs in big organisations | Register incoming Incident Report and automate incident coordination workflows towards incident closure, including automated communication with reporters and handlers. | To coordinate incident handling |
|  | Jira | Internal CSIRT/SOCs | Register incoming Incident Report and automate incident coordination workflows towards incident closure, including automated communication with reporters and handlers. | To coordinate incident handling |
| Analysis automation |  |  |  |  |
|  | theHive5 | CSIRTs | Artifact analysis workflow automation | To manage incident analysis |
|  | cortex | CSIRTs | Artifact analysis workflow automation, mostly from theHive | To give situational awareness from global sources to incident handling |
| Threat analysis and hunting |  |  |  |  |
|  | osquery | Internal SOCs, IR teams | Query endpoints for threat-related artifacts | To give situational awareness from internal hosts to incident handling |
|  | velociraptor | Internal SOCs, IR teams | Query endpoints for threat-related artifacts | To give situational awareness from internal hosts to incident handling |
|  | Dissect | Internal SOCs, IR teams | Query images of virtual machines and other media to analyse incidents | To give situational awareness from collected media to incident handling |
| Response automation |  |  |  |  |
|  | Ossec / Wazuh agent | Internal SOCs | Analyse Linux / Windows / Linux/ UNIX OS activities, execute action on chosen alert | To automate response |

## 7. Service Area: Vulnerability Management

The following services are targeted by automation:

1. 7.1 Service: Vulnerability discovery / research
2. 7.2 Service: Vulnerability report intake
3. 7.3 Service: Vulnerability analysis
4. 7.4 Service: Vulnerability coordination
5. 7.5 Service: Vulnerability disclosure
6. 7.6 Service: Vulnerability response

| Tool Category | Tool | Used mostly by | To do following | In order to serve objective |
| --- | --- | --- | --- | --- |
| Vulnerability scanners |  |  |  |  |
|  | OpenVAS | Smaller CSIRTs | Scanning websites for vulnerabilities | Provide website-related information for vulnerability response |
|  | Nessus Pro | All CSIRTs | Scan infrastructure for vulnerabilities | Provide infrastructure-related information for vulnerability response |
|  | nmap | All CSIRTs | Scan infrastructure for vulnerabilities | Provide infrastructure-related information for vulnerability response |
|  | Netsparker/Acunetix | All CSIRTs | Scan websites for vulnerabilities | Provide website-related information for vulnerability response |
| Vulnerability analysis |  |  |  |  |
|  | taranis / taranis-ng | Coordinating CSIRTs | Monitor new vulnerabilities published, analyse and publish advisories | Maintain and manage situational awareness on vulnerabilities. |

## 8. Service Area: Information Situational Awareness

The following services are targeted by automation:

1. 8.1 Service: Data acquisition
2. 8.2 Service: Analysis and synthesis
3. 8.3 Service: Communication

| Tool Category | Tool | Used mostly by | To do following | In order to serve objective |
| --- | --- | --- | --- | --- |
| Threat intelligence processors and portals |  |  |  |  |
|  | MISP | all CSIRTs, SOCs, ISACs | Automated and manual ingestion of threat intelligence, analysis (enriching, correlation, search, manual analysis and report writing), and automated sharing | Create situational awareness on the threats |
|  | OpenCTI | all CSIRTs, SOCs, ISACs | Automated and manual ingestion of threat intelligence, analysis (enriching, correlation, search, manual analysis and report writing), and sharing out | Create situational awareness on the threats |
|  | ArcticHub | all CSIRTs, SOCs, ISACs | Automated and manual ingestion of threat intelligence, analysis (enriching, correlation, search, manual analysis and report writing), and sharing out | Create situational awareness on the threats |
|  | EclecticIQ | all CSIRTs, SOCs, ISACs | Automated and manual ingestion of threat intelligence, analysis (enriching, correlation, search, manual analysis and report writing), and sharing out | Create situational awareness on the threats |
|  | Anomaly | all CSIRTs, SOCs, ISACs | Automated and manual ingestion of threat intelligence, analysis (enriching, correlation, search, manual analysis and report writing), and sharing out | Create situational awareness on the threats |
|  | ThreatConnect | all CSIRTs, SOCs, ISACs | Automated and manual ingestion of threat intelligence, analysis (enriching, correlation, search, manual analysis and report writing), and sharing out | Create situational awareness on the threats |
| Threat intelligence routing |  |  |  |  |
|  | intelmq | Coordinating CSIRTs | Ingest, process (normalise, enrich) and feed-out threat related data | Process and route situational awareness data |
| Threat intelligence feeds on infrastructure toxicity |  |  |  |  |
|  | ShadowServer | All SOCs and coordinating CSIRTs | Automated feeds on infrastructure misbehaviour | Source reputable global threat and vulnerability data about constituency |
|  | TeamCymru | All SOCs and coordinating CSIRTs | Automated feeds on infrastructure misbehaviour | Source reputable global threat and vulnerability data about constituency |
| Enriching automation |  |  |  |  |
|  | Cortex | all SOCs and CSIRTs, especially ones using theHive | enrich data on indicators from different sources | Collect additional related data for better situational awareness |

## 9. Service Area: Knowledge Management

The following services are targeted by automation:

1. 9.1 Service: Awareness building
2. 9.2 Service: Training and education
3. 9.3 Service: Exercises (CTF and table top)
4. 9.4 Service: Technical and policy advisory (no automation suggested)

| Tool Category | Tool | Used mostly by | To do following | In order to serve objective |
| --- | --- | --- | --- | --- |
| Information Portals |  |  |  |  |
|  | Wordpress | coordinating CSIRTs | Publish website for awareness sharing | Provide contact and description of the team and share awareness, events and training information |
| Information distribution |  |  |  |  |
|  | phpList | Coordinating CSIRTs | Distribute advisories for awareness building | Mail awareness building materials |
| Exercise and training systems |  |  |  |  |
|  | ​CTFd | Coordinating CSIRTs | Manage Capture the Flag exercises and scoring | Conduct cyber-exercises |