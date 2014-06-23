import requests
from requests.auth import HTTPBasicAuth

class BitBucket:
	__apiBaseUrl = None
	__username = None
	__password = None

	def __init__(self, username, password):
		self.__apiBaseUrl = 'https://api.bitbucket.org/2.0'
		self.__username = username
		self.__password = password

	def getPullRequestDetails(self, user, repository, prID):
		url = self.__apiBaseUrl + "/repositories/{0}/{1}/pullrequests/{2}".format(user, repository, prID)
		req = requests.get(url, auth=(self.__username, self.__password))
		return(req.json())

	def getOpenPullRequests(self, user, repository):
		pageCount = 1
		url = self.__apiBaseUrl + "/repositories/{0}/{1}/pullrequests?state=OPEN&page={2}".format(user, repository, pageCount)
		req = requests.get(url, auth=(self.__username, self.__password))
		if req.status_code == 200:
			jsonResponse = req.json()
			openPullRequestsArray = jsonResponse['values']

			while 'next' in jsonResponse:
				pageCount = pageCount+1
				url = self.__apiBaseUrl + "/repositories/{0}/{1}/pullrequests?state=OPEN&page={2}".format(user, repository, pageCount)
				req = requests.get(url, auth=(self.__username, self.__password))
				jsonResponse = req.json()
				openPullRequestsArray.extend(jsonResponse['values'])	
		else:
			print('Request was not successfull. Status Code: '+req.status_code)
			
		return(openPullRequestsArray)