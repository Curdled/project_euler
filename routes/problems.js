var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/*', function(req, res, next) {
    res.render('problem_' + req.params[0]);
});

module.exports = router;
