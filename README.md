Pull Requests Manager for BitBucket
==================================

Dependencies
------------
Install Requests Library (http://docs.python-requests.org/en/latest/user/install/#install)

How to Run the Script
------------
python pr-manager.py -o {owner} -r {repository_name} -u {username} –p {password}

Details
------------
The script parses through the open pull requests looking for any user that is linked to the PR. A user can be linked in two ways: he/she is either a participant or a reviewer. You are a reviewer when you have been specifically added to the PR as a reviewer. You are a participant, when you have commented on a PR but have not been specifically added to a PR. However when you look at the PR directly on BitBucket, BitBucket doesn’t distinguish between reviewers and participants. Therfore for now, this script treats participants as reviewers (for now).

It also does not display any users that are not reviewing pull requests. For example if Joe was not reviewing any pull requests, you would not see 'Joe' with a 0 next to it. Joe's name would simply not show up. This is something that can be improved by getting the list of users added to that repository.
