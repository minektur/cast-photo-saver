cast-photo-saver
================

photo screen saver for chromecast


##fixme

# Setup
To use this you'll need a chromecast developer account.


See: <https://developers.google.com/cast/docs/developers#Get_started>

You'll need to put one of your devices in development mode and set up a test development app.

See: <https://developers.google.com/cast/docs/registration>


At [This Screen](https://cast.google.com/publish/#/overview)  you will first add a new test device then add a new application.

Pick whatever name you want and a custom receiver URL that should be:

`http://192.168.0.100:8000/index.html`

Replacing that IP address with whatever server you will be sharing your images from.  That server is also where you git-clone this project to, make a virtualenv and install dependencies and run the app from. Remember your google-assigned app-id for later.


On the local machine do whatever your platform equivalent of these commands is (e.g. I do approx this on my mac)

    git clone https://github.com/minektur/cast-photo-saver.git
    virtualenv cast-photo-saver
    cd cast-photo-saver
    . bin/activate
    pip install -r requirements.txt

edit `src/cast-photo-saver.py` and change `PICS` to point to wherever your giant nested folder of pictures lives.
(Note you can move the base www document root here also if you want)


edit `src/startme.py` to put in your chromecast IP address and your chrome app ID from before.


run the server and start the cast app:

    cd src
    ./cast-photo-saver.py > /dev/null &
    ./startme.py

Enjoy.



The performance of the cast device on (non-hardware-accelerated) CSS transforms leaves a lot to be desired.  I'm planning on
changing the html/javascript to make transitions nicer in some way.  Or not... 



Ideas:

* performance/CSS limitations
  * split work up
    - load-offscreen early
    - transition in way after loading?
  * opacity changes instead?
  * javascript instead of css?
  * transcode images to lower res on the fly
  * load pre-rendered html5 snippets?
  * turn the whole thing into hardware accelerated stream?
  * 3d transforms?
  * requestanimationframe magic on my own?
  * see <https://plus.google.com/110558071969009568835/posts/NMDm5mDhm6J> for more ideas
  * <http://www.paulirish.com/2012/why-moving-elements-with-translate-is-better-than-posabs-topleft/>
  * non-video elements restricted to 720P  <https://plus.google.com/u/0/+AlbinEkblom/posts/JDhtJTw7jz5>

  

## still left to do 
  * autostart of cast app (startme integration)
  * daemonization
  * config file/command line options
  * maybe? move to control over cast channel
  * use pychromecast to auto-detect device by name

##license
See LICENSE file for details.  MIT/Beerware in general

Proto file for chromecast protobuf format MIT license from Chromium source repo
