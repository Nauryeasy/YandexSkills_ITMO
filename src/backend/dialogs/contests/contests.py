from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *

config = getConfig()
def getResponse(event, context):
    return createResponse(event, config)


def isTriggered(event, context):
    token = {"контесты", "контест", "контестс"}
    return isSimilarTokens(event, token) and isInContext(event, 'news')


contests = {'getResponse': getResponse, 'isTriggered': isTriggered}
