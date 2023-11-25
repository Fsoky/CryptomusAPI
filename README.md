<p align="center">
      <a href="https://imgur.com/osbyhki"><img src="https://i.imgur.com/osbyhki.png" title="source: imgur.com" /></a>
</p>

<p align="center">
    <img src="https://img.shields.io/badge/Version-1.0.0-blueviolet" alt="Project Version">
    <img src="https://img.shields.io/badge/License-MIT-success" alt="License">
</p>
<p align="center">
    <a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&color=0BE67A&center=true&vCenter=true&random=false&width=435&lines=Cryptomus;Crypto+Payment+Gateway" alt="Typing SVG" /></a>
</p>

<h1 align="center"> What are Cryptomus crypto payment gateway features?</h1>
<a href="https://imgur.com/f2PAMBG"><img src="https://i.imgur.com/f2PAMBG.png" title="source: imgur.com" width="128" height="128" align="left"/></a>
<div align="right">
  <h3>🛡 Volatility protection</h3>
  <p>
        Automatic conversion of incoming payments into stablecoins will protect against cryptocurrency volatility. <br/>
        The Withdrawal auto-convert feature allows you to withdraw your crypto in a preferred currency, and both features are completely free to use!
  </p>
</div>

<div>
  <a href="https://imgur.com/jFuoTL3"><img src="https://i.imgur.com/jFuoTL3.png" title="source: imgur.com" align="right"/></a>
  <h3>⚙ Transactions status management</h3>
  <ul>
    <li>Adjust the allowed payment accuracy.</li>
    <li>View if an invoice has been overpaid or underpaid and send an additional invoice to collect a remaining amount.</li>
  </ul>
</div>

<div align="right">
  <a href="https://imgur.com/E4hdG1q"><img src="https://i.imgur.com/E4hdG1q.png" title="source: imgur.com" align="left"/></a>
  <h3>% Flexible commissions for each coin</h3>
  <p>Set additional commissions or add a discount for chosen coins.</p>
</div><br/>

<div>
  <a href="https://imgur.com/XX4pNgu"><img src="https://i.imgur.com/XX4pNgu.png" title="source: imgur.com" align="right"/></a>
  <h3>💬 Support team</h3>
  <ul>
    <li>Telegram</li>
    <li>Email</li>
    <li>Our website in the form of tickets</li>
    <li>As a personal manager for our merchants</li>
  </ul>
</div>

<div align="right">
  <a href="https://imgur.com/mbJvIPu"><img src="https://i.imgur.com/mbJvIPu.png" title="source: imgur.com" align="left"/></a>
  <h3>📄 Mass payouts</h3>
  <p>
        Make mass payouts to thousands of addresses with automatic conversion in just one moment. <br/>
        <a href="https://cryptomus.com/processing">All features</a>
  </p>
</div><br/>

<h1 align="center">About This Project</h1>
<p align="center">
This project is written on pure enthusiasm, I want this library to be usable and used regularly. This project has the ability to run synchronously or asynchronously, which makes it more flexible.
The project will be maintained and improved, and you can buy me a coffee :)
Thanks, have a good day!
</p>

<div align="center">
      <a href="https://www.buymeacoffee.com/fsoky" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;"></a>
</div>

<h1 align="center">Installation</h1>

- Installation using the pip package manager
```bash
$ pip install CryptomusAPI
```
- Install from GitHub *(requires [git](https://git-scm.com/downloads))*
```bash
$ git clone https://github.com/Fsoky/CryptomusAPI
$ cd CryptomusAPI
$ python setup.py install
```
- Or
```bash
$ pip install git+https://github.com/Fsoky/CryptomusAPI
```

<h1 align="center">Get Started</h1>

> [!TIP]
> Refer to the documentation in any unclear situation: https://doc.cryptomus.com/ \
> To get **MERCHANT_ID** and **API_KEY** register and send an application to https://cryptomus.com/
> 
> _⚠ Make sure you have a **ready project** in which you will connect **Cryptomus** otherwise the key will not be issued!_

- You can use the asynchronous manager with
```python
import asyncio
from CryptomusAPI import Cryptomus

MERCHANT_ID = "123ABC"
API_KEY = "12345ABCDE"


async def main() -> None:
    async with Cryptomus(MERCHANT_ID, API_KEY) as api:
        ...


if __name__ == "__main__":
    asyncio.run(main())
```

- Or you can simply create an instance of the Cryptomus class
```python
api = Cryptomus(MERCHANT_ID, API_KEY)
```

### Creating an invoice
```python
await api.payments.create_invoice(
    amount=10,
    order_id="TEST-ORDER-1", # This parameter must not contain spaces.
    currency="USD", # or crypto currency like TON
    lifetime=300 # Invoice lifetime (in seconds), default 3600
)
```

> [!TIP]
> Enums can be used for parameters
```python
from CryptomusAPI.enums import CryptoCurrency
...create_invoice(..., currency=CryptoCurrency.USDT)
```

#### Obtaining data from a method
```python
invoice = await api.payments.create_invoice(...)
print(invoice.result.url) # >>> https://...
```

_The module is under development, please be patient, thank you!_
