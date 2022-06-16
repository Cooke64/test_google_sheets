import requests
from bs4 import BeautifulSoup


class Currency:
    """Получаем данные о курсе доллара к рублю."""
    CUR_RUB = f'https://www.google.com/search?q=курс+доллара+к+рублю&sxsrf=APq-WBtgwZpUEdiN9OaZPdnv7JtulJWiXA%3A1644774378765&ei=6kMJYpapLo_frgSUh6SQDg&ved=0ahUKEwiWxtOEnv31AhWPr4sKHZQDCeIQ4dUDCA4&uact=5&oq=курс+доллара&gs_lcp=Cgdnd3Mtd2l6EAMyCQgjECcQRhCCAjILCAAQgAQQsQMQgwEyCAgAEIAEELEDMgsIABCABBCxAxCDATIICAAQgAQQsQMyCwgAEIAEELEDEIMBMgUIABCABDILCAAQgAQQsQMQgwEyCAgAEIAEELEDMggIABCABBCxAzoHCAAQRxCwAzoKCAAQRxCwAxDJAzoHCAAQsAMQQzoECCMQJzoICAAQgAQQyQNKBAhBGABKBAhGGABQuBJY4CRg8ypoAXABeACAAUWIAdUDkgEBOJgBAKABAcgBCsABAQ&sclient=gws-wiz'
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    def __get_currency_price(self) -> str:
        full_page = requests.get(self.CUR_RUB, headers=self.HEADERS)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.find_all("span", {"class": "DFlfde SwHCTb"})
        return convert[0].text

    def get_res(self) -> float:
        res = float(self.__get_currency_price().replace(",", "."))
        return res


currency = Currency()
