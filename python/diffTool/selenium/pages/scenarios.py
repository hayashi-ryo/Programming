from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pywinauto import Application
from util import take_screenshot, list_frames_and_named_elements
from base import switch_to_frame_safe, windowSwitch, mainMenue

import time
import os
from main import output_dir
# ログイン画面
def login(driver: webdriver, username:str, password: str):
  take_screenshot(driver, driver.title)
  username_field = driver.find_element(By.NAME, "usid")  # `name="usid"`
  password_field = driver.find_element(By.NAME, "pswd")  # `name="pswd"`
  driver.execute_script("arguments[0].value = arguments[1];", username_field, username) # ユーザーIDを入力
  driver.execute_script("arguments[0].value = arguments[1];", password_field, password) # パスワードを入力
  login_button = driver.find_element(By.ID, "button")
  driver.execute_script("arguments[0].click();", login_button)  
  
# 帳票検索
def chouhyou(driver: webdriver):
  driver.switch_to.default_content()
  switch_to_frame_safe(driver, "body")
  driver.switch_to.frame("searchreport_header")
  button = driver.find_element(By.XPATH, "//img[@name='ico_search'][1]")
  driver.execute_script("arguments[0].click();", button)

  # 帳表階層選択画面で仕分け科目を選択する
  main_window_handle = driver.current_window_handle
  print("DEDEDE")
  windowSwitch(driver)
  take_screenshot(driver, driver.title)
  print(driver.title)
  buttons = driver.find_elements(By.XPATH, "//img[@name='ico_folder']") 
  button = buttons[1]
  driver.execute_script("arguments[0].click();", button)
  driver.switch_to.window(main_window_handle)
  take_screenshot(driver, driver.title)
  
  #5
  switch_to_frame_safe(driver, "body")
  driver.switch_to.frame("searchreport_header")
  buttons = driver.find_elements(By.XPATH, "//img[@name='ico_search']")
  button = buttons[1]
  driver.execute_script("arguments[0].click();", button)
  windowSwitch(driver)
  take_screenshot(driver, driver.title)
  print(driver.title)

  #6
  driver.switch_to.window(main_window_handle)
  switch_to_frame_safe(driver, "body")
  driver.switch_to.frame("searchreport_header")
  button = driver.find_element(By.XPATH, "//input[@value='ブックマーク設定']")
  driver.execute_script("arguments[0].click();", button)
  windowSwitch(driver)
  take_screenshot(driver, driver.title)
  print(driver.title)
  
  # 帳票検索本体
  try:
      first_checkbox = driver.find_element(By.XPATH, "//input[@name='atpr'][1]") # 表の一番最初の要素のXPATHを取得
      parent_tr = first_checkbox.find_element(By.XPATH, "./ancestor::tr") # 表自体のtr情報を取得
      tr_elements = driver.find_elements(By.TAG_NAME, "tr") # tr情報の取得
      tr_text_lines = tr_elements[2].text.splitlines() # tr内は改行コードを含めた2行のテキストが存在するので一つ目を取得する
      first_line_text = tr_text_lines[0].strip()
      window = Application(backend="uia").connect(title_re=".*電子帳表システム.*").window(title_re=".*電子帳表システム.*") # window要素をUIAとして取得
      all_controls = window.descendants()
      all_links = window.descendants(control_type="Hyperlink")
      matched_link = None
      for link in all_links:
          link_text = link.window_text().strip()
          if first_line_text  in link_text:
              matched_link = link
              break
      if matched_link:
          matched_link.invoke()
          print("InvokePattern を使ってクリックしました:", matched_link.window_text())
      else:
          print("一致するリンクが見つかりません")
  except Exception as e:
      print("クリックに失敗:", e)

  main_window_handle = driver.current_window_handle
  windowSwitch(driver)
  take_screenshot(driver=driver, base_filename=driver.title)
  print(driver.title)
  driver.close()
  driver.switch_to.window(main_window_handle)

  # 一括印刷
  driver.switch_to.default_content()
  driver.switch_to.frame("body")
  driver.switch_to.frame("searchreport_body")
  try:
      checkboxes = driver.find_element(By.XPATH, "//input[@name='atpr']")
      first_checkbox = checkboxes[0]
      second_checkbox = checkboxes[1]
      try:
          first_checkbox.click()
          second_checkbox.click()
      except:
          driver.execute_script("arguments[0].click();", first_checkbox)
          driver.execute_script("arguments[0].click();", second_checkbox)
  except Exception as e:
      print("クリックに失敗:", e)
  
  try:
    # ボタンの `id` や `name` で取得（適宜修正）
    button = driver.find_element(By.XPATH, "//input[@value='一括印刷']")
    driver.execute_script("arguments[0].click();", button)
    print("「一括印刷」ボタンを押下しました")
  except Exception as e:
      print(f"ボタン操作エラー: {e}")
  
  main_window_handle = driver.current_window_handle
  windowSwitch(driver)
  max_wait_time = 15
  start_time = time.time()
  pdf_path = os.path.join(output_dir, "一括印刷.pdf")
  
  try:
      printer_dropdown = Select(driver.find_element(By.TAG_NAME, "select"))
      printer_dropdown.select_by_visible_text("Microsoft Print to PDF")
      print_button = driver.find_element(By.XPATH, "//input[@value='一括印刷']")
      driver.execute_script("arguments[0].click();", print_button)
      while True:
          try:
              app = Application(backend="win32").connect(title_re=".*名前を付けて保存.*", timeout=1)
              break  # ウィンドウが開いたらループを抜ける
          except:
              if time.time() - start_time > max_wait_time:
                  print("エラー: 「名前を付けて保存」ウィンドウが開きませんでした")
                  exit()
              time.sleep(1)  # 1秒ごとにチェック
      save_dialog = app.window(title_re=".*名前を付けて保存.*")
      save_dialog.wait("exists ready", timeout=10)
      filename_box = save_dialog.child_window(class_name="Edit")
      filename_box.set_text(pdf_path)
      save_button = save_dialog.child_window(title="保存(&S)")
      save_button.wait("exists ready", timeout=5)
      save_button.wait("enabled ready", timeout=2)
      save_button.click()

      # 上書き確認ダイアログ
      start_time = time.time()
      while True:
          try:
              confirm_dialog = app.window(title_re=".*名前を付けて保存の確認.*")
              break  # ウィンドウが開いたらループを抜ける
          except:
              if time.time() - start_time > 5:
                  print("エラー: 「名前を付けて保存」ウィンドウが開きませんでした")
                  exit()
              time.sleep(1)  # 1秒ごとにチェック
      try:
          if confirm_dialog.exists():
              confirm_button = confirm_dialog.child_window(title="はい(&Y)")
              confirm_button.wait("exists ready", timeout=5)
              confirm_button.wait("enabled ready", timeout=2)

              # **ボタンがある限りクリック**
              while confirm_button.exists():
                  confirm_button.click()
                  print("✅ 上書き確認で「はい」をクリックしました")
                  time.sleep(0.5)
      except Exception as e:
          print("⚠️ 上書き確認ダイアログが見つかりませんでした:", e)
  except Exception as e:
      print("エラー発生:", e)
  driver.close()
  driver.switch_to.window(main_window_handle)

