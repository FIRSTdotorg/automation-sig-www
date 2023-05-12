# Scope

Limiting down the scope for IT Security automation tasks is anything but easy. The "cyber" field is expanding faster than defenders can keep up, the number of systems which need to be defended increases faster than organisations can acquire skilled defenders/analysts. With the number of new systems,  the number of vulnerabilities increases seemingly exponentially as well. Given this dynamic setting, one is tempted to feel overloaded by the task to "automate-away" all "cyber problems". So, which use-cases to focus on first for automation?

The both positive as well as somewhat sad insight is, that most organisations face the same basic IT security problems over and over again: for example leaked credentials which need to be reset, or confirming with a user if he/she really logged in from a different country in the middle of the night. Or take weak passwords, vulnerable devices which are internet-facing, etc. Large as well as small organisations all face the very same (often preventable) IT security topics and hence incident response tasks.

In other words, our document will not try to address automating the response to the black-swan, one-time sophisticated  APT attack where the attacker created custom infrastructure for the Command & Control servers. It will rather deal with all the repeated, frequent and boring tasks. The tasks that are easy to fix (theoretically), but still happen across different organisations again and again. The tasks, which consume the most time of your highly skilled SOC or Incident Response Team. The tasks which create alert fatigue for them.... all those are in scope of this document.

Obviously, the tasks considered must be automate-able in the first place.

Another metric to limit our considered use-cases would be the estimated risk to the business. This might differ widely for some organisations and use-cases. However, things like attacks to central resources such as an Active Directory (AD) are universal enough for us to consider it a worth-while use case (to give a random example).

The third way of limiting our scope is to limit ourselves to specific phases of the incident response lifecycle (see [ISO/IEC 27035-3:2020](https://www.iso.org/standard/74033.html)):

For the typical phases of

* prepare & plan →  not in scope
* detect & report → in scope
* assess and decide (triage) → in scope
* respond → in scope
* lessons learnt → not in scope

Therefore, we can say, we will focus on the areas which burn the most time for team members in an IT security team: risks to the biz and hours consumed.

![Is it worth the time?](https://xkcd.com/1205/)

(source: https://xkcd.com/1205/)
