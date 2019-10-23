#!/usr/bin/python
import ast
import requests
import multiprocessing
import json
import re
import sys
import time
import subprocess
import uuid
import random
import urllib
from colorama import init, Fore
from urllib.request import urlopen
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
init(convert=True)
tok = uuid.uuid4()
#Date & Time
def waktu():
    a = time.localtime()
    years = a.tm_mday
    monts = a.tm_mon
    days = a.tm_year
    hr = a.tm_hour
    mn = a.tm_min
    sc = a.tm_sec
    return ('[+] Tanggal :{}\n[+] Bulan :{}\n[+] Tahun :{}\n[+] Time :{}:{}:{}'.format(years, monts, days, hr, mn, sc))

# --------------------------------- Fake You Know ! Coded By Eric Pedra ----------------------------#
domainst = ["mail.apple.com", "mail.appleid.com", "mail.appleid.apple.com"]
mere = ["noreplay", "no-reply"]
random_domain = domainst[random.randint(0, len(domainst) - 1)]
random_word = mere[random.randint(0, len(mere) - 1)]
rd = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(10))
genenum = random.randint(1000000000,9999999999)
Fromaddrs = "{0}{1}{2}{3}".format(random_word, genenum, '@', random_domain)
me = "Apple Support " #domainn tidak bisa d modif
Jadul = "Re: [New Statement Alert] - Thanks Receipt for Your Payment to Apple Store Electronic Center.,LTD #%s"% (rd)
bcc = "bccperson1@gmail.com,bccperson2@yahoo.com"
cc = "anotherperson@gmail.com,someone@yahoo.com"
hps = ["Dolphin Browser", "Ecosia Browser", "Firefox Browser", "Firefox Focus", "Flynx", "Google Chrome", "Kiwi Browser", "Lightning Browser", "Lynket (formerly Chromer)", "Microsoft Edge", "Naked Browser", "Opera's browsers", "Samsung Internet Browser", "Tor Browser for Android"]
hp = ["Android 9", "Android 8.1", "Android 8.0", "Android 7.1.2", "Android 7.1.1", "Android 7.1", "Android 7.0", "Android 6.0.1", "Android 6.0", "Android 5.1.1", "Android 5.1", "Android 5.0.2", "Android 5.0.1", "Android 5.0", "Android 4.4.4", "Android 4.4.3", "Android 4.4.2", "Android 4.4.1", "Android 4.4"]
browsers = ["Mozilla Firefox", "Google Chrome", "Opera", "Microsoft Edge", "Microsoft Internet Explorer", "Vivaldi", "Tor Browser", "Chromium", "Torch Browser", "Maxthon Cloud Browser", "Safari", "UC Browser", "Brave web browser"]
apel = ['iPhone 3G', 'iPhone 3GS', 'iPhone 4', 'iPhone 4S', 'iPhone 5', 'iPhone 5C', 'iPhone 5S', 'iPhone 6', 'iPhone 6 Plus', 'iPhone 6S', 'iPhone 6S Plus', 'iPhone SE', 'iPhone 7', 'iPhone 7 Plus', 'iPhone 8', 'iPhone 8 Plus', 'iPhone X', 'iPhone XR', 'iPhone XS', 'iPhone XS Max']
windowz = ['Windows 10', 'Windows 8.1', 'Windows 8', 'Windows 7', 'Windows Vista', 'Windows XP Professional x64 Edition', 'Windows XP', 'Windows ME', 'Windows 2000', 'Windows 98', 'Windows NT 4.0', 'Windows 95', 'Windows NT 3.51', 'Windows NT 3.5', 'Windows 3.2', 'Windows for Workgroups 3.11', 'Windows NT 3.1', 'Windows 3.1', 'Windows 3.0', 'Windows 2.11', 'Windows 2.10', 'Windows 2.03', 'Windows 1.04', 'Windows 1.03', 'Windows 1.02', 'Windows 1.0', 'Windows 1.0 Beta']
iOS =  ['Windows 10', 'Windows 8.1', 'Windows 8', 'Windows 7', 'Windows Vista', 'Windows Server 2003/XP x64', 'Windows XP', 'Windows XP', 'Mac OS X', 'Mac OS 9', 'Linux', 'Ubuntu', 'iPhone', 'iPod', 'iPad', 'Android', 'BlackBerry', 'Mobile']
countryqq =  ["Afghanistan", "Albania", "Algeria", "American Samoa", "Andorra", "Angola", "Anguilla", "Antarctica", "Antigua and Barbuda", "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia", "Bosnia and Herzegowina", "Botswana", "Bouvet Island", "Brazil", "British Indian Ocean Territory", "Brunei Darussalam", "Bulgaria", "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde", "Cayman Islands", "Central African Republic", "Chad", "Chile", "China", "Christmas Island", "Cocos (Keeling) Islands", "Colombia", "Comoros", "Congo", "Congo, the Democratic Republic of the", "Cook Islands", "Costa Rica", "Cote d'Ivoire", "Croatia (Hrvatska)", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Falkland Islands (Malvinas)", "Faroe Islands", "Fiji", "Finland", "France", "France Metropolitan", "French Guiana", "French Polynesia", "French Southern Territories", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Gibraltar", "Greece", "Greenland", "Grenada", "Guadeloupe", "Guam", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Heard and Mc Donald Islands", "Holy See (Vatican City State)", "Honduras", "Hong Kong", "Hungary", "Iceland", "India", "Indonesia", "Iran (Islamic Republic of)", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea, Democratic People's Republic of", "Korea, Republic of", "Kuwait", "Kyrgyzstan", "Lao, People's Democratic Republic", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libyan Arab Jamahiriya", "Liechtenstein", "Lithuania", "Luxembourg", "Macau", "Macedonia, The Former Yugoslav Republic of", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Martinique", "Mauritania", "Mauritius", "Mayotte", "Mexico", "Micronesia, Federated States of", "Moldova, Republic of", "Monaco", "Mongolia", "Montserrat", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "Netherlands Antilles", "New Caledonia", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Niue", "Norfolk Island", "Northern Mariana Islands", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Pitcairn", "Poland", "Portugal", "Puerto Rico", "Qatar", "Reunion", "Romania", "Russian Federation", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Seychelles", "Sierra Leone", "Singapore", "Slovakia (Slovak Republic)", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Georgia and the South Sandwich Islands", "Spain", "Sri Lanka", "St. Helena", "St. Pierre and Miquelon", "Sudan", "Suriname", "Svalbard and Jan Mayen Islands", "Swaziland", "Sweden", "Switzerland", "Syrian Arab Republic", "Taiwan, Province of China", "Tajikistan", "Tanzania, United Republic of", "Thailand", "Togo", "Tokelau", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Turks and Caicos Islands", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "United States Minor Outlying Islands", "Uruguay", "Uzbekistan", "Vanuatu", "Venezuela", "Vietnam", "Virgin Islands (British)", "Virgin Islands (U.S.)", "Wallis and Futuna Islands", "Western Sahara", "Yemen", "Yugoslavia", "Zambia", "Zimbabwe"]
countrykalital = ['AF','AX','AL','DZ','AS','AD','AO','AI','AQ','AG','AR','AM','AW','AU','AT','AZ','BS','BH','BD','BB','BY','BE','BZ','BJ','BM','BT','BO','BA','BW','BV','BR','IO','BN','BG','BF','BI','KH','CM','CA','CV','KY','CF','TD','CL','CN','CX','CC','CO','KM','CG','CD','CK','CR','CI','HR','CU','CY','CZ','DK','DJ','DM','DO','EC','EG','SV','GQ','ER','EE','ET','FK','FO','FJ','FI','FR','GF','PF','TF','GA','GM','GE','DE','GH','GI','GR','GL','GD','GP','GU','GT','GG','GN','GW','GY','HT','HM','VA','HN','HK','HU','IS','IN','ID','IR','IQ','IE','IM','IL','IT','JM','JP','JE','JO','KZ','KE','KI','KP','KR','KW','KG','LA','LV','LB','LS','LR','LY','LI','LT','LU','MO','MK','MG','MW','MY','MV','ML','MT','MH','MQ','MR','MU','YT','MX','FM','MD','MC','MN','MS','MA','MZ','MM','NA','NR','NP','NL','AN','NC','NZ','NI','NE','NG','NU','NF','MP','NO','OM','PK','PW','PS','PA','PG','PY','PE','PH','PN','PL','PT','PR','QA','RE','RO','RU','RW','SH','KN','LC','PM','VC','WS','SM','ST','SA','SN','CS','SC','SL','SG','SK','SI','SB','SO','ZA','GS','ES','LK','SD','SR','SJ','SZ','SE','CH','SY','TW','TJ','TZ','TH','TL','TG','TK','TO','TT','TN','TR','TM','TC','TV','UG','UA','AE','GB','US','UM','UY','UZ','VU','VE','VN','VG','VI','WF','EH','YE','ZM','ZW']
appsapple =["iTunes & App Store", "iCloud"]
fakeemail =  ["younglex@icloud.com", "prabowo@icloud.com"]
subjectmailer = ['[ Summary Account Report ] Limited access disable', '[ Summary Account Report ] [ Security Check Notice ] Limited access disable', '[ Summary Account Report ] [ Login Activation ] Limited access disable', '[ Summary Account Report ] [ Notification ] Limited access disable', '[ Summary Account Report ] [ Locked ] Limited access disable ', 'Re: [ Statement New Update ] [ Account Alert ] Your Apple ID Has Been Locked at', 'Re: [ New Statement ] Confirmation change password of your Apple account', 'Re: [ Updated Statement Info] Your billing information was changes']
firstname = ['Sophia', 'Jackson', 'Emma', 'Aiden', 'Lucas', 'Liam', 'Ava', 'Mia', 'Noah', 'Isabella', 'Ethan', 'Riley', 'Mason', 'Aria', 'Caden', 'Zoe', 'Oliver', 'Charlotte', 'Elijah', 'Lily', 'Jacob', 'John', 'Lachlan', 'Georgia' ]
lastname = ['Smith', 'Johnson', '1111', 'Brown', 'Jones', 'Miller', 'Davis', 'Garcia', 'Rodriguez', 'Wilson', 'White', 'Martin', 'Anderson', 'Thompson', 'Nguyen', 'Turner', 'Walker', ]
bt = ['O-', 'O+', 'B-', 'B+', 'A-', 'A+', 'AB+', 'AB-', 'O-', 'O+', 'B-', 'B+', 'A-', 'A+', 'AB+']
medexpm = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
kartukredit = ['6***************', '4***************', '5***********', '3***************']
mmdic = ['01','02','03','04','05','06','07','08','09','10','11','12']
typ = ['Visa', 'Mastercard', 'JCB', 'AmericanExpress'] #JIKA KURANG TAMBAHIN SENDIRI
agentr = [
    # "chrome":
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
    "Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/4E423F",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36 Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS i686 4319.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1500.55 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36",
    "Mozilla/5.0 (X11; NetBSD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36",
    "Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/24.0.1292.0 Safari/537.14"

    # "opera"
    "Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16",
    "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14",
    "Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
    "Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02",
    "Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00",
    "Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00",
    "Opera/12.0(Windows NT 5.2;U;en)Presto/22.9.168 Version/12.00",
    "Opera/12.0(Windows NT 5.1;U;en)Presto/22.9.168 Version/12.00",
    "Mozilla/5.0 (Windows NT 5.1) Gecko/20100101 Firefox/14.0 Opera/12.0",
    "Opera/9.80 (Windows NT 6.1; WOW64; U; pt) Presto/2.10.229 Version/11.62",
    "Opera/9.80 (Windows NT 6.0; U; pl) Presto/2.10.229 Version/11.62",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; de) Presto/2.9.168 Version/11.52",
    "Opera/9.80 (Windows NT 5.1; U; en) Presto/2.9.168 Version/11.51",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; de) Opera 11.51",
    "Opera/9.80 (X11; Linux x86_64; U; fr) Presto/2.9.168 Version/11.50",
    "Opera/9.80 (X11; Linux i686; U; hu) Presto/2.9.168 Version/11.50",
    "Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (X11; Linux i686; U; es-ES) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/5.0 Opera 11.11",
    "Opera/9.80 (X11; Linux x86_64; U; bg) Presto/2.8.131 Version/11.10",
    "Opera/9.80 (Windows NT 6.0; U; en) Presto/2.8.99 Version/11.10",
    "Opera/9.80 (Windows NT 5.1; U; zh-tw) Presto/2.8.131 Version/11.10",
    "Opera/9.80 (Windows NT 6.1; Opera Tablet/15165; U; en) Presto/2.8.149 Version/11.1",
    "Opera/9.80 (X11; Linux x86_64; U; Ubuntu/10.10 (maverick); pl) Presto/2.7.62 Version/11.01",
    "Opera/9.80 (X11; Linux i686; U; ja) Presto/2.7.62 Version/11.01",
    "Opera/9.80 (X11; Linux i686; U; fr) Presto/2.7.62 Version/11.01",
    "Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.7.62 Version/11.01",
    "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.7.62 Version/11.01",
    "Opera/9.80 (Windows NT 6.1; U; sv) Presto/2.7.62 Version/11.01",
    "Opera/9.80 (Windows NT 6.1; U; en-US) Presto/2.7.62 Version/11.01",
    "Opera/9.80 (Windows NT 6.1; U; cs) Presto/2.7.62 Version/11.01",
    "Opera/9.80 (Windows NT 6.0; U; pl) Presto/2.7.62 Version/11.01",
    "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.7.62 Version/11.01",
    "Opera/9.80 (Windows NT 5.1; U;) Presto/2.7.62 Version/11.01",
    "Opera/9.80 (Windows NT 5.1; U; cs) Presto/2.7.62 Version/11.01",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.13) Gecko/20101213 Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.7.62 Version/11.01",
    "Mozilla/5.0 (Windows NT 6.1; U; nl; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.01",
    "Mozilla/5.0 (Windows NT 6.1; U; de; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.01",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; de) Opera 11.01",
    "Opera/9.80 (X11; Linux x86_64; U; pl) Presto/2.7.62 Version/11.00",
    "Opera/9.80 (X11; Linux i686; U; it) Presto/2.7.62 Version/11.00",
    "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.6.37 Version/11.00",
    "Opera/9.80 (Windows NT 6.1; U; pl) Presto/2.7.62 Version/11.00",
    "Opera/9.80 (Windows NT 6.1; U; ko) Presto/2.7.62 Version/11.00",
    "Opera/9.80 (Windows NT 6.1; U; fi) Presto/2.7.62 Version/11.00",
    "Opera/9.80 (Windows NT 6.1; U; en-GB) Presto/2.7.62 Version/11.00",
    "Opera/9.80 (Windows NT 6.1 x64; U; en) Presto/2.7.62 Version/11.00",
    "Opera/9.80 (Windows NT 6.0; U; en) Presto/2.7.39 Version/11.00"

    # "firefox": 
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
    "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
    "Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0",
    "Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20120101 Firefox/29.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/29.0",
    "Mozilla/5.0 (X11; OpenBSD amd64; rv:28.0) Gecko/20100101 Firefox/28.0",
    "Mozilla/5.0 (X11; Linux x86_64; rv:28.0) Gecko/20100101 Firefox/28.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:27.3) Gecko/20130101 Firefox/27.3",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:27.0) Gecko/20121011 Firefox/27.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:25.0) Gecko/20100101 Firefox/25.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0",
    "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:24.0) Gecko/20100101 Firefox/24.0",
    "Mozilla/5.0 (Windows NT 6.2; rv:22.0) Gecko/20130405 Firefox/23.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:23.0) Gecko/20131011 Firefox/23.0",
    "Mozilla/5.0 (Windows NT 6.2; rv:22.0) Gecko/20130405 Firefox/22.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:22.0) Gecko/20130328 Firefox/22.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:22.0) Gecko/20130405 Firefox/22.0",
    "Mozilla/5.0 (Microsoft Windows NT 6.2.9200.0); rv:22.0) Gecko/20130405 Firefox/22.0",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/21.0.1",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/21.0.1",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:21.0.0) Gecko/20121011 Firefox/21.0.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:21.0) Gecko/20130331 Firefox/21.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:21.0) Gecko/20100101 Firefox/21.0",
    "Mozilla/5.0 (X11; Linux i686; rv:21.0) Gecko/20100101 Firefox/21.0",
    "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20130514 Firefox/21.0",
    "Mozilla/5.0 (Windows NT 6.2; rv:21.0) Gecko/20130326 Firefox/21.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20130401 Firefox/21.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20130331 Firefox/21.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20130330 Firefox/21.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:21.0) Gecko/20130401 Firefox/21.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:21.0) Gecko/20130328 Firefox/21.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:21.0) Gecko/20100101 Firefox/21.0",
    "Mozilla/5.0 (Windows NT 5.1; rv:21.0) Gecko/20130401 Firefox/21.0",
    "Mozilla/5.0 (Windows NT 5.1; rv:21.0) Gecko/20130331 Firefox/21.0",
    "Mozilla/5.0 (Windows NT 5.1; rv:21.0) Gecko/20100101 Firefox/21.0",
    "Mozilla/5.0 (Windows NT 5.0; rv:21.0) Gecko/20100101 Firefox/21.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:21.0) Gecko/20100101 Firefox/21.0",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64;) Gecko/20100101 Firefox/20.0",
    "Mozilla/5.0 (Windows x86; rv:19.0) Gecko/20100101 Firefox/19.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/19.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/18.0.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0) Gecko/20100101 Firefox/17.0.6"

    # "safari": 
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A",
    "Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.13+ (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10",
    "Mozilla/5.0 (iPad; CPU OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko ) Version/5.1 Mobile/9B176 Safari/7534.48.3",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; de-at) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; da-dk) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; tr-TR) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; ko-KR) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; fr-FR) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; cs-CZ) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; ja-JP) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; zh-cn) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; ja-jp) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; ja-jp) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; zh-cn) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; sv-se) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; ko-kr) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; ja-jp) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; it-it) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; fr-fr) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; es-es) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-us) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-gb) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; de-de) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; sv-SE) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; ja-JP) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; de-DE) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; hu-HU) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; de-DE) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; ru-RU) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; ja-JP) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; it-IT) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-us) AppleWebKit/534.16+ (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; fr-ch) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; de-de) AppleWebKit/534.15+ (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; ar) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
    "Mozilla/5.0 (Android 2.2; Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-HK) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; tr-TR) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; nb-NO) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; fr-FR) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-TW) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; ru-RU) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; zh-cn) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5"

    # "internetexplorer":
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 7.0; InfoPath.3; .NET CLR 3.1.40767; Trident/6.0; en-IN)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)",
    "Mozilla/4.0 (Compatible; MSIE 8.0; Windows NT 5.2; Trident/6.0)",
    "Mozilla/4.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/1.22 (compatible; MSIE 10.0; Windows 3.1)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 7.1; Trident/5.0)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; Media Center PC 6.0; InfoPath.3; MS-RTC LM 8; Zune 4.7)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; Media Center PC 6.0; InfoPath.3; MS-RTC LM 8; Zune 4.7",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 4.0; InfoPath.3; MS-RTC LM 8; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; chromeframe/12.0.742.112)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 4.0; Tablet PC 2.0; InfoPath.3; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; yie8)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET CLR 1.1.4322; .NET4.0C; Tablet PC 2.0)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; FunWebProducts)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; chromeframe/13.0.782.215)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; chromeframe/11.0.696.57)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0) chromeframe/10.0.648.205",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.1; SV1; .NET CLR 2.8.52393; WOW64; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; chromeframe/11.0.696.57)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/4.0; GTB7.4; InfoPath.3; SV1; .NET CLR 3.1.76908; WOW64; en-US)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.2; SV1; .NET CLR 3.3.69573; WOW64; en-US)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; InfoPath.1; SV1; .NET CLR 3.8.36217; WOW64; en-US)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; .NET CLR 2.7.58687; SLCC2; Media Center PC 5.0; Zune 3.4; Tablet PC 3.6; InfoPath.3)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.0; Media Center PC 4.0; SLCC1; .NET CLR 3.0.04320)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 1.1.4322)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; SLCC1; .NET CLR 1.1.4322)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.0; Trident/4.0; InfoPath.1; SV1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.0; Trident/4.0; FBSMTWB; .NET CLR 2.0.34861; .NET CLR 3.0.3746.3218; .NET CLR 3.5.33652; msn OptimizedIE8;ENUS)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; Media Center PC 6.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.3; .NET4.0C; .NET4.0E; .NET CLR 3.5.30729; .NET CLR 3.0.30729; MS-RTC LM 8)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 3.0)"]
