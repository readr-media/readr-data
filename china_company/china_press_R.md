# china_press_R
### 目標：
china 國台辦政務要聞（~2017-05-10） http://www.gwytb.gov.cn/wyly/
china_press 國台辦新聞發佈會（～2000-9-5） http://www.gwytb.gov.cn/xwfbh/
（500）ATIE_press 台企聯新聞中心每日新聞（2013/01/08） http://www.qgtql.com/xwzx/mrxw/

### 國台辦
得到連結 list
```
j=1:9
jj<-as.character()
for(j in 1:9){
html<-read_html(paste0("http://www.gwytb.gov.cn/wyly/index_",j,".htm"))
html_2<-html_nodes(html,".black14pxlist a")
ccc<-html_attr(html_2,'href')
jj<-append(jj,as.character(ccc))}
```
###append 是把 list （結果 chr 也可以）結合在一起的方式
 
```
html_i<-read_html("http://www.gwytb.gov.cn/wyly/index.htm")
html_i2<-html_nodes(html_i,".black14pxlist a")
ccc<-html_attr(html_i2,'href')
```

把兩個資料結合在一起，完成網址清單
```
jjj<-append(jj,ccc)
```

爬內文
```
i=jjj
china<-data.frame()
for(i in jjj){
html<-read_html(paste0("http://www.gwytb.gov.cn/wyly/",i),encoding="GBK")
title<-html_text(html_nodes(html,'h1'))
date<-html_text(html_nodes(html,'h1+ div'))
content<-html_text(html_nodes(html,'#textsize p'))
Sys.sleep(sample(3:5, 1)) 
china<-rbind(china,data.frame(title=title,date=date,content=content))
}

```

### china_press
```
t=1:5
tt<-as.character()
for(t in 1:5){
html<-read_html(paste0("http://www.gwytb.gov.cn/xwfbh/index_",t,".htm"))
html_2<-html_nodes(html,".black14pxlist a")
ccc<-html_attr(html_2,'href')
tt<-append(tt,as.character(ccc))}

html_t<-read_html("http://www.gwytb.gov.cn/xwfbh/index.htm")
html_t2<-html_nodes(html_t,".black14pxlist a")
ccc<-html_attr(html_t2,'href')

ttt<-append(tt,ccc)

i=ttt
china_press<-data.frame()
for(i in ttt){
html<-read_html(paste0("http://www.gwytb.gov.cn/xwfbh/",i),encoding="GBK")
title<-html_text(html_nodes(html,'h1'))
content<-html_text(html_nodes(html,'#textsize'))
Sys.sleep(sample(3:5, 1)) 
china_press<-rbind(china_press,data.frame(title=title,content=content))
}

```

### ATIE_press
```
a=1:19
aa<-as.character()
for(a in 1:19){
html<-read_html(paste0("http://www.qgtql.com/xwzx/mrxw/index_",a,".htm"),encoding="GBK")
html_2<-html_nodes(html,".black14")
ccc<-html_attr(html_2,'href')
aa<-append(aa,as.character(ccc))}

html_a<-read_html("http://www.qgtql.com/xwzx/mrxw/index.htm",encoding="GBK")
html_a2<-html_nodes(html_a,".black14")
kkk<-html_attr(html_a2,'href')

aaa<-append(aa,kkk)

i=aaa
ATIE_press<-data.frame()
for(i in aaa){
html<-read_html(paste0("http://www.qgtql.com/xwzx/mrxw/",i),encoding="GBK")
title<-html_text(html_nodes(html,'td td td td table:nth-child(1) tr:nth-child(2) td'))
date<-html_text(html_nodes(html,'td td td table:nth-child(2) tr:nth-child(1) td'))
content<-html_text(html_nodes(html,'.TRS_Editor'))
Sys.sleep(sample(3:5, 1)) 
ATIE_press<-rbind(ATIE_press,data.frame(title=title,date=date,content=content))
}
```

### ATIE_press_2

```
g=8:19
gg<-as.character()
for(g in 8:19){
html<-read_html(paste0("http://www.qgtql.com/xwzx/mrxw/index_",g,".htm"),encoding="GBK")
html_2<-html_nodes(html,".black14")
ccc<-html_attr(html_2,'href')
gg<-append(gg,as.character(ccc))}

i=gg
ATIE_press_2<-data.frame()
for(i in gg){
html<-read_html(paste0("http://www.qgtql.com/xwzx/mrxw/",i),encoding="GBK")
title<-html_text(html_nodes(html,'td td td td table:nth-child(1) tr:nth-child(2) td'))
date<-html_text(html_nodes(html,'td td td table:nth-child(2) tr:nth-child(1) td'))
content<-html_text(html_nodes(html,'.TRS_Editor'))
Sys.sleep(sample(3:5, 1)) 
ATIE_press_2<-rbind(ATIE_press_2,data.frame(title=title,date=date,content=content))
}
```

