# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
#doelpunten makers
goalscorer1 = "ruud gullit"
goalscorer2 = "marco van basten"
#welke minuut werd er gescoord
goal_0 = 32
goal_1 = 54
# x = space
x=' ';
scorers = (goalscorer1) + x +  str(goal_0), (goalscorer2) + x + str(goal_1)
print (scorers)
report = f'{goalscorer1} scored in the {goal_0}nd minute'" , " f'{goalscorer2} scored in the {goal_1}th minute'
print (report)
player = "frank rijkaard"
first_name= player[0:player.find ( x )]
print (first_name)
last_name_len = (player[player.find(x)+1:len(player)])
print (last_name_len)
name_short = player[0:1]+ "."+ x + last_name_len
print (name_short)
chant = ((first_name)+"!"+ x)*5
print (chant)
goodchant = ( x !=chant.strip()[-1])
print (goodchant)

