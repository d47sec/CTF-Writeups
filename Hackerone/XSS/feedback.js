function sendFeedback(e) {
    e = btoa(e);
    var t = new XMLHttpRequest;
    t.open("POST", "/api/feedback.php", !0), t.setRequestHeader("Content-Type", "application/x-www-form-urlencoded"), t.onreadystatechange = function() {
        this.readyState === XMLHttpRequest.DONE && 200 === this.status && (top.location.href = "/index.php?msg=Thanks, your feedback has been received. We appreciate you sharing your feedback.")
    }, t.send(e)
}

function reportUsera(e, t) {
    t = btoa(t);
    var n = new XMLHttpRequest;
    n.open("POST", "/api/action.php?act=report", !0), n.setRequestHeader("Content-Type", "application/x-www-form-urlencoded"), n.onreadystatechange = function() {
        this.readyState === XMLHttpRequest.DONE && 200 === this.status && (top.location.href = "/index.php?msg=Thanks, your report has been received. You can view your report by clicking 'report user' again.")
    }, n.send("username=" + e + "&msg=" + t)
}

function addComment(e) {
    var t = new XMLHttpRequest;
    t.open("POST", "/api/action.php?act=comment", !0), t.setRequestHeader("Content-Type", "application/x-www-form-urlencoded"), t.onreadystatechange = function() {
        this.readyState === XMLHttpRequest.DONE && 200 === this.status && (top.location.href = "/index.php")
    }, t.send("msg=" + encodeURI(e))
}