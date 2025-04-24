'''' for the inputs with 3 quote marks, please input the code in block format - such as in setup
temp = """40000000
40D00000
00000000
103
415
1
0
1
"""
'''
# for wind velo and angle, please put the whole 8 character code for each, nothing will be added to these inputs
# unlike weather and pin

wind_velocity = """
"""

wind_angle = """
"""
# for weather and pin loc, please use only one digit, as the leading 0s will be auto placed (only 0/1 for weather)
weather = """
"""
# for pin loc, please use the desired pin, so 1/2/3/4
pin = """
"""

# IF using code to automatically assign holes and pars:
# enter the decimal ID
hole_ids = """
"""
# enter just the par amount (3, 4, 5, ect - does not specifically have to match the hole in that slot but may act weirdly if it isnt - im personally unsure of all its effects)
# code is only allocating for 2 hex digits, maximum being 255 in decimal (FF)
# NOTE when changing both holes and pars, sometimes the par will not be able to be changed from its normal
# par, I do not know why it does this but its a case-by-case basis
pars = """
"""
# enter course that is being selected on course selection screen; 1 = laki, 5 = pcg
# if also using the auto hole and par assigner, then keep this number 5 for pcg as those are the ids used
course = "5"




# ONLY EDIT ABOVE
# output should be in the same place the code is located, see file location in the terminal
# file should be called 'c18_output.txt', or whatever you rename it to on line 141

course_id = "201580a0 0000000"
hole_code = "2015809c 000000"
pin_code = "044E66AC 0000000"
wind_velocity_code = "044E6854 "
wind_angle_code = "044E6850 "
weather_code = "044E6858 0000000"
clear = "e2000001 00000000"
setup = """C0000000 0000000D
9421FF80 BC610008
3C608015 6063809C
3C80804E 6084674B
3CA0804E 60A566B1
3CC08015 60C680A0
80E30000 89040000
7C074000 41820008
91030000 89250000
81460000 7C095000
41820010 91260000
48000008 48000004
B8610008 38210080
4E800020 00000000"""

pcg_locations = """044CD0C0 00000
044CD0CC 00000
044CD0D8 00000
044CD0E4 00000
044CD0F0 00000
044CD0FC 00000
044CD108 00000
044CD114 00000
044CD120 00000
044CD12C 00000
044CD138 00000
044CD144 00000
044CD150 00000
044CD15C 00000
044CD168 00000
044CD174 00000
044CD180 00000
044CD18C 00000
"""
pcg_pars = """004CD0C8 000000
004CD0D4 000000
004CD0E0 000000
004CD0EC 000000
004CD0F8 000000
004CD104 000000
004CD110 000000
004CD11C 000000
004CD128 000000
004CD134 000000
004CD140 000000
004CD14C 000000
004CD158 000000
004CD164 000000
004CD170 000000
004CD17C 000000
004CD188 000000
004CD194 000000
"""
velo = wind_velocity.splitlines()
angle = wind_angle.splitlines()
wea = weather.splitlines()
p = pin.splitlines()

pcg_loc = pcg_locations.splitlines()
pcg_p = pcg_pars.splitlines()
id = hole_ids.splitlines()
par = pars.splitlines()

block = ""

assigner = input("Using the PCG autoassigner? input anything for yes, press enter with nothing written for no")
if assigner != "":
    for x in range(0,18):
        hex_loc = "{:03x}".format(int(id[x]))
        block += (pcg_loc[x] + hex_loc + "\n")
    for x in range(0,18):
        hex_par = "{:02x}".format(int(par[x]))
        block += (pcg_p[x] + hex_par + "\n")


block += (setup + "\n" +
    course_id + course + "\n")
for x in range(0,18):
    hex_hole = "{:02x}".format(x)
    block += (hole_code + hex_hole + "\n" +
             pin_code + str(int(p[x]) - 1) + "\n" +
             wind_velocity_code + velo[x] + "\n" +
             wind_angle_code + angle[x] + "\n" +
             weather_code + wea[x] + "\n" +
             clear + "\n")
block += clear
with open("c18_output.txt", "w+") as f:
    f.writelines(block)
