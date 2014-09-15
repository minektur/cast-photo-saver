// fire up cast receiver, if we detect we're being called by a chromecast
function init() {
    if (navigator.userAgent.indexOf("CrKey") > -1) {
        window.castReceiverManager = cast.receiver.CastReceiverManager.getInstance();
        //castReceiverManager.start({maxInactivity: 600});
        window.castReceiverManager.start();
    }
    new_img();
    setInterval('new_img();',12000);
}

// load up the next img  - the random get-query string is to break caching
//  each time you hit /img you get a new image
function new_img() {
    var one = document.getElementById('one');
    var newbg = "url('/img?{0}')".replace('{0}', Math.random());
    one.style.backgroundImage=newbg;
}

