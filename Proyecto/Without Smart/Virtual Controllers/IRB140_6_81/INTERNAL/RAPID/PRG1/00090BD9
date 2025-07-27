MODULE Module1
    CONST robtarget Target_10:=[[-110,-175,-254],[0.990340804,0,0,-0.138654579],[0,-2,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_20:=[[-110,-175,0],[0.990340804,0,0,-0.138654579],[0,-2,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_30:=[[-160,-392.5,-253.927],[1,0,0,0],[0,-2,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_40:=[[-260,-575,0],[0.990340804,0,0,0.138654579],[0,-2,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_50:=[[-260,-575,-100],[0.990340804,0,0,0.138654579],[0,-2,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_60:=[[-160,-575,-85],[0.990340804,0,0,0.138654579],[0,-2,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_70:=[[-160,-575,-5],[0,0.990340804,0.138654579,0],[0,-2,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_80:=[[90,-225,-240],[0.382683434,0,0,0.923879532],[0,-2,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_90:=[[440,125,-200],[0,0,0,1],[0,-2,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_100:=[[340,125,-200],[0,0,0,1],[0,-2,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Home:=[[515,0,712],[0.707106781,0,0.707106781,0],[0,-2,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    PERS tooldata Griper:=[TRUE,[[0,17.5,237],[0.5,-0.5,0.5,0.5]],[1,[0,17.5,237],[1,0,0,0],1,1,1]];
    PERS tooldata Griper_1:=[TRUE,[[0,17.5,237],[1,0,0,0]],[1,[0,17.5,237],[1,0,0,0],2,2,1]];
    TASK PERS wobjdata Mesa:=[FALSE,TRUE,"",[[590,375,260],[0,0,1,0]],[[-60,0,0],[1,0,0,0]]];
!***********************************************************
    !
    ! M?dulo:  Module1
    !
    ! Descripción:
    !   <Introduzca la descripción aquí>
    !
    ! Autor: acer
    !
    ! Versión: 1.0
    !
    !***********************************************************
    
    
    !***********************************************************
    !
    ! Procedimiento Main
    !
    !   Este es el punto de entrada de su programa
    !
    !***********************************************************
    PROC main()
        WHILE TRUE DO
            Path_140;
            IF DI_01 = 1 THEN 
                Set DO_01;
                Path_10;
                Set DO_04;
                Reset DO_04;
                WaitTime 1;
                Path_20;
                WaitTime 1;
                Set DO_05;
                Reset DO_05;
                WaitTime 1;
                Path_10;
                Path_30;
                Path_40;
                WaitTime 1;
                Set DO_04;
                Reset DO_04;
                WaitTime 1;
                Path_50;
                WaitTime 10;
                Path_70;
                WaitTime 1;
                Set DO_05;
                Reset DO_05;
                WaitTime 2;
                Path_50;
                Path_60;
                Path_80;
                WaitTime 1;
                Set DO_04;
                Reset DO_04;
                WaitTime 1;
                Path_90;
                WaitTime 5;
                Path_80;
                WaitTime 2;
                Set DO_05;
                Reset DO_05;
                WaitTime 1;
                Path_90;
                Path_30;
                Reset DO_01;
            ENDIF
        ENDWHILE
    ENDPROC   
    
    PROC Path_10()
        MoveJ Target_10,v100,z10,Griper\WObj:=Mesa;
    ENDPROC
    
    PROC Path_20()
        MoveJ Target_10,v100,z10,Griper\WObj:=Mesa;
        MoveJ Target_20,v100,z10,Griper\WObj:=Mesa;
    ENDPROC
    PROC Path_30()
        MoveJ Target_30,v100,z10,Griper\WObj:=Mesa;
    ENDPROC
    PROC Path_40()
        MoveJ Target_30,v100,z10,Griper\WObj:=Mesa;
        MoveJ Target_40,v100,z10,Griper\WObj:=Mesa;
    ENDPROC
    PROC Path_50()
        MoveJ Target_40,v100,z10,Griper\WObj:=Mesa;
        MoveJ Target_50,v100,z10,Griper\WObj:=Mesa;
    ENDPROC
    PROC Path_60()
        MoveJ Target_60,v100,z100,Griper\WObj:=Mesa;
    ENDPROC
    PROC Path_70()
        MoveJ Target_50,v100,z10,Griper\WObj:=Mesa;
        MoveJ Target_40,v100,z10,Griper\WObj:=Mesa;
    ENDPROC
    PROC Path_80()
        MoveJ Target_60,v100,z10,Griper\WObj:=Mesa;
        MoveJ Target_70,v100,z10,Griper\WObj:=Mesa;
    ENDPROC
    PROC Path_90()
        MoveJ Target_70,v100,z10,Griper\WObj:=Mesa;
        MoveJ Target_60,v100,z10,Griper\WObj:=Mesa;
    ENDPROC
    PROC Path_140()
        MoveJ Home,v100,z10,tool0\WObj:=wobj0;
    ENDPROC
ENDMODULE