# CVE-2019-11223
Arbitrary File Upload in Wordpress Plugin SupportCandy Version 2.0 Below
* https://cert.kalasag.com.ph/news/research/vulnerable-wordpress-plugin-lets-you-take-over-websites/
* https://wordpress.org/plugins/supportcandy/#developers
* https://www.pluginvulnerabilities.com/2019/04/05/arbitrary-file-upload-vulnerability-in-supportcandy/

## Getting Started
```
git clone https://github.com/AngelCtulhu/CVE-2019-11223.git
```
### Prerequisites
```
pip install requests
```

#### Exploitation

in exploit.py change localhost to your target

```
python exploit.py
"http:\/\/localhost\/wp-content\/uploads\/wpsc\/1555513124_shell.php"
```
## Authors

* **Christian Angel** - [KALASAG CERT](https://cert.kalasag.com.ph/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
