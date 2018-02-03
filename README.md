
# How this works

## Installation

- Install `rbenv` (+ `rbenv-install`)
- Install a recent version of ruby `rbenv install ...`
- Install jekyll `gem install jekyll`
- Build the jekyll page package
  - `cd ./source`
  - `bundle install`: this will download all dependencies

## Building the site

- For building just once: `bundle exec jekyll build`
- For continuous builds: `bundle exec jekyll build --watch`
- For deploying a dev server: `bundle exec jekyll serve --incremental`

## Adding new slides (to be automated)

Assuming the presentation is already online through the `slides-content` repository
and has the following path `slides-content/madrid-presentation-18`, create a new file
inside `source/_posts/slides/` with the name `YYYY-MM-DD-madrid-presentation-18.md`.

```yaml
---
layout: archive
title: "Superpresentation"
categories: slides
share: true
excerpt: "Presentation given in Madrid for whatever purposes"
slide-name: madrid-presentation-18
image:
  teaser: /teasers/antwerp-gender-14-400x250.jpg
---
```

This assumes that there is an teaser image inside `source/images/teasers/`. 
In order to create one, grab whatever image from the presentation `whatever-image.png` 
and use `mogrify` to create the teaser:

	`mogrify -resize 400x250 -extent 400x250 -background white -gravity center -format png -path source/images/teasers/ path/to/whatever-image.png`

## rsyncing to ./page and pushing

Since we are using some jekyll plugins that are not run automatically by github,
we need to push the built site to gh-pages (site would be otherwise build by github
but we need the fancy packages). Once the site has been built locally 
(see "Building the site"), we use rsync to update the changes to `./page`.
For convenience, there is a script in `./page/scripts/` `update.sh` that does it.
It has to be run from within `./page/`

Once it's run, just `git add --all & git commit -m added & git push`.
