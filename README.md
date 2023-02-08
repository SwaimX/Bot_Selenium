# Instagram Bot

---

Opportunities:
* Follow all followers of the account
* Unsubscribe from everyone
* Unsubscribe if more than two days have passed
* Unsubscribe if the account does not subscribe in response
* Adds all accounts to the general database as well as to the account database
* Saves your cookies at the first login so that Instagram does not block your logins if you start the bot many times

---

### About Functions

##### Follow all followers of the account

This function asks you for a nickname for all subscribers to which it subscribes, which also enters the account's nickname into the SqlLite database, as well as the time when it was subscribed to it, which is also entered into the general database of the account. It also has a delay of 60 seconds, this is done so that Instagram does not block your actions

##### Unsubscribe from everyone

This function simply goes into your subscriptions and unsubscribes from everyone, also removes them from the account database, but leaves them in the general database

##### Unsubscribe if more than two days have passed

This function unsubscribes from the account only if she subscribed to the account and it is in the personal database, and after unsubscribing, it deletes it from it

##### Checking accounts for mutual subscription

This function looks in your subscriptions to see if the account has subscribed in response, and if the account has subscribed in response, it puts False in the Hose column. It also writes and puts False in a column in the common database so that in the future you know who is worth following and who is not

##### Optimal

This function performs three actions at the same time:
* Follow all followers of the account
* Unsubscribe if more than two days have passed
* Checking accounts for mutual subscription

---



