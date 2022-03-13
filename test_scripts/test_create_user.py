import inspect
from libraries.core import *

from libraries.generate_logs import logging, generate_log
from libraries.logger import logg


class TestAPI_Adequateshop:
    logg=generate_log()

    def setup(self):
        self.logg.info('Started Test Execution')

    def teardown(self):
        self.logg.info('Completed Test Execution ')
        self.logg.info(".......................................................................")

    def test_001(self):
        func_name= self.test_001.__name__
        verifyUserCreattion(func_name)

    def test_002_DependentOntest_001(self):
        func_name = self.test_002_DependentOntest_001.__name__
        loginwiththeregistereduser(func_name)

    def test_003DependentOntest_001(self):
        func_name = self.test_003DependentOntest_001.__name__
        getUSerbyID(func_name)


