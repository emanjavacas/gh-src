
import sys
import os
import argparse
import shutil
import datetime
from subprocess import call


TEMPLATE = """---
layout: archive
title: "{title}"
categories: slides
excerpt: "{excerpt}"
slide-name: {slide}
image:
  teaser: /teasers/{thumbfile}
---
"""


CONVERT = "convert {path} -thumbnail {dims}^ " + \
          "-gravity center -extent {dims} {outfile}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--title', required=True)
    parser.add_argument('--excerpt', required=True)
    parser.add_argument('--slide', required=True)
    parser.add_argument('--image_path', required=True)
    parser.add_argument('--root', default='./')
    parser.add_argument('--dims', default='400x250')

    args = parser.parse_args()

    # create thumbnail
    if not os.path.exists(args.image_path):
        raise ValueError("Couldn't find file {}".format(args.image_path))
    if shutil.which("convert") is None:
        raise ValueError("Looks like ImageMagick is not installed")
    ext = args.image_path.split(".")[-1]
    thumbfile = "{slide}-{dims}.{ext}".format(
        slide=args.slide, dims=args.dims, ext=ext)
    outfile = os.path.join(args.root, "images", "teasers", thumbfile)
    if os.path.exists(outfile):
        print("Thumbnail already exists.")
    ans = input("Create thumbnail {}? (y/n) ".format(outfile))
    while ans not in ('y', 'n'):
        ans = input("Please answer 'y' or 'n'")
    if ans == 'n':
        print("Goodbye")
        sys.exit(0)

    call(CONVERT.format(path=args.image_path, dims=args.dims, outfile=outfile),
         shell=True)

    # create entry
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    slidefile = '{today}-{slide}.md'.format(today=today, slide=args.slide)
    outfile = os.path.join(args.root, '_posts', 'slides', slidefile)

    with open(outfile, 'w+') as f:
        f.write(TEMPLATE.format(
            title=args.title,
            excerpt=args.excerpt,
            slide=args.slide,
            thumbfile=thumbfile))
