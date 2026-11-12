source "https://rubygems.org"

# Local preview:  bundle install && bundle exec jekyll serve
gem "jekyll", "~> 3.9"

# Using GitHub Pages' own build instead? Comment the line above and use this one:
# gem "github-pages", group: :jekyll_plugins

group :jekyll_plugins do
  gem "jekyll-seo-tag", "~> 2.6"
  gem "jekyll-sitemap", "~> 1.3", "< 1.4"
  gem "kramdown-parser-gfm", "~> 1.1.0"
end

gem "webrick", "~> 1.7"   # needed on Ruby 3+

# Windows and JRuby do not include zoneinfo files
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end
gem 'wdm', '>= 0.1.1'
gem 'base64'
gem 'bigdecimal'