#---------------------------------- Coded By : Eric Pedra Area Random ---------------------#
#+xm+ email
#+ip+ ip
ip = '{}.{}.{}.{}'.format(*__import__('random').sample(range(0,255),4))
rd = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(10))
times = time.asctime() #+times+ letter
uname = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for _ in range(16))
gname = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for _ in range(6))
surname = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for _ in range(6))
fpass = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz12345678910') for _ in range(16))
bahas = random.choice(fakeemail) #Random Fake Email
halus = random.choice(appsapple) #Random Apps Apple Tag
saja = random.choice(apel) #Random Apple Phone Tag
diindonesia = random.choice(subjectmailer) #Random Subject
ahah = random.choice(iOS) #Random OS
ahahs = random.choice(agentr) #Random OS
wikwik = random.choice(countryqq) #Random Country Tag
wikwiks = random.choice(countrykalital) #Random Country Capital Tag
nameone = random.choice(firstname)  #Random First Name Tag
nametwo = random.choice(lastname)  #Random Last Name Tag
handphone= random.choice(hps) #Random Android Browsers Tag
handphones = random.choice(hp) #Random Android Version Tag
komputer = random.choice(browsers) #Random Windows Browsers Tag
komputers = random.choice(windowz) #Random Windows Version Tag
#saja = random.choice(frommailer) #Random From Mail
mm = random.choice(mmdic) #Random Monts Number Tag
mms = random.choice(medexpm) #Random Monts Text Tag
mmi = random.choice(bt) #Random Blood Type Tag
creditcards = random.choice(typ) #Random Credit Card Type Tag
creditcardi = random.choice(kartukredit) #Random Credit Card Sensor
binn = random.randint(400000,499999) #Random BIN Visa
creditcard = (binn,genenum) # Random Credit Card No Sensor
age = random.randint(1,40) #Random Age
dayw = random.randint(1,30) #Days Random
born = random.randint(1970,2005) #Years Born
yy = random.randint(2019,2026) #Random Years
geneccvs = random.randint(100,999) #Random CVV AmericanExpress
geneccv = random.randint(100,999) #Random CVV Visa & Mastercard
ordernumber = random.randint(0000000000000, 9999999999999) #Random Order Number
genenum = random.randint(1000000000,9999999999) #Random Number buat tambahkan BIN 10 gits
binns = random.randint(500000,599999) #Random BIN Master Card
binne = random.randint(37000,37999) #Random BIN AmericanExpress 
binnr = random.randint(650000,659999) #Random BIN Discover 
binne = random.randint(356630,358999)  #Random BIN JCB
#function color
color = {
	'black':Fore.BLACK,
	'red': Fore.RED,
	'green':Fore.GREEN,
	'yellow':Fore.YELLOW,
	'blue':Fore.BLUE,
	'cyan':Fore.CYAN,
	'white': Fore.WHITE
	} # List of colors

