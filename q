:setEnvironment
!关闭输出
print_on_cmd=0
stc=1
finish

:create=partPre
-G C E
finish


:create=partMain
E*0.5 C*0.5 G*1.5 E*0.5
D G D
C*0.5 -A*0.5 E*1.5 C*0.5
-B*2 C*0.5 -B*0.5

-A -B C*0.5 D*0.5
-G C D*0.5 E*0.5
F F*0.5 E*0.5 D*0.5 C*0.5
D*2 C*0.5 D*0.5

E*0.5 C*0.5 G*1.5 E*0.5
D G D
C*0.5 -A*0.5 -A -B*0.5 C*0.5
-G*2 0*0.5 -G*0.5

-A -B C*0.5 D*0.5
-G C D*0.5 E*0.5
F F*0.5 E*0.5 D*0.5 C*0.5
C*3

0*2 E*0.5 F*0.5
G*3
G G*0.5 A*0.5 G*0.5 F*0.5
E*3

E*0.5 F*0.5 E*0.5 D*0.5 C*0.5 -B*0.5
-A*0.5 -A*0.5 -B*0.5 C*0.5 D*0.5
finish

-main=0
=partPre*3 -G C
C D

=partMain -G C D*0.5 E*0.5
D*1.5 D*0.5 D*0.5 C*0.5
C*3
-G C 0
-G C E
-G C C*0.5 D*0.5

=partMain -G C*1.5 -B*0.5
-A -B C*0.5 D*0.5
-G*2 C*0.5 -B*0.5
-A -B C*0.5 D*0.5
-G C D*0.5 E*0.5
F F*0.5 E*0.5 D*0.5 C*0.5
finish

stop