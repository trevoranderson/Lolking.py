var request = require('request');
var _ = require('lodash');
var summonerName = "a single hat";
var idgetter = "http://www.lolking.net/search?name=" + summonerName.split(" ").join("") + "&region=na";
request.get(idgetter, function (e, r) {
    var sid = r.request.href.split("/").pop();
    var matchgetter = "http://www.lolking.net/summoner/na/" + sid + "#matches";
    request.get(matchgetter, function (e, r, b) {
        var history = JSON.parse(b.split("var history = ")[1].split(";\n")[0]);
        var names = _.flatten(_.map(history,function (o) { return o.match.teammates.concat(o.match.opponents.concat([o.match.summoner])); }).map(function (o) { return o.map(function (o) { return o.name; }); }));
        var counts = _.countBy(names);
        _.forOwn(counts, function (v, k) {
            if (v > 1) {
                console.log(k + " : " + v);
            }
        });
        while (1) { }
    });
});