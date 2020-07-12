import pyperclip
import re

def phoneNumberExtractor(text):
    """
    Extracts phone numbers from a text

    args:
        text(string): the text to be searched

    returns: 

        a list of phone numbers

    """
    pattern = re.compile(r'''(
        (\d{3} | \(\d{3}\))?
        (\s|-|\.)?
        (\d{3})
        (\s|-|\.)
        (\d{4})
        (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''', re.VERBOSE)

    mo = pattern.findall(text)
    return mo

    
def email_extractor(text):
    """
    extracts emails from a text

    args:
        text (string): the text to be searched 

    return: 
        the emails extracted

    """
    pattern = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z{2,3}])
    
    )''',re.VERBOSE)

    mo = pattern.findall(text)
    return mo


text = str(pyperclip.paste())
matches = []

for groups in phoneNumberExtractor(text):
    phoneNo = '-'.join ([groups[1], groups[3], groups[5] ] )

    if groups[8] != '':
        phoneNum += ' x' + groups[8]

    matches.append(phoneNo)

for groups in email_extractor(text):
    matches.append(groups[0])

    # copy back to clipboard
if len(matches) > 0:

    pyperclip.copy("\n". join(matches))
    print("copied to clipboard")
    print('\n'.join(matches))

else:
    print("no phone number or email found in text")