### ATIE_press_3
```
g=13:19
gg<-as.character()
for(g in 13:19){
html<-read_html(paste0("http://www.qgtql.com/xwzx/mrxw/index_",g,".htm"),encoding="GBK")
html_2<-html_nodes(html,".black14")
ccc<-html_attr(html_2,'href')
gg<-append(gg,as.character(ccc))}

i=gg
ATIE_press_3<-data.frame()
for(i in gg){
html<-read_html(paste0("http://www.qgtql.com/xwzx/mrxw/",i),encoding="GBK")
title<-html_text(html_nodes(html,'td td td td table:nth-child(1) tr:nth-child(2) td'))
date<-html_text(html_nodes(html,'td td td table:nth-child(2) tr:nth-child(1) td'))
content<-html_text(html_nodes(html,'td td td td tr:nth-child(1) td:nth-child(2)'))
Sys.sleep(sample(3:5, 1)) 
ATIE_press_3<-rbind(ATIE_press_3,data.frame(title=title,date=date,content=content))
}
```

```
g=16:19
gg<-as.character()
for(g in 16:19){
html<-read_html(paste0("http://www.qgtql.com/xwzx/mrxw/index_",g,".htm"),encoding="GBK")
html_2<-html_nodes(html,".black14")
ccc<-html_attr(html_2,'href')
gg<-append(gg,as.character(ccc))}

i=gg
ATIE_press_4<-data.frame()
for(i in gg){
html<-read_html(paste0("http://www.qgtql.com/xwzx/mrxw/",i),encoding="GBK")
title<-html_text(html_nodes(html,'td td td td table:nth-child(1) tr:nth-child(2) td'))
date<-html_text(html_nodes(html,'td td td table:nth-child(2) tr:nth-child(1) td'))
content<-html_text(html_nodes(html,'td td td td tr:nth-child(1) td:nth-child(2)'))
Sys.sleep(sample(3:5, 1)) 
ATIE_press_4<-rbind(ATIE_press_4,data.frame(title=title,date=date,content=content))
}
```

```
html<-read_html("http://www.qgtql.com/xwzx/mrxw/index_15.htm"),encoding="GBK")
html_2<-html_nodes(html,".black14")
gg<-html_attr(html_2,'href')

i=gg
ATIE_press_15<-data.frame()
for(i in gg){
html<-read_html(paste0("http://www.qgtql.com/xwzx/mrxw/",i),encoding="GBK")
title<-html_text(html_nodes(html,'td td td td table:nth-child(1) tr:nth-child(2) td'))
date<-html_text(html_nodes(html,'td td td table:nth-child(2) tr:nth-child(1) td'))
content<-html_text(html_nodes(html,'td td td td tr:nth-child(1) td:nth-child(2)'))
Sys.sleep(sample(3:5, 1)) 
ATIE_press_15<-rbind(ATIE_press_15,data.frame(title=title,date=date,content=content))
}
```

```
content<-html_text(html_nodes(html,'.TRS_Editor'))
```

### 資料清理
```
ATIE_press_1<-filter(ATIE_press_all_rows,grepl("企业",content))
ATIE_press_1<-filter(ATIE_press_1,grepl("台湾",content))
ATIE_press_2<-filter(ATIE_press_all_rows,grepl("企业",content))
ATIE_press_2<-filter(ATIE_press_2,grepl("台资",content))
ATIE_press_3<-filter(ATIE_press_all_rows,grepl("集团",content))
ATIE_press_3<-filter(ATIE_press_3,grepl("台湾",content))
ATIE_press_4<-filter(ATIE_press_all_rows,grepl("台商",content))
ATIE_press_5<-filter(ATIE_press_all_rows,grepl("补助",content))
ATIE_press_6<-filter(ATIE_press_all_rows,grepl("补贴",content))
ATIE_press_taiwan<-rbind(ATIE_press_1,ATIE_press_2,ATIE_press_3,ATIE_press_4,ATIE_press_5,ATIE_press_6)
ATIE_press_taiwan<-unique(ATIE_press_taiwan)

h<-ATIE_press_taiwan$content
cc=worker()
cc[h]
ATIE_taiwan<-table(cc[h])
ATIE_taiwan<-data.frame(ATIE_taiwan)
```

```
china_press_1<-filter(china_press,grepl("企业",content))
china_press_1<-filter(china_press_1,grepl("台湾",content))
china_press_2<-filter(china_press,grepl("企业",content))
china_press_2<-filter(china_press_2,grepl("台资",content))
china_press_3<-filter(china_press,grepl("集团",content))
china_press_3<-filter(china_press_3,grepl("台湾",content))
china_press_4<-filter(china_press,grepl("台商",content))
china_press_5<-filter(china_press,grepl("补助",content))
china_press_6<-filter(china_press,grepl("补贴",content))
china_press<-rbind(china_press_1,china_press_2,china_press_3,china_press_4,china_press_5,china_press_6)
china_press<-unique(china_press)

h<-china_press$content
cc=worker()
cc[h]
china_press<-table(cc[h])
china_press<-data.frame(china_press)
```

#中國公司 #Rcode