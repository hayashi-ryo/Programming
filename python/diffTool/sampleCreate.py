import os
from PIL import Image, ImageDraw, ImageFont

# 出力ディレクトリの作成
before_dir = "before"
after_dir = "after"
os.makedirs(before_dir, exist_ok=True)
os.makedirs(after_dir, exist_ok=True)

# 画像サイズ
img_size = (600, 400)

# フォント設定
def get_font(font_size=20):
    try:
        font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Linux環境
        return ImageFont.truetype(font_path, font_size)
    except IOError:
        return ImageFont.load_default()

# ベース画像（表とボタンを含む）
def create_base_image(output_path, table_offset=50, text_variation=False, button_variation=False):
    img = Image.new("RGB", img_size, "white")
    draw = ImageDraw.Draw(img)
    font = get_font(20)  # フォントを関数内で定義

    # タイトル
    draw.text((20, 20), "Comparison Test Image", fill="black", font=font)

    # 表の位置
    table_x, table_y = 50, table_offset  # table_offsetで位置をずらせる

    # 表の枠線
    cell_width, cell_height = 150, 40
    for i in range(4):
        for j in range(3):
            x1, y1 = table_x + j * cell_width, table_y + i * cell_height
            x2, y2 = x1 + cell_width, y1 + cell_height
            draw.rectangle([x1, y1, x2, y2], outline="black", width=2)

    # 表のテキスト（変更可能）
    base_text = [["Item A", "Item B", "Item C"], ["10", "20", "30"], ["40", "50", "60"], ["70", "80", "90"]]
    alt_text = [["Product A", "Product B", "Product C"], ["100", "200", "300"], ["400", "500", "600"], ["700", "800", "900"]]

    text_matrix = alt_text if text_variation else base_text

    for i, row in enumerate(text_matrix):
        for j, text in enumerate(row):
            draw.text((table_x + j * cell_width + 10, table_y + i * cell_height + 10), text, fill="black", font=font)

    # ボタン（変更可能）
    button_x, button_y = 200, 300
    button_text = "Submit" if not button_variation else "Confirm"

    draw.rectangle([button_x, button_y, button_x + 200, button_y + 50], outline="black", width=3)
    draw.text((button_x + 60, button_y + 15), button_text, fill="black", font=font)

    img.save(output_path)

# `before` フォルダにオリジナルの画像を保存
create_base_image(os.path.join(before_dir, "image_1.png"))  # 基準画像1
create_base_image(os.path.join(before_dir, "image_2.png"))  # 基準画像2
create_base_image(os.path.join(before_dir, "image_3.png"))  # 基準画像3
create_base_image(os.path.join(before_dir, "image_4.png"))  # 基準画像4

# `after` フォルダに変更後の画像を保存
create_base_image(os.path.join(after_dir, "image_1.png"), table_offset=100)  # 表の位置変更
create_base_image(os.path.join(after_dir, "image_2.png"), text_variation=True)  # テキスト変更
create_base_image(os.path.join(after_dir, "image_3.png"), button_variation=True)  # ボタン変更
create_base_image(os.path.join(after_dir, "image_4.png"))  # 差分なし

# 作成した画像のリストを表示
created_files_before = os.listdir(before_dir)
created_files_after = os.listdir(after_dir)

created_files_before, created_files_after
