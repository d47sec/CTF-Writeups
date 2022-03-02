var hash = window.location.hash.substr(1);
var result = hash.split("&").reduce(function(e, t) {
    var n = t.split("=");
    return e[n[0]] = n[1], e
}, {});
var tracking = JSON.stringify(result);
var who = (tracking = JSON.parse(tracking)).who;

function editProfile(e) {
    var t = new XMLHttpRequest;
    t.open("POST", "api/action.php?act=editbio", !0), t.setRequestHeader("Content-Type", "application/x-www-form-urlencoded"), t.setRequestHeader("X-SAFEPROTECTION", "enNlYW5vb2Zjb3Vyc2U="), t.onreadystatechange = function() {
        this.readyState === XMLHttpRequest.DONE && this.status
    }, t.send("bio=" + encodeURI(msg))
}

function retrieveEmail(e) {
    var t = new XMLHttpRequest;
    t.open("GET", "api/action.php?act=getemail", !0), t.setRequestHeader("X-SAFEPROTECTION", "enNlYW5vb2Zjb3Vyc2U="), t.onreadystatechange = function() {
        this.readyState === XMLHttpRequest.DONE && this.status
    }, t.send()
}

function sendFeedback(e) {
    e = btoa(e);
    var t = new XMLHttpRequest;
    t.open("POST", "api/feedback.php", !0), t.setRequestHeader("Content-Type", "application/x-www-form-urlencoded"), t.onreadystatechange = function() {
        this.readyState === XMLHttpRequest.DONE && 200 === this.status && (top.location.href = "index.php?msg=Thanks, your feedback has been received. We appreciate you sharing your feedback.")
    }, t.send(e)
}

function reportUsera(e, t) {
    t = btoa(t);
    var n = new XMLHttpRequest;
    n.open("POST", "api/action.php?act=report", !0), n.setRequestHeader("Content-Type", "application/x-www-form-urlencoded"), n.onreadystatechange = function() {
        this.readyState === XMLHttpRequest.DONE && 200 === this.status && (top.location.href = "index.php?msg=Thanks, your report has been received. You can view your report by clicking 'report user' again.")
    }, n.send("username=" + e + "&msg=" + t)
}

function addComment(e) {
    var t = new XMLHttpRequest;
    t.open("POST", "api/action.php?act=comment", !0), t.setRequestHeader("Content-Type", "application/x-www-form-urlencoded"), t.onreadystatechange = function() {
        this.readyState === XMLHttpRequest.DONE && 200 === this.status && (top.location.href = "index.php")
    }, t.send("msg=" + encodeURI(e))
}
1 == who.includes("zsh1") && document.write("<img src=/1x1.gif?" + decodeURI(who) + "></img>");