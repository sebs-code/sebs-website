AUTHOR = 'Sebastian David Lees'
SITENAME = 'Sebastian David Lees Professional & Personal Home Page'
SITEURL = 'https://sebs.website'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Dirct HTML pages
DIRECT_TEMPLATES = ['index', 'about', 'photography']

# TODO: for if I want to add articles in future
# DIRECT_TEMPLATES = ['index', 'about', 'articles', 'photography']
# PAGINATED_DIRECT_TEMPLATES = ['articles']

#  Slugs
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
CATEGORY_URL = "category/{slug}/"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Theme
THEME = 'theme'