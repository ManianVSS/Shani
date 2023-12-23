import requests

class ALM:

    def __init__(self, alm_config_json):
        self.session = None
        self.base_url = alm_config_json['base_url']
        self.domain = alm_config_json['domain']
        self.project = alm_config_json['project']
        self.clientId = alm_config_json['clientId']
        self.secret = alm_config_json['secret']

    def login(self):
        if not self.session:
            self.session = requests.Session()
            self.session.verify = False
            self.session.trust_env = False

        response = self.session.post(url=self.base_url + "/rest/oauth2/login", json={"clientId": self.clientId, "secret": self.secret}, data=None)

        if response.status_code not in [200,399]:
            print("Error in logging into ALM")
            raise Exception("Error in logging into ALM\n", response.content)

    def fetch_requirements(self):
        requirement_url = (self.base_url + "/rest/domains/{}/projects/{}/requirements").format(self.domain, self.project)
        response = self.session.get(url=requirement_url)

        if response.status_code not in [200, 399]:
            print("Error in fetching requirements from ALM")
            raise Exception("Error in fetching requirements from ALM\n", response.content)
        return response
