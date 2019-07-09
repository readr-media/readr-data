# ATIE_press_year_R
```
ATIE_press_2013<-filter(ATIE_press_all_rows,year==2013)
ATIE_press_2014<-filter(ATIE_press_all_rows,year==2014)
ATIE_press_2015<-filter(ATIE_press_all_rows,year==2015)
ATIE_press_2016<-filter(ATIE_press_all_rows,year==2016)
ATIE_press_2017<-filter(ATIE_press_all_rows,year==2017)
ATIE_press_2018<-filter(ATIE_press_all_rows,year==2018)

X2013<-ATIE_press_2013$content
X2014<-ATIE_press_2014$content
X2015<-ATIE_press_2015$content
X2016<-ATIE_press_2016$content
X2017<-ATIE_press_2017$content
X2018<-ATIE_press_2018$content

cc=worker()

cc[X2013]
cc[X2014]
cc[X2015]
cc[X2016]
cc[X2017]
cc[X2018]

ATIE_press_2013<-table(cc[X2013])
ATIE_press_2014<-table(cc[X2014])
ATIE_press_2015<-table(cc[X2015])
ATIE_press_2016<-table(cc[X2016])
ATIE_press_2017<-table(cc[X2017])
ATIE_press_2018<-table(cc[X2018])

ATIE_press_2013<-data.frame(ATIE_press_2013)
ATIE_press_2014<-data.frame(ATIE_press_2014)
ATIE_press_2015<-data.frame(ATIE_press_2015)
ATIE_press_2016<-data.frame(ATIE_press_2016)
ATIE_press_2017<-data.frame(ATIE_press_2017)
ATIE_press_2018<-data.frame(ATIE_press_2018)

ATIE_press_2013$year<-"2013"
ATIE_press_2014$year<-"2014"
ATIE_press_2015$year<-"2015"
ATIE_press_2016$year<-"2016"
ATIE_press_2017$year<-"2017"
ATIE_press_2018$year<-"2018"

ATIE_press_year<-rbind(ATIE_press_2013,ATIE_press_2014,ATIE_press_2015,ATIE_press_2016,ATIE_press_2017,ATIE_press_2018)

ATIE_press_year<-filter(ATIE_press_year,str_length(ATIE_press_year$Var1)>1)

ATIE_press_year<-spread(ATIE_press_year,key="year",value="Freq")
```

#中國公司 #Rcode