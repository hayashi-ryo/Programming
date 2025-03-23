from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.ie.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchFrameException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from util import take_screenshot, reset_screenshot_counter, list_frames_and_named_elements
from pywinauto import Application
import os
import io
import sys
import time

# IEDriverServer のパスを指定
ie_driver_path = "C:\\work\\python\\tool\\IEDriverServer.exe"
service = Service(ie_driver_path)

# IE モードのオプションを設定
ie_options = webdriver.IeOptions()
ie_options.attach_to_edge_chrome = True
ie_options.edge_executable_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"

# **? IEの動作を高速化するオプション**
ie_options.ignore_protected_mode_settings = True  # セキュリティゾーン設定を無視
ie_options.ignore_zoom_level = True  # ズームレベルのチェックを無視
ie_options.require_window_focus = True  # ウィンドウフォーカスを強制
ie_options.native_events = False  # ネイティブイベントを無効化（パフォーマンス改善）
ie_options.introduce_flakiness_by_ignoring_security_domains = True  # セキュリティ設定の影響を無視

# WebDriverを起動
driver = webdriver.Ie(service=service, options=ie_options)

# 画面表示内容の固定化
driver.execute_script("document.body.style.zoom='100%'")
driver.execute_script("window.scrollTo(0, 0);")
driver.set_window_size(600, 1200)

# IEモードで開く
driver.get("http://172.18.227.225/ids/")

# ページのタイトルを取得して記録
print(driver.title)

# スクリーンショット設定
reset_screenshot_counter()
output_dir = "C:\\work\\python\\test"
# take_screenshot(driver=driver, base_filename=driver.title,output_dir=output_dir)

# ユーティリティ
# list_frames_and_named_elements(driver)

# フレームが利用可能になるまで待機してから切り替え
def switch_to_frame_safe(driver, frame_name, max_retries=5):
    retry_count = 0
    driver.switch_to.default_content()
    while retry_count < max_retries:
        try:
            WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it((By.NAME, frame_name)))
            print(f"Switched to frame: {frame_name}")
        except:
            retry_count+=1

def windowSwitch(driver: WebDriver, max_retries: int=5):
    main_window_handle = driver.current_window_handle
    cnt = 0
    while cnt < max_retries:
        try:
            # 新しいウィンドウが開くまで待機 (タイムアウト1秒)
            WebDriverWait(driver, 1).until(lambda d: len(d.window_handles) > 1)
            window_handles = driver.window_handles  # すべてのウィンドウハンドルを取得
            if len(window_handles) > 1:
                break  # 新しいウィンドウが開いたらループを抜ける
        except Exception as e:
            cnt += 1
            print(f"❌ エラー発生: {e}. 再試行 {cnt}/{max_retries}")
    print(driver.title)
    for handle in window_handles:
        if handle != main_window_handle:
            sub_window_handle = handle
            driver.switch_to.window(sub_window_handle)
            break

# ログイン画面
# take_screenshot(driver=driver, base_filename=driver.title,output_dir=output_dir)
username_field = driver.find_element(By.NAME, "usid")  # `name="usid"`
password_field = driver.find_element(By.NAME, "pswd")  # `name="pswd"`
driver.execute_script("arguments[0].value = arguments[1];", username_field, "admin") # ユーザーIDを入力
driver.execute_script("arguments[0].value = arguments[1];", password_field, "admin") # パスワードを入力
login_button = driver.find_element(By.ID, "button")
driver.execute_script("arguments[0].click();", login_button)

# メインメニューからタブを経由して画面移動
def mainMenue(driver: WebDriver, link_text: str, screenshot: bool = False, output_dir: str = "outputDir", max_retries: int = 5):
    if screenshot:
        take_screenshot(driver=driver, base_filename=driver.title, output_dir=output_dir)
    retries = 0
    switch_to_frame_safe(driver, "header")
    while retries < max_retries:
        try:
            # 指定したリンクテキストの要素が現れるまで待機
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, link_text)))
            link = driver.find_element(By.LINK_TEXT, link_text)          
            # JavaScript を使ってクリック（通常のクリックが効かない場合に備える）
            driver.execute_script("arguments[0].click();", link)
            # 成功したらデフォルトコンテンツに戻して関数を終了
            driver.switch_to.default_content()
            print(f"Successfully clicked on '{link_text}'")
            return
        except:
            retries += 1
            print(f"Retry {retries}/{max_retries}: Unable to find frame or element '{link_text}', retrying...")
