from bs4 import BeautifulSoup
import requests
'''
測試用，get web soup.
'''

class GetSoup:

    def __init__(self,url):
        self.url = url
        self.soup = None

    def get_soup(self):
        try :
            # sent  a request
            res = requests.get(self.url)

            # HTTPError
            res.raise_for_status()

            # parsing the html content
            self.soup = BeautifulSoup(res.text, 'html.parser')

        except requests.exceptions.HTTPError as http_err:
            # 專門捕捉網頁狀態碼錯誤 (例如 404, 500)
            raise Exception(f"網頁連線失敗，伺服器回應: {http_err}")
            
        except requests.exceptions.Timeout:
            # 專門捕捉你上一題遇到的「卡很久、超時」問題
            raise Exception("連線超時")
            
        except Exception as err:
            # 其他所有未知的錯誤
            raise Exception(f"發生預期外的錯誤: {err}")


if __name__ == '__main__':
    # input_url = ''
    input_url = input('目標網址：')
    get_soup = GetSoup(input_url)
    get_soup.get_soup()
    print(get_soup.soup)