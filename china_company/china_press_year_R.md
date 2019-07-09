# china_press_year_R
```
china_dep_2011<-filter(china_dep_bus,data==2011)
china_dep_2012<-filter(china_dep_bus,data==2012)
china_dep_2013<-filter(china_dep_bus,data==2013)
china_dep_2014<-filter(china_dep_bus,data==2014)
china_dep_2015<-filter(china_dep_bus,data==2015)
china_dep_2016<-filter(china_dep_bus,data==2016)
china_dep_2017<-filter(china_dep_bus,data==2017)
china_dep_2018<-filter(china_dep_bus,data==2018)
china_dep_2019<-filter(china_dep_bus,data==2019)

X2011<-china_dep_2011$content
X2012<-china_dep_2012$content
X2013<-china_dep_2013$content
X2014<-china_dep_2014$content
X2015<-china_dep_2015$content
X2016<-china_dep_2016$content
X2017<-china_dep_2017$content
X2018<-china_dep_2018$content
X2019<-china_dep_2019$content

cc=worker()

cc[X2011]
cc[X2012]
cc[X2013]
cc[X2014]
cc[X2015]
cc[X2016]
cc[X2017]
cc[X2018]
cc[X2019]

china_press_2011<-table(cc[X2011])
china_press_2012<-table(cc[X2012])
china_press_2013<-table(cc[X2013])
china_press_2014<-table(cc[X2014])
china_press_2015<-table(cc[X2015])
china_press_2016<-table(cc[X2016])
china_press_2017<-table(cc[X2017])
china_press_2018<-table(cc[X2018])
china_press_2019<-table(cc[X2019])

china_press_2011<-data.frame(china_press_2011)
china_press_2012<-data.frame(china_press_2012)
china_press_2013<-data.frame(china_press_2013)
china_press_2014<-data.frame(china_press_2014)
china_press_2015<-data.frame(china_press_2015)
china_press_2016<-data.frame(china_press_2016)
china_press_2017<-data.frame(china_press_2017)
china_press_2018<-data.frame(china_press_2018)
china_press_2019<-data.frame(china_press_2019)

china_press_2011$year<-"2011"
china_press_2012$year<-"2012"
china_press_2013$year<-"2013"
china_press_2014$year<-"2014"
china_press_2015$year<-"2015"
china_press_2016$year<-"2016"
china_press_2017$year<-"2017"
china_press_2018$year<-"2018"
china_press_2019$year<-"2019"

china_press_year<-rbind(china_press_2011,china_press_2012,china_press_2013,china_press_2014,china_press_2015,china_press_2016,china_press_2017,china_press_2018,china_press_2019)

china_press_year<-filter(china_press_year,str_length(china_press_year$Var1)>1)

china_press_year<-spread(china_press_year,key="Var1",value="year")
```

#中國公司 #Rcode