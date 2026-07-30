# -*- coding: utf-8 -*-
"""ふく冷蔵庫アプリの共有用アセット生成（アイコン・OGP画像）"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

BG = (250, 243, 227)
INK = (31, 42, 68)
ACCENT = (76, 160, 90)
SUB = (120, 110, 90)
FONT_PATH = r"C:\Windows\Fonts\meiryob.ttc"
OUT = Path(__file__).parent


def font(size):
    return ImageFont.truetype(FONT_PATH, size)


def draw_frog(d, cx, cy, r):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=ACCENT)
    er = r * 0.34
    for dx in (-r * 0.45, r * 0.45):
        d.ellipse([cx + dx - er, cy - r * 0.75 - er, cx + dx + er, cy - r * 0.75 + er], fill=ACCENT)
        wr = er * 0.62
        d.ellipse([cx + dx - wr, cy - r * 0.78 - wr, cx + dx + wr, cy - r * 0.78 + wr], fill=(255, 255, 255))
        pr = wr * 0.45
        d.ellipse([cx + dx - pr, cy - r * 0.74 - pr, cx + dx + pr, cy - r * 0.74 + pr], fill=(20, 20, 20))
    d.arc([cx - r * 0.45, cy - r * 0.1, cx + r * 0.45, cy + r * 0.55], 20, 160,
          fill=(20, 60, 30), width=max(3, int(r * 0.08)))


def gen_icon(size, out):
    img = Image.new("RGB", (size, size), BG)
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, size - 1, size - 1], radius=size * 0.18, outline=ACCENT, width=max(4, size // 30))
    draw_frog(d, size / 2, size / 2, size * 0.32)
    img.save(out)
    print("saved:", out)


def gen_og():
    W, H = 1200, 630
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W - 1, H - 1], outline=ACCENT, width=14)
    draw_frog(d, 220, H / 2, 130)
    d.text((400, 210), "ふく冷蔵庫", font=font(90), fill=INK, anchor="lm")
    d.text((400, 320), "在庫・レシート・レシピ提案をスマホで", font=font(38), fill=SUB, anchor="lm")
    d.text((400, 380), "自炊記録を手軽に続けるための個人アプリ", font=font(38), fill=SUB, anchor="lm")
    img.save(OUT / "og-image.png")
    print("saved: og-image.png")


if __name__ == "__main__":
    gen_icon(192, OUT / "icon-192.png")
    gen_icon(512, OUT / "icon-512.png")
    gen_og()
