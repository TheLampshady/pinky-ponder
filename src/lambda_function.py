from my_skill import PinkySkill


def lambda_handler(event, context={}):
    return PinkySkill(event=event).response()
