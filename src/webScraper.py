import requests
from bs4 import BeautifulSoup


class WebScraper:
    def __init__(self, url):
        self.url = url
        self.output_data = []

    def __download_web(self, url):
        """
        Descarrega la web guardada a la variable self.url
        :return: Objecte del tipus BeautifulSoup (contingut de la web en HTML)
        """
        page = requests.get(url)

        if page.status_code == 200:
            return BeautifulSoup(page.content, "html.parser")

    def __get_links(self, content):
        """
        Obté els links de l'objecte tipus BeautifulSoup
        :return: null
        """
        list_categories = self.__get_categories(content)

    def __get_categories(self, content):
        """
        Obté el llistat de categories (nom) i la URL d'accés.
        :param content: Objecte del tipus BeautifulSoup
        :return: list_categories: Array
        """
        categories = content.find("div", {"data-component": "navigation-bar"})
        categories_a = categories.findChildren("a", recursive=True)
        list_categories = []

        for category_a in categories_a:
            href = self.url + category_a.get('href')
            name = category_a.get('title')

            if href and name:
                list_categories.append([name, href])

        return list_categories

      def __get_articles(self, content):
        """
        Donat la URL d'una categoria,
        obté el llistat d`'URL d'accés dels articles
        :param categoria: Objecte del tipus String
        :return: list_: Array
        """
        content_html = self.__download_web(content)
        articles = content_html.findChildren("article", recursive=True)
        list_articles = []
        for articles_a in articles:
            href_ = articles_a.find('a')
            if href_:
                url_art = href_.get('href')
                if url_art:
                    list_articles.append([href_])
        return list_articles

    
    def init_process(self):
        """
        Executa el procés de web scraping
        :return: null
        """
        content_html = self.__download_web(self.url)
        self.__get_links(content_html)