"""  
# 帳表検索
driver.switch_to.default_content()

# 帳表検索階層選択ボタンの押下
switch_to_frame_safe(driver, "body")
driver.switch_to.frame("searchreport_header")
button = driver.find_element(By.XPATH, "//img[@name='ico_search'][1]")
driver.execute_script("arguments[0].click();", button)

# 帳表階層選択画面で仕分け科目を選択する
main_window_handle = driver.current_window_handle
print("DEDEDE")
windowSwitch(driver)
take_screenshot(driver=driver, base_filename=driver.title,output_dir=output_dir)
print(driver.title)
# list_frames_and_named_elements(driver)
buttons = driver.find_elements(By.XPATH, "//img[@name='ico_folder']") 
button = buttons[1]
driver.execute_script("arguments[0].click();", button)
driver.switch_to.window(main_window_handle)
take_screenshot(driver=driver, base_filename=driver.title,output_dir=output_dir)

# 5
switch_to_frame_safe(driver, "body")
driver.switch_to.frame("searchreport_header")
buttons = driver.find_elements(By.XPATH, "//img[@name='ico_search']")
button = buttons[1]
driver.execute_script("arguments[0].click();", button)
windowSwitch(driver)
take_screenshot(driver=driver, base_filename=driver.title,output_dir=output_dir)
print(driver.title)
driver.close()

# 6
driver.switch_to.window(main_window_handle)
switch_to_frame_safe(driver, "body")
driver.switch_to.frame("searchreport_header")
button = driver.find_element(By.XPATH, "//input[@value='ブックマーク設定']")
driver.execute_script("arguments[0].click();", button)
windowSwitch(driver)
take_screenshot(driver=driver, base_filename=driver.title,output_dir=output_dir)
print(driver.title)
driver.close()

# driver.close()
driver.switch_to.window(main_window_handle)
take_screenshot(driver=driver, base_filename=driver.title,output_dir=output_dir)
print("DEBUG")
# mainMenue(driver,"帳表検索", False, output_dir)

# 帳表検索本体
mainMenue(driver,"帳表検索", False, output_dir)
driver.switch_to.frame("body")
driver.switch_to.frame("searchreport_header")
button = driver.find_element(By.XPATH, "//input[@value='検　索']")
driver.execute_script("arguments[0].click();", button)
driver.switch_to.default_content()
driver.switch_to.frame("body")
driver.switch_to.frame("searchreport_body")



# 帳表閲覧画面
try:
    first_checkbox = driver.find_element(By.XPATH, "//input[@name='atpr'][1]") # 表の一番最初の要素のXPATHを取得
    parent_tr = first_checkbox.find_element(By.XPATH, "./ancestor::tr") # 表自体のtr情報を取得
    tr_elements = driver.find_elements(By.TAG_NAME, "tr") # tr情報の取得
    # second_tr = 
    # tr_text_lines = second_tr.text.splitlines() 
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
take_screenshot(driver=driver, base_filename=driver.title,output_dir=output_dir)
print(driver.title)
driver.close()
driver.switch_to.window(main_window_handle)

# 一括印刷
driver.switch_to.default_content()
driver.switch_to.frame("body")
driver.switch_to.frame("searchreport_body")
try:
    first_checkbox = driver.find_element(By.XPATH, "//input[@name='atpr'][1]")
    # second_checkbox = driver.find_element(By.XPATH, "//input[@name='atpr'][2]")
    try:
        first_checkbox.click()
        # second_checkbox.click()
    except:
        driver.execute_script("arguments[0].click();", first_checkbox)
        # driver.execute_script("arguments[0].click();", second_checkbox)
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



# 掲示板
mainMenue(driver,"掲示板", True, output_dir)
main_window_handle = driver.current_window_handle
switch_to_frame_safe(driver, "body")
driver.switch_to.frame("msgboard_body")
button = driver.find_element(By.XPATH, "//input[@value='追　加']")
driver.execute_script("arguments[0].click();", button)
windowSwitch(driver)
take_screenshot(driver=driver, base_filename=driver.title,output_dir=output_dir)
print(driver.title)
driver.close()
driver.switch_to.window(main_window_handle)



# パスワード変更
mainMenue(driver,"パスワード変更", True, output_dir)
main_window_handle = driver.current_window_handle
windowSwitch(driver)
take_screenshot(driver=driver, base_filename=driver.title,output_dir=output_dir)
print(driver.title)
driver.close()
driver.switch_to.window(main_window_handle)
"""
# ログ閲覧
mainMenue(driver,"ログ閲覧", True, output_dir)
switch_to_frame_safe(driver, "body")
driver.switch_to.frame("logview_header")
button = driver.find_element(By.XPATH, "//img[@name='ico_search'][1]")
driver.execute_script("arguments[0].click();", button)
driver.switch_to.default_content()
list_frames_and_named_elements(driver)
switch_to_frame_safe(driver, "body")
driver.switch_to.frame("logview_body")
"""

# ユーザー管理
mainMenue(driver,"ユーザー管理", True, output_dir)

# レベル管理
mainMenue(driver,"レベル管理", True, output_dir)

# グループ管理
mainMenue(driver,"グループ管理", True, output_dir)

# データベース管理
mainMenue(driver,"データベース管理", True, output_dir)

# 初期コメント
mainMenue(driver,"初期コメント", True, output_dir)

# 帳表タイプ
mainMenue(driver,"帳表タイプ", True, output_dir)

# 帳表ID置換 
mainMenue(driver,"帳表ID置換", True, output_dir)

"""
# メインメニュー->ログアウト
driver.switch_to.frame("header")
link = driver.find_element(By.LINK_TEXT, "ログアウト")
driver.execute_script("arguments[0].click();", link)

# ブラウザを閉じる
driver.quit()