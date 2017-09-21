# -- FILE: features/steps/example_steps.py
from behave import given, when, then, step
from ladder import Table_Tennis_Ladder




@when('the match result is input')
def step_impl(context):  
    context.result = context.ladder.input_result(context.player_list, 
    	'winner', 'loser')

@then('the winner takes the position of the loser')
def step_impl(context):
    assert context.result[context.initial_index_of_the_user_called_loser] == 'winner'


@given('the winner is ranked {operator} than the loser')
def step_impl(context, operator):

	context.ladder = Table_Tennis_Ladder()

	if operator == "higher":
		context.initial_index_of_the_user_called_winner = 0
		context.initial_index_of_the_user_called_loser = 1
		context.player_list = ['winner','loser']
	elif operator == "lower":
		context.initial_index_of_the_user_called_winner = 1
		context.initial_index_of_the_user_called_loser = 0
		context.player_list = ['loser', 'winner']

@then('the ladder is unaltered')
def step_impl(context):
    assert context.result[context.initial_index_of_the_user_called_winner] == 'winner'



#
# @given('i am ranked above the highest ranked player')
# def step_impl(context):
# 	context.ladder = Table_Tennis_Ladder()
# 	context.player_list = ['a','b']
# 	context.winner = 'a'
# 	context.loser = 'b'
#
# @when('a match occurs')
# def step_impl(context):
#     context.result = context.ladder.input_result(context.player_list,
#     	context.challenger, context.challengee)
#     print (context.result)
#
# @then('nothing happens to me')
# def step_impl(context):
#     assert context.result[0] == 'a'