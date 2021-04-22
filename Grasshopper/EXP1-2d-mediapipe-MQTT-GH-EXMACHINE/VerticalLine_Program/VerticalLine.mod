MODULE VerticalLine

!! ###\   ###\ #####\  ######\##\  ##\##\###\   ##\ #####\ 
!! ####\ ####\##\\\##\##\\\\\\##\  ##\##\####\  ##\##\\\##\
!! ##\####\##\#######\##\     #######\##\##\##\ ##\#######\
!! ##\\##\\##\##\\\##\##\     ##\\\##\##\##\\##\##\##\\\##\
!! ##\ \\\ ##\##\  ##\\######\##\  ##\##\##\ \####\##\  ##\
!! \\\     \\\\\\  \\\ \\\\\\\\\\  \\\\\\\\\  \\\\\\\\  \\\
!! 
!! Program name: VerticalLine
!! Created: 04/21/2021 19:27:45
!! 
!! DISCLAIMER: WORKING WITH ROBOTS CAN BE DANGEROUS!
!! When using robots in a real-time interactive environment, please make sure:
!!     - You have been adequately trained to use that particular machine,
!!     - you are in good physical and mental condition,
!!     - you are operating the robot under the utmost security measures,
!!     - you are following the facility's and facility staff's security protocols,
!!     - and the robot has the appropriate guarding in place, including, but not reduced to:
!!         e -stops, physical barriers, light curtains, etc.
!! The Machina software framework and its generated code is provided as is;
!! use at your own risk. This product is not intended for any use that may
!! involve potential risks of death (including lifesaving equipment),
!! personal injury, or severe property or environmental damage.
!! Machina is in a very early stage of development. You are using this software
!! at your own risk, no warranties are provided herewith, and unexpected
!! results / bugs may arise during its use. Always test and simulate your
!! applications thoroughly before running them on a real device.
!! The author/s shall not be liable for any injuries, damages or losses
!! consequence of using this software in any way whatsoever.
!! 
!! 
!! Copyright(c) 2021 Jose Luis Garcia del Castillo y Lopez
!! https://github.com/RobotExMachina
!! 
!! MIT License
!! 
!! Permission is hereby granted, free of charge, to any person obtaining a copy
!! of this software and associated documentation files(the "Software"), to deal
!! in the Software without restriction, including without limitation the rights
!! to use, copy, modify, merge, publish, distribute, sublicense, and / or sell
!! copies of the Software, and to permit persons to whom the Software is
!! furnished to do so, subject to the following conditions:
!! 
!! The above copyright notice and this permission notice shall be included in all
!! copies or substantial portions of the Software.
!! 
!! THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
!! IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
!! FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
!! AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
!! LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
!! OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
!! SOFTWARE.


  CONST speeddata vel20 := [20,20,20,20];
  CONST speeddata vel100 := [100,100,100,100];

  PROC main()
    ConfJ \Off;
    ConfL \Off;

    MoveAbsJ [[-18, -93, 93, -104, -90, 17], [9E9,9E9,9E9,9E9,9E9,9E9]], vel20, z5, Tool0\WObj:=WObj0;  ! [Set joint rotations to [-18, -93, 93, -104, -90, 17] deg]
    ! [Set motion speed to 100 mm/s or deg/s]
    ! [Set precision radius to 10 mm]
    MoveAbsJ [[-18, -93, 93, -104, -90, 17], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Set joint rotations to [-18, -93, 93, -104, -90, 17] deg]
    MoveL [[-1028.35, 226.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-1028.35, 226.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-1031.35, 223.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-1031.35, 223.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-1028.35, 223.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-1028.35, 223.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-1058.35, 214.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-1058.35, 214.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-1061.35, 232.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-1061.35, 232.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-1061.35, 238.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-1061.35, 238.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-1067.35, 250.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-1067.35, 250.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-1103.35, 247.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-1103.35, 247.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-1121.35, 253.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-1121.35, 253.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-1121.35, 247.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-1121.35, 247.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-1118.35, 247.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-1118.35, 247.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-1112.35, 250.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-1112.35, 250.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-1061.35, 247.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-1061.35, 247.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-1013.35, 256.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-1013.35, 256.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-959.35, 265.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-959.35, 265.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-923.35, 268.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-923.35, 268.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-815.35, 271.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-815.35, 271.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-755.35, 271.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-755.35, 271.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-725.35, 274.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-725.35, 274.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-698.35, 274.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-698.35, 274.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-683.35, 274.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-683.35, 274.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-641.35, 271.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-641.35, 271.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-611.35, 271.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-611.35, 271.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-581.35, 274.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-581.35, 274.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-575.35, 271.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-575.35, 271.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-584.35, 259.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-584.35, 259.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-599.35, 250.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-599.35, 250.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-614.35, 235.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-614.35, 235.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-650.35, 211.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-650.35, 211.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-674.35, 196.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-674.35, 196.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-707.35, 169.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-707.35, 169.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-749.35, 139.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-749.35, 139.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-776.35, 118.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-776.35, 118.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-800.35, 97.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-800.35, 97.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-818.35, 79.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-818.35, 79.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-842.35, 61.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-842.35, 61.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-854.35, 55.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-854.35, 55.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-866.35, 46.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-866.35, 46.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-878.35, 37.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-878.35, 37.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-890.35, 37.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-890.35, 37.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-887.35, 52.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-887.35, 52.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-884.35, 82.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-884.35, 82.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-878.35, 103.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-878.35, 103.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-872.35, 136.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-872.35, 136.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-872.35, 160.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-872.35, 160.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-866.35, 184.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-866.35, 184.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-854.35, 238.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-854.35, 238.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-848.35, 253.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-848.35, 253.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-845.35, 268.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-845.35, 268.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-845.35, 271.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-845.35, 271.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-842.35, 280.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-842.35, 280.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-839.35, 292.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-839.35, 292.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-836.35, 301.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-836.35, 301.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-827.35, 316.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-827.35, 316.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-821.35, 334.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-821.35, 334.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-818.35, 349.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-818.35, 349.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-815.35, 358.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-815.35, 358.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-809.35, 367.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-809.35, 367.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-803.35, 382.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-803.35, 382.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-797.35, 391.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-797.35, 391.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-794.35, 388.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-794.35, 388.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-785.35, 379.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-785.35, 379.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-767.35, 340.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-767.35, 340.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-746.35, 298.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-746.35, 298.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-740.35, 259.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-740.35, 259.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-719.35, 214.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-719.35, 214.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-704.35, 181.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-704.35, 181.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-671.35, 142.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-671.35, 142.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-647.35, 115.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-647.35, 115.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-629.35, 94.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-629.35, 94.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-629.35, 88.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-629.35, 88.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-626.35, 88.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-626.35, 88.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-635.35, 88.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-635.35, 88.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-662.35, 100.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-662.35, 100.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-689.35, 124.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-689.35, 124.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-728.35, 145.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-728.35, 145.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-740.35, 154.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-740.35, 154.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-779.35, 166.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-779.35, 166.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-809.35, 178.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-809.35, 178.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-830.35, 178.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-830.35, 178.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-860.35, 190.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-860.35, 190.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-890.35, 193.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-890.35, 193.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-911.35, 199.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-911.35, 199.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-944.35, 211.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-944.35, 211.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-956.35, 217.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-956.35, 217.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-974.35, 223.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-974.35, 223.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-989.35, 235.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-989.35, 235.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-1013.35, 238.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-1013.35, 238.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-1025.35, 241.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-1025.35, 241.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-1025.35, 238.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-1025.35, 238.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-1037.35, 244.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-1037.35, 244.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-1037.35, 241.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-1037.35, 241.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-1043.35, 247.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-1043.35, 247.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-1034.35, 256.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-1034.35, 256.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-1040.35, 268.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-1040.35, 268.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-1043.35, 265.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-1043.35, 265.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-1043.35, 268.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-1043.35, 268.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-1040.35, 265.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-1040.35, 265.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-1046.35, 268.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-1046.35, 268.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-1046.35, 265.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-1046.35, 265.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-1043.35, 262.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-1043.35, 262.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-1043.35, 259.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-1043.35, 259.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]
    MoveL [[-1007.35, 202.019, 200], [0, 0.7071, 0.7071, 0], [0,0,0,0], [9E9,9E9,9E9,9E9,9E9,9E9]], vel100, z10, Tool0\WObj:=WObj0;  ! [Transform: move to [-1007.35, 202.019, 200] mm and rotate to [[0, 1, 0], [1, 0, 0], [0, 0, -1]]]

  ENDPROC

ENDMODULE
