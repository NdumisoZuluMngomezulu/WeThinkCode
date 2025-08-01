import emoji

def generateEmoji():
    str = input("Enter the text in the form 'thumps_up': ")

    try:
        output = emoji.emojize(str, language = "en")
    except:
        print("Please enter a valid text")
    
    return output


print(generateEmoji())

'''
import emoji

def main():

    user_input = input("Input: ")
    print(emoji.emojize(f"Output: {user_input}", language="alias"))
    '''