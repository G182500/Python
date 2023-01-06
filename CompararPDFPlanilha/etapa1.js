//ETAPA RESPONSÁVEL POR ACESSAR O SITE E BAIXAR O ZIP DOS CERTIFICADOS NO PC
const puppeteer = require('puppeteer');
const path = require('path');
const  fs = require('fs');
const ConfigParser = require('configparser');
const config = new ConfigParser();

config.read('node_config.cfg');

//Orçamentos
const link = config.get('PUPPETEER_VISOMES', 'orcamentos');

//[E1-Visomes] Baixar PDF e armazenar em uma pasta
async function step1(){
    //Inicia Navegador 
    const browser = await puppeteer.launch({
        headless: false,
        devtools: false,
        defaultViewport: null,
        userDataDir: 'ChromeData',
        args: [
        '--window-size=1024,768',
        '--disable-gpu',
        '--disable-dev-shm-usage',
        '--disable-setuid-sandbox',
        '--no-first-run',
        '--no-zygote',
        '--autoplay-policy=user-gesture-required',
        '--disable-background-networking',
        '--disable-background-timer-throttling',
        '--disable-backgrounding-occluded-windows',
        '--disable-breakpad',
        '--disable-client-side-phishing-detection',
        '--disable-component-update',
        '--disable-default-apps',
        '--disable-dev-shm-usage',
        '--disable-domain-reliability',
        '--disable-extensions',
        '--disable-features=AudioServiceOutOfProcess',
        '--disable-hang-monitor',
        '--disable-ipc-flooding-protection',
        '--disable-notifications',
        '--disable-offer-store-unmasked-wallet-cards',
        '--disable-popup-blocking',
        '--disable-print-preview',
        '--disable-prompt-on-repost',
        '--disable-renderer-backgrounding',
        '--disabled-setupid-sandbox',
        '--disable-speech-api',
        '--disable-sync',
        '--hide-scrollbars',
        '--ignore-gpu-blacklist',
        '--metrics-recording-only',
        '--mute-audio',
        '--no-default-browser-check',
        '--no-first-run',
        '--no-pings',
        '--no-sandbox',
        '--no-zygote',
        '--password-store=basic',
        '--use-gl=swiftshader',
        '--use-mock-keychain',
        '--disable-web-security',
        '--disable-blink-features=AutomationControlled',
        '--remote-debugging-port=9222'
        ],
      });

    //Inicia uma nova aba
    const page = await browser.newPage();

    //Acessa o site Visomes
    url = config.get('PUPPETEER_VISOMES', 'login');
    await page.goto(url);
      
    if (page.url() == config.get('PUPPETEER_VISOMES', 'login')) {
    //Aguarda campo email e senha carregar
    await page.waitForSelector('#email');
    await page.waitForSelector('#password');

    //Insere informações de login
    await page.type('#email', config.get('PUPPETEER_VISOMES', 'email'))
    await page.type('#password', config.get('PUPPETEER_VISOMES', 'password'))

    const [button] = await page.$x("//button[contains(., 'Log in')]");

    await Promise.all([
        page.waitForNavigation('domcontentloaded'), // The promise resolves after navigation has finished
        await button.click()
    ])
    }

    url = config.get('PUPPETEER_VISOMES', 'home');
     
    const orcamentos = await page.$$('.m-0');        // Home -> Detalhes do Orçamento

    // way 2    
    const propertyJsHandles = await Promise.all(
        orcamentos.map(handle => handle.getProperty('href'))
    );
    const hrefs2 = await Promise.all(
      propertyJsHandles.map(handle => handle.jsonValue())
    );


    for (let i = 0; i < hrefs2.length; i++) {
        const link = hrefs2[i];

        await page.goto(link);

        await page.waitForSelector('#q_certs');

        const zip = await page.$x("//a[contains(., 'zip')]");

        await zip[0].click();
    }

    await page.waitForTimeout(300000)

    await browser.close();
}

step1()