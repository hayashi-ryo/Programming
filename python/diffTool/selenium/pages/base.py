from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

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

# 安全にウィンドウをスイッチ
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

# メインメニューからタブを経由して画面移動
def mainMenue(driver: WebDriver, link_text: str,max_retries: int = 5):
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
