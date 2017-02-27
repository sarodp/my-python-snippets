--TMEASURE
----------------------------------------------
create table TMEASURE 
(
  ID integer primary key autoincrement,
  STAG character(10) not null,
  SVALUE real not null,
  TSTAMP datetime default (datetime('now','localtime'))
);

--TSETTING
--------------------------------------------------
create table TSETTING
(
  STAG character(10) primary key not null,
  DESC1 character(50),
  UNIT  character(10),

  MIN real not null,
  MAX real not null,
  ALARMLO real not null,
  ALARMHI real not null,
  
  STYPE character(20),
  CODE1 character(20),
  CODE2 character(20),
  CODE3 character(20)
);
