from time import sleep

from behave import given, when, then


@given('user is on https://sylwia-wozniak.github.io/works/todolist_own/')
def step_start_page(context):
    context.driver.get('https://sylwia-wozniak.github.io/works/todolist_own/')


@when('user types a {task_name}')
def step_type_task(context, task_name):
    context.driver.find_element_by_class_name('task-input').send_keys(str(task_name))
    sleep(1)


@when('user types {too_long_task_name}')
def step_type_task(context, too_long_task_name):
    context.driver.find_element_by_class_name('task-input').send_keys(str(too_long_task_name))
    sleep(1)


@when('user clicks \'add\'')
def step_add_task(context):
    context.driver.find_element_by_class_name('task-add').click()
    sleep(1)


@then('{task_name} is created')
def step_create_task(context, task_name):
    context.driver.save_screenshot('to-do-list-task-{}.png'.format(task_name))
    assert context.driver.find_element_by_class_name('note')


@then('user sees an alert - empty input')
def step_alert(context):
    context.driver.save_screenshot('to-do-list-empty-input.png')
    assert context.driver.find_element_by_class_name('alert-empty')


@then('user sees an alert - too long name')
def step_alert(context):
    context.driver.save_screenshot('to-do-list-too-long-name.png')
    assert context.driver.find_element_by_class_name('alert-empty')