#LOCATION
url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)
#Data Informasi Location
IP=data['ip']
org=data['org']
city = data['city']
country=data['country']
region=data['region']
#Connection
merah = color['red']+"{0}"+color['white']
hijau = color['green']+"{0}"+color['white']
w 		= merah.format("XMailer Tools Token")
gans 	= merah.format(" Genarate Token... \n")
kamek 	= hijau.format(" Success... \n")
sangat 	= merah.format("Loading Data...  \n")
sambut 	= hijau.format(" Success... \n")
coded 	= merah.format("Connecting To Network...\n")
pontianak 	= hijau.format(" Success... \n")
me 		= merah.format("Thanks Usage Tools XMailer\n")
kao 	= hijau.format("  Success... \n")
exit = "[========]"
for l in w:
	sys.stdout.write(l)
	sys.stdout.flush()
	time.sleep(0.05)
for l in gans:
	sys.stdout.write(l)
	sys.stdout.flush()
	time.sleep(0.05)
for l in kamek:
	sys.stdout.write(l)
	sys.stdout.flush()
	time.sleep(0.5)
for l in sangat:
	sys.stdout.write(l)
	sys.stdout.flush()
	time.sleep(0.05)
for l in sambut:
	sys.stdout.write(l)
	sys.stdout.flush()
	time.sleep(0.05)
