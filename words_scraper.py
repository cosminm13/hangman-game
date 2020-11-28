import requests
from bs4 import BeautifulSoup


def get_category(URL):
    page_html = requests.get(URL).content  # get html content
    soup = BeautifulSoup(page_html, 'html.parser')  # parse html content with bs4
    category_name = str(soup.find(class_='body-title__title').contents[0])  # extract category name
    return category_name


def scrape_category(URL):
    try:
        page_html = requests.get(URL).content  # get html content
    except Exception as e:
        print('Could not fetch page!')
    soup = BeautifulSoup(page_html, 'html.parser')  # parse html content with bs4
    category_name = str(soup.find(class_='body-title__title').contents[0])  # extract category name
    words_soup = soup(class_='wordlist-item')  # extract content from category

    words = []
    for word in words_soup:
        words.append(word.contents)  # append extracted content to list
    words = [word for sublist in words for word in sublist]  # join individual lists together

    for word in words:
        if 'bs4.element.Tag' in str(type(word)):
            words.remove(word)  # remove words that don't match the format
    words = [str(word) for word in words]
    for word in words:
        if 'href' in word:
            words.remove(word)  # remove words that don't match the format
    return category_name, words
