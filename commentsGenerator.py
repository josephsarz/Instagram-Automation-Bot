import string 
import random

# Generating name functions 
def generateComment():
        comments = ['Nice shot! @{}',
                        'I love your profile! @{}',
                        'Your feed is an inspiration :thumbsup:',
                        'Just incredible :open_mouth:',
                        'What camera did you use @{}?',
                        'Love your posts @{}',
                        'Looks awesome @{}',
                        'Getting inspired by you @{}',
                        ':raised_hands: Yes!',
                        'I can feel your passion @{} :muscle:',
                        'wow',
                        'This is lovely',
                        'cool']
        return ''.join(random.choice(comments) 

