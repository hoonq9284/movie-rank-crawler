import requests
import config.config as config
from bs4 import BeautifulSoup


def get_movie_rank():
    """
    requests 라이브러리를 이용하여 naver 포털 사이트에 현재 상영영화 검색
    이후에, bs4 라이브러리를 이용하여 현재 상영영화 타이틀 정보 크롤링
    :return:
    """
    url = config.url
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    movies = soup.find_all('div', class_=config.movie_info_class)

    rankings = []
    for movie in movies[:10]:
        title = movie.find('a', class_=config.movie_info_title)
        rankings.append(title.text)

    return rankings


def save_to_file(rankings):
    """
    현재 상영영화 데이터를 크롤링한 정보를 txt 파일로 생성하고, 현재 위치에 저장
    :param rankings:
    :return:
    """
    with open('movie_ranking.txt', 'w', encoding='utf-8') as file:
        for title in rankings:
            line = f"영화 제목 : {title}\n"
            file.write(line)
            print(line.strip())


if __name__ == '__main__':
    print("==================== 현재 상영 영화 ====================")
    movie_rankings = get_movie_rank()
    save_to_file(movie_rankings)
