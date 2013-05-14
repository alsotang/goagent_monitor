import ConfigParser
import StringIO


def getAppidFromINI(file_content):
    cf = ConfigParser.ConfigParser()
    config_io = StringIO.StringIO(file_content)
    cf.readfp(config_io)

    return cf.get('gae', 'appid').split('|')
