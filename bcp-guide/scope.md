# Scope

Defining the scope for IT security automation tasks is far from straightforward. The cybersecurity landscape is evolving faster than defenders can keep pace. As organizations adopt more systems fast than we can manage. Come ChatGPT, come AI to the mix of systems which we add on top of each other. Alongside this growth, vulnerabilities appear at an accelerating rate. This poses as challenge: how do we determine which security tasks to automate first?

The mere term "Automation" is too broad to decide and this document would become too large.

The somewhat comforting—yet sobering—realization is that most organizations face the *same* recurring IT security issues. Over and over again. Examples include resetting leaked credentials, verifying whether a login from another country was legitimate, or remediating weak passwords and vulnerable internet-facing devices.
Another typical use-case is about getting a feed of "things which are wrong in one's network", fetching the feed, enriching it, filtering it and distributing the enriched envent and/or putting into some SIEM. This ETL process is very common.
Regardless of size, organizations are plagued by these common, often avoidable security issues that require repeated incident response actions.

This insight, that the most boring, mundane, repetitive and trivial IT security issues (credential leaks, etc.) are affecting all of us, allows us to define the scope of our document: we want to help people solve these. These issues are just too common.

We do **not** aim to address rare, complex scenarios such as advanced persistent threat (APT) attacks involving custom-built Command & Control infrastructure. Instead, we focus on the routine, high-frequency, and time-consuming tasks. These are the issues that are theoretically simple to fix, yet continuously drain time and energy from highly skilled SOC and Incident Response teams. They are the root cause of alert fatigue—and **they are the tasks we aim to automate**.

Of course, to be within scope, a task must be technically automatable (and hence well defined).

Another dimension for limiting our scope is by aligning with specific phases of the **incident response lifecycle**, as defined in [ISO/IEC 27035-3:2020](https://www.iso.org/standard/74033.html):

| ISO Response cycle Phase  | In Scope?       |
|---------------------------|-----------------|
| Prepare & Plan            | ❌ Not in scope |
| Detect & Report           | ✅ In scope     |
| Assess and Decide (Triage)| ✅ In scope     |
| Respond                   | ✅ In scope     |
| Lessons Learned           | ❌ Not in scope |

The decision of what ISO phase would be in scope was a bit arbitrary, but it helped to limit the scope.

In summary, we will concentrate on the areas that consume the most time from IT security teams and present the most significant risk to the business. These are the ideal candidates for automation.

![Is it worth the time?](https://imgs.xkcd.com/comics/is_it_worth_the_time.png)

*Source: [xkcd #1205](https://xkcd.com/1205/)*
