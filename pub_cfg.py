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
sub_nick = lambda i: f'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[{i}]/div[2]/div/div/div/span/a/span/div'

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

#
#/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/span/a/span/div
#/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div[2]/div[1]/div/div/span/a/span/div