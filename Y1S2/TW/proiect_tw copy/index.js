const express = require("express");
app = express();

app.set("view engine", "ejs");

app.use("/resources", express.static(__dirname+"/resources"));

app.get(["/","/home","/home"], function(req, res) {
    res.render("pages/home");
});

app.get("/*", function(req, res) {
    console.log(req.url);
    res.render("pages" + req.url, function(err, renderRes) {
        if(err) {
            if(err.message.startsWith("Failed to lookup view")) {
                res.render("pages/error_404");
            }
        }
        else {
            res.send(renderRes);
        }
    });
});

app.listen(8888);
console.log("Serverul a pornit!");