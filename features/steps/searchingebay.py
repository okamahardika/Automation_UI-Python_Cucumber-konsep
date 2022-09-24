
from sqlite3 import Time
from telnetlib import STATUS
from threading import Thread
from time import time
from behave import *
import click
from selenium import webdriver


@when('open ebay homepage')
def step_impl(context):
    context.driver.get("https://www.ebay.com/")


@when('click shop by category')
def step_impl(context):
    status = context.driver.find_element_by_xpath(
        "/html/body/header/table/tbody/tr/td[2]/div/button"). click()


@when('click cellphone and accesoriss')
def step_impl(context):
    status = context.driver.find_element_by_xpath(
        "/html/body/header/table/tbody/tr/td[2]/div/div/table/tbody/tr/td[1]/ul[2]/li[4]/a"). click()


@when('click cellphone & smartphone')
def step_impl(context):
    status = context.driver.find_element_by_xpath(
        "/html/body/div[4]/div[3]/div[1]/div/div/div/section/ul/li[3]/a"). click()
    assert status is True
