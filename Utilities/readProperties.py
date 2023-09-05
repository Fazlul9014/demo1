import configparser



config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class Readconfig():

    @staticmethod
    def getApplicati0nURL():
        url=config.get('common info','base_url')
        return url

    @staticmethod
    def get_username():
        username = config.get('common info','useremail')
        return username

    @staticmethod
    def get_password():
        password = config.get('common info','password')
        return password