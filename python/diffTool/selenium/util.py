from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.ie.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import os
import time
from selenium.webdriver.remote.webdriver import WebDriver
from PIL import Image

from main import screenshot_enabled
from main import output_dir

# カウンター変数（シナリオ全体で共有）
_screenshot_counter = 1

def reset_screenshot_counter():
    """
    スクリーンショットのカウンターをリセットする。
    新しいシナリオを開始する際に呼び出す。
    """
    global _screenshot_counter
    _screenshot_counter = 1


def take_screenshot(driver: WebDriver, base_filename: str,
                     full_page: bool = False, delay: int = 0, width: int = 1920, height: int = 1080):
    """
    Seleniumを利用してスクリーンショットを取得する関数。
    自動的に連番を付与し、カウンターを増加させる。

    Args:
        driver (WebDriver): SeleniumのWebDriverインスタンス
        base_filename (str): 基本ファイル名（連番付きのスクリーンショット名を生成）
        full_page (bool, optional): Trueの場合、ページ全体のスクリーンショットを撮る. Defaults to False.
        delay (int, optional): スクリーンショット取得前の待機時間（秒）. Defaults to 0.
        width (int, optional): 固定化するブラウザの横幅. Defaults to 1920.
        height (int, optional): 固定化するブラウザの高さ. Defaults to 1080.

    Returns:
        str: 保存したスクリーンショットのフルパス
    """

    global _screenshot_counter
    if not screenshot_enabled:
        return

    os.makedirs(output_dir, exist_ok=True)  # ディレクトリ作成（存在しない場合）

    # 連番付きのファイル名を決定
    filename = f"{_screenshot_counter:02d}_{base_filename}.png"
    filepath = os.path.join(output_dir, filename)

    # カウンターを増加
    _screenshot_counter += 1

    # 必要に応じて待機
    if delay > 0:
        time.sleep(delay)

    # **画面サイズを統一**
    driver.set_window_size(width, height)

    # **ズーム倍率・スクロール位置の統一**
    WebDriverWait(driver, 10).until(lambda d: d.execute_script("return document.body !== null"))
    driver.execute_script("document.body.style.zoom='100%'")
    driver.execute_script("window.scrollTo(0, 0);")

    if full_page:
        screenshot_full_page(driver, filepath, width, height)
    else:
        driver.save_screenshot(filepath)

    print(f"スクリーンショットを保存しました: {filepath}")
    return filepath


def screenshot_full_page(driver: WebDriver, filepath: str, width: int, height: int):
    """
    フルページのスクリーンショットを取得する（スクロール処理を含む）

    Args:
        driver (WebDriver): SeleniumのWebDriverインスタンス
        filepath (str): 保存するスクリーンショットのフルパス
        width (int): ブラウザの横幅
        height (int): ブラウザの高さ
    """
    total_width = driver.execute_script("return document.body.scrollWidth")
    total_height = driver.execute_script("return document.body.scrollHeight")

    driver.set_window_size(width, height)  # 高さは固定し、横幅を調整

    stitched_image = Image.new("RGB", (total_width, total_height))
    scroll_position = 0
    screenshot_parts = []

    while scroll_position < total_height:
        driver.execute_script(f"window.scrollTo(0, {scroll_position});")
        time.sleep(0.3)  # 画面のレンダリング待機
        temp_screenshot = f"{filepath}_part.png"
        driver.save_screenshot(temp_screenshot)
        screenshot_parts.append((scroll_position, temp_screenshot))
        scroll_position += height  # 画面高さ分スクロール

    # 画像を結合
    for pos, img_path in screenshot_parts:
        part_img = Image.open(img_path)
        stitched_image.paste(part_img, (0, pos))

    stitched_image.save(filepath)
    print(f"フルページスクリーンショットを保存しました: {filepath}")

    # 一時ファイル削除
    for _, img_path in screenshot_parts:
        os.remove(img_path)

# フレーム内の全ての name を持つ要素 + 表示されているテキストを取得
def list_named_elements(driver: WebDriver, depth=0):
    elements = driver.find_elements(By.XPATH, "//*[@name]")  # name 属性を持つ要素を取得
    text_elements = driver.find_elements(By.XPATH, "//*[text() and not(self::script or self::style)]")  # 表示テキストを持つ要素を取得

    if elements:
        print(f"{'  ' * depth}見つかった name 要素の数: {len(elements)}")
        for index, elem in enumerate(elements):
            try:
                # name 属性を取得
                name = driver.execute_script("return arguments[0].name;", elem)
                if not name:
                    name = "[取得不可]"

                # タグ名を取得
                tag = elem.tag_name or "[取得不可]"

                # value を取得（input, select の場合）
                value = "[なし]"
                if tag == "input":
                    value = driver.execute_script("return arguments[0].value;", elem) or "[なし]"

                print(f"{'  ' * depth}  name[{index}]: tag='{tag}', name='{name}', value='{value}'")
            except Exception as e:
                print(f"{'  ' * depth}  name[{index}]: [取得不可] ({e})")

    if text_elements:
        print(f"{'  ' * depth}見つかった画面テキストの数: {len(text_elements)}")
        for index, elem in enumerate(text_elements):
            try:
                text = elem.text.strip()
                tag = elem.tag_name or "[取得不可]"
                if text:  # 空白文字のみのものを除外
                    print(f"{'  ' * depth}  text[{index}]: tag='{tag}', text='{text}'")
            except Exception as e:
                print(f"{'  ' * depth}  text[{index}]: [取得不可] ({e})")

# フレーム一覧を取得し、各フレーム内の name 要素と画面テキストも出力する（再帰）
def list_frames_and_named_elements(driver, depth=0):
    frames = driver.find_elements(By.TAG_NAME, "frame")  # すべての frame を取得
    iframes = driver.find_elements(By.TAG_NAME, "iframe")  # すべての iframe も取得
    all_frames = frames + iframes  # frame と iframe を統合

    print(f"{'  ' * depth}見つかったフレームの数: {len(all_frames)}")

    # 現在のフレーム内の name 要素 + 画面テキストを表示
    list_named_elements(driver, depth)

    for index, frame in enumerate(all_frames):
        try:
            # get_attribute("name") の代わりに JavaScript で name を取得
            name = driver.execute_script("return arguments[0].name;", frame)
            if not name:
                name = "[No Name]"
        except:
            name = "[取得不可]"

        print(f"{'  ' * depth}フレーム[{index}]: name='{name}'")

        # フレームに切り替えて再帰的に探索
        driver.switch_to.frame(frame)
        list_frames_and_named_elements(driver, depth + 1)
        driver.switch_to.parent_frame()  # 元のフレームに戻る