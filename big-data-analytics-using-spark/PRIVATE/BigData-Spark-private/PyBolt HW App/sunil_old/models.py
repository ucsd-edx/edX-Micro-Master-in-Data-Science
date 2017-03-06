import simplejson as json

auth_dict=json.loads(open("student-list.json").read())

class User:
    
    def __init__(self, username, password):
        self.username = username
	self.password = password

    @property
    def is_authenticated(self):
	if self.username in auth_dict:
		if self.password==auth_dict[self.username]:
            		return True
	else:
	    return False

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.username)