for l in coded:
	sys.stdout.write(l)
	sys.stdout.flush()
	time.sleep(0.05)
for l in pontianak:
	sys.stdout.write(l)
	sys.stdout.flush()
	time.sleep(0.05)
for l in me:
	sys.stdout.write(l)
	sys.stdout.flush()
	time.sleep(0.05)
for l in kao:
	sys.stdout.write(l)
	sys.stdout.flush()
	time.sleep(0.05)
# Banner
def banner():  
    print (color['green']  +  "          `.---::---.`         " + color['cyan'] + time.strftime(' [%A,%d %B %Y]') )
    print (color['green']  + "      .::-.`.`....`.-::.      " + color['cyan']  + time.strftime('  [%H:%M:%S %p]')) 
    print (color['green']  + "    -:.`  .`  ``  `.  `.:-    " + color['cyan']  + ('  Your IP detail ') + color['white'])
    print (color['green']  + "  `:-   `.    ``    .`   -:`  " + color['cyan']  + ('  IP : {}').format(IP))
    print (color['green']  + " `/.```..`````..`````..```./` " + color ['cyan'] + ('  Region : {}') .format (region))
    print (color['green']  + " /.    .      ``      .    .: " + color ['cyan'] + ('  Country : {}') .format (country))
    print (color['green']  + " ./    .`      ``      `.    /." + color ['cyan'] + (' City : {}') .format (city))
    print (color['green']  + "-:````-```````..```````-````:-"  + color ['cyan'] + ('  Org : {}') .format (org))
    print (color['green']  + "./    .`      ``      `.    /."  +  color ['cyan'] +  ("  Your Token : {}") .format (tok.hex))
    print (color['green']  + " :.    .      ``      .    -: "  + color['white']) 
    print (color['green']  + " `/.```..`````..`````..```-/` " + color['white']) 
    print (color['green']  + "  `:-   `.    ``    .`   -:`  " + color['white']   )
    print (color['green']  + "    -:.`  .`  ``  `.  `.:-    "  + color['white']   )
    print (color['green']  + "      .::-.`....`.`.-::.      "  + color['white']   )
    print (color['green']  + "         `.---::---.`         " + color['white'] )
    print (color['white']  + "[+]======================================== " + color['white']   )
    #print (color['cyan'] + time.strftime('[%A,%d %B %Y]') )
    #print (time.strftime('[%H:%M:%S %p]'))
    #print  ('Your IP detail ')
    #print ('IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0}'.format(org,region,country,city,IP))
    #print stuff
    #print "Credit Card :", fake.credit_card_full(card_type=None)
    #print ("Your Token :", tok.hex)
    #print fake.iban()
    print (color['green'] + "[+] DISCLAIMER : Developer are not responsible for the uses of XMailer" + color['white'])
    print (color['green'] + "[+] [IndoSec] [IndoXploit] [Evolution] [XMailer]" + color['white'])
    print (color['green'] + ("[+] CONTACT = Eric Pedra | erikpedraz10@gmail.com ") + color['white'])
    print (color['green'] + ("[+] FACEBOOK = https://www.facebook.com/Ahmad.AI.Ghazali ") + color['white'])
    print (color['green'] + ("[+] SCRIPT PROGRAMMED BY ZeroByte DENGAN PYTHON3 .") + color['white'])
    print (color['green'] + ('[+] UPDATE DONE '))
    print (color['green'] + ("[+] SENDER WITH SMTP  ") + color['white'])
    print (color['white'] + "[+]======================================== " + color['white'])
