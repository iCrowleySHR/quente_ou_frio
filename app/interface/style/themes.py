from . import colors, fonts

THEME = {
    "window": {
        "bg": colors.BACKGROUND
    },
    "label_title": {
        "bg": colors.BACKGROUND,
        "fg": colors.TEXT,
        "font": fonts.TITLE_FONT
    },
    "label_text": {
        "bg": colors.BACKGROUND,
        "fg": colors.TEXT,
        "font": fonts.TEXT_FONT
    },
    "entry": {
        "bg": colors.SECONDARY,
        "fg": colors.TEXT,
        "insertbackground": colors.TEXT,
        "font": fonts.TEXT_FONT,
        "relief": "flat",
        "justify": "center",
        "width": 15
    },
    "button": {
        "bg": colors.ACCENT,
        "fg": colors.TEXT,
        "activebackground": colors.PRIMARY,
        "activeforeground": colors.TEXT,
        "font": fonts.BUTTON_FONT,
        "relief": "flat",
        "width": 12
    }
}
