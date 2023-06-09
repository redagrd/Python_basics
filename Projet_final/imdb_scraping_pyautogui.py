import webbrowser
import pyautogui
import pyperclip
from time import sleep
import pandas as pd

def open_url_on_chrome(url):
    chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
    webbrowser.open(chrome_path)
    buttongoogle = pyautogui.locateOnScreen('images\\google.PNG', grayscale=True, confidence=.5)
    buttongoogle = pyautogui.center(buttongoogle)
    pyautogui.moveTo(buttongoogle)
    pyperclip.copy(url)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press('enter')
    pyautogui.move(0,100)
    sleep(5)

def get_star_center_coordinates():
    star = pyautogui.locateOnScreen('images\star.PNG', grayscale=True, confidence=.8)
    #Searches for the image
    if star != None:
        star = pyautogui.center(star)
    else : star = pyautogui.size()
    return star

def position_comment_on_top():
    pyautogui.scroll(-100)
    sleep(.08)
    Y_star = pyautogui.size()[1]
    star = get_star_center_coordinates()
    
    while (star[1]<=Y_star):
        Y_star = star[1]
        pyautogui.scroll(-100)
        sleep(.08)
        star = get_star_center_coordinates()
    pyautogui.scroll(100)
    sleep(.08)
    return(star)

def reveal_review_if_necessary():
    fleche = pyautogui.locateOnScreen('images\\fleche.PNG', grayscale=True, confidence=.8)
    if fleche != None:
        fleche = pyautogui.center(fleche)
        pyautogui.moveTo(fleche)
        pyautogui.click()


def get_mouse_to_end_of_review_position(star):
    done = False
    while not done:
        permalink = pyautogui.locateOnScreen('images\\permalink.PNG', grayscale=True, confidence=.8)
        if (permalink != None):
            permalink = pyautogui.center(permalink)
            if permalink[1]>star[1]:
                pyautogui.moveTo(permalink)
                pyautogui.move(-30,-50)
                done = True
            else:
                pyautogui.scroll(-100)
                sleep(.08)
        else:
            pyautogui.scroll(-100)
            sleep(.08)

def extract_data_from_text_block(text_block):
    text_block = text_block.splitlines()
    reviewer_and_review_date =text_block[1].split()
    # The string whith the reviewer name is stuck with the review day
    reviewer_and_review_day = reviewer_and_review_date[0]
    # we check if the second to last character is part of the reviewer name or the review day
    second_to_last_char =reviewer_and_review_day[-2]

    reviewer = reviewer_and_review_day[:-1]
    review_date = ' '.join([reviewer_and_review_day[-1],reviewer_and_review_date[1],reviewer_and_review_date[2]])
    if second_to_last_char.isdigit():
        if int(reviewer_and_review_day[-2:])<=31:
            reviewer = reviewer_and_review_day[:-2]
            review_date = ' '.join([reviewer_and_review_day[-2:],reviewer_and_review_date[1],reviewer_and_review_date[2]])

    review = ' '.join(text_block[2:])
    return reviewer, review_date, review



def get_review_content():
    sleep(1)
    star = get_star_center_coordinates()
    pyautogui.moveTo(star)


    pyautogui.click()
    pyautogui.press('tab')
    pyautogui.hotkey('shift', 'f10')
    pyautogui.press('down',presses=5)
    review_url = pyperclip.paste()
    print(review_url)

    pyautogui.click()
    pyautogui.press('tab',presses=2)
    pyautogui.hotkey('shift', 'f10')
    pyautogui.press('down',presses=5)
    pyautogui.press('enter')
    reviewer_url = pyperclip.paste()
    print(reviewer_url)

    pyautogui.mouseDown()
    pyautogui.move(50,0)
    pyautogui.mouseUp()
    pyautogui.hotkey('ctrl', 'c')
    score = pyperclip.paste()
    print(score)

    pyautogui.move(-60,15)
    pyautogui.click()
    pyautogui.mouseDown()
    pyautogui.move(0,5)
    get_mouse_to_end_of_review_position(star)

    pyautogui.mouseUp()
    pyautogui.hotkey('ctrl', 'c')
    text_block = pyperclip.paste()

    reviewer, review_date, review = extract_data_from_text_block(text_block)

    review_dict = {'id':i,
                   'score':score,
                   'reviewer':reviewer,
                   'reviewer_url':reviewer_url,
                   'review_url':review_url,
                   'review_date':review_date,
                   'review':review}
    return review_dict



if __name__ == "__main__": 
    url = 'https://www.imdb.com/title/tt3042408/reviews/?ref_=tt_ov_rt'
    open_url_on_chrome(url)
    review_list = []
    for i in range(5):
        print("Review",i)
        position_comment_on_top()
        reveal_review_if_necessary()
        review_dict = get_review_content()
        review_list.append(review_dict)
        #print(review_dict)

    df = pd.DataFrame.from_dict(review_list)        # Formattage en Dataframe Pandas
    df.to_csv("reviews.csv",index=False)
                   
