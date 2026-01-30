import configparser

config = configparser = configparser.ConfigParser()
config.read(".\Configurations\\config.ini")

class ReadConfigClass:

    @staticmethod
    def get_data_for_email():
        return config.get("login_data", "email") #Credencetest@test.com

    @staticmethod
    def get_data_for_password():
        return config.get("login_data", "password") #Credence@123

    @staticmethod
    def get_data_for_login_url():
        return config.get("application_url", "login_url ")  # https://automation.credence.in/login

    @staticmethod
    def get_data_for_registration_url():
        return config.get("application_url", "registration_url ")  # https://automation.credence.in/register