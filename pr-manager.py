from bitbucketapi.api import BitBucket
import operator
from collections import OrderedDict
import sys
import getopt

def main(argv):                 
        try:                                
            opts, args = getopt.getopt(argv, "hu:p:o:r:d", ["help", "username=", "password=", "owner=", "repository=" "debug"]) 
        except getopt.GetoptError:           
            #usage()                          
            sys.exit(2) 

        for opt, arg in opts:               
            if opt in ("-h", "--help"):      
                print ''                     
                sys.exit()                  
            elif opt == '-d':                
                global _debug               
                _debug = 1                  
            elif opt in ("-u", "--username"): 
                username = arg          
            elif opt in ("-p", "--password"): 
                password = arg         
            elif opt in ("-o", "--owner"): 
                owner = arg             
            elif opt in ("-r", "--repository"): 
                repository = arg     


        bucket = BitBucket(username, password)
        openPullRequestsArray = bucket.getOpenPullRequests(owner, repository)

        userReviewersCount = {}
        pullRequestsDaysOld = {}

        for pullRequest in openPullRequestsArray:
            pullRequestDetails = bucket.getPullRequestDetails(owner, repository, pullRequest['id'])
            print('\n-------------------------------------------------\n'+str(pullRequest['id'])+': '+pullRequest['title']+' ('+pullRequest['author']['display_name']+')\n-------------------------------------------------')
            #reviewersArray = pullRequestDetails['reviewers']
            #for reviewerDict in reviewersArray:
            #    print(reviewerDict['display_name'])

            participantsArray = pullRequestDetails['participants']
            for participantsDict in participantsArray:
                if (participantsDict['user']['display_name'] != pullRequest['author']['display_name']):# and (participantsDict['role'] == 'REVIEWER'):
                    print(participantsDict['user']['display_name'])
                    if participantsDict['user']['display_name'] in userReviewersCount:
                        userReviewersCount[participantsDict['user']['display_name']] += 1
                    else:
                        userReviewersCount[participantsDict['user']['display_name']] = 1

            print('')

        sortedUserReviewersCount = OrderedDict(sorted(userReviewersCount.items(), key=lambda item: item[1]))
        print('\n=========================================================')
        print('                          STATS                            ')
        print('=========================================================\n')

        print('# of Open Pull Requests: '+str(len(openPullRequestsArray)))
        print('\n# of Pending Pull Requests per User')
        print('-----------------------------------')

        for userDisplayName in sortedUserReviewersCount:
            print(str(sortedUserReviewersCount[userDisplayName])+' '+userDisplayName)

if __name__ == "__main__":
    main(sys.argv[1:])