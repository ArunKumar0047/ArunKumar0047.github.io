import datetime

AUTHOR = 'Arunkumar'
SITENAME = 'Arunkumar M'
SITEURL = ''

# Path to content, pages, and theme
PATH = 'content'
PAGE_PATHS = ['pages']
THEME = 'theme'

TIMEZONE = 'Europe/Rome'
DEFAULT_LANG = 'en'

# Add the current year to the context
YEAR = datetime.date.today().year

# URL and save paths for articles and pages
ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

# Define the navigation menu for the single-page layout
MENUITEMS = (
    ('About', '#about'),
    ('Experience', '#experience'),
    ('Education', '#education'),
    ('Projects', '#projects'),
    ('Blogs', '#blogs'),
    ('Contact', '#contact'),
)

# We want a dedicated page for all blog posts
DIRECT_TEMPLATES = ['index', 'blog']
BLOG_SAVE_AS = 'blog.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
