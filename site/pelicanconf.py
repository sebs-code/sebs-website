# Global site settings
AUTHOR = 'Sebastian David Lees'
SITENAME = 'Sebastian David Lees Professional & Personal Home Page'
SITEURL = 'https://sebs.website'
DEFAULT_LANG = 'en'
DELETE_OUTPUT_DIRECTORY = True
TIMEZONE = 'Europe/London'
DEFAULT_METADATA = {'Content-Type': 'text/html'}
DATE_FORMATS = {
    'en': '%b %d, %Y',
}

# Paths
THEME = 'theme/'
PATH = 'content/'
STATIC_PATHS = ['img/']
OUTPUT_PATH = 'output/'
DIRECT_TEMPLATES = ['index', 'about', 'blog', 'photography', 'talks-and-interviews']
PAGINATED_TEMPLATES = {'blog': None}
DEFAULT_PAGINATION = 15

# Supress Author and Category Generation
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''

# html content generation
USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'blog'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
TAG_SAVE_AS = "blog/{slug}.html"

# slugs
ARTICLE_URL = 'blog/{slug}'
TAG_URL = "blog/{slug}"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