# ============
# clear screen
if sys.platform == 'linux' or sys.platform == 'linux2':
    subprocess.call("clear", shell=True)
    banner()
    pass
else:
	
    banner()

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

time.sleep(1.5)
print (color['green'] + "Pilih Server Anda" )
print (color['green'] + "Fiture")
print (color['green'] + "[1] Gmail  ")
print (color['green'] + "[0] EXIT" + color['white'])
print ("")




# ===============================
# bacot 
kontol = input('Server root@Zerobyte: ')
elist = input('Email List: ')


#----------------------------------------Area Config Coded Eric Pedra -------------------------------#
#Login Your SMTP ! 
gm = "fireflyddc@juno.com", "fireflyddc"
def gmailx(xm, gm):
	me = "Apple Support " 
	#frommailer = ["Apple", "Apple Notice", "Apple Reminder", "Apple Locked", "Apple Disabled", "Apple Support", "Apple Alert", "Apple Security" , "Apple Service", "Apple Update"]
   # iOS =  ['Windows 10', 'Windows 8.1', 'Windows 8', 'Windows 7', 'Windows Vista', 'Windows Server 2003/XP x64', 'Windows XP', 'Windows XP', 'Mac OS X', 'Mac OS 9', 'Linux', 'Ubuntu', 'iPhone', 'iPod', 'iPad', 'Android', 'BlackBerry', 'Mobile']
  #  fakeemail =  ["younglex@icloud.com", "prabowo@icloud.com"]
   # appsapple =["iTunes", "iCloud"]
    
	msg = MIMEMultipart('alternative')
	msg['Subject'] = "Case:[Our server detects abmormal traffic in your Apple-ld]"
	msg['From'] = me
	msg['To'] = xm
	
	#hanya = random.choice(letter) #letter 
	#diindonesia = random.choice(subjectmailer) #random subject
	#saja = random.choice(frommailer) #random subject
	#bahas = random.choice(fakeemail) #random frommail
	#halus = random.choice(appsapple) #random fakemail
	#ahah = random.choice(iOS) #random OS
   # wikwik = random.choice(countryq) #random countryq
   # uname = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for _ in range(16))
  #  surname = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for _ in range(6))
  #  gname = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for _ in range(6))
 #   fpass = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz12345678910') for _ in range(16))
	ip = ''.join(random.choice('1234567890') for _ in range(3))
	rd = ''.join(random.choice('1234567890abcdefghijklmnOPQRSTUVWXYZ') for _ in range(6))

	text = ""
	html = """\
<!DOCTYPE html>
<html>
<HEAD>
<STYLE>
.cssage P
{
margin:0px;
padding:0px
}
body.cssage
{
font-size: 12pt;
font-family:Calibri
}
</STYLE>

</HEAD>
<BODY class="cssage">
<BR>
<TABLE style="FONT-FAMILY: 'Times New Roman'" border=0 cellSpacing=0 cellPadding=0 width=600 align="center">
<TR class=header>
<TD colSpan=2>
<img src="https://4.bp.blogspot.com/-YWpfWpuV8Qk/W_EZfariB1I/AAAAAAAAAUQ/ZY8O2NyfXQ8DMwzGbFeT3_B9jYOuFRK5gCLcBGAs/s1600/automatic.png" width="238" height="17">
<br><br>
<img src="https://4.bp.blogspot.com/-io-3QJPHFg4/W_EYh1su-CI/AAAAAAAAATw/JdKyNaUTHKcJpZEZJgdricOSQTz7w8IVACLcBGAs/s1600/dearc.png" width="128" height="36">
<br><br>
<P style="LINE-HEIGHT: 21px; FONT-FAMILY: 'Trebuchet MS', Arial, Helvetica, sans-serif; COLOR: rgb(84,84,84); FONT-SIZE: 14px">
Your Apple ID-"""+xm+"""-was used to sign into iCloud from a different device.
<br>
<br>
Device: iPhone 8
<br>
Location: CA, USA
<br>
Ip Address: 231."""+ip+""".76.34
<br>
<br>
If you've not signed into iCloud recenly and believe someone my have accessed your account<br>
go to Apple ID and make sure you are indeed the owner of the account.
<BR>Case: """+rd+"""</P>
<br>
<BR>
 <a href="http://ur-l.me/appsolved034" target="_blank">
	<img src="https://4.bp.blogspot.com/-Gd_bvyActRw/W-eBm2qcu-I/AAAAAAAAATQ/4I9IH-fRX_YK6Xedrzd2zyBYlb3UTzHSACPcBGAYYCw/s1600/click.png" width="150" height="14">
 </a>
<br>
<br>
<tr>
<TD colSpan=2>
<img src="
	https://1.bp.blogspot.com/-Vp75cM7sDt0/W-eBZGaGfyI/AAAAAAAAATI/3BY5GXjPiiwgfIFGfI9Eg4Yiu9iNCJBsQCPcBGAYYCw/s1600/down.png" width="600" height="110">
</TD></TABLE></BODY></html>
	"""

	part1 = MIMEText(text, 'plain')
	part2 = MIMEText(html, 'html')

	msg.attach(part1)
	msg.attach(part2)

	mail = smtplib.SMTP('smtp.gmail.net', 587)

	mail.ehlo()
	mail.starttls()

	noti = mail.login(gm[0], gm[1])
	mail.sendmail(me, xm, msg.as_string())
	print ("[+] From Mail : ", me)
	print (waktu()+str(noti)+str(xm))
	mail.quit()

if (kontol == 1):
    print ("\nGmail ...!")
    print (("[+] Loading Data..."))
    time.sleep(2)
    print (color['green'] + "Success" + color['white'])
    time.sleep(1.5)
    print ("[+] Getting Resource... ...")
    time.sleep(2)
    print (color['green'] + "Success" + color['white'])
    time.sleep(1.5)
    print ("[+] Setting Connection...")
    time.sleep(2)
    print (color['green'] + "Success" + color['white'])
    time.sleep(1.5)
    print ("[+] Connecting To Network... ")
    time.sleep(2)
    print (color['green'] + "Success" + color['white'])
    time.sleep(1.5)
    hadeh = open(elist, "r")
    emel = hadeh.readlines()
    print ("[*] Kiriman...")
    a = 0
    for xm in emel:
        username = xm.split('@')[0] # Get Username Email
        domain = xm.split('@')[1] #Get Domain Email
        a += 1
        print ("Nomor : %s" % a) 
        gmailx(xm, gm)  # xm array dari email
        


    hadeh.close()
    pass

else:
    print ("Keluar")
    print ("Terima Kasih Telah Meggunakan Tools/Alat Kami !")



