# Title: Malicious Domain Takedown

## Goals:
  * analyze reported URLs
  * check for malicious content
  * report URL/Domain for takedown

## Playbook
### Requirements
   * Analysis environment with no risk of infecting others
   * check if the reported Site is malicious
     * Phishing
     * Malware
     * Known bad patterns
   * report to the analyst
   * access for dns lookups, whois, asn

### Triggers
   The playbook starts with a request that could come from an automatic scanner, manual report, automatic report from an external partner

### Steps

1. receive analysis request
1. check request authorization
  1. if requester is not authorized, exit early
1. is the URL already known?
  1. exit early if URL is already known
1. access URL
  1. exit early if response is invalid (e.g., 404 not found)
1. Check response for
  * phishing content
  * known malware patterns
  * known bad patterns like modified javascript code
1. Classify URL
1. get abuse contact, ASN
1. send out notification
  * AS abuse contact
  * IP abuse contact
1. Add malicious URL to internal blocklists

### Diagram
![Domain Takedown Diagram](./diagram.png)

### Results
  * take down request are sent, the domain will hopefully be made unavailable soon
  * internal users are protected via the blocklists

## Implementations

## SOAR

### Artifact Repository
  * Responses and screenshots might be stored for some time, to document the requests
