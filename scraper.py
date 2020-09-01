from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import enquiries
import webbrowser

channels = {
    "RoosterTeeth": "https://www.youtube.com/c/roosterteeth/videos",
    "AchievementHunter": "https://www.youtube.com/user/AchievementHunter/videos",
    "LetsPlay": "https://www.youtube.com/c/Letsplay/videos",
    "FunHaus": "https://www.youtube.com/c/Funhaus/videos"
}
rt_titles = {}
ah_titles = {}
lp_titles = {}
fh_titles = {}

driver = webdriver.Chrome()


def roosterteeth():
    driver.get(channels.get('RoosterTeeth'))
    video_titles = driver.find_elements_by_id("video-title")
    urls = driver.find_elements_by_xpath(
        '//*[@id="video-title"]')

    # Scraping the titles of every video on the initial load of the page
    rt_videos = []
    for title in video_titles:
        text = title.text
        rt_videos.append(text)

    # Scraping the direct link to the videos for every video that was scraped
    rt_video_urls = []
    for hrefs in urls:
        href = hrefs.get_attribute("href")
        rt_video_urls.append(href)

    for n in range(0, 11):
        rt_titles[rt_videos[n]] = rt_video_urls[n]


def achievementhunter():
    driver.get(channels.get('AchievementHunter'))
    video_titles = driver.find_elements_by_id("video-title")
    urls = driver.find_elements_by_xpath(
        '//*[@id="video-title"]')

    # Scraping the titles of every video on the initial load of the page
    ah_videos = []
    for title in video_titles:
        text = title.text
        ah_videos.append(text)

    # Scraping the direct link to the videos for every video that was scraped
    ah_video_urls = []
    for hrefs in urls:
        href = hrefs.get_attribute("href")
        ah_video_urls.append(href)

    for n in range(0, 11):
        ah_titles[ah_videos[n]] = ah_video_urls[n]


def letsplay():
    driver.get(channels.get('LetsPlay'))
    video_titles = driver.find_elements_by_id("video-title")
    urls = driver.find_elements_by_xpath(
        '//*[@id="video-title"]')

    # Scraping the titles of every video on the initial load of the page
    lp_videos = []
    for title in video_titles:
        text = title.text
        lp_videos.append(text)

    # Scraping the direct link to the videos for every video that was scraped
    lp_video_urls = []
    for hrefs in urls:
        href = hrefs.get_attribute("href")
        lp_video_urls.append(href)

    for n in range(0, 11):
        lp_titles[lp_videos[n]] = lp_video_urls[n]


def funhaus():
    driver.get(channels.get('FunHaus'))
    video_titles = driver.find_elements_by_id("video-title")
    urls = driver.find_elements_by_xpath(
        '//*[@id="video-title"]')

    # Scraping the titles of every video on the initial load of the page
    fh_videos = []
    for title in video_titles:
        text = title.text
        fh_videos.append(text)

    # Scraping the direct link to the videos for every video that was scraped
    fh_video_urls = []
    for hrefs in urls:
        href = hrefs.get_attribute("href")
        fh_video_urls.append(href)

    for n in range(0, 11):
        fh_titles[fh_videos[n]] = fh_video_urls[n]


def main():
    roosterteeth()
    achievementhunter()
    letsplay()
    funhaus()

    driver.close()

    while True:
        channel_choice = enquiries.choose(
            "### ROOSTERTEETH FAMILY LATEST VIDEOS ###", channels.keys())

        if "RoosterTeeth" in channel_choice:
            rt_choice = enquiries.choose(
                "Choose a video to watch", rt_titles.keys())
            url = rt_titles.get(rt_choice)
            webbrowser.open(url)
            continue
        elif "AchievementHunter" in channel_choice:
            ah_choice = enquiries.choose(
                "Choose a video to watch", ah_titles.keys())
            url = ah_titles.get(ah_choice)
            webbrowser.open(url)
            continue
        elif "LetsPlay" in channel_choice:
            lp_choice = enquiries.choose(
                "Choose a video to watch", lp_titles.keys())
            url = lp_titles.get(lp_choice)
            webbrowser.open(url)
            continue
        elif "FunHaus" in channel_choice:
            fh_choice = enquiries.choose(
                "Choose a video to watch", fh_titles.keys())
            url = fh_titles.get(fh_choice)
            webbrowser.open(url)
            continue


main()
