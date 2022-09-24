import random

def getPrompt():
    data = [
    "Share about an adventure to a theme park.", 
    "Share about a fun time with your Dad, Mom, or sibling.",
    "Share about how you met your best friends.",
    "Share about a time you performed in front of a large audience.",
    "Share about a fun vacation with your friends or family."
    ]
    random.shuffle(data)
    return data[0]

