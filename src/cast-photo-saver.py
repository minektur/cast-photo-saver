#!/usr/bin/env python
""" Simple Background Photo Screen-Saver for Chromecast. """
# pylint doesn't like good command-line names
#pylint: disable=invalid-name

import os
import imghdr
import bottle
import random
# import daemon

PICS = u"/Users/fred/Pictures/iPhoto Library/Masters"
DOCROOT = u'www'


def dir_file_list():
    """ make a list of directories that have files in them in PICS """
    showlist = []
    for root, _, files, in os.walk(PICS):
        if files:
            showlist.append((root, files))
    return showlist


def rand_img_gen(showlist=None):
    """ make a generator that finds directories, randomizes the order,
        and returns pics from those directories one at a time """
    while True:
        if not showlist:
            showlist = dir_file_list()
            random.shuffle(showlist)
        while showlist:
            path, files = showlist.pop()
            for img in files:
                ftype = imghdr.what(os.path.join(path, img))
                if ftype not in ['gif', 'jpeg', 'png', 'bmp']:
                    continue
                yield (path, img)

RAND_IMG = rand_img_gen()


@bottle.route('/img')
def send_img():
    """ file-route to serve a randomish pic from PICS """
    path, fname = RAND_IMG.next()
    resp = bottle.static_file(fname, path)
    # anti-cache headers as seen at:
    # http://stackoverflow.com/questions/9884513/avoid-caching-of-the-http-responses
    bottle.response.set_header('Expires', 'Tue, 03 Jul 2001 06:00:00 GMT')
    bottle.response.set_header('Last-Modified', '{now} GMT')
    bottle.response.set_header('Cache-Control',
                               'no-store, no-cache, must-revalidate, max-age=0')
    bottle.response.set_header('Cache-Control', 'post-check=0, pre-check=0')
    bottle.response.set_header('Pragma', 'no-cache')
    return resp


@bottle.route('/')
@bottle.route('/index.html')
def send_index():
    """ file-route to handle / and index.html """
    return bottle.static_file('index.html', '.')


@bottle.route('/app.js')
def send_appjs():
    """ file route for app.js """
    return bottle.static_file('app.js', '.')


def main():
    """ startup and deamonization """
    os.chdir(DOCROOT)
    # with daemon.DaemonContext():
    bottle.run(host='', port=8000)


if __name__ == "__main__":
    main()
