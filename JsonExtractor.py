import json

class JsonConfig():
    def __init__(self):
        # This is a JsonConfig file which we can update if there is any change in the schema.
        self.keys = ['user_list_size','user_list']
        self.user_list_keys = ['list_id','first name','last name','email']
        self.output = 'data.json'

class JsonExtractor():
    def createJson(self, userList):
        # creating and empty dictionary which will later be dumped into the json file
        config = JsonConfig()
        data = {}
        user_list = list(userList)
        data[config.keys[0]] = len(user_list)
        data[config.keys[1]] = []

        # looping through the userList datapoint and creating a dictionary
        for ls in user_list:
            data[config.keys[1]].append({
                config.user_list_keys[0]: ls[0],
                config.user_list_keys[1]: ls[1],
                config.user_list_keys[2]: ls[2],
                config.user_list_keys[3]: ls[3]
            })

        # dumping the dictionary into the output file
        with open(config.output, 'w') as outfile:
            json.dump(data, outfile, indent = 3)
        return config.output
