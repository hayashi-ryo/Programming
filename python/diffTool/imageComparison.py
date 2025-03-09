import os
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim
from fpdf import FPDF

def get_image_pairs(dir1, dir2):
    files1 = set(os.listdir(dir1))
    files2 = set(os.listdir(dir2))
    common_files = sorted(files1.intersection(files2))
    return [(os.path.join(dir1, f), os.path.join(dir2, f)) for f in common_files if f.endswith(('.png', '.jpg', '.jpeg'))]

def compare_images(img1_path, img2_path):
    img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)

    if img1.shape != img2.shape:
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    score, diff = ssim(img1, img2, full=True)
    diff = (diff * 255).astype(np.uint8)
    edge_diff = cv2.absdiff(cv2.Canny(img1, 50, 150), cv2.Canny(img2, 50, 150))
    _, thresh = cv2.threshold(edge_diff, 30, 255, cv2.THRESH_BINARY)
    kernel = np.ones((5,5), np.uint8)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    img_diff = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)

    valid_contours = [c for c in contours if cv2.contourArea(c) > 100]
    changed_cells = [(cv2.boundingRect(c)) for c in valid_contours if cv2.boundingRect(c)[3] > 15 and cv2.boundingRect(c)[2] > 30]
    num_text_changes = len(changed_cells)
    avg_text_change_area = sum(w * h for _, _, w, h in changed_cells) / (num_text_changes or 1)
    for x, y, w, h in changed_cells:
        cv2.rectangle(img_diff, (x, y), (x+w, y+h), (255, 0, 0), 2)

    output_dir = "output/difference_images"
    os.makedirs(output_dir, exist_ok=True)
    diff_image_path = f"{output_dir}/diff_{os.path.basename(img1_path)}"
    cv2.imwrite(diff_image_path, img_diff)
    
    heatmap_path = f"{output_dir}/heatmap_{os.path.basename(img1_path)}"
    plt.figure(figsize=(6, 4))
    plt.imshow(thresh, cmap='hot', interpolation='nearest')
    plt.colorbar()
    plt.title(f"Heatmap: {os.path.basename(img1_path)}")
    plt.savefig(heatmap_path)
    plt.close()

    return score, num_text_changes, avg_text_change_area, diff_image_path, heatmap_path

def generate_pdf_report(html_file, pdf_file):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=10)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    with open(html_file, "r", encoding="utf-8") as f:
        for line in f:
            pdf.cell(200, 10, txt=line.strip(), ln=True)
    
    pdf.output(pdf_file)

def generate_reports(results):
    results.sort()
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    
    summary_html = f"summary_report.html"
    detailed_html = f"detailed_report.html"
    summary_pdf = f"{output_dir}/summary_report.pdf"
    detailed_pdf = f"{output_dir}/detailed_report.pdf"
    
    # HTML レポート作成
    with open(summary_html, 'w') as f:
        f.write("<html><head><title>Summary Report</title></head><body>")
        f.write("<h2>Summary Report</h2>")
        f.write("<table border='1'><tr><th>Image Name</th><th>Differences Detected</th><th>Difference Preview</th></tr>")
        for img_name, score, changes, area, diff_path, _ in results:
            diff_status = "Yes" if changes > 0 else "No"
            diff_preview = f"<img src='{diff_path}' width='150'>" if changes > 0 else "-"
            f.write(f"<tr><td>{img_name}</td><td>{diff_status}</td><td>{diff_preview}</td></tr>")
        f.write("</table></body></html>")
    
    with open(detailed_html, 'w') as f:
        f.write("<html><head><title>Detailed Report</title></head><body>")
        f.write("<h2>Detailed Report</h2>")
        f.write("<table border='1'><tr><th>Image Name</th><th>Original</th><th>Modified</th><th>Difference</th><th>Heatmap</th></tr>")
        for img_name, _, _, _, diff_path, heatmap_path in results:
            f.write(f"<tr><td>{img_name}</td>")
            f.write(f"<td><img src='before/{img_name}' width='150'></td>")
            f.write(f"<td><img src='after/{img_name}' width='150'></td>")
            f.write(f"<td><img src='{diff_path}' width='150'></td>")
            f.write(f"<td><img src='{heatmap_path}' width='150'></td></tr>")
        f.write("</table></body></html>")
    
    # HTML を PDF に変換
    generate_pdf_report(summary_html, summary_pdf)
    generate_pdf_report(detailed_html, detailed_pdf)

def main():
    dir1 = "before/"
    dir2 = "after/"
    print(f"選択されたディレクトリ: \n1: {dir1}\n2: {dir2}")
    image_pairs = get_image_pairs(dir1, dir2)
    results = []
    os.makedirs("output", exist_ok=True)
    
    for img1, img2 in image_pairs:
        score, num_text_changes, avg_area, diff_path, heatmap_path = compare_images(img1, img2)
        results.append([os.path.basename(img1), score, num_text_changes, avg_area, diff_path, heatmap_path])
    
    generate_reports(results)
    print("レポートが生成されました: output/summary_report.html, output/detailed_report.html, output/summary_report.pdf, output/detailed_report.pdf")

if __name__ == "__main__":
    main()
