# -- FILE: features/steps/example_steps.py
from behave import given, when, then, step
from table_tennis_ladder import Table_Tennis_Ladder

@given('i am below another player')
def step_impl(context):
	context.ladder = Table_Tennis_Ladder()
	context.player_list = ['a','b']
	context.challenger = 'b'
	context.challengee = 'a'

@when('i beat that player above me')
def step_impl(context):  
    context.result = context.ladder.input_result(context.player_list, 
    	context.challenger, context.challengee)

@then('i take their position')
def step_impl(context):
    assert context.result[0] == 'b'



@given('i am above another player')
def step_impl(context):
	context.ladder = Table_Tennis_Ladder()
	context.player_list = ['a','b']
	context.challenger = 'b'
	context.challengee = 'a'

@when('i beat that player below me')
def step_impl(context):  
    context.result = context.ladder.input_result(context.player_list, 
    	context.challenger, context.challengee)
    print (context.result)

@then('nothing happens')
def step_impl(context):
    assert context.result[0] == 'a'