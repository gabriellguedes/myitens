'use strict';

const { WPTRunner } = require('../common/wpt');

const runner = new WPTRunner('dom/events');

runner.setFlags(['--experimental-global-customevent']);

runner.runJsTests();
