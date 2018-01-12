const { spawn } = require('child_process');
const py = spawn('python3', ['test.py']);

py.stdout.on('data', function(data) {
    console.log(`stdout: ${data}`);
});

py.stderr.on('data', function(data) {
    console.log(`stderr: ${data}`);
});

py.on('close', function(code) {
    console.log(`child process exited with code ${code}`);
});
