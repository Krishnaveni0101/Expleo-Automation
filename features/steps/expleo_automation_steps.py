import time
from behave import *
from selenium import webdriver
from selenium.webdriver.support.color import Color


@given('launch chrome browser')
def launch_chrome_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@when('navigate to url')
def open_website_url(context):
    time.sleep(5)
    context.driver.get("https://the-internet.herokuapp.com/challenging_dom")


@then('verify website is launched successfully')
def verify_website_load(context):
    time.sleep(5)
    element = context.driver.find_element_by_xpath("//div[@class='example']/h3[contains(text(),"
                                                   "'Challenging DOM')]")
    context.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element,
                                  "background:yellow; color:red; border: 4px dotted solid red")
    time.sleep(4)
    is_displayed = context.driver.find_element_by_xpath("//div[@class='example']/h3[contains(text(),"
                                                        "'Challenging DOM')]").is_displayed()
    assert is_displayed is True


@then('verify button "{button_number}" background color is "{color_name}"')
def verify_button_color(context, button_number, color_name):
    color_switcher = {
        "blue": "#2ba6cb",
        "red": "#c60f13",
        "green": "#5da423"
    }
    element_color = Color.from_string(
        context.driver.find_element_by_xpath(f"//a[contains(@class,'button')][{button_number}]")
            .value_of_css_property('background-color')).hex
    color = color_switcher.get(color_name)
    print(color)
    print(element_color)
    assert element_color == color


@then('number of "{column_or_row}" in the table is "{number}"')
def count_table_row_column(context, column_or_row, number):
    if column_or_row == "rows":
        row_count = len(context.driver.find_elements_by_xpath("//div[contains(@class,'large-10 columns')]//tr"))
        print(row_count)
        assert int(number) == row_count
    elif column_or_row == "columns":
        column_count = len(context.driver.find_elements_by_xpath("//div[contains(@class,'large-10 columns')]"
                                                                 "//tr[1]/th"))
        print(column_count)
        assert int(number) == column_count
    else:
        raise Exception


@then('validate table has no duplicate values')
def no_duplicate_values(context):
    duplicate_text = None
    row_count = len(context.driver.find_elements_by_xpath("//div[contains(@class,'large-10 columns')]//tr"))
    column_count = len(context.driver.find_elements_by_xpath("//div[contains(@class,'large-10 columns')]"
                                                             "//tr[1]/th"))
    cell_value = "//div[contains(@class,'large-10 columns')]//tr[{}]/td[{}]"
    for row in range(1, row_count):
        for column in range(1, column_count + 1):
            cell_text = context.driver.find_element_by_xpath(cell_value.format(str(row), str(column))).text
            print(cell_text)
            if cell_text != duplicate_text:
                duplicate_text = cell_text
                print(duplicate_text)
            else:
                raise Exception


@then('validate table position of word "{text}" is "{position}"')
def validate_table_position(context, text, position):
    row_count = len(context.driver.find_elements_by_xpath("//div[contains(@class,'large-10 columns')]//tr"))
    column_count = len(context.driver.find_elements_by_xpath("//div[contains(@class,'large-10 columns')]"
                                                             "//tr[1]/th"))
    cell_value = "//div[contains(@class,'large-10 columns')]//tr[{}]/td[{}]"
    for row in range(1, row_count):
        for column in range(1, column_count + 1):
            cell_text = context.driver.find_element_by_xpath(cell_value.format(str(row), str(column))).text
            print(cell_text)
            if cell_text == text:
                text_table_position = f"{str(row)}*{str(column)}"
                if text_table_position == str(position):
                    print(f"{text} position is {text_table_position}")
                    break
                else:
                    raise Exception


@then('validate error is thrown for word "{text}" which is not available in table')
def throw_error(context, text):
    row_count = len(context.driver.find_elements_by_xpath("//div[contains(@class,'large-10 columns')]//tr"))
    column_count = len(context.driver.find_elements_by_xpath("//div[contains(@class,'large-10 columns')]"
                                                             "//tr[1]/th"))
    cell_value = "//div[contains(@class,'large-10 columns')]//tr[{}]/td[{}]"
    for row in range(1, row_count):
        for column in range(1, column_count + 1):
            cell_text = context.driver.find_element_by_xpath(cell_value.format(str(row), str(column))).text
            print(cell_text)
            if cell_text == text:
                pass
            elif row == (row_count - 1) and column == column_count:
                raise Exception(f"{text} is not available in the table")


@then('verify the presence of answer and highlight it')
def value_changed_validation(context):
    canvas_text = context.driver.find_element_by_xpath("//canvas[contains(@id,'canvas')]")
    context.driver.execute_script("arguments[0].scrollIntoView();", canvas_text)
    context.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", canvas_text,
                                  "background:red; color:yellow; border: 4px dotted solid red")
    time.sleep(5)


@then('close browser')
def close_browser(context):
    context.driver.close()
