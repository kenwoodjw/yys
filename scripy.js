/**
 * Created by kenwood on 17-6-30.
 */
var http = require("http");
var https = require('https');
var mysql = require('mysql');
var arguments = process.argv.splice(2);
var start=arguments[0];
var end=arguments[1];
var connection = mysql.createConnection({
    host: 'localhost',
    user: 'user',
    password: '123456',
    database: 'test'
});

connection.connect();
for (let k = start; k <= end; k++) {
    var sql = '';
    var timestamp = Date.parse(new Date());
    var options = {
        host: 'comp-sync.webapp.163.com',
        path: '/g37/sync_paged_list?per_page=200&page=' + k + '&_=' + timestamp
    };
    https.get(options, function (res) {
        var json = '';
        res.on('data', function (d) {
            json += d;
        });
        res.on('end', function () {
            json = JSON.parse(json);
            for (var i in json) {
                var arr = [];
                var value = json[i];
                for (var j in value) {
                    var arr = [];
                    arr.push(value[j].get_time, value[j].prop_info.from, value[j].req_id, value[j].prop_info.prop_name.split("式神")[0], value[j].prop_info.prop_name.split("式神")[1], value[j].user_info.nick, value[j].user_info.server, value[j].user_info.uid);
                    sql = "insert into `yys` values ('" + value[j].req_id + "','" + value[j].get_time + "','" + value[j].prop_info.from + "','" + value[j].prop_info.prop_name.split("式神")[0] + "','" + value[j].prop_info.prop_name.split("式神")[1] + "','" + value[j].user_info.nick + "','" + value[j].user_info.server + "','" + value[j].user_info.uid + "');";
                    console.log(sql);
                    connection.query(sql, function (err, rows, fields) {
                        console.log(err);
                    });
                }
            }
        });
    });
}
