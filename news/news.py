class News:
    def __init__(self, url):
        self.url = url

    def clean_article_text(self, paragraphs):
        cleaned_text = []
        for p in paragraphs:
            p_text = p.get_text().strip()
            cleaned_text.append(p_text)
        return " ".join(cleaned_text)

    def fetch_news(self):
        pass
