var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/*', function(req, res, next) {
    console.log(req.params)
    res.render('Problem' + req.params[0]);
});

module.exports = router;
