# pdroulette

> _Russian roulette like game with PagerDuty_

A super simple game, where you can select your friends and colleagues (the list is collected from your company's PagerDuty account).
If you hit 'Play!', one of you will get a PagerDuty right away.
Have fun :)

### Setup

 * Create an escalation policy in PagerDuty (with only you on it)
 * Create a service in PagerDuty with the freshly created escalation policy
 * Create and API key in PagerDuty (with full access privileges)
 * Create a secrets.json file based on the secrets_template.json file 