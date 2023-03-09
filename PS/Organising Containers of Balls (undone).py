"""

10
2
999336263 998799923
998799923 999763019
4
997612619 934920795 998879231 999926463
960369681 997828120 999792735 979622676
999013654 998634077 997988323 958769423
997409523 999301350 940952923 993020546
9
993263231 806455183 972467746 761846174 226680660 667393859 815298761 790313908 997845516
873142072 579210472 996344520 999601755 904458846 663577990 980240637 713052540 963408591
551159221 873763794 752756532 798803609 670921889 995259612 981339960 763904498 499472207
975980611 999974039 729219884 834636710 973988213 969888254 846967495 687204298 511348404
993232608 998103218 857820670 995587240 817798750 773950980 824882180 797565274 887424441
847857578 768853671 916073200 982234748 986511977 733420232 997714976 819799716 891570083
733197334 985682497 612123868 971798655 999905357 710092446 997494889 683312998 850074746
799093993 543648222 944524289 814951921 981087922 997222915 506561779 997697933 652807674
989362549 973516812 891706714 786904549 982329176 376575034 993535504 984745483 777613376
8
46243313 92616295 67710591 64815435 54972858 72243452 43981963 98839842
92051933 89794374 13448199 23493279 82268795 11069706 82550576 19654929
81743395 56456242 80407875 99464396 95594850 44919631 12483256 54576390
31379865 35550507 13850344 82310457 35039216 11977132 44906966 58819635
10544893 81324309 69520528 81983330 45347555 78383273 77715274 86346533
78482611 37125744 47756688 70062813 86629089 81735741 38208033 80479682
59164275 5441347 85517562 78736923 59124243 51404960 24474089 27179427
48097170 61680833 13467922 1371525 59776803 85694885 96662368 52983154
4
990446736 997114107 981378365 996304832
998069384 997117556 999915673 983059005
977726971 997275340 996964137 999686661
999000949 999267170 999903443 992602611
8
95191218 87409555 42950393 42038751 84631134 48464787 59894151 72209295
10208942 40165003 24468583 74313769 78553469 12298347 92465316 98013853
11962063 97319173 32772008 57537234 47515651 96327283 13026475 6272697
15196842 74022651 40230895 29947691 22917615 13671399 53857449 59913669
12346213 63160025 19794975 11420503 11101182 7020704 99262506 99345314
63048552 59405595 80841813 57114539 698590 30758610 35361024 19021664
48021465 59401215 33812089 32481698 38580652 37607783 66478344 64808679
21875586 87926772 98872000 19211740 76777430 661772 86446637 49124189
5
979032185 977330496 624547097 994815517 999577525
539128031 998016416 976111699 872522746 999964658
997364357 998086547 951266271 999938891 821877010
988421608 997815396 999690278 997717508 566289150
999245153 797284221 998318595 710308158 998035207
3
997427147 999234285 998319806
993127006 999257405 999972351
999251470 996489548 994064605
2
999789250 999886349
999654053 999789250
5
793248296 992239720 805150460 911286487 830355332
994381728 671232291 999428047 887238380 999950552
994157957 987220978 763871658 995769647 999904596
999500311 735194138 984736325 992803407 967745073
998302692 946393168 999044508 892881333 942969283
Possible
Possible
Possible
Impossible
Possible
Impossible
Possible
Possible
Possible
Possible

"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    # Write your code here
    l = len(container)
    def calcnon(c, i):#find how many balls dont belong to container i
        return sum(c[i])-c[i][i]
    def findall(c ,i):# find all i type balls in all containers
        return sum([c[k][i] for k in range(l)])
    def swapall(c, i):
        count = 0
        for k in range(l):
            if k!=i:
                c[i][i] += c[k][i]
                count += c[k][i]
                c[k][i] = 0
        return c, count
    def swappar(c,i): # swap all the i in k baskets into basket i
        count = 0
        for k in range(l):
            if k!=i:
                iink, kini = c[k][i], c[i][k]
                swap = min(iink, kini)
                count += swap
                c[i][i] += swap
                c[k][i], c[i][k] = c[k][i]-swap, c[i][k]-swap
        return c, count
    flag = 1
    from copy import deepcopy
    c = deepcopy(container)
    cnt_chg = -1
    def tryswap(c):
        count = 0
        for i in range(l):
            cni =  calcnon(c, i)
            ci = findall(c, i) - c[i][i]
            print(cni, ci)
            if cni==ci: # when i type ball outside equals to other type balls in container i, just swap 
                c, cnt = swapall(c,i)
            else: # otherwise, try to swap all the i in every basket back first, see if we still have something left
                c, cnt = swappar(c, i)
            count+=cnt
        return c, count
    while(cnt_chg!=0):
        cnt_chg = 0
        c, cnt_chg = tryswap(c)
    print(c)
    return "Possible" if flag else "Impossible"

# def organizingContainers(container):
#     # Write your code here
#     l = len(container)
#     def calcnon(c, i):#find how many balls dont belong to container i
#         return sum(c[i])-c[i][i]
#     def findall(c ,i):# find all i type balls in all containers
#         return sum([c[k][i] for k in range(l)])-c[i][i]
#     from copy import deepcopy
#     c = deepcopy(container)
#     flag = 1
#     for i in range(l):
#         nci = calcnon(c,i)
#         ci = findall(c,i)
#         print(nci, ci)
#         # if ci!=nci:
#         #     return "Impossible"
#     return "Possible"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
