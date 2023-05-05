const { Builder, By, Key, until } = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');

async function goGetter() {
    

// set up the webdriver in headless mode
let options = new chrome.Options();
options.addArguments('--headless', '--disable-gpu');
let driver = new Builder().forBrowser('chrome').build();

// navigate to a web page
await driver.get('http://flowtech.local');

// add your Selenium code here
let title = await driver.getTitle();
let wordPress = await driver.findElement(By.text('head'));
console.log(wordPress);
console.log(title);
// close the browser
await driver.quit();
}

goGetter()
