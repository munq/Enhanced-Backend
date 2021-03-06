const path = require('path');
const logger = require('morgan');
const cookieParser = require('cookie-parser');
const bodyParser = require('body-parser');
const express = require('express');
const routes = require('./routes');
const API = require('../api');
const Player = require('../player');
const config = require('../config');

function initializeLocals(app) {
  app.locals.mapCells = []; // not const
  app.locals.authInfo = null;
  app.locals.nearbyPokemons = [];
  app.locals.apiEndpoint = null;
  app.locals.player = new Player();
  app.locals.pokemons = [];
  app.locals.items = {};
  app.locals.api = new API(app);
  app.locals.appConfig = config.app;
}

module.exports = app => {
  // app.set('views', path.join(__dirname, 'views'));
  // app.set('view engine', 'html');
  initializeLocals(app);

  app.set('json spaces', 2);

  // app.use(favicon(__dirname + '/public/img/favicon.ico'));
  app.use(logger('dev'));
  app.use(bodyParser.json());
  app.use(bodyParser.urlencoded({
    extended: true,
  }));
  app.use(cookieParser());
  app.use(express.static(path.join(__dirname, 'public')));

  app.use('/', routes);

  // catch 404 and forward to error handler
  app.use((req, res, next) => {
    const err = new Error('Not Found');
    err.status = 404;
    next(err);
  });

  // error handlers
  // eslint-disable-next-line no-unused-vars
  app.use((err, req, res, next) => {
    res
      .status(err.status || 500)
      .json({
        message: err.message,
        error: (app.get('env') === 'development') ? err : {},
      });
  });
};
