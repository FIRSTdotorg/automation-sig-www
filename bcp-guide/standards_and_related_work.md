# Standards & Related work

This chapter describes both standards and related work. We decided to
list the most commonly used standards which need to be understood by
most IR automation tools. Having common standards and making sure that
the tool you are evaluating conforms to it, allows for easier
interoperability. This is why we decided to list the standards here as
well. 

*XXX please list all similar documents which pre-date our document XXX*

Modelling languages for Playbooks
=================================

The following section lists known standards for playbook modelling
languages. Both standardised ones as well as de-facto standards.

CACAO
-----

**Reference**:
<https://docs.oasis-open.org/cacao/security-playbooks/v1.0/security-playbooks-v1.0.html> 

**Status**: Actively maintained and standardized under the auspices of
[OASIS](https://docs.oasis-open.org/).

**Used** **by**:

-   Shuffler: <https://shuffler.io/docs/architecture#frameworks> 

**Description:**

CACAO takes a lot of ideas from BPMN and builds on top of it.

*\<XXX insert description. What is it? How to use it? Which tools use
it? Who will be using it?  XXX \>*

COPS (Demisto / XSOAR )
-----------------------

**Reference**: <https://github.com/demisto/COPS>

**Status**: Seems to be abandoned on github? 

**Used by: ?** *XXX not sure, does someone know if it is even used
internally in XSOAR? XXX*

**Description:**

Palo Alto was involved in CACAO, but what happened then?

*\<XXX insert description. What is it? How to use it? Which tools use
it? Who will be using it?  XXX \>*

BPMN
----

**Reference**:
<https://en.wikipedia.org/wiki/Business_Process_Model_and_Notation>

**Status**: 

**Used by: **

-   **Commercial:** [Red Hat Process
    Automation](https://www.redhat.com/en/products/process-automation),
    **Open Source Upstream:** [jBPM](https://www.jbpm.org/) /
    [Kogito](https://kogito.kie.org/)

**Description:**

*\<XXX insert description. What is it? How to use it? Which tools use
it? Who will be using it?  XXX \>*

Are there SOARs which use BPMN? BPMN is useful as a reference maybe.
Open Source BPMN tools (apache projects) : <https://github.com/camunda>

List of BPMN engines:
<https://en.wikipedia.org/wiki/List_of_BPMN_2.0_engines> 

Jason Comment: Many open source orchestrators lack here 

Kestrel
-------

**Reference**:  <https://kestrel.readthedocs.io/en/latest/> 

**Status**: 

**Used by: **

**Description**:  more for threat hunting, less for automation?. Might
be a response in automation.

Standards For Incident Fields & Metrics
=======================================

VERIS
-----

**Reference:** <http://veriscommunity.net/>

**Status:** Active & Maintained by the Verizon Security Research & Cyber
Intelligence Center

**Used by:**

**Description:** a set of metrics designed to provide a common language
for describing security incidents in a structured and repeatable
manner. 

**Note:** Still picking through this to see how relevant it will be, but
it came up in a discussion about producing useful metrics surrounding
incidents.

Incident data exchange and information sharing standards
========================================================

MISP
----

**Reference:** <https://www.misp-project.org/datamodels/>

**Status:** Active & Maintained as part of the MISP project

**Used by:**

**Description:** a set of metrics designed to provide a common language
for describing security incidents in a structured and repeatable
manner. 

Standards for classification / taxonomies
-----------------------------------------

RSIT
----

**Reference:**
<https://github.com/enisaeu/Reference-Security-Incident-Taxonomy-Task-Force> 

**Status:** Active & Maintained. Stewardship by
[ENISA](https://www.enisa.europa.eu/publications/reference-incident-classification-taxonomy).
Standardisation by the [RSIT Working
Group](https://github.com/enisaeu/Reference-Security-Incident-Taxonomy-Task-Force/blob/master/Documentation/ToR.md)
(which usually meets next to TF-CSIRT conferences).

**Used by:** most CSIRTs in Europe at least. A (very reduced) list of
users and tools is listed
[here](https://github.com/enisaeu/Reference-Security-Incident-Taxonomy-Task-Force/blob/master/Documentation/Dependencies%20and%20tool%20mapping.md). 
There are far more users globally.

**Description:** A common high level reference taxonomy to classify
incidents. Detailed description on use-cases here:
<https://github.com/enisaeu/Reference-Security-Incident-Taxonomy-Task-Force/blob/master/Documentation/Use%20Cases.md> 

MISP taxonomies
---------------

**Reference:** <https://github.com/MISP/misp-taxonomies/>

**Status:** Active & Maintained. Stewardship by
[t](https://www.enisa.europa.eu/publications/reference-incident-classification-taxonomy)he
MISP Team / CIRCL.

**Used by:** MISP uses potentially all of these taxonomies internally.
You can enable or disable individual taxonomies within MISP.

**Description:** The MISP team started to convert all kinds of
taxonomies which they encountered into a machine readable format
(\"machinetag.json\"). A very simple example of such a machine readable
taxonomy is the [Admiralty
Scale](https://github.com/MISP/misp-taxonomies/tree/main/admiralty-scale)
taxonomy. If you compare the taxonomy to its
[machinetag.json](https://github.com/MISP/misp-taxonomies/blob/main/admiralty-scale/machinetag.json)
representation, you can easily see how labels in a taxonomy get mapped.
Therefore, this approach is flexible enough for nearly all taxonomy
mappings which MISP wants to support.
