"""Text-Overlay-Generator: Hintergrundbild + Hook-Text -> fertiges Bild-Post.

Kein KI-Bild-Look: nimmt ein echtes Foto (Petras Portrait oder ein
thematisch passendes Bild) und legt den Text typografisch darüber —
das klassische "Zitat-Karte"-Format, das im Feed funktioniert.

CLI:
    python render_image.py --background ../assets/images/petra-portrait.jpg \
        --text "Du verlierst dich nicht auf einmal." \
        --footer "Ich stand nie auf meiner eigenen Liste" \
        --out ../assets/output/beispiel.jpg

Als Modul:
    from render_image import render
    render(background_path, text, output_path, footer="Buchtitel")
"""
import argparse
import textwrap

from PIL import Image, ImageDraw, ImageFont

CANVAS_SIZE = (1080, 1350)  # 4:5, Instagram-Empfehlung
MARGIN = 90
MAX_TEXT_HEIGHT_RATIO = 0.55  # Textblock darf max. 55% der Bildhöhe einnehmen

FONT_CANDIDATES_BOLD = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
]
FONT_CANDIDATES_REGULAR = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
]


def _load_font(candidates: list, size: int) -> ImageFont.FreeTypeFont:
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    raise OSError(
        "Keine passende Schriftart gefunden. Auf Ubuntu/GitHub-Actions: "
        "'apt-get install fonts-dejavu-core' oder FONT_CANDIDATES_BOLD anpassen."
    )


def _cover_resize(image: Image.Image, size: tuple) -> Image.Image:
    """Skaliert + croppt zentriert, damit das Bild die Zielfläche exakt füllt."""
    target_w, target_h = size
    src_w, src_h = image.size
    scale = max(target_w / src_w, target_h / src_h)
    new_size = (round(src_w * scale), round(src_h * scale))
    image = image.resize(new_size, Image.LANCZOS)
    left = (image.width - target_w) // 2
    top = (image.height - target_h) // 2
    return image.crop((left, top, left + target_w, top + target_h))


def _wrap_and_fit(draw: ImageDraw.ImageDraw, text: str, max_width: int, max_height: int) -> tuple:
    """Findet die größte Schriftgröße, bei der der umgebrochene Text noch passt."""
    for size in range(96, 31, -4):
        font = _load_font(FONT_CANDIDATES_BOLD, size)
        avg_char_w = font.getlength("Mm") / 2 or 1
        wrap_width = max(1, int(max_width / avg_char_w))
        lines = textwrap.wrap(text, width=wrap_width, break_long_words=False, break_on_hyphens=False) or [text]
        line_height = font.getbbox("Mg")[3] + 14
        block_height = line_height * len(lines)
        widths = [draw.textlength(line, font=font) for line in lines]
        if block_height <= max_height and max(widths, default=0) <= max_width:
            return font, lines, line_height
    # Fallback: kleinste Größe, notfalls überlaufend
    font = _load_font(FONT_CANDIDATES_BOLD, 32)
    lines = textwrap.wrap(text, width=28, break_long_words=False, break_on_hyphens=False) or [text]
    return font, lines, font.getbbox("Mg")[3] + 14


def render(background_path: str, text: str, output_path: str, footer: str = None) -> None:
    base = Image.open(background_path).convert("RGB")
    base = _cover_resize(base, CANVAS_SIZE)

    # Dunkler Verlauf von der Mitte nach unten, damit der Text immer lesbar ist,
    # unabhängig vom Hintergrundbild.
    gradient = Image.new("L", (1, CANVAS_SIZE[1]), color=0)
    for y in range(CANVAS_SIZE[1]):
        fade_start = CANVAS_SIZE[1] * 0.35
        if y < fade_start:
            alpha = 0
        else:
            alpha = int(200 * (y - fade_start) / (CANVAS_SIZE[1] - fade_start))
        gradient.putpixel((0, y), min(alpha, 200))
    gradient = gradient.resize(CANVAS_SIZE)
    overlay = Image.new("RGBA", CANVAS_SIZE, (0, 0, 0, 0))
    overlay.putalpha(gradient)
    base = Image.alpha_composite(base.convert("RGBA"), overlay)

    draw = ImageDraw.Draw(base)
    max_width = CANVAS_SIZE[0] - 2 * MARGIN
    max_height = int(CANVAS_SIZE[1] * MAX_TEXT_HEIGHT_RATIO)
    font, lines, line_height = _wrap_and_fit(draw, text, max_width, max_height)

    block_height = line_height * len(lines)
    y = CANVAS_SIZE[1] - MARGIN - block_height
    if footer:
        y -= 60  # Platz für die Fußzeile lassen

    for line in lines:
        width = draw.textlength(line, font=font)
        x = (CANVAS_SIZE[0] - width) / 2
        draw.text((x, y), line, font=font, fill="white")
        y += line_height

    if footer:
        footer_font = _load_font(FONT_CANDIDATES_REGULAR, 34)
        footer_text = footer.upper()
        width = draw.textlength(footer_text, font=footer_font)
        x = (CANVAS_SIZE[0] - width) / 2
        draw.text((x, CANVAS_SIZE[1] - MARGIN - 10), footer_text, font=footer_font, fill=(230, 230, 230))

    base.convert("RGB").save(output_path, "JPEG", quality=92)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bild + Text-Overlay rendern")
    parser.add_argument("--background", required=True)
    parser.add_argument("--text", required=True)
    parser.add_argument("--footer", default=None)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    render(args.background, args.text, args.out, footer=args.footer)
    print(f"Gespeichert: {args.out}")