def keijiban(driver: webdriver):
  mainMenue(driver,"掲示板", True, output_dir)
  main_window_handle = driver.current_window_handle
  switch_to_frame_safe(driver, "body")
  driver.switch_to.frame("msgboard_body")
  button = driver.find_element(By.XPATH, "//input[@value='追　加']")
  driver.execute_script("arguments[0].click();", button)
  windowSwitch(driver)
  take_screenshot(driver=driver, base_filename=driver.title)
  print(driver.title)
  driver.close()
  driver.switch_to.window(main_window_handle)

def passwordkanri(driver: webdriver):
  mainMenue(driver,"パスワード変更", True, output_dir)
  main_window_handle = driver.current_window_handle
  windowSwitch(driver)
  take_screenshot(driver=driver, base_filename=driver.title)
  print(driver.title)
  driver.close()
  driver.switch_to.window(main_window_handle)
  
def logetsuran(driver: webdriver):
  mainMenue(driver,"ログ閲覧", True, output_dir)
  switch_to_frame_safe(driver, "body")
  driver.switch_to.frame("logview_header")
  button = driver.find_element(By.XPATH, "//img[@name='ico_search'][1]")
  driver.execute_script("arguments[0].click();", button)
  driver.switch_to.default_content()
  list_frames_and_named_elements(driver)
  switch_to_frame_safe(driver, "body")
  driver.switch_to.frame("logview_body")
