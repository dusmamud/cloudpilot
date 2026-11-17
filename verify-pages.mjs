import { chromium } from '/home/hatch/.npm-global/lib/node_modules/playwright/index.mjs'
const routes = ['/','/features','/pricing','/how-it-works','/about','/contact','/request-demo','/login','/tools','/tools/flowmaster','/tools/insightpro','/tools/teamsync','/solutions','/solutions/startups','/solutions/teams','/solutions/enterprise','/customers','/customers/nimbus','/customers/fieldset','/customers/loopwork','/integrations','/security','/compare','/changelog','/resources','/roi-calculator','/help','/careers','/blog','/blog/automate-workflows','/blog/data-driven-decisions','/blog/remote-team-collaboration','/privacy-policy','/terms','/cookie-policy','/sitemap']
const browser = await chromium.launch()
let fails = []
for (const r of routes) {
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } })
  const errors = []
  page.on('pageerror', e => errors.push(String(e)))
  const res = await page.goto('http://127.0.0.1:4175' + r, { waitUntil: 'networkidle' }).catch(e => null)
  if (!res || res.status() >= 400) fails.push(r + ' HTTP ' + (res && res.status()))
  if (errors.length) fails.push(r + ' pageerror: ' + errors.join('; '))
  await page.close()
}
console.log('routes checked:', routes.length, 'fails:', fails.length)
fails.forEach(f => console.log('FAIL', f))
// overflow + screenshots
for (const w of [360, 390, 768, 1440]) {
  const page = await browser.newPage({ viewport: { width: w, height: 900 } })
  await page.goto('http://127.0.0.1:4175/', { waitUntil: 'networkidle' })
  await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight))
  await page.waitForTimeout(800)
  const m = await page.evaluate(() => ({ sw: document.documentElement.scrollWidth, iw: window.innerWidth }))
  console.log(`home ${w}px scrollWidth=${m.sw} innerWidth=${m.iw} overflow=${m.sw > m.iw}`)
  await page.evaluate(() => window.scrollTo(0, 0))
  await page.waitForTimeout(600)
  await page.screenshot({ path: `/tmp/cloudpilot-home-${w}.png` })
  await page.close()
}
// interactions: pricing toggle, ROI, help search, login
const page = await browser.newPage({ viewport: { width: 1280, height: 900 } })
await page.goto('http://127.0.0.1:4175/pricing', { waitUntil: 'networkidle' })
await page.getByText('Monthly', { exact: true }).click().catch(e => console.log('pricing toggle fail', e.message))
console.log('pricing monthly text:', (await page.textContent('body')).includes('$19'))
await page.goto('http://127.0.0.1:4175/login', { waitUntil: 'networkidle' })
await page.getByText('Fill demo account').click()
await page.getByText('Sign in', { exact: true }).click()
await page.waitForTimeout(400)
console.log('login demo ok:', (await page.textContent('body')).includes('Signed in (demo)'))
await page.goto('http://127.0.0.1:4175/help', { waitUntil: 'networkidle' })
await page.getByPlaceholder('Search help articles').fill('SSO')
await page.waitForTimeout(300)
console.log('help search SSO:', (await page.textContent('body')).includes('Set up SSO'))
await page.goto('http://127.0.0.1:4175/roi-calculator', { waitUntil: 'networkidle' })
console.log('roi has saved:', (await page.textContent('body')).includes('Saved per year'))
await browser.close()
console.log('DONE')
