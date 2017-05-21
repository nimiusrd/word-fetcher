const chokidar = require('chokidar')
const spawn = require('child_process').spawn

function test() {
  spawn('python', ['-m', 'flake8', '--exclude', './**/node_modules', '.'], { stdio: 'inherit' })
  spawn('python', ['-m', 'unittest', '-v'], { stdio: 'inherit' })
}

const watcher = chokidar.watch('./**/*.py', {ignored: /node_modules/})
watcher.on('change', path => {
  console.log(`changed: ${path}`)
  test()
})

test()