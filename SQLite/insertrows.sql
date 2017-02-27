--insert TSETTING
--------------------------------------------------------
insert into TSETTING 
 (STAG,DESC1,UNIT,STYPE,CODE1,MIN,MAX,ALARMLO,ALARMHI) 
 values 
 ('T1','---','C','TEMPERATURE','R101',0,100,20,40);

insert into TSETTING 
 (STAG,DESC1,UNIT,STYPE,CODE1,MIN,MAX,ALARMLO,ALARMHI) 
 values 
 ('T2','---','C','TEMPERATURE','R201',0,100,20,40);

insert into TSETTING 
 (STAG,DESC1,UNIT,STYPE,CODE1,MIN,MAX,ALARMLO,ALARMHI) 
 values 
 ('H1','---','%','HUMIDITY','R101',0,100,40,70);

insert into TSETTING 
 (STAG,DESC1,UNIT,STYPE,CODE1,MIN,MAX,ALARMLO,ALARMHI) 
 values 
 ('H2','---','%','HUMIDITY','R201',0,100,40,70);

insert into TSETTING 
 (STAG,DESC1,UNIT,STYPE,CODE1,MIN,MAX,ALARMLO,ALARMHI) 
 values 
 ('KW1','---','KW','POWER','R101',0.0,5.0,0.0,4.0);
 
insert into TSETTING 
 (STAG,DESC1,UNIT,STYPE,CODE1,MIN,MAX,ALARMLO,ALARMHI) 
 values 
 ('KW2','---','KW','POWER','R201',0.0,10.0,0.0,9.0);

---insert TMEASURE
---------------------------------------------------------
insert into TMEASURE (STAG,SVALUE) values ('T1',25.0);
insert into TMEASURE (STAG,SVALUE) values ('T2',35.0);
insert into TMEASURE (STAG,SVALUE) values ('H1',70);
insert into TMEASURE (STAG,SVALUE) values ('H2',56);
insert into TMEASURE (STAG,SVALUE) values ('KW1',2.75);
insert into TMEASURE (STAG,SVALUE) values ('KW2',0.44);
