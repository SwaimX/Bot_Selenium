#The Xpath

# What is i in xpath, this is a number that you can get by copying the first and second
# elements of xpath, and how is this number different in these xpath. Mostly it's somewhere
# at the end

# The accept cookie button is optional
cookies_accept = '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]'

# This is a nickname input field for auth
auth_login = '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div[1]/div[1]/div/label/input'

# This is the password input field for auth
auth_password = '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div[1]/div[2]/div/label/input'

# This is the login button
auth_btn = '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button'

# This is the subscribe button in the followers of the account
sub_subscribeb = lambda i: f'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[{i}]/div[3]/button'

#This button cancels clicking if you clicked on an account to which you are already subscribed
sub_cancel = '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]'

#This is the text of the niku account
def sub_nick(i):
    if i == 1:
        return f'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div/span/a/span/div'
    else:
        return f'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[{i}]/div[2]/div/div/div/div/span/a/span/div'


def hose_no(i):
    if i == 1:
        # This is the text of the first nickname
        return f'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[{i}]/div[2]/div[1]/div/div/span/a/span/div'
    else:
        # This is the text of the second nickname
        return f'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[{i}]/div[2]/div[1]/div/div/span/a/span/div'

# This button to click is tracked in your followers made to scroll the page
hose_for_scroll = lambda i: f'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[{i}]/div[3]/button'

# This is to click cancel pressing the above button
hose_for_cancel = '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]'

## Unsubs everyone

# This is a xpath button following in your subscriptions
following = lambda i: f'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{i}]/div[3]/button'

# This is a xpath button unsubscribe
unsub = '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[1]'

## Unsub if time more two deys

# This xpath of button following on the page of the user you are subscribed to
followingser = "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button"

# This xpath button unsubscribe

unsubs = '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[7]'

# /html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[3]/button
# /html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[3]/div[3]/button

#/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/span/a/span/div
#/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div[2]/div[1]/div/div/span/a/span/div

# /html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div/span/a/span/div
# /html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div/a/span/div

# /html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div/span/a/span/div
# /html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[3]/div[2]/div/div/div/div/span/a/span/div