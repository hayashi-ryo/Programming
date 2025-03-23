from selenium import webdriver
from selenium.webdriver.ie.service import Service

def ie_setting(ie_driver_path: str, url: str):
    service = Service(ie_driver_path)

    # IE モードのオプションを設定
    ie_options = webdriver.IeOptions()
    ie_options.attach_to_edge_chrome = True
    ie_options.edge_executable_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"

    # IEの動作を高速化するオプション
    ie_options.ignore_protected_mode_settings = True  # セキュリティゾーン設定を無視
    ie_options.ignore_zoom_level = True  # ズームレベルのチェックを無視
    ie_options.require_window_focus = True  # ウィンドウフォーカスを強制
    ie_options.native_events = False  # ネイティブイベントを無効化（パフォーマンス改善）
    ie_options.introduce_flakiness_by_ignoring_security_domains = True  # セキュリティ設定の影響を無視

    driver = webdriver.Ie(service=service, options=ie_options)

    # 画面表示内容の固定化
    driver.execute_script("document.body.style.zoom='100%'")
    driver.execute_script("window.scrollTo(0, 0);")
    driver.set_window_size(600, 1200)
    
    # webを表示
    driver.get(url)
    
    return driver