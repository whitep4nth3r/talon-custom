from talon import Module
 
mod = Module()
 
@mod.capture(rule='runner <word>')
def npm_script(m) -> str:
  'Run an npm script.'
  return 'npm run ' + m.word.lower()

@mod.capture(rule='pit runner <word>')
def pnpm_script(m) -> str:
  'Run a pnpm script.'
  return 'pnpm run ' + m.word.lower()

@mod.capture(rule='main runner <word>')
def ntl_script(m) -> str:
  'Run a netlify script.'
  return 'ntl ' + m.word.lower()

@mod.capture(rule='log <word>')
def console_log(m) -> str:
  'console log in javascript'
  return 'console.log(' + m.word.lower() + ')'

