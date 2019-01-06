CREATE TABLE ENROL

( sno VARCHAR(3) NOT NULL,

  cno VARCHAR(4) NOT NULL,

  grade VARCHAR(2),

  midterm INTEGER,

  final INTEGER,

  PRIMARY KEY(sno, cno),

  FOREIGN KEY(sno) REFERENCES STUDENT(sno),

  FOREIGN KEY(cno) REFERENCES COURSE(cno));



학생 테이블과, 과목 테이블 작성해오기



# 학생 테이블

CREATE STUDENT



CREATE COURSE

### 