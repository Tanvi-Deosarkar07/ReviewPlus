from google_play_scraper import reviews

def get_reviews(app_id='com.duolingo', count=100):
    result, _ = reviews(app_id, lang='en', country='us', count=count)
    return [r['content'] for r in result if r['content']]