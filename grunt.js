/*global module:false*/
var path = require('path');

module.exports = function(grunt) {

  grunt.initConfig({
    pkg: '<json:package.json>',
    meta: {
      banner: '/*! <%= pkg.title || pkg.name %> - v<%= pkg.version %> - ' + '<%= grunt.template.today("yyyy-mm-dd") %>\n' + ' * Copyright (c) <%= grunt.template.today("yyyy") %> <%= pkg.author.name %>;\n' + ' */'
    },
    watch : {
      files : ['core/*.py'],
      tasks: 'restart_flask'
    }
  });

  // Create a new task.
  grunt.registerTask('restart_flask', 'Print out "awesome!!!"', function() {
    var awesome = grunt.helper('restart_flask');
    grunt.log.write(awesome);
  });

  // Register a helper.
  grunt.registerHelper('restart_flask', function() {

    var sys   = require('sys'),
    exec  = require('child_process').exec,
    child;

    child = exec('bin/restart_flask.sh', 
      function (error, stdout, stderr) {
        sys.print('stdout: ' + stdout);
        sys.print('stderr: ' + stderr);
        if (error !== null) {
          console.log('exec error: ' + error);
        }
        sys.print('\n\n');
    });

    return 'Restart Flask server !';
  });

  // Create a new task.
  grunt.registerTask('start_flask', 'Print out "awesome!!!"', function() {
    var awesome = grunt.helper('start_flask');
    grunt.log.write(awesome);
  });

  // Register a helper.
  grunt.registerHelper('start_flask', function() {

    var sys   = require('sys'),
    exec  = require('child_process').exec,
    child;

    child = exec('bin/stop_flask.sh; bin/start_flask.sh', 
      function (error, stdout, stderr) {
        sys.print('stdout: ' + stdout);
        sys.print('stderr: ' + stderr);
        if (error !== null) {
          console.log('exec error: ' + error);
        }
        sys.print('\n\n');
    });

    return 'Start Flask server !';
  });
  // Default task.
  grunt.registerTask('default', 'start_flask watch');

};


