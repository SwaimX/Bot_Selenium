# Instagram Bot

---

Advantages:
* The bot works without Xpath due to this I do not need a proxy
* The bot simultaneously works with many accounts


---

Opportunities:
* Follow all followers of the account
* Unsubscribe from everyone
* Unsubscribe if more than two days have passed
* Unsubscribe if the account does not subscribe in response
* Adds all accounts to the general database as well as to the account database
* Saves your cookies at the first login so that Instagram does not block your logins if you start the bot many times

---

### Get started


---

### About Functions

##### Follow all followers of the account

This function asks you for a nickname for all subscribers to which it 
subscribes, which also enters the account's nickname into the SqlLite 
database, as well as the time when it was subscribed to it, which is also 
entered into the general database of the account. It also has a delay of 60 
seconds, this is done so that Instagram does not block your actions

##### Unsubscribe from everyone

This function simply goes into your subscriptions and unsubscribes from 
everyone, also removes them from the account database, but leaves them in 
the general database

##### Unsubscribe if more than two days have passed

This function unsubscribes from the account only if she subscribed to the
account and it is in the personal database, and after unsubscribing, it 
deletes it from it

##### Checking accounts for mutual subscription

This function looks in your subscriptions to see if the account has
subscribed in response, and if the account has subscribed in response, 
it puts False in the Hose column. It also writes and puts False in a column 
in the common database so that in the future you know who is worth following 
and who is not

##### Optimal

This function performs three actions at the same time:
* Follow all followers of the account
* Unsubscribe if more than two days have passed
* Checking accounts for mutual subscription

---

### Public Configuration

This is a pub_kfg file, it stores all Xpath. To get the Xpath,
you need to go to the browser and right-click
on the Xpath element of which you need to select
view the code, then the element highlighted in blue,
right-click on it and select in chrome to copy the full Xpath in 
Firefox, just Xpath. Congratulations, you have received a Xpath

### Cfg

This file saves your personal settings, such as your login, password, 
and whether the browser will be in the background or not 



