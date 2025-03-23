from selenium import webdriver
from ie import ie_setting
from util import reset_screenshot_counter

from pages.scenarios import login, chouhyou, keijiban, passwordkanri, logetsuran
def main():
  # シナリオ走行向け各種設定
  ie_driver_path = "C:\\work\\python\\tool\\IEDriverServer.exe" # IEドライバーの格納ディレクトリ
  url = "http://172.18.227.225/ids/" # テスト対象環境URL
  username = "admin"
  password = "admin"
  screenshot = False # スクリーンショット取得設定
  output_dir = "C:\\work\\python\\test" # スクリーンショット格納ディレクトリ
  
  # 事前準備
  screenshot_enabled = False 
  reset_screenshot_counter()
  driver = ie_setting(ie_driver_path, url)
  
  # 実行シナリオ設定
  login(driver, username, password)
  chouhyou(driver)
  keijiban(driver)
  passwordkanri(driver)
  logetsuran(driver)
  driver.quit()
  
if __name__ == "__main__":
    main()
