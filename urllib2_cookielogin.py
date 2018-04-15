import urllib2
import urllib


url = "http://www.renren.com/380147955/profile"
headers = {
    "Host":"rcd.renren.com",
    "Connection":"keep-alive",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36",
    "Accept":"image/webp,image/apng,image/*,*/*;q=0.8",
    "Referer":"http://zhibo.renren.com/top",
    # "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Cookie":"anonymid=jf1ealsa4q121c; depovince=ZGQT; _r01_=1; JSESSIONID=abca_7PHQMRpibEZAUjjw; ick_login=a4bff827-4cde-4352-b3e3-8d3efddecd90; first_login_flag=1; ln_uact=weixingchana@163.com; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; loginfrom=syshome; jebe_key=d06e43fc-bd38-4a4b-b587-eb5aee194a42%7C1dbe15e3b38587697e2a4817e93ef1c8%7C1521655337025%7C1%7C1521655336196; wp_fold=0; ch_id=10050; BAIDU_SSP_lcr=https://www.baidu.com/link?url=EfgXJVmEgOqY7nvAoVVE57WPcfrw2eMBG6cbqz3RF-G&wd=&eqid=b0724b730004c04f000000035ab29fee; jebecookies=b07251a9-01af-4a0a-9018-fee28d4c195f|||||; _de=5C9295832432323DD18ED0F76CED7B0E5212E40F3D18115C; p=407c17e3ebbd4d9835205769c86287615; t=9c2858e5ff8993ea56c7a1db1238ac7b5; societyguester=9c2858e5ff8993ea56c7a1db1238ac7b5; id=380147955; xnsid=b63ee2fe",


}

request = urllib2.Request(url,headers=headers)
response = urllib2.urlopen(request)

print response.read()